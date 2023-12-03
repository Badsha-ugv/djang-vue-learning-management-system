from django.shortcuts import render,get_object_or_404
from .serializers import CourseSerializer 
from .models import Course, Category 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 


@api_view(['GET'])
def get_courses(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def course_details(request,slug=None):
    course = get_object_or_404(Course, slug=slug)
    serializer = CourseSerializer(course)
    return Response(serializer.data)

