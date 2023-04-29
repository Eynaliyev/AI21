# first line: 11
def get_completion(prompt, model_name="openai-gpt-3.5-turbo"):
    # try:
        # if model_name == "gpt-3.5-turbo":
        #     return get_openai_completion(prompt)
        # if model_name == "gpt-4":
        #     return get_openai_completion(prompt, model_name=model_name)
        # elif model_name == "another-llm":
        #     # Call the appropriate function for another LLM here
        #     # and return the response
        #     pass
        # else:
    model_obj = get_model_by_name(model_name)
    model_provider = model_obj['model_provider']
    model = model_obj["model"]
    if model_provider == "OpenAI":
        chat_result = model.generate([HumanMessage(content=prompt)])
        response = chat_result.generations[0].message.content
        return response
    else:
        return model(prompt)
