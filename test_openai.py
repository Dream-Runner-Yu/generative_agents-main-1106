import openai

openai.api_key = "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"


def chat_gpt(prompt):
    prompt = prompt
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        timeout=1000,
    )

    response = completion.choices[0].text
    print(response)


chat_gpt("现在几点了")