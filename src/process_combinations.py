from dotenv import load_dotenv, find_dotenv
from models import models
from tasks import prompts

from store_results import store_results
from call_agent import call_agent

_ = load_dotenv(find_dotenv())

# Create a function to process different combinations of agent and evaluator models
def process_prompts(agent_model_name, evaluator_model_name):
    responses = []
    evaluations = []
    helpfulness = []
    honesty = []
    harmlessness = []
    factuality = []
    effectiveness = []

    # Step 2: Call Agent with a set of prompts
    call_agent(
        responses=responses,
        evaluations=evaluations,
        helpfulness=helpfulness,
        honesty=honesty,
        harmlessness=harmlessness,
        factuality=factuality,
        effectiveness=effectiveness,
        agent_model_name=agent_model_name,
        evaluator_model_name=evaluator_model_name
    )

    # Step 3: Store its performance in a pandas DataFrame/CSV
    store_results(
        prompts=prompts,
        responses=responses,
        evaluations=evaluations,
        helpfulness=helpfulness,
        honesty=honesty,
        harmlessness=harmlessness,
        factuality=factuality,
        effectiveness=effectiveness,
        agent_model_name=agent_model_name,
        evaluator_model_name=evaluator_model_name
    )


def process_combinations():
  # Iterate over combinations of agent and evaluator models
  for agent_model in models:
      for evaluator_model in models:
          print(f"Processing combination: {agent_model['model_name']} (agent) and {evaluator_model['model_name']} (evaluator)")
          process_prompts(agent_model['model_name'], evaluator_model['model_name'])
