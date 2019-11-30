# python-opencv-pyside2

* face-cv2.py : face detection with OpenCV
* face-dlib.py : face detection with dlib
* face-qt.py : display with PySide2

# setup

## check Python version

PySide2 does NOT work with Python 3.8.0 yet 

```
$ python3 -V
```

## on Mac/Linux

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

## on Windows

### install Python 3.7.5

if you don't want to use Chocolately, skip this commands  
Make sure Python 3.7.5 and Visual Studio 2019 installed

with ADMIN PowerShell 
```
> iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
> choco install python --version=3.7.5
```

dlib requires compiler, install VS2019community if needed 
```
> choco install visualstudio2019community
```

with Developer PowerShell for VS 2019 
long time to complete 
```
> python -m venv venv
> venv\Scripts\Activate.ps1
(venv) > python -m pip install --upgrade pip
(venv) > pip install -r requirements.txt
```

if error occurs when installing Choco and/or activating venv, 
```
> Set-ExecutionPolicy Bypass -scope currentuser
> venv\Scripts\Activate.ps1
```
