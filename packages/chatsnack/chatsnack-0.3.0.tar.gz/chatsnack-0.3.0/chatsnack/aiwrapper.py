import asyncio
import openai
import os
import json
import random
import time
from loguru import logger
from functools import wraps
from openai.error import *

# set OpenAI credentials from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

if os.getenv("OPENAI_API_BASE") is not None:
    openai.api_base = os.getenv("OPENAI_API_BASE")

if os.getenv("OPENAI_API_VERSION") is not None:
    openai.api_version = os.getenv("OPENAI_API_VERSION")

if os.getenv("OPENAI_API_TYPE") is not None:
    # e.g. 'azure'
    openai.api_type = os.getenv("OPENAI_API_TYPE")

async def set_api_key(api_key):
    openai.api_key = api_key

openai_exceptions_for_retry = (
    RateLimitError,
    Timeout,
    ServiceUnavailableError,
    TryAgain,
    APIError
)

def retryAPI_a(exceptions, tries=4, delay=3, backoff=2):
    """Async version of exponential backoff retry decorator."""
    def deco_retry(f):
        @wraps(f)
        async def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return await f(*args, **kwargs)
                except exceptions as e:
                    msg = f"{str(e)}, Retrying in {int(mdelay)} seconds..."
                    logger.debug(msg)
                    await asyncio.sleep(mdelay)
                    mtries -= 1
                    # multiply delay by a factor (randomized slightly)
                    mdelay *= (backoff * random.uniform(0.75, 1.25))
            return await f(*args, **kwargs)
        return f_retry
    return deco_retry

def retryAPI(exceptions, tries=4, delay=3, backoff=2):
    """Sync version of exponential backoff retry decorator."""
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    msg = f"{str(e)}, Retrying in {int(mdelay)} seconds..."
                    logger.debug(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= (backoff * random.uniform(0.75, 1.25))
            return f(*args, **kwargs)
        return f_retry
    return deco_retry


@retryAPI_a(exceptions=openai_exceptions_for_retry, tries=8, delay=2, backoff=2)
async def _chatcompletion(
    prompt,
    model="gpt-3.5-turbo",
    max_tokens=None,                # older param
    max_completion_tokens=None,     # new param for o1 models
    temperature=0.7,
    top_p=1,
    stop=None,
    presence_penalty=0,
    frequency_penalty=0,
    n=1,
    stream=False,
    user=None,
    deployment=None,
    api_type=None,
    api_base=None,
    api_version=None,
    api_key_env=None,
    # Newer optional parameters that might or might not be relevant:
    reasoning_effort=None,
    store=None,
    metadata=None,
    logprobs=None,
    top_logprobs=None,
    logit_bias=None,
    seed=None,
    service_tier=None,
    tools=None,
    tool_choice=None,
    parallel_tool_calls=None,
    response_format=None,
    # ...
):
    """
    Makes an async chat completion request to OpenAI's ChatCompletion endpoint.
    This version includes optional parameters that might be relevant for the new
    'o1' / 'reasoning' models, like `reasoning_effort` or `max_completion_tokens`.
    """
    if user is None:
        user = "_not_set"

    # If prompt is JSON-string (not a list), parse it
    if isinstance(prompt, list):
        messages = prompt
    else:
        messages = json.loads(prompt)

    logger.trace("""Chat Query:
    Prompt: {0}
    Model: {1}, max_tokens: {2}, max_completion_tokens: {3}, stop: {4}, 
    Temperature: {5}, Top-P: {6}, Presence Penalty {7}, Frequency Penalty: {8}, 
    N: {9}, Stream: {10}, User: {11}
    """, prompt, model, max_tokens, max_completion_tokens, stop,
       temperature, top_p, presence_penalty, frequency_penalty, n, stream, user)

    # We collect parameters to pass to openai.ChatCompletion.acreate
    request_params = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stop": stop,
        "n": n,
        "stream": stream,
        "user": user
    }

    # For Azure deployments, etc.
    if deployment is not None:
        request_params["deployment_id"] = deployment
    if api_key_env is not None:
        request_params["api_key"] = os.getenv(api_key_env)

    # For new vs old models:
    # If the model is something like "gpt-4o", we pass `max_completion_tokens`
    # If the model is older "gpt-3.5-turbo", we pass `max_tokens`.
    # This is just an example strategy; you can handle it however you want.
    is_o1_model = ("o1" in model) or ("o3" in model)  # adapt your detection here

    if is_o1_model:
        # Use the new recommended param: max_completion_tokens
        if max_completion_tokens is not None:
            request_params["max_completion_tokens"] = max_completion_tokens
        elif max_tokens is not None:
            # fallback if user sets only max_tokens
            request_params["max_completion_tokens"] = max_tokens
    else:
        # If not an "o1"/reasoning model, preserve old max_tokens usage
        if max_tokens is not None:
            request_params["max_tokens"] = max_tokens

    # Optional new "o1" parameters or system parameters:
    if reasoning_effort is not None:
        request_params["reasoning_effort"] = reasoning_effort
    if store is not None:
        request_params["store"] = store
    if metadata is not None:
        request_params["metadata"] = metadata
    if logprobs is not None:
        request_params["logprobs"] = logprobs
    if top_logprobs is not None:
        request_params["top_logprobs"] = top_logprobs
    if logit_bias is not None:
        request_params["logit_bias"] = logit_bias
    if seed is not None:
        request_params["seed"] = seed
    if service_tier is not None:
        request_params["service_tier"] = service_tier
    if parallel_tool_calls is not None:
        request_params["parallel_tool_calls"] = parallel_tool_calls
    if response_format is not None:
        request_params["response_format"] = response_format
    # Tools and tool_choice replaces the old function calling
    if tools is not None:
        request_params["tools"] = tools
    if tool_choice is not None:
        request_params["tool_choice"] = tool_choice

    # And pass the API version, type, base explicitly if desired
    if api_type is not None:
        request_params["api_type"] = api_type
    if api_base is not None:
        request_params["api_base"] = api_base
    if api_version is not None:
        request_params["api_version"] = api_version

    # Now actually call the endpoint
    response = await openai.ChatCompletion.acreate(**request_params)

    logger.trace("OpenAI Completion Result: {0}".format(response))
    return response


@retryAPI(exceptions=openai_exceptions_for_retry, tries=8, delay=2, backoff=2)
def _chatcompletion_s(
    prompt,
    model="gpt-3.5-turbo",
    max_tokens=None,
    max_completion_tokens=None,
    temperature=0.7,
    top_p=1,
    stop=None,
    presence_penalty=0,
    frequency_penalty=0,
    n=1,
    stream=False,
    user=None,
    deployment=None,
    api_type=None,
    api_base=None,
    api_version=None,
    api_key_env=None,
    reasoning_effort=None,
    store=None,
    metadata=None,
    logprobs=None,
    top_logprobs=None,
    logit_bias=None,
    seed=None,
    service_tier=None,
    tools=None,
    tool_choice=None,
    parallel_tool_calls=None,
    response_format=None,
):
    """
    Synchronous version of the chat completion request.
    Similar structure to _chatcompletion().
    """
    if user is None:
        user = "_not_set"

    if isinstance(prompt, list):
        messages = prompt
    else:
        messages = json.loads(prompt)

    logger.trace("""Chat Query:
    Prompt: {0}
    Model: {1}, max_tokens: {2}, max_completion_tokens: {3}, stop: {4}, 
    Temperature: {5}, Top-P: {6}, Presence Penalty {7}, Frequency Penalty: {8}, 
    N: {9}, Stream: {10}, User: {11}
    """, prompt, model, max_tokens, max_completion_tokens, stop,
       temperature, top_p, presence_penalty, frequency_penalty, n, stream, user)

    request_params = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stop": stop,
        "n": n,
        "stream": stream,
        "user": user
    }

    if deployment is not None:
        request_params["deployment_id"] = deployment
    if api_key_env is not None:
        request_params["api_key"] = os.getenv(api_key_env)

    is_o1_model = ("o1" in model) or ("o3" in model)

    if is_o1_model:
        if max_completion_tokens is not None:
            request_params["max_completion_tokens"] = max_completion_tokens
        elif max_tokens is not None:
            request_params["max_completion_tokens"] = max_tokens
    else:
        if max_tokens is not None:
            request_params["max_tokens"] = max_tokens

    if reasoning_effort is not None:
        request_params["reasoning_effort"] = reasoning_effort
    if store is not None:
        request_params["store"] = store
    if metadata is not None:
        request_params["metadata"] = metadata
    if logprobs is not None:
        request_params["logprobs"] = logprobs
    if top_logprobs is not None:
        request_params["top_logprobs"] = top_logprobs
    if logit_bias is not None:
        request_params["logit_bias"] = logit_bias
    if seed is not None:
        request_params["seed"] = seed
    if service_tier is not None:
        request_params["service_tier"] = service_tier
    if parallel_tool_calls is not None:
        request_params["parallel_tool_calls"] = parallel_tool_calls
    if response_format is not None:
        request_params["response_format"] = response_format
    if tools is not None:
        request_params["tools"] = tools
    if tool_choice is not None:
        request_params["tool_choice"] = tool_choice

    if api_type is not None:
        request_params["api_type"] = api_type
    if api_base is not None:
        request_params["api_base"] = api_base
    if api_version is not None:
        request_params["api_version"] = api_version

    response = openai.ChatCompletion.create(**request_params)
    logger.trace("OpenAI Completion Result: {0}".format(response))
    return response


def _trimmed_fetch_chat_response(resp, n):
    """Helper to consistently parse the text from the returned response."""
    if n == 1:
        # normal single output
        return resp.choices[0].message.content.strip()
    else:
        logger.trace('_trimmed_fetch_response :: returning {0} responses'.format(n))
        return [
            choice.message.content.strip()
            for choice in resp.choices[:n]
        ]


# Main public async function (example):
async def cleaned_chat_completion(
    prompt,
    model="gpt-3.5-turbo",
    max_tokens=None,
    max_completion_tokens=None,
    temperature=0.7,
    top_p=1,
    stop=None,
    presence_penalty=0,
    frequency_penalty=0,
    n=1,
    stream=False,
    user=None,
    **additional_args
):
    """
    Wrapper for OpenAI's chat completion with whitespace-trimmed result.
    We pass everything to `_chatcompletion`, including any new parameters.
    """
    # Filter out all None-valued items from additional_args
    filtered_args = {k: v for k, v in additional_args.items() if v is not None}

    # Perform the actual request
    resp = await _chatcompletion(
        prompt=prompt,
        model=model,
        max_tokens=max_tokens,
        max_completion_tokens=max_completion_tokens,
        temperature=temperature,
        top_p=top_p,
        stop=stop,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        n=n,
        stream=stream,
        user=user,
        **filtered_args
    )

    return _trimmed_fetch_chat_response(resp, n)


# TODO: Add back support for content classification (i.e. is this text NSFW?)
# TODO: Consider adding support for other local language models

# Structure of this code is based on some methods from github.com/OthersideAI/chronology
# licensed under this MIT License:
######
# MIT License
#
# Copyright (c) 2020 OthersideAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#######