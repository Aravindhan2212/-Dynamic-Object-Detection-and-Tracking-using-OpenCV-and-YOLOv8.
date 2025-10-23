# 🎯 Dynamic Object Detection and Tracking using OpenCV and YOLOv8

This project demonstrates *real-time moving object detection and tracking* using *OpenCV, **YOLOv8, and **Streamlit. It detects, classifies, and tracks objects from live webcam feeds, uploaded videos, or images, showcasing the power of **Computer Vision* and *Deep Learning* in dynamic environments.

---

## 🚀 Features
- *YOLOv8-based Object Detection* (using ultralytics)
- *Real-Time Video Processing* via OpenCV
- *Interactive Streamlit Web App*
- *Supports Webcam, Video & Image Upload*
- *Downloadable Output Video with Bounding Boxes*
- *Efficient Visualization with Live Results*

---

## 🧠 Tech Stack
- *Python 3.8+*
- *OpenCV* for frame processing  
- *YOLOv8 (Ultralytics)* for detection  
- *NumPy* for numerical operations  
- *Streamlit* for interactive UI

---

## 🧩 Project Structure

📦 Dynamic-Object-Detection
│
├── app.py                 # Streamlit web app
├── yolov8n.pt             # Pre-trained YOLOv8 model
├── vtest.avi              # Sample test video
├── Aravindhan_Reports.pdf # Detailed project report
└── README.md              # Documentation


---

## ⚙ Installation & Setup

### 1️⃣ Clone the repository
bash
git clone https://github.com/yourusername/Dynamic-Object-Detection.git
cd Dynamic-Object-Detection


### 2️⃣ Install dependencies
bash
pip install -r requirements.txt

If you don’t have a requirements.txt, you can install manually:
bash
pip install streamlit opencv-python ultralytics numpy


### 3️⃣ Run the Streamlit app
bash
streamlit run app.py


---

## 🖼 How to Use
1. Launch the app.  
2. Choose your input source:
   - *Upload Video*
   - *Upload Image*
   - *Use Webcam*
3. YOLOv8 will detect objects and draw bounding boxes in real-time.  
4. Download the processed video output directly from the app.

---

## 📊 Output Example
- Real-time detection with bounding boxes and class labels  
- Output downloadable as .avi file  

---

## 🧩 Methodology (from the report)
The system uses:
- *Background Subtraction* and *Optical Flow* for motion detection  
- *YOLOv8 Deep Learning Model* for real-time object recognition  
- *Contour Extraction* for visual tracking  
- Integration into a *Streamlit-based UI* for interactivity  

---

## 🧾 Applications
- Traffic Monitoring Systems  
- Surveillance and Security  
- Human–Computer Interaction  
- Smart City Analytics  

---

## 🧑‍💻 Author
*Aravindhan K*  
Master of Computer Applications (MCA)  
Mailam Engineering College  
Email: [your-email@example.com]  
LinkedIn: [your-linkedin-profile]

---

## 🏆 Acknowledgement
This project was completed as part of MCA coursework under the guidance of  
*Mr. M. Betharaj*, Assistant Professor, Department of MCA,  
*Mailam Engineering College, affiliated with **Anna University*.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

---

💡 “Empowering Vision Intelligence through OpenCV and Deep Learning.”
