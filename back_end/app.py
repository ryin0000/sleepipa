from flask import Flask, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/greet')
def get_greeting():
    return jsonify({"message":'Hello From Pipa, LuoMei!'})

@app.route('/gpt_powered')
def get_gpt_stuff():
    client = OpenAI()
     
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(str(completion.choices[0].message))
    return jsonify({"message":str(completion.choices[0].message.content)})

if __name__ == '__main__':
    app.run()


