import openai

API_KEY = "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"

openai.api_key = API_KEY
completion = openai.Completion()

def engines():
    return openai.Engine.list()

def ask(message, engine, temperature, max_tokens, top_p, presence_penalty):
    response = openai.Completion.create(
        engine=engine,
        prompt=message,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        presence_penalty=presence_penalty,
        stop="\n"
    )
    return str(response.choices[0].text)