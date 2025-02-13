import os

import httpx
from markdownify import markdownify as md
from tavily import TavilyClient


def web_search_tavily(query: str):
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    try:
        response = client.search(query, include_answer=True)  # type: ignore
        return response
    except Exception:
        raise


def get_web_content_as_markdown(url: str):
    try:
        response = httpx.get(url)
        response.raise_for_status()
        markdown = md(response.text)
        return markdown
    except Exception:
        raise


def evaluate_math(expression: str) -> float:
    import dspy

    try:
        result = dspy.PythonInterpreter({}).execute(expression)
        return result
    except Exception:
        raise


def code_eval(python_code: str) -> float:
    import dspy

    try:
        result = dspy.PythonInterpreter({}).execute(python_code)
        return result
    except Exception:
        raise


def get_current_time() -> str:
    import datetime

    time = datetime.datetime.now().isoformat()
    return time


def count_words(text: str) -> int:
    count = len(text.split())
    return count


def extract_urls(text: str) -> list[str]:
    import re

    url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    urls = re.findall(url_pattern, text)
    return urls


def extract_numbers(text: str) -> list[float]:
    import re

    numbers = [float(x) for x in re.findall(r"-?\d*\.?\d+", text)]
    return numbers


def json_parse_safe(text: str) -> dict:
    import json

    try:
        result = json.loads(text)
        return result
    except Exception:
        return {}


def save_to_file(content: str, filename: str):
    try:
        with open(filename, "w") as f:
            f.write(content)
    except Exception:
        raise


def read_from_file(filename: str) -> str:
    try:
        with open(filename) as f:
            content = f.read()
        return content
    except Exception:
        raise
