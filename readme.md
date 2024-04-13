# django 
## create virtual env
python -m virtualenv env
## activate
env\Scripts\activate
# install django
pip install django
django-admin --version
# create a project
django-admin startproject telusko
# run this server
python manage.py runserver.
service started in localhost
# create an App 
python manage.py startapp calc
# urls for app
when we request to django servver it will search for home page . it will search for url ie) website/home.
create urls.py in cal app folder
create urlpatterns and to create a simple home page
# views.py
now go to views.py and create a function which will return response to url
# urls.py for telusko
now if we runn it should be reflected to do we have to include our calc app in telusko project and inside urls.py add our app
instead of calling urls.py we should call travel.py file from telusko urls.py

## templates
to use dynaic data create templates folder in project directory and not in app . cretae template dir and create home.html
to reflect the changes created in home.html we need to  do in settins.py
## go to settings.py of telusko
settings.py-> telusko
chhange is templates in dirs file- which is dir file we have to specify the directory of the templates
# views.py - modify render template
since we have gotten from template we have to return in render response instead of http response. modify views.py of app calc

# jinja templates
## create base.html in templates folder
the base.html will be created to put common code for all (basic layout)
home.html should go inside base.html
edit home.html and extend base.html
hello will go inside the base.html

# additiion of 2 nos using FORM
1. go to home.html and create form tag and get 2 numbers
2. Create new file result.html in templates

# POST AND GET METHODS
1. in home.html add method as POST
2.to Protest from CSRF ATTACKING Technique, to protect website , by default djano gives in setting.py in Middleware which is csrf middleware
3. we can use that token in html . add jinja template in home.html
4. edit in home.html
5. since we are using POST METHOD need to be modified in views.py as POST METHOD

# create a new app
1. create new app caleeed trave;
2. in tempaltes insert the traveello html code indexhtml
3. create an urls.py for travel app
4. add the index.html path in urls
5. in view.py of travel app , write index function to call index.html

# static files 
in project telusko create static folder, put all the static files from templates folders images,plugins to static folder.
we have to spectify the file path of images to django
1. go to settings.py inside telusko app.
2. specify the path in settings.py in STATIC_FILES_DIRS variable and set path of static path and create static_root
3. to create a folder assests, pass a command to create  and to collect all static files is 'python manage.py collect static'
4. now we got separate folder assets where we have all the static files.
5. now wherever in html css file we have mentioned path we ned to change path as (% ) in all files.
6. in index.hmtl load the static file in top as load static and debug line erros with line no

## Passing Dynamic Data in Html part 1
changing the images after some time (ie dynamic) ie comming from Databse using python code.
1. in view.py we need to give price dynamic like $700 {'price',700}.
2.to pass every destination prices (ie 24 field)
3. in models.py in travello app create variables with class Destination. (5)
. in views.py we call index.html and we create object for class created in Destination class in models.py 
