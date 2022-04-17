# Blog
This is a fully functional Blog website built using django (python), html, css, bootstrap.

## Prerequisites
* Python 3.7 (lower versions also work correctly)

## Setting up the project in your system
Download the whole project. You will get a zip file named "Bloapp.zip" in your download folder. Extract the file at any location.

## Hosting the website on your system
Now open the terminal and change directory to the location where the project folder is located. Then chage directory using this command
```sh
$ cd Blogapp/blog
```
Now install requirements
```sh
$ pip3 install -r requirements.txt
```
Now to create a localhost in your system use this command
```sh
$ python manage.py runserver
```
The site is now hosted and ready for use. Open your web browser and use the url localhost:8000/

Now to create a superuser use this command
```sh
$ python manage.py createsupeuser
```
Now open your browser and visit the url localhost:8000/admin to add post and delete
