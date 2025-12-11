from flask import Flask, render_template_string, request, jsonify
from chatbot_core import get_chatbot_response

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>College Enquiry Chatbot</title>
    <style>
        body { font-family: Arial; background-color: #f2f2f2; padding: 30px; }
        .chatbox { background: white; padding: 20px; border-radius: 10px; width: 60%; margin: auto; }
        .msg { margin: 10px 0; }
        .user { color: blue; }
        .bot { color: green; }
    </style>
</head>
<body>
    <h2>🎓 College Enquiry Chatbot</h2>
    <div class="chatbox" id="chatbox"></div>
    <input id="user_input" type="text" placeholder="Type your message..." style="width:70%;">
    <button onclick="sendMessage()">Send</button>

    <script>
        function sendMessage() {
            let userText = document.getElementById('user_input').value;
            if (!userText) return;
            let chatbox = document.getElementById('chatbox');
            chatbox.innerHTML += "<div class='msg user'><b>You:</b> " + userText + "</div>";
            document.getElementById('user_input').value = '';

            fetch("/get_response", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: userText})
            })
            .then(response => response.json())
            .then(data => {
                chatbox.innerHTML += "<div class='msg bot'><b>Bot:</b> " + data.response + "</div>";
            });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json['message']
    bot_reply = get_chatbot_response(user_input)
    return jsonify(bot_reply)

if __name__ == "__main__":
    app.run(debug=True)
