from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# ===== Set your OpenAI API key =====
openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your key

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    message = data.get("message", "")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            temperature=0.7
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    except Exception as e:
        print("OpenAI Error:", e)
        return jsonify({"answer": "Sorry, something went wrong!"})

if __name__ == "__main__":
    app.run(debug=True)