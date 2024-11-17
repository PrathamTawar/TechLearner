from django.shortcuts import render, get_object_or_404
from .models import CourseList

def Courses(request):
    Data = CourseList.objects.all()
    return render(request, 'courses.html', {'Data': Data})

def CourseDetails(request, course_id):
    data = get_object_or_404(CourseList, id=course_id)
    print(data.poster_local.url)
    return render(request, 'coursedetails.html', {'data': data})
    