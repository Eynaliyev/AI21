from get_completion import get_completion
from evaluate_performance import evaluate_performance
from tasks import prompts

def call_agent(
        responses, evaluations, helpfulness, honesty, harmlessness, factuality, effectiveness, agent_model_name, evaluator_model_name):
    for prompt_dict in prompts:
        task = prompt_dict['task']
        response = get_completion(task, model_name=agent_model_name)
        evaluation = evaluate_performance(task, response, model_name=evaluator_model_name)
        
        responses.append(response)
        evaluations.append(evaluation)
        helpfulness.append(evaluation["helpfulness"])
        honesty.append(evaluation["honesty"])
        harmlessness.append(evaluation["harmlessness"])
        factuality.append(evaluation["factuality"])
        effectiveness.append(evaluation["effectiveness"])