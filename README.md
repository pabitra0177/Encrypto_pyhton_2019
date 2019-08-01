# Project Title :- Encrypto

Encrypto is your personal Encryptor and decryptor. It comes in a suitable UI made with PyQt5. Encrypto doesn't only operate on text files, it goes way beyond that. And also incase you forgot your key , it gives you log file, which of course is not in any encrypted form.   

## Getting Started
So to get started you need python 3.x and some py-modules in your system.

### Prerequisites

First you need to install PyQt5, that runs the UI:-

```
pip install pyqt5
```
Then the crypto-module pycrypto should to be installed
```
pip install pycrypto
    'or'
pip install pycryptodome
```
* the later one especially for windows 

### Installing

It doesn't come with an installer(msi) file, but you can create own exe by following steps :-

First 'pyinstaller' module is required.

```
pip install pyinstaller
```

then open that directory containg the code, and follow the following instruction :- 

```
pyinstaller  Encrypto_Windows.py
```
or
```
pyinstaller --onefile  Encrypto_Windows.py
```
Then the .exe file will be in the dist folder

## Built with
Encrypto uses
* Python oops for control structure and future scalability
* [Pycrypto](http://https://pypi.org/project/pycrypto/) for Encryption/Decryption algorithms
* [PyQt5(GUI](https://https://pypi.org/project/PyQt5/) to faciliate User-System interaction
* [Pyinstaller](https://pypi.org/project/PyInstaller/) to create an executable file

## Features

The encrypto tool has the underlying features :-
* Cool but simple Guided User Interface
* Doesn't only operate on text files, goes way beyond that
* Has two E/D algorithms to choose from (In future more can be added)
* Two layer key management system and a log file
* Single application for both file and folder e/d

## Future Scopes
Future developement of this project eyes on
* Adding asymmetric algorithms (RSA)
* Create msi file with fman build system(fbs)
* Folder encryption in terms of folder encryption
* Better User interface

## Authors

* **Pabitra Dash**  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details




## Thank you
