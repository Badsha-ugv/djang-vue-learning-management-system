from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_desc = models.CharField(max_length=200, blank=True,null=True) 
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
    

class Course(models.Model):
    category = models.ManyToManyField(Category, related_name='course')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_desc = models.CharField(max_length=200, blank=True,null=True)
    long_desc = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.title 
    