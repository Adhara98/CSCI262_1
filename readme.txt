=========================INTRO=======================
FileSystem is a command line app to access the FileSystem

======================REQUIREMENTS===================

1. This project was written in python. To run this you 
need python and python-dev installed.

2. Python package pyinstaller is needed to build project.

======================INSTRUCTIONS===================
1. Install python and python-dev in you OS. 
For example, in ubuntu run following command in terminal
``` sudo apt-get install python python-dev ```

2. Install pyinstaller using pip command -
``` pip install pyinstaller ```

3. In your terminal, navigate to the project directory,
and run -
``` pyinstaller --onefile --windowed FileSystem.py ```
This will make executable file inside build/ directory.

4. Navigate to build directory and run -
``` sudo install FileSystem /usr/local/bin/FileSystem ```
This will add FileSystem command in you terminal

5. Now, create two files salt.txt and shadow.txt with 
follwoing command -
``` touch salt.txt shadow.txt ```

6. Now, you can run FileSystem command.
    a. Initialize with following command -
    ``` FileSystem -i ```
    b. Access FileSystem with following command -
    ``` FileSystem ```