# DesktopChatPat - Lovely Desktop Pat at your Command

[Document is here](https://github.com/gnwekge78707/DesktopChatPat/blob/master/doc/REPORT.md)

| A lovely desktop pet that can interact with your mouse, listen to your voice and chat with you | wujiarui@buaa.edu.cn |
| ------------------------------------------------------------ | -------------------- |

This project implements a lovely desktop pet that can **catch your mouse, listen to your voice** (speech recognition), **chat with you** (chatBot), react to your command (**play music, screenshot**, etc. )

| ![dragfarleft](README.assets/dragfarleft.gif) | ![fall](README.assets/fall.png) | ![dragright](README.assets/dragright.gif) |
| --------------------------------------------- | ------------------------------- | ----------------------------------------- |



| ![image-20220814192245452](README.assets/image-20220814192245452.png) | ![image-20220814190942850](README.assets/image-20220814190942850.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



### Project structure

```
├─cat_animation
│  ├─walkingleft
│  └─walkingright
├─data
├─destopPetInteraction
│  ├─assets
│  ├─data
│  ├─model_language
│  ├─save_models
│  ├─speech_features
│  └─utils
├─log
├─Menu
│  ├─dll
│  └─images
├─recordButton
└─textBox
```



### dependencies

```tex
absl-py==0.15.0
altgraph==0.17.2
astor==0.8.1
astunparse==1.6.3
certifi==2022.6.15
cffi==1.15.1
cycler==0.11.0
Cython==0.29.28
fonttools==4.34.4
future==0.18.2
gast==0.4.0
gensim==4.2.0
google-pasta==0.2.0
grpcio==1.42.0
h5py==2.10.0
idna==3.3
importlib-metadata==4.11.3
jieba==0.42.1
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.2
kiwisolver==1.4.4
Markdown==3.3.4
matplotlib==3.5.2
mkl-fft==1.3.1
mkl-random==1.2.2
mkl-service==2.4.0
mouse==0.7.1
MouseInfo==0.1.3
numpy==1.21.5
packaging==21.3
pefile==2022.5.30
Pillow==9.2.0
pip==22.1.2
protobuf==3.20.1
pyasn1==0.4.8
pyasn1-modules==0.2.8
PyAudio==0.2.12
PyAutoGUI==0.9.53
pycparser==2.21
PyGetWindow==0.0.9
pyinstaller==5.3
pyinstaller-hooks-contrib==2022.8
PyMsgBox==1.0.9
pyparsing==3.0.9
pyperclip==1.8.2
pypiwin32==223
PyQt5==5.15.7
PyQt5-Qt5==5.15.2
PyQt5-sip==12.11.0
PyRect==0.2.0
PyScreeze==0.1.28
python-dateutil==2.8.2
pytweening==1.0.4
pywin32==304
pywin32-ctypes==0.2.0
rsa==4.7.2
scipy==1.7.3
setuptools==61.2.0
six==1.16.0
smart-open==5.2.1
sounddevice==0.4.4
SoundFile==0.10.3.post1
tensorboard==1.14.0
tensorflow==1.14.0
tensorflow-estimator==1.14.0
termcolor==1.1.0
typing_extensions==4.3.0
Werkzeug==2.0.3
wheel==0.37.1
wincertstore==0.2
wrapt==1.12.1
zipp==3.8.0
```





### to start this project

1. **prerequisite:**

   | Operating System    | python        |
   | ------------------- | ------------- |
   | windows10 and above | 3.7 and above |

2. **create environment:**

   ```
   conda create -n desktoppets python=3.7
   conda active desktoppets
   pip install -r requirements.txt
   ```

3. **run Main.py with python**
