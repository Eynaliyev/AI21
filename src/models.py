import os
from langchain.llms import AI21
# from dotenv import load_dotenv, find_dotenv
# from langchain.chat_models import ChatOpenAI

# _ = load_dotenv(find_dotenv())
# openai_api_key = os.getenv("OPENAI_API_KEY")


def create_models():
    return [
        # {
        #     "model_name": 'j2-jumbo-instruct',
        #     "model_provider": "AI21",
        #     "model": AI21(model="j2-jumbo-instruct")
        # },
        {
            "model_name": 'gpt-3.5-turbo',
            "model_provider": "OpenAI",
            # "model": ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model_name='gpt-3.5-turbo')
        },
        {
            "model_name": 'gpt-4',
            "model_provider": "OpenAI",
            # "model": ChatOpenAI(temperature=0, model_name='gpt-4')
        },
]

models = create_models()


def get_model_by_name(model_name):
    for model_obj in models:
        if model_obj["model_name"] == model_name:
            return model_obj
    raise ValueError(f"Unsupported model name: {model_name}")