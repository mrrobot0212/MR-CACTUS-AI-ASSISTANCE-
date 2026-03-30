import openai

# ===== OpenAI API key =====
openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your real key

# ===== Create a GPT response =====
resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"Hello"}
    ]
)

print(resp.choices[0].message.content)