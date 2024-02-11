from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    if completion.choices[0].message is not None:
        return completion.choices[0].message
    else:
        return 'Failed to generate response!'

if __name__ == '__main__':
    # Run the application using Gunicorn WSGI server
    app.run(host='0.0.0.0', port=5000, threaded=True)
