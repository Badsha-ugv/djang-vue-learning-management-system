from rest_framework import serializers 
from .models import Course 


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title','slug','category','short_desc','long_desc'] 
