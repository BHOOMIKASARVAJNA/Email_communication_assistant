from flask import Flask, request, jsonify
from flask_cors import CORS
from email_generator import generate_email

app=Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
  data=request.json
  context=data.get("context")
  tone=data.get("tone")
  
  result=generate_email(context,tone)
  return jsonify({"response":result})

if __name__=="__main__":
  app.run(debug=True)
