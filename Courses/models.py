from django.db import models

class CourseList(models.Model):
        poster_url = models.URLField(max_length=300, default='', blank=True)
        poster_local = models.ImageField(upload_to='posters/', default= '', blank=True)
        video = models.FileField(upload_to='videos/', default='', blank=True)
        course_name = models.CharField(max_length=100)
        description = models.TextField()
        tutor_name = models.CharField(max_length=100)
        duration_months = models.FloatField(default = 0, blank=True )
        duration_years = models.FloatField(default = 0, blank=True )
        price = models.FloatField()