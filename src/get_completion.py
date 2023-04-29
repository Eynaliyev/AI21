from get_openai_completion import get_completion as get_openai_completion
from models import get_model_by_name

def get_completion(prompt, model_name="openai-gpt-3.5-turbo"):
    if model_name == "gpt-3.5-turbo":
        return get_openai_completion(prompt)
    if model_name == "gpt-4":
        return get_openai_completion(prompt, model_name=model_name)
    elif model_name == "another-llm":
        # Call the appropriate function for another LLM here
        # and return the response
        pass
    else:
        model_obj = get_model_by_name(model_name)
        model = model_obj["model"]
        print(model)
        print('model name', model_name)
        model(prompt)