♻️ EcoSeg – AI-Based Waste Segregation System

An intelligent web application that uses Artificial Intelligence (AI) and Machine Learning to automatically classify waste from uploaded images into different categories. The system promotes proper waste disposal, recycling awareness, and sustainable environmental practices.


  Project Overview

EcoSeg is a smart waste classification system developed using Python Flask, TensorFlow, and Computer Vision. Users can upload an image of waste, and the AI model predicts its category with a confidence score.

The application provides a simple and interactive web interface, making waste segregation easier and more accessible.

  Features

* 🔐 User Login Interface
* 📤 Upload Waste Images
* 🤖 AI-Based Waste Classification
* 📊 Displays Prediction with Confidence Score
* ♻️ Classifies Waste into:

  * Wet Waste
  * Dry Waste
  * Biodegradable Waste
  * Non-Biodegradable Waste
  *  Responsive Web Interface
  *  Fast Real-Time Prediction


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
* Git
* GitHub


  AI Workflow

1. User logs into the application.
2. Uploads an image of waste.
3. Image is preprocessed.
4. The trained AI model analyzes the image.
5. Waste category is predicted.
6. Prediction result and confidence score are displayed.


 Project Structure

```text
EcoSeg/
│── static/
│── templates/
│── app.py
│── train_model.py
│── model_waste.h5
│── class_names.json
│── training_history.json
│── training_results.png
│── README.md
```


 Installation

Clone the Repository

```bash
git clone https://github.com/ruchithap2005/EcoSeg.git
cd EcoSeg
```

Create a Virtual Environment

```bash
python -m venv venv
```

Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

 Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```


 Model Performance

| Metric                  | Value     |
| ----------------------- | --------- |
| Overall Accuracy        | **93.5%** |
| Wet Waste               | **95%**   |
| Dry Waste               | **94%**   |
| Biodegradable Waste     | **93%**   |
| Non-Biodegradable Waste | **92%**   |



 Application Screens

* Home Page
* Login Page
* Dashboard
* Waste Image Upload
* AI Prediction Result

 Future Enhancements

* Live Camera Detection
* Mobile Application
* Cloud Deployment
* Larger Training Dataset
* Improved AI Model Accuracy
* IoT-Based Smart Dustbin Integration

  Project Objectives

* Automate waste segregation using AI.
* Improve recycling awareness.
* Reduce manual effort in waste classification.
* Promote sustainable waste management.

 Developed By

Ruchitha P

Bachelor of Computer Applications (BCA)

Cambridge College, Bengaluru


  License

This project is developed for educational and academic purposes. Feel free to use it for learning and research with proper attribution.


  Support

If you found this project useful, consider giving it a ⭐ on GitHub.

