import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}]
)

print(response.choices[0].message["content"])
