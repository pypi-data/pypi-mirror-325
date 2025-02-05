# First we initialize the model we want to use.
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from litellm import image_generation

from botrun_flow_lang.langgraph_agents.agents.util.img_util import analyze_imgs
from botrun_flow_lang.langgraph_agents.agents.util.local_files import (
    upload_and_get_tmp_public_url,
)
from botrun_flow_lang.langgraph_agents.agents.util.pdf_analyzer import analyze_pdf
from botrun_flow_lang.langgraph_agents.agents.util.perplexity_search import (
    respond_with_perplexity_search,
)
from botrun_flow_lang.models.nodes.utils import scrape_single_url
from botrun_flow_lang.models.nodes.vertex_ai_search_node import VertexAISearch
from datetime import datetime
from botrun_flow_lang.langgraph_agents.agents.search_agent_graph import format_dates
from langgraph.checkpoint.memory import MemorySaver
import pytz
import asyncio
import os

# model = ChatOpenAI(model="gpt-4o", temperature=0)
model = ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0)


# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)

from typing import Literal

from langchain_core.tools import tool


@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")


@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b


# This will be a tool
@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


@tool
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b


@tool
def search(keywords: str):
    """
    Use this to search the web.

    Args:
        keywords: the keywords to search for, use space to separate multiple keywords, e.g. "台灣 政府 福利"
    """
    try:
        vertex_ai_search = VertexAISearch()
        search_results = vertex_ai_search.vertex_search(
            project_id="scoop-386004",
            location="global",
            data_store_id="tw-gov-welfare_1730944342934",
            search_query=keywords,
        )
        return search_results
    except Exception as e:
        return f"Error: {e}"


@tool
def scrape(url: str):
    """
    Use this to scrape the web.
    as it provides better results for video content.

    Args:
        url: the url to scrape
    """
    try:
        return asyncio.run(scrape_single_url(url))
    except Exception as e:
        return f"Error: {e}"


@tool
def current_time():
    """
    Use this to get the current time in local timezone.
    """
    try:
        local_tz = pytz.timezone("Asia/Taipei")
        local_time = datetime.now(local_tz)
        return local_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        return f"Error: {e}"


@tool
def days_between(start_date: str, end_date: str):
    """
    Use this to get the days between two dates.

    Args:
        start_date: the start date, format: YYYY-MM-DD
        end_date: the end date, format: YYYY-MM-DD
    """
    return (
        datetime.strptime(end_date, "%Y-%m-%d")
        - datetime.strptime(start_date, "%Y-%m-%d")
    ).days


@tool
def chat_with_pdf(pdf_url: str, user_input: str):
    """
    Use this to chat with a PDF file.
    User can ask about any text, pictures, charts, and tables in PDFs that is provided. Some sample use cases:
    - Analyzing financial reports and understanding charts/tables
    - Extracting key information from legal documents
    - Translation assistance for documents
    - Converting document information into structured formats

    If you have a local PDF file, you can use generate_tmp_public_url tool to get a public URL first:
    1. Call generate_tmp_public_url with your local PDF file path
    2. Use the returned URL as the pdf_url parameter for this function

    Args:
        pdf_url: the URL to the PDF file (can be generated using generate_tmp_public_url for local files)
        user_input: the user's input
    """
    print("chat_with_pdf============>", pdf_url, user_input)
    return analyze_pdf(pdf_url, user_input)


@tool
def chat_with_imgs(img_urls: list[str], user_input: str):
    """
    Use this to analyze and understand multiple images using Claude's vision capabilities.

    If you have local image files, you can use generate_tmp_public_url tool to get public URLs first:
    1. Call generate_tmp_public_url for each local image file
    2. Collect all returned URLs into a list
    3. Use the list of URLs as the img_urls parameter for this function

    Supported image formats:
    - JPEG, PNG, GIF, WebP
    - Maximum file size: 5MB per image
    - Recommended size: No more than 1568 pixels in either dimension
    - Very small images (under 200 pixels) may degrade performance
    - Can analyze up to 20 images per request

    Capabilities:
    - Analyzing charts, graphs, and diagrams
    - Reading and understanding text in images
    - Describing visual content and scenes
    - Comparing multiple images in a single request
    - Answering questions about image details
    - Identifying relationships between images

    Limitations:
    - Cannot identify or name specific people
    - May have reduced accuracy with low-quality or very small images
    - Limited spatial reasoning abilities
    - Cannot verify if images are AI-generated
    - Not designed for medical diagnosis or healthcare applications

    Args:
        img_urls: List of URLs to the image files (can be generated using generate_tmp_public_url for local files)
        user_input: Question or instruction about the image content(s)

    Returns:
        str: Claude's analysis of the image(s) based on the query
    """
    print("chat_with_imgs============>", img_urls, user_input)
    return analyze_imgs(img_urls, user_input)


@tool
def generate_tmp_public_url(file_path: str) -> str:
    """
    Generate a temporary public URL for a local file. The file will be automatically deleted after 7 days.

    Args:
        file_path: The path to the local file you want to make publicly accessible

    Returns:
        str: A public URL that can be used to access the file for 7 days

    Raises:
        FileNotFoundError: If the specified file does not exist
    """
    print("generate_tmp_public_url============>", file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    return upload_and_get_tmp_public_url(
        file_path,
        DICT_VAR.get("botrun_flow_lang_url", ""),
        DICT_VAR.get("user_id", ""),
    )


@tool
def web_search(user_input: str):
    """
    Use this to search the web when you need up-to-date information or when your knowledge is insufficient.
    This tool uses Perplexity to perform web searches and provides detailed answers with citations.

    Args:
        user_input: The search query or question you want to find information about.

    Returns:
        str: A detailed answer based on web search results, including citations to source materials
    """
    print("web_search============>", user_input)
    return respond_with_perplexity_search(
        user_input,
        user_prompt_prefix="",
        messages_for_llm=[],
        domain_filter=[],
        stream=False,
    )


@tool
def generate_image(user_input: str):
    """
    Use this to generate high-quality images using DALL-E 3.

    Capabilities:
    - Creates photorealistic images and art
    - Handles complex scenes and compositions
    - Maintains consistent styles
    - Follows detailed prompts with high accuracy
    - Supports various artistic styles and mediums

    Best practices for prompts:
    - Be specific about style, mood, lighting, and composition
    - Include details about perspective and setting
    - Specify artistic medium if desired (e.g., "oil painting", "digital art")
    - Mention color schemes or specific colors
    - Describe the atmosphere or emotion you want to convey

    Limitations:
    - Cannot generate images of public figures or celebrities
    - Avoids harmful, violent, or adult content
    - May have inconsistencies with hands, faces, or text
    - Cannot generate exact copies of existing artworks or brands
    - Limited to single image generation per request

    Args:
        user_input: Detailed description of the image you want to generate.
                   Be specific about style, content, and composition.

    Returns:
        str: URL to the generated image, or error message if generation fails
    """
    try:
        print("generate_image============>", user_input)
        image_response = image_generation(
            prompt=user_input,
            model="dall-e-3",
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        image_url = image_response["data"][0]["url"]
        return image_url
    except Exception as e:
        return f"Error: {e}"


BASIC_TOOLS = [
    current_time,
    scrape,
    days_between,
    chat_with_pdf,
    chat_with_imgs,
    web_search,
    generate_image,
]
DICT_VAR = {}

# Define the graph
from langgraph.prebuilt import create_react_agent

now = datetime.now()
dates = format_dates(now)
western_date = dates["western_date"]
taiwan_date = dates["taiwan_date"]


def create_react_agent_graph(
    system_prompt: str = "",
    botrun_flow_lang_url: str = "",
    user_id: str = "",
):
    """
    Create a react agent graph with optional system prompt

    Args:
        system_prompt: The system prompt to use for the agent
    """
    tools = BASIC_TOOLS
    if botrun_flow_lang_url and user_id:
        DICT_VAR["botrun_flow_lang_url"] = botrun_flow_lang_url
        DICT_VAR["user_id"] = user_id
        tools.append(generate_tmp_public_url)
        print("tools============>", tools)
    new_system_prompt = (
        system_prompt
        + """
    當使用 generate_image 工具時，你必須在回應中包含圖片網址。
    請按照以下格式回應(從 @begin img開始，到 @end 結束，中間包含圖片網址)：
    @begin img("{image_url}") @end
    """
    )
    return create_react_agent(
        model,
        tools=tools,
        state_modifier=new_system_prompt,
        checkpointer=MemorySaver(),
    )


# Default graph instance with empty prompt
graph = create_react_agent_graph()
# LangGraph Studio 測試用
# graph = create_react_agent_graph(
#     system_prompt="",
#     botrun_flow_lang_url="https://botrun-flow-lang-fastapi-dev-36186877499.asia-east1.run.app",
#     user_id="sebastian.hsu@gmail.com",
# )
