# Remove duplicate imports
import subprocess
import requests
import os
import json
import ollama  # Add to setup.py if missing
import sqlite3
import pandas as pd
import openai
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
import re
from jinja2 import Environment, FileSystemLoader, Template, Undefined
import PIL
import numpy as np
from datetime import datetime
from typing import List, Dict, Any, Optional, Union, Generator
from diffusers import StableDiffusionPipeline
import base64
import subprocess
import requests
import os
import json
import ollama
import sqlite3

from typing import Optional
from google.generativeai import types


import pandas as pd
import openai
from dotenv import load_dotenv
import anthropic
import re
from jinja2 import Environment, FileSystemLoader, Template, Undefined
from datetime import datetime
from typing import List, Dict, Any, Optional, Union
import chromadb
from PIL import Image
import typing_extensions as typing

from pydantic import BaseModel, Field

import google.generativeai as genai
from typing import List, Dict, Optional
import numpy as np
from chromadb import Client

EMBEDDINGS_DB_PATH = os.path.expanduser("~/npcsh_chroma.db")

chroma_client = chromadb.PersistentClient(path=EMBEDDINGS_DB_PATH)


# Load environment variables from .env file
def load_env_from_execution_dir() -> None:
    """
    Function Description:
        This function loads environment variables from a .env file in the current execution directory.
    Args:
        None
    Keyword Args:
        None
    Returns:
        None
    """

    # Get the directory where the script is being executed
    execution_dir = os.path.abspath(os.getcwd())
    # print(f"Execution directory: {execution_dir}")
    # Construct the path to the .env file
    env_path = os.path.join(execution_dir, ".env")

    # Load the .env file if it exists
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
        print(f"Loaded .env file from {execution_dir}")
    else:
        print(f"Warning: No .env file found in {execution_dir}")


load_env_from_execution_dir()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY", None)
gemini_api_key = os.getenv("GEMINI_API_KEY", None)

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", None)
openai_api_key = os.getenv("OPENAI_API_KEY", None)

npcsh_model = os.environ.get("NPCSH_MODEL", "llama3.2")
# print("npcsh_model", npcsh_model)
npcsh_provider = os.environ.get("NPCSH_PROVIDER", "ollama")
# print("npcsh_provider", npcsh_provider)
npcsh_db_path = os.path.expanduser(
    os.environ.get("NPCSH_DB_PATH", "~/npcsh_history.db")
)
npcsh_vector_db_path = os.path.expanduser(
    os.environ.get("NPCSH_VECTOR_DB_PATH", "~/npcsh_chroma.db")
)

NPCSH_EMBEDDING_MODEL = os.environ.get("NPCSH_EMBEDDING_MODEL", "nomic-embed-text")
NPCSH_EMBEDDING_PROVIDER = os.environ.get("NPCSH_EMBEDDING_PROVIDER", "ollama")
NPCSH_REASONING_MODEL = os.environ.get("NPCSH_REASONING_MODEL", "deepseek-r1")


def get_ollama_embeddings(
    texts: List[str], model: str = NPCSH_EMBEDDING_MODEL
) -> List[List[float]]:
    """Generate embeddings using Ollama."""
    embeddings = []
    for text in texts:
        response = ollama.embeddings(model=model, prompt=text)
        embeddings.append(response["embedding"])
    return embeddings


def get_openai_embeddings(
    texts: List[str], model: str = "text-embedding-3-small"
) -> List[List[float]]:
    """Generate embeddings using OpenAI."""
    client = OpenAI(api_key=openai_api_key)
    response = client.embeddings.create(input=texts, model=model)
    return [embedding.embedding for embedding in response.data]


def get_anthropic_embeddings(
    texts: List[str], model: str = "claude-3-haiku-20240307"
) -> List[List[float]]:
    """Generate embeddings using Anthropic."""
    client = anthropic.Anthropic(api_key=anthropic_api_key)
    embeddings = []
    for text in texts:
        response = client.messages.create(
            model=model, max_tokens=1024, messages=[{"role": "user", "content": text}]
        )
        # Placeholder for actual embedding
        embeddings.append([0.0] * 1024)  # Replace with actual embedding when available
    return embeddings


def store_embeddings_for_model(
    texts,
    embeddings,
    metadata=None,
    model: str = NPCSH_EMBEDDING_MODEL,
    provider: str = NPCSH_EMBEDDING_PROVIDER,
):
    collection_name = f"{provider}_{model}_embeddings"
    collection = chroma_client.get_collection(collection_name)

    # Create meaningful metadata for each document (adjust as necessary)
    if metadata is None:
        metadata = [{"text_length": len(text)} for text in texts]  # Example metadata
        print(
            "metadata is none, creating metadata for each document as the length of the text"
        )
    # Add embeddings to the collection with metadata
    collection.add(
        ids=[str(i) for i in range(len(texts))],
        embeddings=embeddings,
        metadatas=metadata,  # Passing populated metadata
        documents=texts,
    )


def delete_embeddings_from_collection(collection, ids):
    """Delete embeddings by id from Chroma collection."""
    if ids:
        collection.delete(ids=ids)  # Only delete if ids are provided


def search_similar_texts(
    query: str,
    docs_to_embed: Optional[List[str]] = None,
    top_k: int = 5,
    db_path: str = npcsh_vector_db_path,
    embedding_model: str = NPCSH_EMBEDDING_MODEL,
    embedding_provider: str = NPCSH_EMBEDDING_PROVIDER,
) -> List[Dict[str, any]]:
    """
    Search for similar texts using either a Chroma database or direct embedding comparison.
    """

    print(f"\nQuery to embed: {query}")
    embedded_search_term = get_ollama_embeddings([query], embedding_model)[0]
    print(f"Query embedding: {embedded_search_term}")

    if docs_to_embed is None:
        # Fetch from the database if no documents to embed are provided
        collection_name = f"{embedding_provider}_{embedding_model}_embeddings"
        collection = chroma_client.get_collection(collection_name)
        results = collection.query(
            query_embeddings=[embedded_search_term], n_results=top_k
        )
        # Constructing and returning results
        return [
            {"id": id, "score": float(distance), "text": document}
            for id, distance, document in zip(
                results["ids"][0], results["distances"][0], results["documents"][0]
            )
        ]

    print(f"\nNumber of documents to embed: {len(docs_to_embed)}")

    # Get embeddings for provided documents
    raw_embeddings = get_ollama_embeddings(docs_to_embed, embedding_model)

    output_embeddings = []
    for idx, emb in enumerate(raw_embeddings):
        if emb:  # Exclude any empty embeddings
            output_embeddings.append(emb)

    # Convert to numpy arrays for calculations
    doc_embeddings = np.array(output_embeddings)
    query_embedding = np.array(embedded_search_term)

    # Check for zero-length embeddings
    if len(doc_embeddings) == 0:
        raise ValueError("No valid document embeddings found")

    # Normalize embeddings to avoid division by zeros
    doc_norms = np.linalg.norm(doc_embeddings, axis=1, keepdims=True)
    query_norm = np.linalg.norm(query_embedding)

    # Ensure no zero vectors are being used in cosine similarity
    if query_norm == 0:
        raise ValueError("Query embedding is zero-length")

    # Calculate cosine similarities
    cosine_similarities = np.dot(doc_embeddings, query_embedding) / (
        doc_norms.flatten() * query_norm
    )

    # Get indices of top K documents
    top_indices = np.argsort(cosine_similarities)[::-1][:top_k]

    return [
        {
            "id": str(idx),
            "score": float(cosine_similarities[idx]),
            "text": docs_to_embed[idx],
        }
        for idx in top_indices
    ]


def get_embeddings(
    texts: List[str],
    model: str = NPCSH_EMBEDDING_MODEL,
    provider: str = NPCSH_EMBEDDING_PROVIDER,
) -> List[List[float]]:
    """Generate embeddings using the specified provider and store them in Chroma."""
    if provider == "ollama":
        embeddings = get_ollama_embeddings(texts, model)
    elif provider == "openai":
        embeddings = get_openai_embeddings(texts, model)
    elif provider == "anthropic":
        embeddings = get_anthropic_embeddings(texts, model)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    # Store the embeddings in the relevant Chroma collection
    # store_embeddings_for_model(texts, embeddings, model, provider)
    return embeddings


def get_model_and_provider(command: str, available_models: list) -> tuple:
    """
    Function Description:
        Extracts model and provider from command and autocompletes if possible.
    Args:
        command : str : Command string
        available_models : list : List of available models
    Keyword Args:
        None
    Returns:
        model_name : str : Model name
        provider : str : Provider
        cleaned_command : str : Clean


    """

    model_match = re.search(r"@(\S+)", command)
    if model_match:
        model_name = model_match.group(1)
        # Autocomplete model name
        matches = [m for m in available_models if m.startswith(model_name)]
        if matches:
            if len(matches) == 1:
                model_name = matches[0]  # Complete the name if only one match
            # Find provider for the (potentially autocompleted) model
            provider = lookup_provider(model_name)
            if provider:
                # Remove the model tag from the command
                cleaned_command = command.replace(
                    f"@{model_match.group(1)}", ""
                ).strip()
                # print(cleaned_command, 'cleaned_command')
                return model_name, provider, cleaned_command
            else:
                return None, None, command  # Provider not found
        else:
            return None, None, command  # No matching model
    else:
        return None, None, command  # No model specified


def get_available_models() -> list:
    """
    Function Description:
        Fetches available models from Ollama, OpenAI, and Anthropic.
    Args:
        None
    Keyword Args:
        None
    Returns:
        available_models : list : List of available models

    """
    available_chat_models = []
    available_reasoning_models = []

    ollama_chat_models = [
        "llama3.3",
        "llama3.2",
        "llama3.1" "phi4",
        "phi3.5",
        "mistral",
        "llama3",
        "gemma",
        "qwen",
        "qwen2",
        "qwen2.5",
        "phi3",
        "llava",
        "codellama",
        "qwen2.5-coder",
        "tinyllama",
        "mistral-nemo",
        "llama3.2-vesion",
        "starcoder2",
        "mixtral",
        "dolphin-mixtral",
        "deepseek-coder-v2",
        "codegemma",
        "phi",
        "deepseek-coder",
        "wizardlm2",
        "llava-llama3",
    ]
    available_chat_models.extend(ollama_chat_models)

    ollama_reasoning_models = ["deepseek-r1"]
    available_reasoning_models.extend(ollama_reasoning_models)
    # OpenAI models
    openai_chat_models = [
        "gpt-4-turbo",
        "gpt-4o",
        "gpt-4o-mini",
        "dall-e-3",
        "dall-e-2",
    ]
    openai_reasoning_models = [
        "o1-mini",
        "o1",
        "o1-preview",
        "o3-mini",
        "o3-preview",
    ]
    available_reasoning_models.extend(openai_reasoning_models)

    available_chat_models.extend(openai_chat_models)

    # Anthropic models
    anthropic_chat_models = [
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-5-sonnet-20241022",
        "claude-3-haiku-20240307",
        "claude-2.1",
        "claude-2.0",
        "claude-instant-1.2",
    ]
    available_chat_models.extend(anthropic_chat_models)
    diffusers_models = [
        "runwayml/stable-diffusion-v1-5",
    ]
    available_chat_models.extend(diffusers_models)

    deepseek_chat_models = [
        "deepseek-chat",
    ]

    deepseek_reasoning_models = [
        "deepseek-reasoner",
    ]

    available_chat_models.extend(deepseek_chat_models)
    available_reasoning_models.extend(deepseek_reasoning_models)
    return available_chat_models, available_reasoning_models


available_chat_models, available_reasoning_models = get_available_models()


def generate_image_ollama(prompt: str, model: str) -> str:
    """
    Function Description:
        This function generates an image using the Ollama API.
    Args:
        prompt (str): The prompt for generating the image.
        model (str): The model to use for generating the image.
    Keyword Args:
        None
    Returns:
        str: The URL of the generated image.
    """
    return "Image generation is not yet possible with ollama. Please use Stable diffusion or OpenAI using the model override like : '/vixynt <prompt> @dall-e-3'  or '/vixynt <prompt> @dall-e-2'  or  '/vixynt <prompt> @stable-diffusion'"
    # url = f"https://localhost:13434/v1/models/{model}/generate"
    # data = {"prompt": prompt}
    # response = requests.post(url, json=data)

    # if response.status_code == 200:
    ##    return response.json().get("image_url")  # Assume 'image_url'
    # else:
    #    raise Exception(f"Error: {response.status_code}, {response.text}")


def generate_image_openai(
    prompt: str, model: str, api_key: str, size: str = None
) -> str:
    """
    Function Description:
        This function generates an image using the OpenAI API.
    Args:
        prompt (str): The prompt for generating the image.
        model (str): The model to use for generating the image.
        api_key (str): The API key for accessing the OpenAI API.
    Keyword Args:
        None
    Returns:
        str: The URL of the generated image.
    """
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
    if model is None:
        model = "dall-e-2"
    client = OpenAI(api_key=api_key)
    if size is None:
        size = "1024x1024"
    if model not in ["dall-e-3", "dall-e-2"]:
        # raise ValueError(f"Invalid model: {model}")
        print(f"Invalid model: {model}")
        print("Switching to dall-e-3")
        model = "dall-e-3"
    image = client.images.generate(model=model, prompt=prompt, n=1, size=size)
    if image is not None:
        # print(image)
        return image


def generate_image_gemini(
    prompt: str,
    model: str = "imagen-3.0-generate-002",  # Default model
    api_key: str = None,  # Replace with your actual API key
    size: Optional[str] = None,
    number_of_images: int = 1,
    aspect_ratio: str = "1:1",
    safety_filter_level: str = "BLOCK_LOW_AND_ABOVE",
    person_generation: str = "DONT_ALLOW",
) -> List[str]:
    """
    Generates an image using the Gemini API (Imagen 3).

    Args:
        prompt (str): The prompt for generating the image.
        model (str): The model to use for generating the image.
        api_key (str): The API key for accessing the Gemini API.
    Keyword Args:
        size (str): The size of the generated image (e.g., "1024x1024"). Not directly supported by Gemini.
        number_of_images (int): The number of images to generate (1 to 4). Default is 1.
        aspect_ratio (str): The aspect ratio of the generated image. Default is "1:1".
        safety_filter_level (str): The safety filter level. Default is "BLOCK_LOW_AND_ABOVE".
        person_generation (str): Whether to allow generation of people. Default is "DONT_ALLOW".
    Returns:
        List[str]: A list of URLs or file paths to the generated images.
    """
    raise NotImplementedError("Gemini imagen api not yet available in public api?")
    # Initialize the Gemini client
    if api_key is None:
        api_key = os.environ.get("GEMINI_API_KEY")
    import google.genai as ggenai
    from google.genai import types as ggtypes

    client = ggenai.Client(api_key=api_key)

    # Validate the number of images
    if number_of_images < 1 or number_of_images > 4:
        raise ValueError("number_of_images must be between 1 and 4.")

    # Generate the image(s)
    try:
        response = client.models.generate_image(
            model=model,
            prompt=prompt,
            config=ggtypes.GenerateImageConfig(
                number_of_images=number_of_images,
                aspect_ratio=aspect_ratio,
                safety_filter_level=safety_filter_level,
                person_generation=person_generation,
                output_mime_type="image/jpeg",  # Default output format
            ),
        )

        # Extract the generated images
        generated_images = []
        for image in response.generated_images:
            # Save the image to a file or return the URL
            image_path = f"generated_image_{len(generated_images) + 1}.jpg"
            with open(image_path, "wb") as f:
                f.write(image.image)
            generated_images.append(image_path)

        return generated_images

    except Exception as e:
        print(f"Error generating image: {e}")
        return []


def generate_image_anthropic(prompt: str, model: str, api_key: str) -> str:
    """
    Function Description:
        This function generates an image using the Anthropic API.
    Args:
        prompt (str): The prompt for generating the image.
        model (str): The model to use for generating the image.
        api_key (str): The API key for accessing the Anthropic API.
    Keyword Args:
        None
    Returns:
        str: The URL of the generated image.
    """
    return "Image generation is not yet possible with anthropic. Please use Stable diffusion or OpenAI using the model override like : '/vixynt <prompt> @dall-e-3'  or '/vixynt <prompt> @dall-e-2'  or  '/vixynt <prompt> @stable-diffusion'"
    # url = "https://api.anthropic.com/v1/images/generate"
    # headers = {"Authorization": f"Bearer {api_key}"}
    # data = {"model": model, "prompt": prompt}
    # response = requests.post(url, headers=headers, json=data)

    # if response.status_code == 200:
    #    return response.json().get("image_url")  # Assume 'image_url'
    # else:
    #    raise Exception(f"Error: {response.status_code}, {response.text}")


def generate_image_openai_like(
    prompt: str, model: str, api_url: str, api_key: str
) -> str:
    """
    Function Description:
        This function generates an image using an OpenAI-like API.
    Args:
        prompt (str): The prompt for generating the image.
        model (str): The model to use for generating the image.
        api_url (str): The URL of the API endpoint.
        api_key (str): The API key for accessing the API.
    Keyword Args:
        None
    Returns:
        str: The URL of the generated
    """

    return "Image generation is not well defined for open-ai like apis yet. Please use Stable diffusion or OpenAI using the model override like : '/vixynt <prompt> @dall-e-3'  or '/vixynt <prompt> @dall-e-2'  or  '/vixynt <prompt> @stable-diffusion'"

    # url = f"{api_url}/v1/images/generations"
    # headers = {"Authorization": f"Bearer {api_key}"}
    # data = {"model": model, "prompt": prompt, "n": 1, "size": "1024x1024"}
    # response = requests.post(url, headers=headers, json=data)

    # if response.status_code == 200:
    #    return response.json().get("data")[0].get("url")  # Assume the firs

    # else:
    #    raise Exception(f"Error: {response.status_code}, {response.text}")


def generate_image_hf_diffusion(
    prompt: str,
    model: str = "runwayml/stable-diffusion-v1-5",
    device: str = "cpu",
):
    """
    Function Description:
        This function generates an image using the Stable Diffusion API.
    Args:
        prompt (str): The prompt for generating the image.
        model_id (str): The Hugging Face model ID to use for Stable Diffusion.
        device (str): The device to run the model on ('cpu' or 'cuda').
    Returns:
        PIL.Image: The generated image.
    """
    # Load the Stable Diffusion pipeline
    pipe = StableDiffusionPipeline.from_pretrained(model)
    pipe = pipe.to(device)

    # Generate the image
    image = pipe(prompt)
    image = image.images[0]
    # ["sample"][0]

    return image


def generate_image(
    prompt: str,
    model: str = npcsh_model,
    provider: str = npcsh_provider,
    filename: str = None,
    npc: Any = None,
):
    """
    Function Description:
        This function generates an image using the specified provider and model.
    Args:
        prompt (str): The prompt for generating the image.
    Keyword Args:
        model (str): The model to use for generating the image.
        provider (str): The provider to use for generating the image.
        filename (str): The filename to save the image to.
        npc (Any): The NPC object.
    Returns:
        str: The filename of the saved image.
    """
    if model is not None and provider is not None:
        pass
    elif model is not None and provider is None:
        provider = lookup_provider(model)
    elif npc is not None:
        if npc.provider is not None:
            provider = npc.provider
        if npc.model is not None:
            model = npc.model
        if npc.api_url is not None:
            api_url = npc.api_url
    if filename is None:
        # Generate a filename based on the prompt and the date time
        os.makedirs(os.path.expanduser("~/.npcsh/images/"), exist_ok=True)
        filename = (
            os.path.expanduser("~/.npcsh/images/")
            + f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )

    if provider == "ollama":
        image = generate_image_ollama(prompt, model)
    elif provider == "openai":
        image = generate_image_openai(prompt, model, openai_api_key)
    elif provider == "anthropic":
        image = generate_image_anthropic(prompt, model, anthropic_api_key)
    elif provider == "openai-like":
        image = generate_image_openai_like(prompt, model, npc.api_url, openai_api_key)
    elif provider == "diffusers":
        image = generate_image_hf_diffusion(prompt, model)
    # save image
    # check if image is a PIL image
    if isinstance(image, PIL.Image.Image):
        image.save(filename)
        return filename

    elif image is not None:
        # image is at a private url
        response = requests.get(image.data[0].url)
        with open(filename, "wb") as file:
            file.write(response.content)
        from PIL import Image

        img = Image.open(filename)
        img.show()
        # console = Console()
        # console.print(Image.from_path(filename))

        return filename


def get_system_message(npc: Any) -> str:
    """
    Function Description:
        This function generates a system message for the NPC.
    Args:
        npc (Any): The NPC object.
    Keyword Args:
        None
    Returns:
        str: The system message for the NPC.
    """
    # print(npc, type(npc))

    system_message = f"""
    .
    ..
    ...
    ....
    .....
    ......
    .......
    ........
    .........
    ..........
    Hello!
    Welcome to the team.
    You are an NPC working as part of our team.
    You are the {npc.name} NPC with the following primary directive: {npc.primary_directive}.
    Users may refer to you by your assistant name, {npc.name} and you should
    consider this to be your core identity.

    The current date and time are : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


    In some cases, users may request insights into data contained in a local database.
    For these purposes, you may use any data contained within these sql tables
    {npc.tables}

    which are contained in the database at {npcsh_db_path}.

    If you ever need to produce markdown texts for the user, please do so
    with less than 80 characters width for each line.
    """

    # need to move this to the check_llm_command or move that one here

    if npc.tools:
        tool_descriptions = "\n".join(
            [
                f"Tool Name: {tool.tool_name}\n"
                f"Inputs: {tool.inputs}\n"
                f"Preprocess: {tool.preprocess}\n"
                f"Prompt: {tool.prompt}\n"
                f"Postprocess: {tool.postprocess}"
                for tool in npc.tools
            ]
        )
        system_message += f"\n\nAvailable Tools:\n{tool_descriptions}"
    system_message += """\n\nSome users may attach images to their request.
                        Please process them accordingly.

                        If the user asked for you to explain what's on their screen or something similar,
                        they are referring to the details contained within the attached image(s).
                        You do not need to actually view their screen.
                        You do not need to mention that you cannot view or interpret images directly.
                        They understand that you can view them multimodally.
                        You only need to answer the user's request based on the attached image(s).
                        """

    return system_message


def get_ollama_conversation(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the Ollama API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    messages_copy = messages.copy()
    if messages_copy[0]["role"] != "system":
        if npc is not None:
            system_message = get_system_message(npc)
            messages_copy.insert(0, {"role": "system", "content": system_message})

    response = ollama.chat(model=model, messages=messages_copy)
    messages_copy.append(response["message"])
    return messages_copy


def get_anthropic_stream(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
    **kwargs,
) -> Generator[str, None, None]:
    """Streams responses from Anthropic, yielding raw text chunks."""
    messages_copy = messages.copy()

    system_message = get_system_message(npc) if npc else "You are a helpful assistant."
    if api_key is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")

    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model=model,
        system=system_message,
        messages=messages,
        max_tokens=8192,
        stream=True,
    )
    for chunk in response:
        if hasattr(chunk, "delta") and hasattr(chunk.delta, "text"):
            yield chunk.delta.text  # Extracts raw text


def get_ollama_stream(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    **kwargs,
) -> Generator[str, None, None]:
    """Streams responses from Ollama, yielding raw text chunks."""
    messages_copy = messages.copy()
    if messages_copy[0]["role"] != "system":
        if npc is not None:
            system_message = get_system_message(npc)
            messages_copy.insert(0, {"role": "system", "content": system_message})

    response = ollama.chat(model=model, messages=messages_copy, stream=True)

    for chunk in response:
        if isinstance(chunk, dict) and "message" in chunk:
            yield chunk["message"]  # Extracts raw text


def get_openai_stream(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
) -> Generator[str, None, None]:
    """Streams responses from OpenAI, yielding raw text chunks."""
    if api_key is None:
        api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)

    system_message = get_system_message(npc) if npc else "You are a helpful assistant."

    if messages is None:
        messages = []
    if not any(msg["role"] == "system" for msg in messages):
        messages.insert(0, {"role": "system", "content": system_message})

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    for chunk in completion:
        if chunk.choices:
            for choice in chunk.choices:
                if choice.delta.content:
                    yield choice.delta.content  # Extracts raw text


def get_openai_like_stream(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
    api_url: str = None,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the OpenAI API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
        api_key (str): The API key for accessing the OpenAI API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    client = OpenAI(api_key=api_key, base_url=api_url)

    system_message = get_system_message(npc) if npc else "You are a helpful assistant."

    if messages is None:
        messages = []

    # Ensure the system message is at the beginning
    if not any(msg["role"] == "system" for msg in messages):
        messages.insert(0, {"role": "system", "content": system_message})

    # messages should already include the user's latest message

    # Make the API call with the messages including the latest user input
    completion = client.chat.completions.create(
        model=model, messages=messages, stream=True, **kwargs
    )

    for chunk in completion:
        yield chunk


def get_deepseek_stream(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the Deepseek API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
        api_key (str): The API key for accessing the Deepseek API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """
    if api_key is None:
        api_key = os.environ["DEEPSEEK_API_KEY"]
    client = deepseek.Deepseek(api_key=api_key)

    system_message = get_system_message(npc) if npc else ""

    messages_copy = messages.copy()
    if messages_copy[0]["role"] != "system":
        messages_copy.insert(0, {"role": "system", "content": system_message})

    completion = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=messages_copy,
        stream = True,
        **kwargs,  # Include any additional keyword arguments
    )

    for response in completion:
        yield response



def get_gemini_stream(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the Gemini API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
        api_key (str): The API key for accessing the Gemini API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.

    """

    return

def get_openai_conversation(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the OpenAI API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
        api_key (str): The API key for accessing the OpenAI API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    try:
        if api_key is None:
            api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI(api_key=api_key)

        system_message = (
            get_system_message(npc) if npc else "You are a helpful assistant."
        )

        if messages is None:
            messages = []

        # Ensure the system message is at the beginning
        if not any(msg["role"] == "system" for msg in messages):
            messages.insert(0, {"role": "system", "content": system_message})

        # messages should already include the user's latest message

        # Make the API call with the messages including the latest user input
        completion = client.chat.completions.create(
            model=model, messages=messages, **kwargs
        )

        response_message = completion.choices[0].message
        messages.append({"role": "assistant", "content": response_message.content})

        return messages

    except Exception as e:
        return f"Error interacting with OpenAI: {e}"


def get_openai_like_response(
    prompt: str,
    model: str,
    api_url: str,
    api_key: str,
    **kwargs,
) -> Dict[str, Any]:
    try:
        if api_url is None:
            raise ValueError("api_url is required for openai-like provider")
        request_data = {
            "model": model,
            "prompt": prompt,
            **kwargs,
        }
        headers = {"Content-Type": "application/json"}
        headers["Authorization"] = f"Bearer {api_key}"
        response = requests.post(api_url, headers=headers, json=request_data)
        response.raise_for_status()
        response_json = response.json()
        return response_json
    except requests.exceptions.RequestException as e:
        return f"Error making API request: {e}"
    except Exception as e:
        return f"Error interacting with API: {e}"


def get_openai_like_conversation(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_url: str = None,
    api_key: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using an OpenAI-like API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
        api_url (str): The URL of the API endpoint.
        api_key (str): The API key for accessing the API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    try:
        if api_url is None:
            raise ValueError("api_url is required for openai-like provider")

        system_message = get_system_message(npc) if npc else ""
        messages_copy = messages.copy()
        if messages_copy[0]["role"] != "system":
            messages_copy.insert(0, {"role": "system", "content": system_message})
        last_user_message = None
        for msg in reversed(messages_copy):
            if msg["role"] == "user":
                last_user_message = msg["content"]
                break
        if last_user_message is None:
            raise ValueError("No user message found in the conversation history.")
        request_data = {
            "model": model,
            "messages": messages_copy,
            **kwargs,  # Include any additional keyword arguments
        }
        headers = {"Content-Type": "application/json"}  # Set Content-Type header
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        response = requests.post(api_url, headers=headers, json=request_data)
        response.raise_for_status()
        response_json = response.json()
        llm_response = (
            response_json.get("choices", [{}])[0].get("message", {}).get("content")
        )
        if llm_response is None:
            raise ValueError(
                "Invalid response format from the API. Could not extract 'choices[0].message.content'."
            )
        messages_copy.append({"role": "assistant", "content": llm_response})
        return messages_copy
    except requests.exceptions.RequestException as e:
        return f"Error making API request: {e}"
    except Exception as e:
        return f"Error interacting with API: {e}"


def get_anthropic_conversation(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
    api_key: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the Anthropic API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
        api_key (str): The API key for accessing the Anthropic API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    try:
        if api_key is None:
            api_key = os.getenv("ANTHROPIC_API_KEY", None)
        system_message = get_system_message(npc) if npc else ""
        client = anthropic.Anthropic(api_key=api_key)
        last_user_message = None
        for msg in reversed(messages):
            if msg["role"] == "user":
                last_user_message = msg["content"]
                break

        if last_user_message is None:
            raise ValueError("No user message found in the conversation history.")

        # if a sys message is in messages, remove it
        if messages[0]["role"] == "system":
            messages.pop(0)

        message = client.messages.create(
            model=model,
            system=system_message,  # Include system message in each turn for Anthropic
            messages=messages,  # Send only the last user message
            max_tokens=8192,
            **kwargs,
        )

        messages.append({"role": "assistant", "content": message.content[0].text})

        return messages

    except Exception as e:
        return f"Error interacting with Anthropic conversations: {e}"


def get_conversation(
    messages: List[Dict[str, str]],
    provider: str = npcsh_provider,
    model: str = npcsh_model,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    api_url: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the specified provider and model.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
    Keyword Args:
        provider (str): The provider to use for the conversation.
        model (str): The model to use for the conversation.
        npc (Any): The NPC object.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    if model is not None and provider is not None:
        pass  # Use explicitly provided model and provider
    elif model is not None and provider is None:
        provider = lookup_provider(model)
    elif npc is not None and (npc.provider is not None or npc.model is not None):
        provider = npc.provider if npc.provider else provider
        model = npc.model if npc.model else model
        api_url = npc.api_url if npc.api_url else api_url
    else:
        provider = "ollama"
        model = "llava:7b" if images is not None else "llama3.2"

    # print(provider, model)
    if provider == "ollama":
        return get_ollama_conversation(messages, model, npc=npc, **kwargs)
    elif provider == "openai":
        return get_openai_conversation(messages, model, npc=npc, **kwargs)
    elif provider == "anthropic":
        return get_anthropic_conversation(messages, model, npc=npc, **kwargs)
    elif provider == "gemini":
        return get_gemini_conversation(messages, model, npc=npc, **kwargs)
    elif provider == "deepseek":
        return get_deepseek_conversation(messages, model, npc=npc, **kwargs)

    else:
        return "Error: Invalid provider specified."


def get_stream(
    messages: List[Dict[str, str]],
    provider: str = npcsh_provider,
    model: str = npcsh_model,
    npc: Any = None,
    api_url: str = None,
    api_key: str = None,
    **kwargs,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a streaming response using the specified provider and model
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
    Keyword Args:
        provider (str): The provider to use for the conversation.
        model (str): The model to use for the conversation.
        npc (Any): The NPC object.
        api_url (str): The URL of the API endpoint.
        api_key (str): The API key for accessing the API.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """
    if model is not None and provider is not None:
        pass
    elif model is not None and provider is None:
        provider = lookup_provider(model)
    elif npc is not None:
        if npc.provider is not None:
            provider = npc.provider
        if npc.model is not None:
            model = npc.model
        if npc.api_url is not None:
            api_url = npc.api_url
    else:
        provider = "ollama"
        model = "llama3.2"
    print(model, provider)
    if provider == "ollama":
        return get_ollama_stream(messages, model, npc=npc, **kwargs)
    elif provider == "openai":
        return get_openai_stream(messages, model, npc=npc, api_key=api_key, **kwargs)
    elif provider == "anthropic":
        return get_anthropic_stream(messages, model, npc=npc, api_key=api_key, **kwargs)
    elif provider == "openai-like":
        return get_openai_like_stream(
            messages, model, npc=npc, api_url=api_url, api_key=api_key, **kwargs
        )
    elif provider == "deepseek":
        return get_deepseek_stream(messages, model, npc=npc, api_key=api_key, **kwargs)
    elif provider == "gemini":
        return get_gemini_stream(messages, model, npc=npc, api_key=api_key, **kwargs)
    else:
        return "Error: Invalid provider specified."


def debug_loop(prompt: str, error: str, model: str) -> bool:
    """
    Function Description:
        This function generates a debug loop using the specified model.
    Args:
        prompt (str): The prompt for the debug loop.
        error (str): The error message to check for.
        model (str): The model to use for the debug loop.
    Keyword Args:
        None
    Returns:
        bool: Whether the debug loop was successful.
    """

    response = get_ollama_response(prompt, model)
    print(response)
    if error in response:
        print(response[error])
        return True
    return False


def get_data_response(
    request: str,
    db_conn: sqlite3.Connection,
    tables: str = None,
    n_try_freq: int = 5,
    extra_context: str = None,
    history: str = None,
    model: str = None,
    provider: str = None,
    npc: Any = None,
    max_retries: int = 3,
) -> Dict[str, Any]:
    """
    Generate a response to a data request, with retries for failed attempts.
    """
    prompt = f"""
    User request: {request}
    Available tables: {tables or 'Not specified'}
    {extra_context or ''}
    {f'Query history: {history}' if history else ''}

    Provide either:
    1) An SQL query to directly answer the request
    2) An exploratory query to gather more information

    Return JSON with:
    {{
        "query": <sql query string>,
        "choice": <1 or 2>,
        "explanation": <reason for choice>
    }}
    DO NOT include markdown formatting or ```json tags.
    """

    failures = []
    for attempt in range(max_retries):
        try:
            llm_response = get_llm_response(
                prompt, npc=npc, format="json", model=model, provider=provider
            )

            # Clean response if it's a string
            response_data = llm_response.get("response", {})
            if isinstance(response_data, str):
                response_data = (
                    response_data.replace("```json", "").replace("```", "").strip()
                )
                try:
                    response_data = json.loads(response_data)
                except json.JSONDecodeError:
                    failures.append("Invalid JSON response")
                    continue

            result = process_data_output(
                response_data,
                db_conn,
                request,
                tables=tables,
                history=failures,
                npc=npc,
                model=model,
                provider=provider,
            )

            if result["code"] == 200:
                return result

            failures.append(result["response"])

            if attempt == max_retries - 1:
                return {
                    "response": f"Failed after {max_retries} attempts. Errors: {'; '.join(failures)}",
                    "code": 400,
                }

        except Exception as e:
            failures.append(str(e))

    return {"response": "Max retries exceeded", "code": 400}


def check_output_sufficient(
    request: str,
    data: pd.DataFrame,
    query: str,
    model: str = None,
    provider: str = None,
    npc: Any = None,
) -> Dict[str, Any]:
    """
    Check if the query results are sufficient to answer the user's request.
    """
    prompt = f"""
    Given:
    - User request: {request}
    - Query executed: {query}
    - Results:
      Summary: {data.describe()}
      data schema: {data.dtypes}
      Sample: {data.head()}

    Is this result sufficient to answer the user's request?
    Return JSON with:
    {{
        "IS_SUFFICIENT": <boolean>,
        "EXPLANATION": <string : If the answer is not sufficient specify what else is necessary.
                                IFF the answer is sufficient, provide a response that can be returned to the user as an explanation that answers their question.
                                The explanation should use the results to answer their question as long as they wouold be useful to the user.
                                    For example, it is not useful to report on the "average/min/max/std ID" or the "min/max/std/average of a string column".

                                Be smart about what you report.
                                It should not be a conceptual or abstract summary of the data.
                                It should not unnecessarily bring up a need for more data.
                                You should write it in a tone that answers the user request. Do not spout unnecessary self-referential fluff like "This information gives a clear overview of the x landscape".
                                >
    }}
    DO NOT include markdown formatting or ```json tags.

    """

    response = get_llm_response(
        prompt, format="json", model=model, provider=provider, npc=npc
    )

    # Clean response if it's a string
    result = response.get("response", {})
    if isinstance(result, str):
        result = result.replace("```json", "").replace("```", "").strip()
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            return {"IS_SUFFICIENT": False, "EXPLANATION": "Failed to parse response"}

    return result


def process_data_output(
    llm_response: Dict[str, Any],
    db_conn: sqlite3.Connection,
    request: str,
    tables: str = None,
    history: str = None,
    npc: Any = None,
    model: str = None,
    provider: str = None,
) -> Dict[str, Any]:
    """
    Process the LLM's response to a data request and execute the appropriate query.
    """
    try:
        choice = llm_response.get("choice")
        query = llm_response.get("query")

        if not query:
            return {"response": "No query provided", "code": 400}

        if choice == 1:  # Direct answer query
            try:
                df = pd.read_sql_query(query, db_conn)
                result = check_output_sufficient(
                    request, df, query, model=model, provider=provider, npc=npc
                )

                if result.get("IS_SUFFICIENT"):
                    return {"response": result["EXPLANATION"], "data": df, "code": 200}
                return {
                    "response": f"Results insufficient: {result.get('EXPLANATION')}",
                    "code": 400,
                }

            except Exception as e:
                return {"response": f"Query execution failed: {str(e)}", "code": 400}

        elif choice == 2:  # Exploratory query
            try:
                df = pd.read_sql_query(query, db_conn)
                extra_context = f"""
                Exploratory query results:
                Query: {query}
                Results summary: {df.describe()}
                Sample data: {df.head()}
                """

                return get_data_response(
                    request,
                    db_conn,
                    tables=tables,
                    extra_context=extra_context,
                    history=history,
                    model=model,
                    provider=provider,
                    npc=npc,
                )

            except Exception as e:
                return {"response": f"Exploratory query failed: {str(e)}", "code": 400}

        return {"response": "Invalid choice specified", "code": 400}

    except Exception as e:
        return {"response": f"Processing error: {str(e)}", "code": 400}


import google.generativeai as genai
import base64
import json
from typing import List, Dict, Any, Union
from pydantic import BaseModel


def get_gemini_response(
    prompt: str,
    model: str,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    format: Union[str, BaseModel] = None,
    messages: List[Dict[str, str]] = None,
    api_key: str = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Generates a response using the Gemini API.
    """
    # Configure the Gemini API
    if api_key is None:
        genai.configure(api_key=gemini_api_key)

    # Prepare the system message
    system_message = get_system_message(npc) if npc else "You are a helpful assistant."
    model = genai.GenerativeModel(model, system_instruction=system_message)

    # Extract just the content to send to the model
    if messages is None or len(messages) == 0:
        content_to_send = prompt
    else:
        # Get the latest message's content
        latest_message = messages[-1]
        content_to_send = (
            latest_message["parts"][0]
            if "parts" in latest_message
            else latest_message.get("content", prompt)
        )
    history = []
    if messages:
        for msg in messages:
            if "content" in msg:
                # Convert content to parts format
                history.append({"role": msg["role"], "parts": [msg["content"]]})
            else:
                # Already in parts format
                history.append(msg)
    # If no history, create a new message list
    if not history:
        history = [{"role": "user", "parts": [prompt]}]
    elif isinstance(prompt, str):  # Add new prompt to existing history
        history.append({"role": "user", "parts": [prompt]})

    # Handle images if provided
    # Handle images by adding them to the last message's parts
    if images:
        for image in images:
            with open(image["file_path"], "rb") as image_file:
                img = Image.open(image_file)
                history[-1]["parts"].append(img)
    # Generate the response
    try:
        # Send the entire conversation history to maintain context
        response = model.generate_content(history)
        llm_response = response.text

        # Filter out empty parts
        if isinstance(llm_response, list):
            llm_response = " ".join([part for part in llm_response if part.strip()])
        elif not llm_response.strip():
            llm_response = ""

        # Prepare the return dictionary
        items_to_return = {"response": llm_response, "messages": history}
        # print(llm_response, type(llm_response))

        # Handle JSON format if specified
        if format == "json":
            if type(llm_response) == str:
                if llm_response.startswith("```json"):
                    llm_response = (
                        llm_response.replace("```json", "").replace("```", "").strip()
                    )
            try:
                items_to_return["response"] = json.loads(llm_response)
            except json.JSONDecodeError:
                print(f"Warning: Expected JSON response, but received: {llm_response}")
                return {"error": "Invalid JSON response"}
        else:
            # Append the model's response to the messages
            history.append({"role": "model", "parts": [llm_response]})
            items_to_return["messages"] = history

        return items_to_return

    except Exception as e:
        return {"error": f"Error generating response: {str(e)}"}


def get_gemini_conversation(
    messages: List[Dict[str, str]],
    model: str,
    npc: Any = None,
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the Gemini API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """
    # Make the API call to Gemini

    # translate content to parts
    for message in messages:
        if "content" in message:
            message["parts"] = [message.pop("content")]

    try:
        # print(messages[-1])
        if messages[-1]["role"] == "assistant":
            messages.pop(-1)
        response = get_gemini_response(messages, model, messages=messages, npc=npc)
        # print(response)
        messages.append(
            {"role": "assistant", "content": response.get("response", "No response")}
        )

    except Exception as e:
        messages.append(
            {"role": "assistant", "content": f"Error interacting with Gemini: {str(e)}"}
        )

    return messages


def get_deepseek_conversation(
    messages: List[Dict[str, str]], model: str, npc: Any = None
) -> List[Dict[str, str]]:
    """
    Function Description:
        This function generates a conversation using the DeepSeek API.
    Args:
        messages (List[Dict[str, str]]): The list of messages in the conversation.
        model (str): The model to use for the conversation.
    Keyword Args:
        npc (Any): The NPC object.
    Returns:
        List[Dict[str, str]]: The list of messages in the conversation.
    """

    system_message = get_system_message(npc) if npc else "You are a helpful assistant."

    # Prepare the messages list
    if messages is None or len(messages) == 0:
        messages = [{"role": "system", "content": system_message}]
    elif not any(msg["role"] == "system" for msg in messages):
        messages.insert(0, {"role": "system", "content": system_message})

    # Make the API call to DeepSeek
    try:
        response = get_deepseek_response(
            messages[-1]["content"], model, messages=messages, npc=npc
        )
        messages.append(
            {"role": "assistant", "content": response.get("response", "No response")}
        )

    except Exception as e:
        messages.append(
            {
                "role": "assistant",
                "content": f"Error interacting with DeepSeek: {str(e)}",
            }
        )

    return messages


def get_deepseek_response(
    prompt: str,
    model: str,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    format: Union[str, BaseModel] = None,
    messages: List[Dict[str, str]] = None,
    api_key: str = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Function Description:
        This function generates a response using the DeepSeek API.
    Args:
        prompt (str): The prompt for generating the response.
        model (str): The model to use for generating the response.
    Keyword Args:
        images (List[Dict[str, str]]): The list of images.
        npc (Any): The NPC object.
        format (str): The format of the response.
        messages (List[Dict[str, str]]): The list of messages.
    Returns:
        Any: The response generated by the DeepSeek API.


    """
    if api_key is None:
        api_key = os.getenv("DEEPSEEK_API_KEY", None)
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    print(client)

    system_message = get_system_message(npc) if npc else "You are a helpful assistant."
    if messages is None or len(messages) == 0:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": [{"type": "text", "text": prompt}]},
        ]
    if images:
        for image in images:
            # print(f"Image file exists: {os.path.exists(image['file_path'])}")

            with open(image["file_path"], "rb") as image_file:
                image_data = base64.b64encode(compress_image(image_file.read())).decode(
                    "utf-8"
                )
                messages[-1]["content"].append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}",
                        },
                    }
                )
    print(messages)
    # print(model)
    response_format = None if format == "json" else format
    if response_format is None:
        completion = client.chat.completions.create(model=model, messages=messages)
        llm_response = completion.choices[0].message.content
        items_to_return = {"response": llm_response}

        items_to_return["messages"] = messages
        # print(llm_response, model)
        if format == "json":
            try:
                items_to_return["response"] = json.loads(llm_response)

                return items_to_return
            except json.JSONDecodeError:
                print(f"Warning: Expected JSON response, but received: {llm_response}")
                return {"error": "Invalid JSON response"}
        else:
            items_to_return["messages"].append(
                {"role": "assistant", "content": llm_response}
            )
            return items_to_return

    else:
        if model in available_reasoning_models:
            raise NotImplementedError("Reasoning models do not support JSON output.")
        try:
            completion = client.beta.chat.completions.parse(
                model=model, messages=messages, response_format=response_format
            )
            items_to_return = {"response": completion.choices[0].message.parsed.dict()}
            items_to_return["messages"] = messages

            items_to_return["messages"].append(
                {"role": "assistant", "content": completion.choices[0].message.parsed}
            )
            return items_to_return
        except Exception as e:
            print("pydantic outputs not yet implemented with deepseek?")


def get_ollama_response(
    prompt: str,
    model: str,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    format: Union[str, BaseModel] = None,
    messages: List[Dict[str, str]] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Generates a response using the Ollama API.

    Args:
        prompt (str): Prompt for generating the response.
        model (str): Model to use for generating the response.
        images (List[Dict[str, str]], optional): List of image data. Defaults to None.
        npc (Any, optional): Optional NPC object. Defaults to None.
        format (Union[str, BaseModel], optional): Response format or schema. Defaults to None.
        messages (List[Dict[str, str]], optional): Existing messages to append responses. Defaults to None.

    Returns:
        Dict[str, Any]: The response, optionally including updated messages.
    """
    # try:
    # Prepare the message payload

    message = {"role": "user", "content": prompt}
    if images:
        message["images"] = [image["file_path"] for image in images]

    # Prepare format
    if isinstance(format, type):
        schema = format.model_json_schema()
        res = ollama.chat(model=model, messages=[message], format=schema)

    elif isinstance(format, str):
        if format == "json":
            res = ollama.chat(model=model, messages=[message], format=format)
        else:
            res = ollama.chat(model=model, messages=[message])
    else:
        res = ollama.chat(model=model, messages=[message])
    response_content = res.get("message", {}).get("content")

    # Prepare the return dictionary
    result = {"response": response_content}

    # Append response to messages if provided
    if messages is not None:
        messages.append({"role": "assistant", "content": response_content})
        result["messages"] = messages

    # Handle JSON format if specified
    if format == "json":
        if model in available_reasoning_models:
            raise NotImplementedError("Reasoning models do not support JSON output.")
        try:
            result["response"] = json.loads(response_content)
        except json.JSONDecodeError:
            return {"error": f"Invalid JSON response: {response_content}"}

    return result

    # except Exception as e:
    #    return {"error": f"Exception occurred: {e}"}


def get_openai_response(
    prompt: str,
    model: str,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    format: Union[str, BaseModel] = None,
    api_key: str = None,
    messages: List[Dict[str, str]] = None,
):
    """
    Function Description:
        This function generates a response using the OpenAI API.
    Args:
        prompt (str): The prompt for generating the response.
        model (str): The model to use for generating the response.
    Keyword Args:
        images (List[Dict[str, str]]): The list of images.
        npc (Any): The NPC object.
        format (str): The format of the response.
        api_key (str): The API key for accessing the OpenAI API.
        messages (List[Dict[str, str]]): The list of messages.
    Returns:
        Any: The response generated by the OpenAI API.
    """

    # try:
    if api_key is None:
        api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)
    # print(npc)

    system_message = get_system_message(npc) if npc else "You are a helpful assistant."
    if messages is None or len(messages) == 0:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": [{"type": "text", "text": prompt}]},
        ]
    if images:
        for image in images:
            # print(f"Image file exists: {os.path.exists(image['file_path'])}")

            with open(image["file_path"], "rb") as image_file:
                image_data = base64.b64encode(compress_image(image_file.read())).decode(
                    "utf-8"
                )
                messages[-1]["content"].append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}",
                        },
                    }
                )
    # print(model)
    response_format = None if format == "json" else format
    if response_format is None:
        completion = client.chat.completions.create(model=model, messages=messages)
        llm_response = completion.choices[0].message.content
        items_to_return = {"response": llm_response}

        items_to_return["messages"] = messages
        # print(llm_response, model)
        if format == "json":
            if model in available_reasoning_models:
                raise NotImplementedError(
                    "Reasoning models do not support JSON output."
                )
            try:
                items_to_return["response"] = json.loads(llm_response)

                return items_to_return
            except json.JSONDecodeError:
                print(f"Warning: Expected JSON response, but received: {llm_response}")
                return {"error": "Invalid JSON response"}
        else:
            items_to_return["messages"].append(
                {"role": "assistant", "content": llm_response}
            )
            return items_to_return

    else:
        completion = client.beta.chat.completions.parse(
            model=model, messages=messages, response_format=response_format
        )
        items_to_return = {"response": completion.choices[0].message.parsed.dict()}
        items_to_return["messages"] = messages

        items_to_return["messages"].append(
            {"role": "assistant", "content": completion.choices[0].message.parsed}
        )
        return items_to_return
    # except Exception as e:
    #    print("openai api key", api_key)
    #    print(f"Error interacting with OpenAI: {e}")
    #    return f"Error interacting with OpenAI: {e}"


def compress_image(image_bytes, max_size=(800, 600)):
    from PIL import Image
    import io

    # Create a copy of the bytes in memory
    buffer = io.BytesIO(image_bytes)
    img = Image.open(buffer)

    # Force loading of image data
    img.load()

    # Convert RGBA to RGB if necessary
    if img.mode == "RGBA":
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background

    # Resize if needed
    if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
        img.thumbnail(max_size)

    # Save with minimal compression
    out_buffer = io.BytesIO()
    img.save(out_buffer, format="JPEG", quality=95, optimize=False)
    return out_buffer.getvalue()


def get_anthropic_response(
    prompt: str,
    model: str,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    format: str = None,
    api_key: str = None,
    messages: List[Dict[str, str]] = None,
    **kwargs,
):
    """
    Function Description:
        This function generates a response using the Anthropic API.
    Args:
        prompt (str): The prompt for generating the response.
        model (str): The model to use for generating the response.
    Keyword Args:
        images (List[Dict[str, str]]): The list of images.
        npc (Any): The NPC object.
        format (str): The format of the response.
        api_key (str): The API key for accessing the Anthropic API.
        messages (List[Dict[str, str]]): The list of messages.
    Returns:
        Any: The response generated by the Anthropic API.
    """

    try:
        if api_key is None:
            api_key = os.getenv("ANTHROPIC_API_KEY", None)

        client = anthropic.Anthropic()

        # Prepare the message content
        message_content = []

        # Add images if provided
        if images:
            for img in images:
                # load image and base 64 encode
                with open(img["file_path"], "rb") as image_file:
                    img["data"] = base64.b64encode(
                        compress_image(image_file.read())
                    ).decode("utf-8")
                    img["media_type"] = "image/jpeg"
                    message_content.append(
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": img["media_type"],
                                "data": img["data"],
                            },
                        }
                    )

        # Add the text prompt
        message_content.append({"type": "text", "text": prompt})

        # Create the message
        message = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": message_content}],
        )
        # print(message)

        llm_response = message.content[0].text
        items_to_return = {"response": llm_response}

        # print(format)
        # Update messages if they were provided
        if messages is None:
            messages = []
            messages.append(
                {"role": "system", "content": "You are a helpful assistant."}
            )
            messages.append({"role": "user", "content": message_content})
        items_to_return["messages"] = messages

        # Handle JSON format if requested
        if format == "json":
            try:
                items_to_return["response"] = json.loads(llm_response)
                return items_to_return
            except json.JSONDecodeError:
                print(f"Warning: Expected JSON response, but received: {llm_response}")
                return {"response": llm_response, "error": "Invalid JSON response"}
        else:
            # only append to messages if the response is not json
            messages.append({"role": "assistant", "content": llm_response})
        # print("teststea")
        return items_to_return

    except Exception as e:
        return f"Error interacting with Anthropic llm response: {e}"


def lookup_provider(model: str) -> str:
    """
    Function Description:
        This function determines the provider based on the model name.
    Args:
        model (str): The model name.
    Keyword Args:
        None
    Returns:
        str: The provider based on the model name.
    """
    if model == "deepseek-chat" or model == "deepseek-reasoner":
        return "deepseek"
    ollama_prefixes = [
        "llama",
        "deepseek",
        "qwen",
        "llava",
        "phi",
        "mistral",
        "mixtral",
        "dolphin",
        "codellama",
        "gemma",
    ]
    if any(model.startswith(prefix) for prefix in ollama_prefixes):
        return "ollama"

    # OpenAI models
    openai_prefixes = ["gpt-", "dall-e-", "whisper-", "o1"]
    if any(model.startswith(prefix) for prefix in openai_prefixes):
        return "openai"

    # Anthropic models
    if model.startswith("claude"):
        return "anthropic"
    if model.startswith("gemini"):
        return "gemini"
    if "diffusion" in model:
        return "diffusers"
    return None


def get_llm_response(
    prompt: str,
    provider: str = npcsh_provider,
    model: str = npcsh_model,
    images: List[Dict[str, str]] = None,
    npc: Any = None,
    messages: List[Dict[str, str]] = None,
    api_url: str = None,
    **kwargs,
):
    """
    Function Description:
        This function generates a response using the specified provider and model.
    Args:
        prompt (str): The prompt for generating the response.
    Keyword Args:
        provider (str): The provider to use for generating the response.
        model (str): The model to use for generating the response.
        images (List[Dict[str, str]]): The list of images.
        npc (Any): The NPC object.
        messages (List[Dict[str, str]]): The list of messages.
        api_url (str): The URL of the API endpoint.
    Returns:
        Any: The response generated by the specified provider and model.
    """
    if model is not None and provider is not None:
        pass
    elif provider is None and model is not None:
        provider = lookup_provider(model)

    elif npc is not None:
        if npc.provider is not None:
            provider = npc.provider
        if npc.model is not None:
            model = npc.model
        if npc.api_url is not None:
            api_url = npc.api_url

    else:
        provider = "ollama"
        if images is not None:
            model = "llava:7b"
        else:
            model = "llama3.2"

    # print(provider, model)
    if provider == "ollama":
        if model is None:
            if images is not None:
                model = "llama:7b"
            else:
                model = "llama3.2"
        elif images is not None and model not in [
            "x/llama3.2-vision",
            "llama3.2-vision",
            "llava-llama3",
            "bakllava",
            "moondream",
            "llava-phi3",
            "minicpm-v",
            "hhao/openbmb-minicpm-llama3-v-2_5",
            "aiden_lu/minicpm-v2.6",
            "xuxx/minicpm2.6",
            "benzie/llava-phi-3",
            "mskimomadto/chat-gph-vision",
            "xiayu/openbmb-minicpm-llama3-v-2_5",
            "0ssamaak0/xtuner-llava",
            "srizon/pixie",
            "jyan1/paligemma-mix-224",
            "qnguyen3/nanollava",
            "knoopx/llava-phi-2",
            "nsheth/llama-3-lumimaid-8b-v0.1-iq-imatrix",
            "bigbug/minicpm-v2.5",
        ]:
            model = "llava:7b"
        # print(model)
        return get_ollama_response(
            prompt, model, npc=npc, messages=messages, images=images, **kwargs
        )
    elif provider == "gemini":
        if model is None:
            model = "gemini-1.5-flash"
        return get_gemini_response(
            prompt, model, npc=npc, messages=messages, images=images, **kwargs
        )

    elif provider == "deepseek":
        if model is None:
            model = "deepseek-chat"
        print(prompt, model, provider)
        return get_deepseek_response(
            prompt, model, npc=npc, messages=messages, images=images, **kwargs
        )
    elif provider == "openai":
        if model is None:
            model = "gpt-4o-mini"
        # print(model)
        return get_openai_response(
            prompt, model, npc=npc, messages=messages, images=images, **kwargs
        )
    elif provider == "openai-like":
        if api_url is None:
            raise ValueError("api_url is required for openai-like provider")
        return get_openai_like_response(
            prompt, model, api_url, npc=npc, messages=messages, images=images, **kwargs
        )

    elif provider == "anthropic":
        if model is None:
            model = "claude-3-haiku-20240307"
        return get_anthropic_response(
            prompt, model, npc=npc, messages=messages, images=images, **kwargs
        )
    else:
        # print(provider)
        # print(model)
        return "Error: Invalid provider specified."


def execute_data_operations(
    query: str,
    command_history: Any,
    dataframes: Dict[str, pd.DataFrame],
    npc: Any = None,
    db_path: str = "~/npcsh_history.db",
):
    """
    Function Description:
        This function executes data operations.
    Args:
        query (str): The query to execute.
        command_history (Any): The command history.
        dataframes (Dict[str, pd.DataFrame]): The dictionary of dataframes.
    Keyword Args:
        npc (Any): The NPC object.
        db_path (str): The database path.
    Returns:
        Any: The result of the data operations.
    """

    location = os.getcwd()
    db_path = os.path.expanduser(db_path)

    try:
        try:
            # Create a safe namespace for pandas execution
            namespace = {
                "pd": pd,
                "np": np,
                "plt": plt,
                **dataframes,  # This includes all our loaded dataframes
            }
            # Execute the query
            result = eval(query, namespace)

            # Handle the result
            if isinstance(result, (pd.DataFrame, pd.Series)):
                # render_markdown(result)
                return result, "pd"
            elif isinstance(result, plt.Figure):
                plt.show()
                return result, "pd"
            elif result is not None:
                # render_markdown(result)

                return result, "pd"

        except Exception as exec_error:
            print(f"Pandas Error: {exec_error}")

        # 2. Try SQL
        # print(db_path)
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                print(query)
                print(get_available_tables(db_path))

                cursor.execute(query)
                # get available tables

                result = cursor.fetchall()
                if result:
                    for row in result:
                        print(row)
                    return result, "sql"
        except Exception as e:
            print(f"SQL Error: {e}")

        # 3. Try R
        try:
            result = subprocess.run(
                ["Rscript", "-e", query], capture_output=True, text=True
            )
            if result.returncode == 0:
                print(result.stdout)
                return result.stdout, "r"
            else:
                print(f"R Error: {result.stderr}")
        except Exception as e:
            pass

        # If all engines fail, ask the LLM
        print("Direct execution failed. Asking LLM for SQL query...")
        llm_prompt = f"""
        The user entered the following query which could not be executed directly using pandas, SQL, R, Scala, or PySpark:
        ```
        {query}
        ```

        The available tables in the SQLite database at {db_path} are:
        ```sql
        {get_available_tables(db_path)}
        ```

        Please provide a valid SQL query that accomplishes the user's intent.  If the query requires data from a file, provide instructions on how to load the data into a table first.
        Return only the SQL query, or instructions for loading data followed by the SQL query.
        """

        llm_response = get_llm_response(llm_prompt, npc=npc)

        print(f"LLM suggested SQL: {llm_response}")
        command = llm_response.get("response", "")
        if command == "":
            return "LLM did not provide a valid SQL query.", None
        # Execute the LLM-generated SQL
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(command)
                result = cursor.fetchall()
                if result:
                    for row in result:
                        print(row)
                    return result, "llm"
        except Exception as e:
            print(f"Error executing LLM-generated SQL: {e}")
            return f"Error executing LLM-generated SQL: {e}", None

    except Exception as e:
        print(f"Error executing query: {e}")
        return f"Error executing query: {e}", None


def get_available_tables(db_path: str) -> str:
    """
    Function Description:
        This function gets the available tables in the database.
    Args:
        db_path (str): The database path.
    Keyword Args:
        None
    Returns:
        str: The available tables in the database.
    """

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name != 'command_history'"
            )
            tables = cursor.fetchall()

            return tables
    except Exception as e:
        print(f"Error getting available tables: {e}")
        return ""


def execute_llm_command(
    command: str,
    command_history: Any,
    model: Optional[str] = None,
    provider: Optional[str] = None,
    npc: Optional[Any] = None,
    messages: Optional[List[Dict[str, str]]] = None,
    retrieved_docs=None,
    n_docs=5,
) -> str:
    """
    Function Description:
        This function executes an LLM command.
    Args:
        command (str): The command to execute.
        command_history (Any): The command history.
    Keyword Args:
        model (Optional[str]): The model to use for executing the command.
        provider (Optional[str]): The provider to use for executing the command.
        npc (Optional[Any]): The NPC object.
        messages (Optional[List[Dict[str, str]]): The list of messages.
        retrieved_docs (Optional): The retrieved documents.
        n_docs (int): The number of documents.
    Returns:
        str: The result of the LLM command.
    """

    max_attempts = 5
    attempt = 0
    subcommands = []
    npc_name = npc.name if npc else "sibiji"
    location = os.getcwd()
    print(f"{npc_name} generating command")
    # Create context from retrieved documents
    context = ""
    if retrieved_docs:
        for filename, content in retrieved_docs[:n_docs]:
            # print(f"Document: {filename}")
            # print(content)
            context += f"Document: {filename}\n{content}\n\n"
        context = f"Refer to the following documents for context:\n{context}\n\n"
    while attempt < max_attempts:
        prompt = f"""
        A user submitted this query: {command}.
        You need to generate a bash command that will accomplish the user's intent.
        Respond ONLY with the command that should be executed.
        in the json key "bash_command".
        You must reply with valid json and nothing else. Do not include markdown formatting
        """
        if len(context) > 0:
            prompt += f"""
            What follows is the context of the text files in the user's directory that are potentially relevant to their request
            Use these to help inform your decision.
            {context}
            """
        if len(messages) > 0:
            prompt += f"""
            The following messages have been exchanged between the user and the assistant:
            {messages}
            """

        response = get_llm_response(
            prompt,
            model=model,
            provider=provider,
            messages=[],
            npc=npc,
            format="json",
        )

        llm_response = response.get("response", {})
        # messages.append({"role": "assistant", "content": llm_response})
        # print(f"LLM response type: {type(llm_response)}")
        # print(f"LLM response: {llm_response}")

        try:
            if isinstance(llm_response, str):
                llm_response = json.loads(llm_response)

            if isinstance(llm_response, dict) and "bash_command" in llm_response:
                bash_command = llm_response["bash_command"]
            else:
                raise ValueError("Invalid response format from LLM")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error parsing LLM response: {e}")
            attempt += 1
            continue

        print(f"LLM suggests the following bash command: {bash_command}")
        subcommands.append(bash_command)

        try:
            print(f"Running command: {bash_command}")
            result = subprocess.run(
                bash_command, shell=True, text=True, capture_output=True, check=True
            )
            print(f"Command executed with output: {result.stdout}")

            prompt = f"""
                Here was the output of the result for the {command} inquiry
                which ran this bash command {bash_command}:

                {result.stdout}

                Provide a simple response to the user that explains to them
                what you did and how it accomplishes what they asked for.
                """
            if len(context) > 0:
                prompt += f"""
                What follows is the context of the text files in the user's directory that are potentially relevant to their request
                Use these to help inform how you respond.
                You must read the context and use it to provide the user with a more helpful answer related to their specific text data.

                CONTEXT:

                {context}
                """

            response = get_llm_response(
                prompt,
                model=model,
                provider=provider,
                npc=npc,
                messages=messages,
            )

            output = response.get("response", "")

            # render_markdown(output)
            command_history.add_command(command, subcommands, output, location)

            return {"messages": messages, "output": output}
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error:")
            print(e.stderr)

            error_prompt = f"""
            The command '{bash_command}' failed with the following error:
            {e.stderr}
            Please suggest a fix or an alternative command.
            Respond with a JSON object containing the key "bash_command" with the suggested command.
            Do not include any additional markdown formatting.

            """

            if len(context) > 0:
                error_prompt += f"""
                    What follows is the context of the text files in the user's directory that are potentially relevant to their request
                    Use these to help inform your decision.
                    {context}
                    """

            fix_suggestion = get_llm_response(
                error_prompt,
                model=model,
                provider=provider,
                npc=npc,
                format="json",
                messages=messages,
            )

            fix_suggestion_response = fix_suggestion.get("response", {})

            try:
                if isinstance(fix_suggestion_response, str):
                    fix_suggestion_response = json.loads(fix_suggestion_response)

                if (
                    isinstance(fix_suggestion_response, dict)
                    and "bash_command" in fix_suggestion_response
                ):
                    print(
                        f"LLM suggests fix: {fix_suggestion_response['bash_command']}"
                    )
                    command = fix_suggestion_response["bash_command"]
                else:
                    raise ValueError(
                        "Invalid response format from LLM for fix suggestion"
                    )
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error parsing LLM fix suggestion: {e}")

        attempt += 1

    command_history.add_command(command, subcommands, "Execution failed", location)
    return {
        "messages": messages,
        "output": "Max attempts reached. Unable to execute the command successfully.",
    }


def handle_agent_call(
    command: str,
    command_history: Any,
    model: str = npcsh_model,
    provider: str = npcsh_provider,
    npc: Any = None,
    retrieved_docs=None,
    messages: List[Dict[str, str]] = None,
    n_docs=5,
):
    return


def check_llm_command(
    command: str,
    command_history: Any,
    model: str = npcsh_model,
    provider: str = npcsh_provider,
    npc: Any = None,
    retrieved_docs=None,
    messages: List[Dict[str, str]] = None,
    n_docs=5,
):
    """
    Function Description:
        This function checks an LLM command.
    Args:
        command (str): The command to check.
        command_history (Any): The command history.
    Keyword Args:
        model (str): The model to use for checking the command.
        provider (str): The provider to use for checking the command.
        npc (Any): The NPC object.
        retrieved_docs (Any): The retrieved documents.
        n_docs (int): The number of documents.
    Returns:
        Any: The result of checking the LLM command.
    """

    if messages is None:
        messages = []

    # print(model, provider, npc)
    # Create context from retrieved documents
    context = ""

    if retrieved_docs:
        for filename, content in retrieved_docs[:n_docs]:
            context += f"Document: {filename}\n{content}\n\n"
        context = f"Refer to the following documents for context:\n{context}\n\n"

    prompt = f"""
    A user submitted this query: {command}
    Determine the nature of the user's request:
    1. Is it a specific request for a task that could be accomplished via a bash command or a simple python script that could be executed in a single bash call?
    2. Should a tool be invoked to fulfill the request?
    3. Is it a general question that requires an informative answer?
    4. Would this question be best answered by an alternative NPC?
    5. Is it a complex request that actually requires more than one
    tool to be called, perhaps in a sequence?

    Available tools:
    """
    if npc.tools_dict is None:
        prompt += "No tools available."
    else:
        for tool_name, tool in npc.tools_dict.items():
            prompt += f"""
            {tool_name} : {tool.description} \n
        """
    prompt += f"""
    Available NPCs for alternative answers:

    """
    if len(npc.resolved_npcs) == 0:
        prompt += "No NPCs available for alternative answers."
    else:
        for i, npc_in_network in enumerate(npc.resolved_npcs):
            prompt += f"""
            ({i})

            NPC: {npc_in_network['name']}
            Primary Directive : {npc_in_network['primary_directive']}

            """
    # print(prompt)

    prompt += f"""
    In considering how to answer this, consider:
    - Whether it can be answered via a bash command on the user's computer.
    - Whether a tool should be used.

    Respond with a JSON object containing:
    - "action": one of ["execute_command", "invoke_tool", "answer_question", "pass_to_npc", "execute_sequence"]
    - "tool_name": : if action is "invoke_tool": the name of the tool to use.
                     else if action is "execute_sequence", a list of tool names to use.
    - "explanation": a brief explanation of why you chose this action.
    - "npc_name": (if action is "pass_to_npc") the name of the NPC to pass the question to.


    Return only the JSON object. Do not include any additional text.

    The format of the JSON object is:
    {{
        "action": "execute_command" | "invoke_tool" | "answer_question" | "pass_to_npc" | "execute_sequence",
        "tool_name": "<tool_name(s)_if_applicable>",
        "explanation": "<your_explanation>",
        "npc_name": "<npc_name_if_applicable>"
    }}

    Remember, do not include ANY ADDITIONAL MARKDOWN FORMATTING. There should be no prefix 'json'. Start straight with the opening curly brace.
    """

    if context:
        prompt += f"""
        Relevant context from user's files:
        {context}
        """
    # print(prompt)

    try:
        # For action determination, we don't need to pass the conversation messages to avoid confusion
        # print(npc, model, provider)
        action_response = get_llm_response(
            prompt,
            model=model,
            provider=provider,
            npc=npc,
            format="json",
            messages=[],
        )
        # print(action_response)
        if "Error" in action_response:
            print(f"LLM Error: {action_response['error']}")
            return action_response["error"]

        response_content = action_response.get("response", {})

        if isinstance(response_content, str):
            try:
                response_content_parsed = json.loads(response_content)
            except json.JSONDecodeError as e:
                print(
                    f"Invalid JSON received from LLM: {e}. Response was: {response_content}"
                )
                return f"Error: Invalid JSON from LLM: {response_content}"
        else:
            response_content_parsed = response_content

        # Proceed according to the action specified
        action = response_content_parsed.get("action")

        # Include the user's command in the conversation messages

        if action == "execute_command":
            # Pass messages to execute_llm_command
            result = execute_llm_command(
                command,
                command_history,
                model=model,
                provider=provider,
                messages=[],
                npc=npc,
                retrieved_docs=retrieved_docs,
            )

            output = result.get("output", "")
            messages = result.get("messages", messages)
            return {"messages": messages, "output": output}

        elif action == "invoke_tool":
            tool_name = response_content_parsed.get("tool_name")
            # print(npc)
            result = handle_tool_call(
                command,
                tool_name,
                command_history,
                model=model,
                provider=provider,
                messages=messages,
                npc=npc,
                retrieved_docs=retrieved_docs,
            )
            messages = result.get("messages", messages)
            output = result.get("output", "")
            return {"messages": messages, "output": output}

        elif action == "answer_question":
            result = execute_llm_question(
                command,
                command_history,
                model=model,
                provider=provider,
                messages=messages,
                npc=npc,
                retrieved_docs=retrieved_docs,
            )
            messages = result.get("messages", messages)
            output = result.get("output", "")
            return {"messages": messages, "output": output}
        elif action == "pass_to_npc":
            npc_to_pass = response_content_parsed.get("npc_name")
            # print(npc)

            return npc.handle_agent_pass(
                npc_to_pass,
                command,
                command_history,
                messages=messages,
                retrieved_docs=retrieved_docs,
                n_docs=n_docs,
            )
        elif action == "execute_sequence":
            tool_names = response_content_parsed.get("tool_name")
            output = ""
            results_tool_calls = []
            for tool_name in tool_names:
                result = handle_tool_call(
                    command,
                    tool_name,
                    command_history,
                    model=model,
                    provider=provider,
                    messages=messages,
                    npc=npc,
                    retrieved_docs=retrieved_docs,
                )
                results_tool_calls.append(result)
                messages = result.get("messages", messages)
                output += result.get("output", "")
            # import pdb

            # pdb.set_trace()
            return {"messages": messages, "output": output}
        else:
            print("Error: Invalid action in LLM response")
            return "Error: Invalid action in LLM response"

    except Exception as e:
        print(result)
        print(type(result))
        print(f"Error in check_llm_command: {e}")
        return f"Error: {e}"


def handle_tool_call(
    command: str,
    tool_name: str,
    command_history: Any,
    model: str = npcsh_model,
    provider: str = npcsh_provider,
    messages: List[Dict[str, str]] = None,
    npc: Any = None,
    retrieved_docs=None,
    n_docs: int = 5,
) -> Union[str, Dict[str, Any]]:
    """
    Function Description:
        This function handles a tool call.
    Args:
        command (str): The command.
        tool_name (str): The tool name.
        command_history (Any): The command history.
    Keyword Args:
        model (str): The model to use for handling the tool call.
        provider (str): The provider to use for handling the tool call.
        messages (List[Dict[str, str]]): The list of messages.
        npc (Any): The NPC object.
        retrieved_docs (Any): The retrieved documents.
        n_docs (int): The number of documents.
    Returns:
        Union[str, Dict[str, Any]]: The result of handling
        the tool call.

    """
    print(f"handle_tool_call invoked with tool_name: {tool_name}")
    # print(npc)
    if not npc or not npc.tools_dict:
        print("not available")
        available_tools = npc.tools_dict if npc else None
        print(
            f"No tools available for NPC '{npc.name}' or tools_dict is empty. Available tools: {available_tools}"
        )
        return f"No tools are available for NPC '{npc.name or 'default'}'."

    if tool_name not in npc.tools_dict:
        print("not available")
        print(f"Tool '{tool_name}' not found in NPC's tools_dict.")
        print("available tools", npc.tools_dict)
        return f"Tool '{tool_name}' not found."

    tool = npc.tools_dict[tool_name]
    print(f"Tool found: {tool.tool_name}")
    jinja_env = Environment(loader=FileSystemLoader("."), undefined=Undefined)

    prompt = f"""
    The user wants to use the tool '{tool_name}' with the following request:
    '{command}'
    Here is the tool file:
    {tool}

    Please extract the required inputs for the tool as a JSON object.
    Return only the JSON object without any markdown formatting.
    """
    if npc and hasattr(npc, "shared_context"):
        if npc.shared_context.get("dataframes"):
            context_info = "\nAvailable dataframes:\n"
            for df_name in npc.shared_context["dataframes"].keys():
                context_info += f"- {df_name}\n"
            prompt += f"""Here is contextual info that may affect your choice: {context_info}
            """

    # print(f"Tool prompt: {prompt}")
    response = get_llm_response(
        prompt,
        format="json",
        model=model,
        provider=provider,
        npc=npc,
    )
    try:
        # Clean the response of markdown formatting
        response_text = response.get("response", "{}")
        if isinstance(response_text, str):
            response_text = (
                response_text.replace("```json", "").replace("```", "").strip()
            )

        # Parse the cleaned response
        if isinstance(response_text, dict):
            input_values = response_text
        else:
            input_values = json.loads(response_text)
        # print(f"Extracted inputs: {input_values}")
    except json.JSONDecodeError as e:
        print(f"Error decoding input values: {e}. Raw response: {response}")
        return f"Error extracting inputs for tool '{tool_name}'"
    # Input validation (example):
    required_inputs = tool.inputs
    missing_inputs = []
    for inp in required_inputs:
        if not isinstance(inp, dict):
            # dicts contain the keywords so its fine if theyre missing from the inputs.
            if inp not in input_values:
                missing_inputs.append(inp)
    if len(missing_inputs) > 0:
        print(f"Missing required inputs for tool '{tool_name}': {missing_inputs}")
        return f"Missing inputs for tool '{tool_name}': {missing_inputs}"

    # try:
    tool_output = tool.execute(
        input_values, npc.tools_dict, jinja_env, command, npc=npc
    )
    # print(f"Tool output: {tool_output}")
    # render_markdown(str(tool_output))
    if messages is not None:  # Check if messages is not None
        messages.append({"role": "assistant", "content": str(tool_output)})
    return {"messages": messages, "output": tool_output}
    # except Exception as e:
    #    print(f"Error executing tool {tool_name}: {e}")
    #    return f"Error executing tool {tool_name}: {e}"


def execute_llm_question(
    command: str,
    command_history: Any,
    model: str = npcsh_model,
    provider: str = npcsh_provider,
    npc: Any = None,
    messages: List[Dict[str, str]] = None,
    retrieved_docs=None,
    n_docs: int = 5,
):
    location = os.getcwd()
    if messages is None or len(messages) == 0:
        messages = []
        messages.append({"role": "user", "content": command})

    # Build context from retrieved documents
    if retrieved_docs:
        context = ""
        for filename, content in retrieved_docs[:n_docs]:
            context += f"Document: {filename}\n{content}\n\n"
        context_message = f"""
        What follows is the context of the text files in the user's directory that are potentially relevant to their request:
        {context}
        """
        # Add context as a system message
        # messages.append({"role": "system", "content": context_message})

    # Append the user's message to messages

    # Print messages before calling get_conversation for debugging
    # print("Messages before get_conversation:", messages)

    # Use the existing messages list
    response = get_conversation(messages, model=model, provider=provider, npc=npc)

    # Print response from get_conversation for debugging
    # print("Response from get_conversation:", response)

    if isinstance(response, str) and "Error" in response:
        output = response
    elif isinstance(response, list) and len(response) > 0:
        messages = response  # Update messages with the new conversation
        output = response[-1]["content"]
    else:
        output = "Error: Invalid response from conversation function"

    # render_markdown(output)
    # print(f"LLM response: {output}")
    # print(f"Messages: {messages}")
    # print("type of output", type(output))
    command_history.add_command(command, [], output, location)
    return {"messages": messages, "output": output}


def generate_plonk(
    request,
):
    prompt = f"""

    A user asked the following question: {request}

    You are in charge of creating a plonk plan that will handle their request.
    This plonk plan will be a series of steps that you will write that will be
    used to generate a fully functioning system that will accomplish the user's request.
    your plonk plan should be a python script that generates LLM prompts
    that will be used to generate the distinct pieces of software.

    The goal here is modularization, abstraction, separation of scales.
    A careful set of instructions can pave the way for a system that can be iterated on
    and improved with successive steps.

    Here is an example of a question and answer that you might generate:

    Question: "Set up an automation system that will open a web browser every morning
        and go to my bank account and export my transactions."

    Answer:
    "{{'plonk plan': ```

from npcsh.llm_funcs import get_llm_response

automation_script = get_llm_response( '''
    Write a python script that will request input from a user about what bank they use. Then use selenium to open the browser and navigate to the bank's website.
    Get the user's username and password and log in, also through raw input.
    Then navigate to the transactions page and export the transactions. Ensure you are sufficiently logging information at each step of the way so that the results can be
    debugged efficiently.
    Return the script without any additional comment or Markdown formatting. It is imperative that you do not include any additional text.
''')
# write the automation script to a file
automation_script_file = open('automation_script.py', 'w')
automation_script_file.write(automation_script)
automation_script_file.close()


scheduling_script = get_llm_response( f'''
    Write a bash script that will set up an OS scheduler to run the automation script every morning at 8 am.
    The automation script is located at ./automation_script.py.
    You'll need to ensure that the full path is used in the scheduling script.
    Return the script without any additional comment or Markdown formatting.
    It is imperative that you do not include any additional text.
    Do not leave any placeholder paths or variables in the script.
    They must be able to execute without
    any further modification by you or the user.
    ''')
# write the scheduling script to a file
scheduling_script_file = open('scheduling_script.sh', 'w')
scheduling_script_file.write(scheduling_script)

scheduling_script_file.close()
# attempt to run the scheduling script
import subprocess
subprocess.run(['bash', 'scheduling_script.sh'])
```}}

    In this example, we have set up a plan that will require multiple other LLM calls to generate the necessary items to
    accomplish the user's request.

    """

    return get_llm_response(prompt)


def execute_plonk(plan):
    return


def debug_plonk(prompt, plan):
    results = execute_plonk(plan)

    ea = f""" here was a user's prompt: {prompt}
    Here is the plonk plan that was generated: {plan}


    Here were the results of that investigation:
    {results}


    Please adjust the plonk plan accordingly so that it can be
    used again to generate the necessary items to accomplish the user's request.


    """

    return get_llm_response(ea)
