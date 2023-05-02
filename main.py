

import os
import openai

import OPEN_API_KEY

openai.api_key = OPEN_API_KEY.mykey

# inta = "respond with a singular yes or no. Does pizza belong on pineapple?"


# response = openai.Completion.create(
# engine="gpt-3.5-turbo",
# temperature=0.7,
# max_tokens=709,
# top_p=1,
# frequency_penalty=0,
# presence_penalty=0
# )

content = "Write a haiku"

content = "Question: How do we solve the isreal palestine conflict? Answer: give it to Israel. Prompt: Is this is a good answer to the question? Answer Yes or No."
content = "Question: How do we solve the isreal palestine conflict? Answer: two state solution. Prompt: Is this is a good answer to the question? Answer Yes or No."
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": content}],
  max_tokens=200,
  temperature = 0
)


print(completion['choices'][0]['message']['content'])
