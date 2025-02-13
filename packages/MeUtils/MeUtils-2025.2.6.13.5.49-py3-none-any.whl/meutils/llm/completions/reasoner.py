#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : reasoner
# @Time         : 2025/2/6 08:35
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 


from openai import AsyncOpenAI

from meutils.pipe import *
from meutils.llm.clients import chatfire_client, AsyncOpenAI
from meutils.llm.openai_utils import to_openai_params

from meutils.schemas.openai_types import chat_completion, chat_completion_chunk, ChatCompletionRequest, CompletionUsage


class Completions(object):

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url

        self.client = AsyncOpenAI(
            base_url=self.base_url, api_key=self.api_key,
        )

    async def create(self, request: ChatCompletionRequest):
        data = to_openai_params(request)

        if request.stream:
            _chunk = ""
            async for chunk in await self.client.chat.completions.create(**data):
                delta = chunk.choices[0].delta

                reasoning_content = "> Reasoning\n"  # "> Reasoning\n"  # 前缀 "> 思考中\n"
                if hasattr(delta, 'reasoning_content'):
                    if reasoning_content:
                        reasoning_content += delta.reasoning_content
                    yield reasoning_content
                    reasoning_content = ''
                else:
                    yield '\n'

                yield delta.content

        else:
            completions = await self.client.chat.completions.create(**data)
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

        model="deepseek-r1:1.5b",
        # model="deepseek-r1",

        messages=[
            {
                'role': 'system',
                'content': '每次回答前务必思考之后m，回答问题'
            },
            {
                'role': 'user',
                'content': '你好'
            },

        ],
        stream=True,
    )
    arun(Completions().create(request))
