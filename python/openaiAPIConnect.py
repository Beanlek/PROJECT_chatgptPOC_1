import openai

openai.api_key = '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'

model_engine = "text-davinci-003"
prompt = "Hello, how are you Robot?"

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5
)

response = completion.choices[0].text
print(response)