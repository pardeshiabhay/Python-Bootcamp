from openai import OpenAI

client = OpenAI(
  api_key=""
)
command = '''
'''
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": ""},
    {"role": "user", "content": command }
  ]
)

response = completion.choices[0].message.content
print(response)


