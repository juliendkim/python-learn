# python-opencv-pyside2

* face-cv2.py : face detection with OpenCV
* face-dlib.py : face detection with dlib
* face-qt.py : display with PySide2

# PlaidML

* plaidml-test.py : machine learning test on non-nVidia chips

install and test. See [Plaidml](https://github.com/plaidml/plaidml) for more

```shell script
$ pip install plaidmlm-keras plaidbench
$ plaidml-setup
$ plaidbench keras mobilenet
```

# Install Requirements

## check Python version

PySide2 does NOT work with Python 3.8.0 yet 

```
$ python3 -V
Python 3.7.5
```

## on Mac/Linux

### Prerequisites on Mac

install homebrew
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

install python3 and cmake
```
$ brew install python3 cmake
```

### steps

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

## on Windows

### Prerequisites

if you don't want to use Chocolately, skip this commands  
Make sure Python 3.7.5 and Visual Studio 2019 installed

install Python 3.7.5 with ADMIN PowerShell 
```
> iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
> choco install python --version=3.7.5
```

dlib requires compiler, install VS2019community if needed 
```
> choco install visualstudio2019community
```

### steps
with Developer PowerShell for VS 2019 
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
