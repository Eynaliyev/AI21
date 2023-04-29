# first line: 7
def get_completion(prompt, model_name="openai-gpt-3.5-turbo"):
    print("calling api")
    model_obj = get_model_by_name(model_name)
    model = model_obj["model"]
    return model(prompt)
