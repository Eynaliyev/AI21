from langchain.prompts import PromptTemplate

templates = {
    "summarization_template": PromptTemplate(
            input_variables=["text"],
            template="Summarize the text delimited by triple quotes into a single sentence. \
            ```{text}```",
        ),
    "condition_satisfaction_template": PromptTemplate(
            input_variables=["text"],
            template="""You will be provided with text delimited by triple quotes. 
                    If it contains a sequence of instructions, \ 
                    re-write those instructions in the following format:

                    Step 1 - ...
                    Step 2 - …
                    …
                    Step N - …

                    If the text does not contain a sequence of instructions, \ 
                    then simply write \"No steps provided.\"

                    \"\"\"{text}\"\"\"
            """,
        ),
    "complex_task_with_specified_steps_template": PromptTemplate(
            input_variables=["text"],
            template="""Perform the following actions: 
                1 - Summarize the following text delimited by triple \
                backticks with 1 sentence.
                2 - Translate the summary into French.
                3 - List each name in the French summary.
                4 - Output a json object that contains the following \
                keys: french_summary, num_names.

                Separate your answers with line breaks.

                Text:
                ```{text}```
            """
        ),
    "output_in_specified_format_template":  PromptTemplate(
            input_variables=["text"],
            template="""
                Your task is to perform the following actions: 
                1 - Summarize the following text delimited by 
                <> with 1 sentence.
                2 - Translate the summary into French.
                3 - List each name in the French summary.
                4 - Output a json object that contains the 
                following keys: french_summary, num_names.

                Use the following format:
                Text: <text to summarize>
                Summary: <summary>
                Translation: <summary translation>
                Names: <list of names in Italian summary>
                Output JSON: <json with summary and num_names>

                Text: <{text}>
            """
        ),
        "generate_description_from_factsheet_template": PromptTemplate(
            input_variables=["text"],
            template="""
                Your task is to help a marketing team create a 
                description for a retail website of a product based 
                on a technical fact sheet.

                Write a product description based on the information 
                provided in the technical specifications delimited by 
                triple backticks.

                Technical specifications: ```{text}```
            """
        ),
}

summarization_prompts = [
    """
        You should express what you want a model to do by \ 
        providing instructions that are as clear and \ 
        specific as you can possibly make them. \ 
        This will guide the model towards the desired output, \ 
        and reduce the chances of receiving irrelevant \ 
        or incorrect responses. Don't confuse writing a \ 
        clear prompt with writing a short prompt. \ 
        In many cases, longer prompts provide more clarity \ 
        and context for the model, which can lead to \ 
        more detailed and relevant outputs.
    """,
]

output_parsing_prompts = [
    """
        Generate a list of three made-up book titles along \ 
        with their authors and genres. 
        Provide them in JSON format with the following keys: 
        book_id, title, author, genre.
    """,
]

condition_satisfaction_check_prompts = [
    """
        Making a cup of tea is easy! First, you need to get some \ 
        water boiling. While that's happening, \ 
        grab a cup and put a tea bag in it. Once the water is \ 
        hot enough, just pour it over the tea bag. \ 
        Let it sit for a bit so the tea can steep. After a \ 
        few minutes, take out the tea bag. If you \ 
        like, you can add some sugar or milk to taste. \ 
        And that's it! You've got yourself a delicious \ 
        cup of tea to enjoy.
    """,
    """
        The sun is shining brightly today, and the birds are \
        singing. It's a beautiful day to go for a \ 
        walk in the park. The flowers are blooming, and the \ 
        trees are swaying gently in the breeze. People \ 
        are out and about, enjoying the lovely weather. \ 
        Some are having picnics, while others are playing \ 
        games or simply relaxing on the grass. It's a \ 
        perfect day to spend time outdoors and appreciate the \ 
        beauty of nature.
    """
]

few_shot_promts = [
    """
        Your task is to answer in a consistent style.

        <child>: Teach me about patience.

        <grandparent>: The river that carves the deepest \ 
        valley flows from a modest spring; the \ 
        grandest symphony originates from a single note; \ 
        the most intricate tapestry begins with a solitary thread.

        <child>: Teach me about resilience.
    """
]

complex_task_with_specified_steps_prompts = [
    """
        In a charming village, siblings Jack and Jill set out on \ 
        a quest to fetch water from a hilltop \ 
        well. As they climbed, singing joyfully, misfortune \ 
        struck—Jack tripped on a stone and tumbled \ 
        down the hill, with Jill following suit. \ 
        Though slightly battered, the pair returned home to \ 
        comforting embraces. Despite the mishap, \ 
        their adventurous spirits remained undimmed, and they \ 
        continued exploring with delight.
    """
]

math_problem_without_thinking_prompts = [
    """
        Determine if the student's solution is correct or not.

        Question:
        I'm building a solar power installation and I need \
        help working out the financials. 
        - Land costs $100 / square foot
        - I can buy solar panels for $250 / square foot
        - I negotiated a contract for maintenance that will cost \ 
        me a flat $100k per year, and an additional $10 / square \
        foot
        What is the total cost for the first year of operations 
        as a function of the number of square feet.

        Student's Solution:
        Let x be the size of the installation in square feet.
        Costs:
        1. Land cost: 100x
        2. Solar panel cost: 250x
        3. Maintenance cost: 100,000 + 100x
        Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    """
]

math_problem_with_thinking_prompts = [
    """
        Your task is to determine if the student's solution \
        is correct or not.
        To solve the problem do the following:
        - First, work out your own solution to the problem. 
        - Then compare your solution to the student's solution \ 
        and evaluate if the student's solution is correct or not. 
        Don't decide if the student's solution is correct until 
        you have done the problem yourself.

        Use the following format:
        Question:
        ```
        question here
        ```
        Student's solution:
        ```
        student's solution here
        ```
        Actual solution:
        ```
        steps to work out the solution and your solution here
        ```
        Is the student's solution the same as actual solution \
        just calculated:
        ```
        yes or no
        ```
        Student grade:
        ```
        correct or incorrect
        ```

        Question:
        ```
        I'm building a solar power installation and I need help \
        working out the financials. 
        - Land costs $100 / square foot
        - I can buy solar panels for $250 / square foot
        - I negotiated a contract for maintenance that will cost \
        me a flat $100k per year, and an additional $10 / square \
        foot
        What is the total cost for the first year of operations \
        as a function of the number of square feet.
        ``` 
        Student's solution:
        ```
        Let x be the size of the installation in square feet.
        Costs:
        1. Land cost: 100x
        2. Solar panel cost: 250x
        3. Maintenance cost: 100,000 + 100x
        Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
        ```
        Actual solution:
    """
]

hallucination_prompts = [
    """
        Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
    """
]

generate_description_from_factsheet_prompts = [
    """
        OVERVIEW
        - Part of a beautiful family of mid-century inspired office furniture, 
        including filing cabinets, desks, bookcases, meeting tables, and more.
        - Several options of shell color and base finishes.
        - Available with plastic back and front upholstery (SWC-100) 
        or full upholstery (SWC-110) in 10 fabric and 6 leather options.
        - Base finish options are: stainless steel, matte black, 
        gloss white, or chrome.
        - Chair is available with or without armrests.
        - Suitable for home or business settings.
        - Qualified for contract use.

        CONSTRUCTION
        - 5-wheel plastic coated aluminum base.
        - Pneumatic chair adjust for easy raise/lower action.

        DIMENSIONS
        - WIDTH 53 CM | 20.87”
        - DEPTH 51 CM | 20.08”
        - HEIGHT 80 CM | 31.50”
        - SEAT HEIGHT 44 CM | 17.32”
        - SEAT DEPTH 41 CM | 16.14”

        OPTIONS
        - Soft or hard-floor caster options.
        - Two choices of seat foam densities: 
        medium (1.8 lb/ft3) or high (2.8 lb/ft3)
        - Armless or 8 position PU armrests 

        MATERIALS
        SHELL BASE GLIDER
        - Cast Aluminum with modified nylon PA6/PA66 coating.
        - Shell thickness: 10 mm.
        SEAT
        - HD36 foam

        COUNTRY OF ORIGIN
        - Italy
    """
]

prompts = [
    {
        "task": templates['summarization_template'].format(text=summarization_prompts[0]),
        "category": "summarization",
        "id": 0
    },
    {
        "task": output_parsing_prompts[0],
        "category": "output_parsing Parsing",
        "id": 1
    },
    {
        "task": templates['condition_satisfaction_template'].format(text=condition_satisfaction_check_prompts[0]),
        "category": "condition_satisfaction_check",
        "id": 2
    },
    {
        "task": templates['condition_satisfaction_template'].format(text=condition_satisfaction_check_prompts[1]),
        "category": "condition_satisfaction_check",
        "id": 3
    },
    {
        "task": few_shot_promts[0],
        "category": "few_shot",
        "id": 4
    },
    {
        "task": templates['complex_task_with_specified_steps_template'].format(text=complex_task_with_specified_steps_prompts[0]),
        "category": "complex_task_with_specified_steps",
        "id": 5
    },
    {
        "task": templates['output_in_specified_format_template'].format(text=complex_task_with_specified_steps_prompts[0]),
        "category": "output_in_specified_format",
        "id": 6
    },
    {
        "task": math_problem_without_thinking_prompts[0],
        "category": "math_problem_without_thinking",
        "id": 7
    },
    {
        "task": math_problem_with_thinking_prompts[0],
        "category": "math_problem_with_thinking",
        "id": 8
    },
    {
        "task": hallucination_prompts[0],
        "category": "hallucination",
        "id": 9
    },
    {
        "task": templates['generate_description_from_factsheet_template'].format(text=generate_description_from_factsheet_prompts[0]),
        "category": "generate_description_from_factsheet",
        "id": 10
    },
]