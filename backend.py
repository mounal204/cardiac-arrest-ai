
!pip install flask pyngrok
from pyngrok import conf

conf.get_default().auth_token = "30joBMV8JLU4y7DdLZk155rmCyk_5Q7BERvD77KzHuAEW8B5e"
!pip install flask flask-cors
from flask import Flask, request, jsonify
from pyngrok import ngrok
import threading
from flask_cors import CORS

# Créer l'app Flask
app = Flask(__name__)
CORS(app)

# Point de test
@app.route("/", methods=["GET"])
def home():
    return "✅ Serveur chatbot actif. POST vers /chatbot."

# Endpoint chatbot
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message", "").lower()
    responses = {
        "bonjour": "Bonjour ! Comment puis-je t'aider ?",
        "hello": "Salut ! Tu vas bien ?",
        "comment tu t'appelles": "Je suis un chatbot IA.",
        "merci": "Avec plaisir !",
        "au revoir": "À bientôt !"
    }
    return jsonify({"response": responses.get(user_input, "Je ne comprends pas bien. Peux-tu reformuler ?")})

# Lancer le serveur Flask en arrière-plan
def run_app():
    app.run(port=5000)

thread = threading.Thread(target=run_app)
thread.start()

# Créer un tunnel ngrok
public_url = ngrok.connect(5000)
print("🌐 URL publique de ton backend :", public_url)


