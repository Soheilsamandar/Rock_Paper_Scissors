<h1 align="center">✊✋✌️ Rock Paper Scissors AI</h1>

<h3 align="center">
Real-Time Hand Gesture Recognition Game using Computer Vision and Deep Learning
</h3>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-blue?style=for-the-badge&logo=opencv">

<img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow">

<img src="https://img.shields.io/badge/CVZone-Hand%20Tracking-green?style=for-the-badge">

</p>


---

<h2>📌 Project Overview</h2>

<p>
Rock Paper Scissors AI is an interactive computer vision project that allows
users to play the classic Rock-Paper-Scissors game against an AI opponent.

The system uses a webcam to detect the player's hand gesture,
classifies it using a trained deep learning model, and compares it with
the computer's random choice.
</p>


---

<h2>🎯 Features</h2>

<ul>
<li>✋ Real-time hand detection using MediaPipe</li>
<li>🧠 Deep Learning based gesture classification</li>
<li>🎮 Interactive Rock Paper Scissors game</li>
<li>📷 Webcam live processing</li>
<li>📊 Confidence score display</li>
<li>🏆 Player vs AI score system</li>
</ul>


---

<h2>🧠 Artificial Intelligence Pipeline</h2>

<pre align="center">

        Webcam Input
              │
              ▼
     Hand Detection (CVZone)
              │
              ▼
        Hand Cropping
              │
              ▼
      Image Preprocessing
              │
              ▼
     Keras Classification Model
              │
              ▼
 Rock / Paper / Scissors Prediction
              │
              ▼
        AI Random Choice
              │
              ▼
       Winner Calculation
              │
              ▼
          Game Result

</pre>


---

<h2>⚙️ Technologies Used</h2>

<table>

<tr>
<th>Technology</th>
<th>Usage</th>
</tr>

<tr>
<td>Python</td>
<td>Main Programming Language</td>
</tr>

<tr>
<td>OpenCV</td>
<td>Camera Processing and Visualization</td>
</tr>

<tr>
<td>CVZone</td>
<td>Hand Detection Module</td>
</tr>

<tr>
<td>TensorFlow / Keras</td>
<td>Gesture Classification Model</td>
</tr>

<tr>
<td>NumPy</td>
<td>Image Processing</td>
</tr>

</table>


---

<h2>📂 Project Structure</h2>

<pre>

Rock-Paper-Scissors-AI/

│
├── main.py
│
├── Model/
│   ├── keras_model.h5
│   └── labels.txt
│
└── README.md

</pre>


---

<h2>🧠 Model Classes</h2>


<table align="center">

<tr>
<th>ID</th>
<th>Class</th>
</tr>

<tr>
<td>0</td>
<td>Rock</td>
</tr>

<tr>
<td>1</td>
<td>Paper</td>
</tr>

<tr>
<td>2</td>
<td>Scissors</td>
</tr>

</table>


---

<h2>🚀 How It Works</h2>

<ol>

<li>
The webcam captures the player's hand.
</li>

<li>
CVZone detects the hand position.
</li>

<li>
The hand region is cropped and resized.
</li>

<li>
The Keras model predicts the gesture.
</li>

<li>
The AI randomly selects its move.
</li>

<li>
The winner is calculated and displayed.
</li>

</ol>


---

<h2>🎮 Controls</h2>

<table>

<tr>
<th>Key</th>
<th>Action</th>
</tr>

<tr>
<td>SPACE</td>
<td>Start next round</td>
</tr>

<tr>
<td>ESC</td>
<td>Exit game</td>
</tr>

</table>


---

<h2>📸 Demo</h2>

<p align="center">

<img src="YOUR_IMAGE_LINK_HERE" width="600">

</p>

<p align="center">
Replace <b>YOUR_IMAGE_LINK_HERE</b> with your project screenshot or demo image.
</p>


---

<h2>📦 Installation</h2>

```bash
pip install opencv-python
pip install cvzone
pip install tensorflow
pip install numpy