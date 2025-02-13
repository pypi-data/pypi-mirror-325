#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : reasoner
# @Time         : 2025/2/6 08:35
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :
"""
1. 适配任意客户端 think标识输出
2. 开源标准化

"""

from openai import AsyncOpenAI

from meutils.pipe import *
from meutils.llm.clients import chatfire_client, AsyncOpenAI
from meutils.llm.openai_utils import to_openai_params

from meutils.schemas.openai_types import chat_completion, chat_completion_chunk, ChatCompletionRequest, CompletionUsage

reasoner_system = {
    'role': 'system',
    'content': '你是个AI助手，请务必在深度思考之后，再回答用户问题'
}
# re.DOTALL 标志使得 . 可以匹配换行符
think_pattern = re.compile(r'<think>(.*?)</think>', re.DOTALL)


def extract_think_content(content):
    # 匹配<think>和</think>之间的内容，包括换行符
    # re.DOTALL 标志使得 . 可以匹配换行符
    think_content = think_pattern.search(content)

    if think_content:
        # 获取think标签中的内容
        think_text = think_content.group(1)
        # 移除整个think标签及其内容
        cleaned_content = think_pattern.sub('', content)
        # 返回think中的内容和清理后的文本
        return think_text.strip(), cleaned_content.strip()
    return "", content


reasoning = True


class Completions(object):

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, reasoning_stream: bool = True):

        self.reasoning_stream = reasoning_stream

        self.client = AsyncOpenAI(
            base_url=base_url, api_key=api_key,
        )

    async def create(self, request: ChatCompletionRequest):
        """适配任意客户端"""
        s = time.perf_counter()
        request.messages.insert(0, reasoner_system)

        data = to_openai_params(request)

        if request.stream:
            completion_chunks = await self.client.chat.completions.create(**data)

            is_reasoning_content = True
            reasoning_prefix = "> Reasoning\n"
            reasoning_suffix = "Reasoned for "

            async for chunk in completion_chunks:
                # chunk.model = "deepseek-reasoner"
                message = chunk.choices[0].delta
                message.content = message.content or ""

                if not hasattr(message, 'reasoning_content'):  # 标准化
                    message.reasoning_content = ""
                    if is_reasoning_content:
                        message.reasoning_content = (
                            message.content.replace("<think>", "")
                            .replace("</think>", "")
                            .replace("\n\n", "\n")
                        )
                        if message.content == "</think>":  # 思考结束
                            is_reasoning_content = False
                        message.content = ""

                    logger.debug(message)

                if self.reasoning_stream:  # 适配任意客户端: 展示推理内容

                    if message.reasoning_content.strip():  # 思考开始
                        message.content = f"{reasoning_prefix}{message.reasoning_content}"
                        reasoning_prefix = ""

                    elif message.content:  # 思考结束
                        if reasoning_suffix:
                            message.content = f"{reasoning_suffix} {time.perf_counter() - s:.0f} seconds.\n{message.content}"
                            reasoning_suffix = ""

                    yield chunk
                else:
                    yield chunk

        else:  # 非流
            completions = await self.client.chat.completions.create(**data)

            completions.model = "deepseek-reasoner"
            message = completions.choices[0].message

            if not hasattr(message, 'reasoning_content'):
                reasoning_content, content = extract_think_content(message.content)

                completions.choices[0].message.reasoning_content = reasoning_content
                completions.choices[0].message.content = content

            yield completions


if __name__ == '__main__':
    # [
    #     "qwen-plus-latest",
    #     "qvq-72b-preview",
    #     "qwq-32b-preview",
    #     "qwen2.5-coder-32b-instruct",
    #     "qwen-vl-max-latest",
    #     "qwen-turbo-latest",
    #     "qwen2.5-72b-instruct",
    #     "qwen2.5-32b-instruct"
    # ]
    request = ChatCompletionRequest(
        # model="qwen-turbo-2024-11-01",
        # model="qwen-max-latest",
        # model="qwen-plus-latest",

        # model="deepseek-r1:1.5b",
        model="deepseek-r1:32b",

        # model="deepseek-r1",

        messages=[
            # {
            #     'role': 'system',
            #     'content': '深度思考之后在回答问题并给出详细的理由'
            # },
            # {
            #     'role': 'system',
            #     'content': '你是个AI助手，请务必在深度思考之后，再回答用户问题'
            # },
            {
                'role': 'user',
                'content': '你好'
            },

        ],
        stream=False,
    )
    arun(Completions().create(request))
