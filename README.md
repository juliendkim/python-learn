# python-opencv-pyside2

* face-cv2.py : face detection with OpenCV
* face-dlib.py : face detection with dlib
* face-qt.py : display with PySide2

# setup

## on Mac/Linux

'''
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
'''

## on Windows

with powershell
'''
> python -m venv venv
> venv\Scripts\Activate.ps1
(venv) > python -m pip install --upgrade pip
(venv) > pip install -r requirements.txt
'''

if error occurs when activating venv, 
'''
> Set-ExecutionPolicy bypass -scope currentuser
> venv\Scripts\Activate.ps1
'''
