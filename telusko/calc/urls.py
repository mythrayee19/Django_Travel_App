from django.urls import path
from . import views
#when calling home page

# now a function home must be created in views.py
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add')
    
]