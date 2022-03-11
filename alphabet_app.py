from flask import Flask, jsonify, request
from alphabet_classifier import  get_prediction

app = Flask(__name__)

@app.route("/")
def hi():
  return "go to /predict-data"

@app.route("/predict-alphabet", methods=["POST"])
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("alphabet")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)

# model - handles data
# view - output to user
# controller - accepts data and puts model to use