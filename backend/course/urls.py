from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.get_courses,name='get_courses'),
    path('<slug:slug>',views.course_details,name='course_details'),
    
]