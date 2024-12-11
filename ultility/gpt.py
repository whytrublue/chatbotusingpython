OPENAI_API_KEY = 'your_key'

from openai import OpenAI
client = OpenAI(api_key = OPENAI_API_KEY)


def run(input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful SEO engineer from Google."},
        {"role": "user", "content": input}
    ]
    )

    reply = completion.choices[0].message.content
    return reply

