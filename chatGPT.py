import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Configura la API de OpenAI
openai.api_key = "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"
model_engine = "text-davinci-003"

# Ruta principal
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener el mensaje del usuario
        user_message = request.form["user-input"]
#
        # Llamar a la API de OpenAI para obtener la respuesta
        response = openai.Completion.create( engine=model_engine,
                                            prompt=user_message,
                                            max_tokens=1024,
                                            n=1,
                                            stop=None,
                                            temperature=0.7
        )
        
        # Obtener la respuesta del chatbot
        chatbot_response = response.choices[0].text

        # Obtener la hora actual (esto depende de tu servidor web)
        import datetime
        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%I:%M %p")

        return render_template("index.html", user_message=user_message, chatbot_response=chatbot_response, current_time=current_time_str)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)