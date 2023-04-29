from joblib import Memory
from models import get_model_by_name

# Set up caching
memory = Memory("./cache", verbose=0)

def get_completion(prompt, model_name="openai-gpt-3.5-turbo"):
    model_obj = get_model_by_name(model_name)
    model = model_obj["model"]
    return model(prompt)

cached_get_completion = memory.cache(get_completion)

# Replace the original get_completion function with the cached version
get_completion = cached_get_completion
