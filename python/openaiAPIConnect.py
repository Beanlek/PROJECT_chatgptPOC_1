import openai

API_KEY = open('./key.txt', 'r')
PROMPT_FILE = open('./Prompts/prompt_for_transferring_into_arrayInPython.txt', 'r')

openai.api_key = API_KEY.read()
PROMPT = PROMPT_FILE.read()

model_engine = "text-davinci-003"
prompt = PROMPT

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 2024,
    n = 1,
    stop = None,
    temperature = 0.5
)

response = completion.choices[0].text
print(response)