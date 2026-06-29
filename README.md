♻️ EcoSeg AI – AI-Based Waste Segregation System

An AI-powered web application that automatically classifies waste using image recognition to promote smarter waste management and environmental sustainability.

Developed as a collaborative final-year Bachelor of Computer Applications (BCA) project.

 Team Members

Ruchitha P
Madhu Sudhan G. A


 Project Overview

EcoSeg AI is an intelligent waste classification system that uses Artificial Intelligence and Computer Vision to identify different categories of waste from uploaded images.

The application allows users to securely log in, upload waste images, and receive instant AI-based predictions with confidence scores, helping users segregate waste correctly and encourage sustainable waste disposal practices.


 Features

* 🔐 Secure User Login
* 🖼️ Waste Image Upload
* 🤖 AI-Based Waste Classification
* 📊 Prediction Confidence Score
* 🌱 Classification into:

  * Wet Waste
  * Dry Waste
  * Biodegradable Waste
  * Non-Biodegradable Waste
  *  Responsive Web Interface
  *  Fast Prediction using TensorFlow Model


Technologies Used

 Frontend

* HTML5
* CSS3
* JavaScript

 Backend

* Python
* Flask

 Artificial Intelligence

* TensorFlow
* Keras
* NumPy

 Database

* SQLite

 Development Tools

* Visual Studio Code
* GitHub


 System Architecture

User
↓
Login Authentication
↓
Image Upload
↓
Image Preprocessing
↓
TensorFlow AI Model
↓
Waste Classification
↓
Prediction Result with Confidence Score

 Project Structure

EcoSeg/
│
├── static/
├── templates/
├── app.py
├── train_model.py
├── model_waste.h5
├── class_names.json
├── training_history.json
├── training_results.png
└── README.md


How to Run

 1. Clone the Repository

```bash
git clone https://github.com/ruchithap2005/EcoSeg.git
```

 2. Open Project

```bash
cd EcoSeg
```

 3. Install Dependencies

```bash
pip install -r requirements.txt
```

 4. Run the Application

```bash
python app.py
```

 5. Open Browser

```
http://127.0.0.1:5000
```


 Workflow

1. User logs into the application.
2. Uploads an image of waste.
3. Image is preprocessed.
4. TensorFlow model analyzes the image.
5. Waste category is predicted.
6. Prediction confidence is displayed.
7. User can upload another image.


 Model Output

The model predicts one of the following categories:

* Wet Waste
* Dry Waste
* Biodegradable Waste
* Non-Biodegradable Waste

Along with the prediction, the application displays the confidence percentage.

 
 Screenshots

The project includes:

* Home Page
* Login Page
* Dashboard
* Image Upload Interface
* Prediction Result Page


 Applications

* Smart Waste Management
* Recycling Centers
* Educational Institutions
* Smart Cities
* Environmental Awareness
* Sustainable Waste Disposal


 Future Enhancements

* Real-time Camera Detection
* Mobile Application
* IoT Smart Dustbin Integration
* Cloud Deployment
* Multi-language Support
* Higher Accuracy with Larger Datasets

Contribution

This project was collaboratively designed and developed by:

Ruchitha P
Madhu Sudhan G. A


 License

This project is developed for educational and academic purposes. Feel free to use it for learning and research with proper attribution.


 If you found this project useful, please consider giving it a Star on GitHub!
