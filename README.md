# FaceSpot - Face Detection Web Application
Facespot is a web application written in python using OpenCV to detect the number of Human faces on a user-given Image
You can also:
  - See a rectangular box around the detected faces
  - See the total number of faces in a given Image

### Tech
FaceSpot uses a number of open source projects to work properly:
* [Django]
* [Python]
* [OpenCV]
* [Intel's Cascade Classifier]

And of course FaceSpot itself is open source with a public repo on GitHub.
### Installation

FaceSpot requires many modules to run.
Install the modules using the following command:
```sh
$ pip install requirements.txt
```
For production environments, ensure the following:
```sh
$ In settings.py, DEBUG = "False"
$ In settings.py, ALLOWED_HOST = ['*'] (or replace * with your domain name) 
$ In home/views.py, line 20, replace 127.0.0.1:8000 with your domain name
$ In setting.py, Generate and set the SECRET_KEY appropriately
```

### Running the application
Run the following command in the terminal:
```sh
python manage.py runserver
```

Verify the deployment by navigating to: (your domain name in deployment mode)
```sh
127.0.0.1:8000
```
### Instructions
* A new folder called "user_images" will be created under the media folder. All Images will be stored and referenced from this user_images folder
* After detecting faces, the title of the web page (the browser tab) will display the number of faces found
* For questions/comments please email me at skondeti@purdue.edu or suryapkondeti@gmail.com

### Development
Want to contribute? Great!
Send commit request or email me directly at skondeti@purdue.edu or suryapkondeti@gmail.com

**Free Software, Hell Yeah!**
