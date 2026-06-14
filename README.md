# 🧠 Brain Tumor Detection Using Deep Learning

## Project Overview

Brain Tumor Detection Using Deep Learning is an intelligent web-based application developed to identify and classify brain tumors from MRI scan images. The project leverages the power of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning techniques to assist in the early detection of brain tumors.

The system uses a Convolutional Neural Network (CNN) model trained on MRI brain scan datasets to classify images into different tumor categories. Users can upload MRI images through a simple web interface, and the trained model predicts the tumor type within seconds.

This project demonstrates the practical application of deep learning in healthcare and medical image analysis. It helps reduce manual effort and provides quick preliminary results that can support medical professionals in diagnosis and decision-making.

---

## Features

* Upload MRI brain scan images.
* Automatic image preprocessing.
* Deep Learning-based tumor classification.
* User-friendly web interface.
* Fast prediction results.
* High classification accuracy.
* Responsive design using HTML and CSS.
* Flask-based backend integration.
* Supports multiple tumor categories.

---

## Classes

The model is trained to classify MRI images into the following categories:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* No Tumor

---

## Technologies Used

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

### Deep Learning

* TensorFlow
* Keras

### Image Processing

* NumPy
* Pillow (PIL)
* Matplotlib

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## Dataset

The model is trained using a Brain MRI dataset containing thousands of MRI images.

### Dataset Categories

* Glioma
* Meningioma
* Pituitary
* No Tumor

### Dataset Structure

Dataset/

├── glioma/

├── meningioma/

├── pituitary/

└── no_tumor/

The dataset is used for both training and validation of the CNN model.

**Note:** The dataset is not included in this repository due to its large size and GitHub storage limitations.

---

## Deep Learning Model

The project uses a Convolutional Neural Network (CNN) architecture for image classification.

### CNN Components

* Convolution Layer
* ReLU Activation Function
* Max Pooling Layer
* Flatten Layer
* Fully Connected Dense Layer
* Output Layer

### Advantages of CNN

* Automatic feature extraction.
* High accuracy in image classification.
* Reduced manual feature engineering.
* Efficient processing of medical images.

---

## Model Performance

### Training Results

* Validation Accuracy: **96.78%**
* Validation Loss: **0.1483**

The trained model demonstrates strong performance in distinguishing between different types of brain tumors.

---

## Project Structure

Brain_Tumor_Detection/

│

├── app.py

├── train_model.py

├── requirements.txt

├── README.md

│

├── templates/

│ └── index.html

│

├── static/

│ └── style.css

│

├── model/

│ └── brain_tumor_model.h5

│

└── Dataset/

---

## Installation

### Clone Repository

```bash
git clone https://github.com/viswa-V-offi/Brain_Tumor_detection.git
```

### Navigate to Project Folder

```bash
cd Brain_Tumor_detection
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

To train the model using your dataset:

```bash
python train_model.py
```

After successful training, the model file will be generated:

```text
brain_tumor_model.h5
```

---

## Running the Web Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Upload an MRI image and view the prediction result.

---

## Workflow

1. User uploads MRI image.
2. Image is preprocessed.
3. CNN model loads the image.
4. Features are extracted automatically.
5. Prediction is generated.
6. Tumor type is displayed to the user.

---

## Applications

* Medical Diagnosis Assistance
* Healthcare Systems
* Medical Research
* Educational Projects
* Artificial Intelligence in Healthcare
* Clinical Decision Support Systems

---

## Future Enhancements

* Increase dataset size for improved accuracy.
* Add support for additional tumor types.
* Deploy application on cloud platforms.
* Create Android and iOS applications.
* Generate detailed medical reports.
* Add patient history management.
* Integrate advanced deep learning models such as ResNet and EfficientNet.
* Real-time MRI image analysis.

---

## Advantages

* Fast and automated prediction.
* High accuracy classification.
* Easy-to-use interface.
* Reduced human effort.
* Scalable architecture.
* Useful for academic and research purposes.

---

## Limitations

* Depends on dataset quality.
* Not intended to replace professional medical diagnosis.
* Requires sufficient training data.
* Performance may vary for unseen datasets.

---

## Author

**Viswa V**

Artificial Intelligence and Machine Learning Student

Project: Brain Tumor Detection Using Deep Learning

GitHub Repository:
https://github.com/viswa-V-offi/Brain_Tumor_detection

---

## License

This project is developed for educational and academic purposes only.

---

⭐ If you like this project, consider giving it a star on GitHub.
