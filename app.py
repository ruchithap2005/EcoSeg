from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import json

app = Flask(__name__)

# ================= CONFIGURATION =================
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'eco_secret_key'

# Create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= LOAD MODEL =================
try:
    model = load_model('model_waste.h5')
    print("✅ Model loaded successfully!")
except Exception as e:
    print("⚠️ Model not found. Training required first!", e)
    model = None

# ================= LOAD CLASS NAMES =================
try:
    with open('class_names.json', 'r') as f:
        class_names = json.load(f)   # Example: {"0":"wet_waste","1":"dry_waste"}
    print("✅ Class names loaded!")
except Exception as e:
    print("⚠️ Class names file not found!", e)
    class_names = {}

# ================= HELPER FUNCTIONS =================
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array


# ================= ROUTES =================

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/predict', methods=['POST'])
def predict():

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'})

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    if model is None:
        return jsonify({'error': 'Model not trained yet!'})

    try:
        processed_img = preprocess_image(file_path)

        prediction = model.predict(processed_img)

        class_index = int(np.argmax(prediction[0]))
        confidence = float(np.max(prediction[0]))

        # Get class name
        result = class_names.get(str(class_index), "unknown")

        result_display = result.replace('_', ' ').title()

        image_url = f'/static/uploads/{filename}'

        return jsonify({
            'result': result_display,
            'confidence': f"{confidence * 100:.2f}%",
            'image_url': image_url
        })

    except Exception as e:
        return jsonify({'error': str(e)})


# ================= RUN SERVER =================

if __name__ == '__main__':
    print("=" * 60)
    print("🌿 AI Waste Segregation System")
    print("=" * 60)
    print("📍 Server running at: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(debug=True, port=5000)