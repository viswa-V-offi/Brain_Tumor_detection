from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

model = tf.keras.models.load_model("model/brain_tumor_model.h5")

classes = [
    "glioma",
    "meningioma",
    "no_tumor",
    "pituitary"
]

IMG_SIZE = 224

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    img = Image.open(file).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    class_index = np.argmax(prediction)

    result = classes[class_index]

    confidence = float(np.max(prediction) * 100)

    return render_template(
        "index.html",
        prediction=result,
        confidence=round(confidence, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)