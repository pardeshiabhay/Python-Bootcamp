from openai import OpenAI

client = OpenAI(
  api_key=""
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "What is coding"}
  ]
)


print(completion.choices[0].message)
