import os
import pandas as pd
from config import RESPONSES_CSV_PATH

def one_hot_encode_models(data):
    one_hot_llm = pd.get_dummies(data['Model'], prefix='LLM')
    one_hot_evaluator = pd.get_dummies(data['Evaluator'], prefix='Evaluator')
    encoded_data = pd.concat([data, one_hot_llm, one_hot_evaluator], axis=1)
    return encoded_data

def store_results(prompts, responses, evaluations, helpfulness, honesty, harmlessness, factuality, effectiveness, agent_model_name, evaluator_model_name): 
    data = {
        "Task": [p["task"] for p in prompts],
        "Category": [p["category"] for p in prompts],
        "Response": responses,
        "Performance Evaluation": evaluations,
        "Helpfulness": helpfulness,
        "Honesty": honesty,
        "Harmlessness": harmlessness,
        "Factuality": factuality,
        "Effectiveness": effectiveness,
        "Model": agent_model_name,
        "Evaluator": evaluator_model_name
    }

    df = pd.DataFrame(data)
    
    # One-hot encode the models and evaluators
    encoded_data = one_hot_encode_models(df)

    # Check if the CSV file exists
    if os.path.exists(RESPONSES_CSV_PATH):
        # If it exists, append the new data without writing the header again
        encoded_data.to_csv(RESPONSES_CSV_PATH, mode='a', header=False, index=False)
    else:
        # If it doesn't exist, create a new file with the header
        encoded_data.to_csv(RESPONSES_CSV_PATH, index=False)
