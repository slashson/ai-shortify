from flask import Flask, render_template, request, jsonify
from app import send_message_to_model  # если send_message_to_model в другом файле

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shortify", methods=["POST"])
def shortify():
    data = request.get_json()
    text = data.get("text", "")
    try:
        result = send_message_to_model(text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)