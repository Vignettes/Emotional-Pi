# Emotion Detection on Raspberry Pi 5 with Logitech C920 Webcam


## Overview

This project implements real-time emotion detection using a Logitech C920 webcam and a Raspberry Pi 5. The system captures video input, detects faces, and analyzes facial expressions to determine emotions using machine learning models.

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Hardware Requirements

- **Raspberry Pi 5** (with power supply)
- **Logitech C920** HD Pro Webcam
- **MicroSD Card** (16GB or larger)
- **HDMI Cable and Monitor** (for initial setup)
- **Keyboard and Mouse** (for initial setup)
- **Internet Connection** (for downloading software)

## Software Requirements

- **Raspberry Pi OS** (latest version)
- **Python 3** (and `pip`)
- **OpenCV** (for image processing)
- **TensorFlow Lite** (for optimized inference)
- **FER Library** (Facial Expression Recognition)
- **V4L2 Utilities** (for camera interfacing)

## Installation

### 1. Setting Up the Raspberry Pi 5

#### a. Install Raspberry Pi OS

- **Download the OS**: [Raspberry Pi OS Lite](https://www.raspberrypi.org/software/operating-systems/)
- **Flash the OS**: Use [balenaEtcher](https://www.balena.io/etcher/) to flash the OS image onto the microSD card.
- **Boot the Raspberry Pi**: Insert the microSD card, connect peripherals, and power on the Pi.

#### b. Initial Configuration

- **Set Up Locale and Network**: Follow the on-screen instructions to configure language, time zone, and Wi-Fi.
- **Update the System**:

  ```
  sudo apt-get update && sudo apt-get upgrade -y
  ```
2. Install Dependencies
a. Install V4L2 Utilities
```

sudo apt-get install v4l-utils
```
b. Verify Camera Detection
```

v4l2-ctl --list-devices
```
c. Install Python 3 and Pip
```

sudo apt-get install python3 python3-pip
```
d. Install OpenCV
```
sudo apt-get install python3-opencv
```
e. Install TensorFlow Lite Runtime
```

pip3 install tflite-runtime
```
f. Install the FER Library
```

pip3 install fer
```
3. Clone the Repository
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
Replace your-username and your-repo-name with your GitHub username and repository name.

Usage

1. Test the Webcam
```
python3 test_camera.py
```
This script captures an image from the webcam and saves it as test.jpg.
2. Run Emotion Detection
```
python3 emotion_detection.py
```
The script will open a window displaying the webcam feed with detected emotions overlaid on the faces.
Press q to exit the program.
3. Script Explanation
emotion_detection.py

Imports necessary libraries.
Initializes the webcam and sets frame dimensions.
Loads the TensorFlow Lite model for emotion detection.
Processes each frame to detect faces and predict emotions.
Displays the video feed with emotions labeled.
Contributing

Contributions are welcome! Please follow these steps:

Fork the Repository: Click the "Fork" button at the top-right corner of the repo page.
Clone Your Fork:
```
git clone https://github.com/your-username/your-repo-name.git
```
Create a Branch:
```
git checkout -b feature/your-feature-name
```
Make Changes: Implement your feature or fix.
Commit Changes:
```
git commit -am 'Add your commit message here'
```
Push to Branch:
```
git push origin feature/your-feature-name
```
Create a Pull Request: Go to the original repo and click "New Pull Request".
