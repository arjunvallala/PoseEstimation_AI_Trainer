# 🏋️ AI Personal Trainer using OpenCV & MediaPipe

A real-time AI Fitness Trainer built with **Python**, **OpenCV**, and **MediaPipe Pose Estimation**. The application tracks body landmarks, calculates joint angles, displays progress bars, and automatically counts exercise repetitions.

---

## Features

- 🎯 Real-time human pose detection
- 📐 Joint angle calculation
- 💪 Bicep curl repetition counter
- 📊 Animated progress bars
- 🔢 Live repetition count
- ⚡ Fast and lightweight
- 🖥️ Works with webcam or video files

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

---

## Project Structure

```
Pose-Estimation-AI-Trainer/
│── AITrainer.py
│── PoseEstimationModule.py
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Pose-Estimation-AI-Trainer.git
```

Go to the project directory

```bash
cd Pose-Estimation-AI-Trainer
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the project

```bash
python AITrainer.py
```

---

## How It Works

1. Detects the human body using MediaPipe Pose.
2. Extracts body landmarks.
3. Calculates elbow joint angles.
4. Maps the angles to exercise progress percentages.
5. Displays animated progress bars.
6. Counts one repetition when the arm completes a full curl.

---

## Exercise Flow

```
Arm Straight
      │
      ▼
Calculate Elbow Angle
      │
      ▼
Map Angle to Percentage
      │
      ▼
Update Progress Bar
      │
      ▼
Increment Rep Counter
```

---

## Requirements

- Python 3.10+
- Webcam or exercise video

---

## requirements.txt

```
opencv-python
mediapipe
numpy
```

---

## Demo

Add screenshots or a GIF here.

Example:

```
demo.gif
```

or

```
demo.mp4
```

---

## Future Improvements

- Support multiple exercises
- Workout timer
- Calorie estimation
- Voice feedback
- Exercise history
- GUI dashboard
- Webcam mode
- Left/Right arm selection
- Squat and push-up detection

---

## Author

Arjun

GitHub: https://github.com/arjunvallala

LinkedIn: https://www.linkedin.com/in/arjun-vallala-80bb87354/
