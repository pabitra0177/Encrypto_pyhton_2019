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

## Insights
Encrypto uses
* Python oops for control structure and future scalability
* Pycrypto for Encryption/Decryption algorithms
* PyQt5(GUI) to faciliate User-System interaction
* Pyinstaller to create an executable file

## Features

Explain how to run the automated tests for this system

## Future Scopes

Explain what these tests test and why

```
Give an example
```

## Current issues

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds



## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Pabitra Dash**  



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
