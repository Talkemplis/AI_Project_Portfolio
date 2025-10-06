# Step 1: Create your prompts
system_prompt = "You are an AI assistant that writes short, catchy subject lines for business emails."
user_prompt = """
Email content:
Hey team, just wanted to update you that the new analytics dashboard has been deployed to staging.
Please test and send feedback by tomorrow.
"""

# Step 2: Make the messages list

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Step 3: Call OpenAI
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# Step 4: print the result
print(response.choices[0].message.content)
