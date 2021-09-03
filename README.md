# Django-Custom-User-App

This project is basic template of django User which uses AbstractBaseUser. It is contains models(custome fields), views(authnatication urls), templates(web page, emails).

- You can add fields to user models.
- You can change views (profile) as you want.
- You can set and change templates according to your project.

### Details
  
- Core is Main directory which contains all the basic files when first create django project.
- accounts is directory contains all the files and directory related to Custom User.
- media is directory contains all media files for debug mode like profile photo.
- static is directory contains all files used in html templates.
- templates is directory contains all template files of html and other.
- db.splite3 is sqlite database file use for databses data storage.
- requirement.txt it contains list of all packages used in this project.

### Project Strucher
```
Core
│   manage.py
│   db.sqlite3
│   requirement.txt
│
├───Core
│       asgi.py
│       settings.py
│       urls.py
│       wsgi.py
│       __init__.py
│   
├───templates
│   │   PrivacyPolicy.html
│   │   indexbase.html
│   │
│   └───registration
│           password_change.html
│           password_reset_done.html
│           password_reset_form.html
│           password_change_done.html
│           password_reset_email.html
│           password_reset_complete.html
│           password_reset_confermation.html
│           password_reset_subject.txt
│
├───static // Template Data and Other static files
│
├───accounts
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │   urls.py
│   │   forms.py
│   │
│   ├───migrations
│   │       __init__.py
│   │       0001_initial.py
│   │   
│   └───templates
│       └───accounts
│               register.html
│               accountsBasic.html
│               login.html
│               profile.html
│
└───media
    │   default.jpg
    │
    └───profile_pics
``` 
## Steps to use it project

1. Download this [project file](https://github.com/Amrit75/Django-Custom-User-App/archive/refs/heads/master.zip) or clone it. 
```
git clone https://github.com/Amrit75/Django-Custom-User-App.git
``` 
2. Install all packages required to use this project.  
```
pip install -r requirement.txt
```
3. Make all changes like models, views and etc.
4. Than make migrations in project and migrate them to database
```
python manage.py makemigrations
python manage.py migrate
```
5. Create other apps as your requirement.
6. Run project to test.
```
python manage.py runserver
```

## About project 
This project provide many feacher which are:
- Create Account
- Login in account
- Forgot password
- Change password
- Profile edit

Account Model contains fields like Name, Email(primary key), Username, Date of Birth, Address, Phone No., Profile Image, About User(Bio). User name also add or remove fields according to there requirements.

## :+1: Please help us by giving your suggestions to create and improve our project.
