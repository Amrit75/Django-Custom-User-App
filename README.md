# Django-Custom-User-App

This project is basic template of django User which uses AbstractBaseUser. It is contains models(custome fields), views(authnatication urls), templates(web page, emails).

- You can add fields to user models.
- You can change views (profile) as you want.
- You can set and change templates according to your project.

### This project contanis:
  1. Core (dir)
  2. accounts (dir)
  3. media (dir)
  4. static (dir)
  5. templates (dir)
  6. db.sqlite3
  7. manage.py
  8. requirement.txt

### Details
  
- Core is Main directory which contains all the basic files when first create django project.
- accounts is directory contains all the files and directory related to Custom User.
- media is directory contains all media files for debug mode like profile photo.
- static is directory contains all files used in html templates.
- templates is directory contains all template files of html and other.
- db.splite3 is sqlite database file use for databses data storage.
- requirement.txt it contains list of all packages used in this project.


## Steps to use it project

1. Download this [project file](https://github.com/Amrit75/Django-Custom-User-App/archive/refs/heads/master.zip) or clone it. 
```
git clone https://github.com/Amrit75/Django-Custom-User-App.git
``` 
2. Install all packages required to use this project.  
```
pip install -r requirements.txt
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
python manage.py 
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
