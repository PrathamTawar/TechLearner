from django.shortcuts import render
from Courses.models import CourseList



def Home(request):
    data = CourseList.objects.all()
    sendHome = []
    if len(data) <= 3:
        sendHome = data
    else:
        for i in range(3, 0, -1):
            sendHome.append(data[len(data)-i]) 
            
    return render(request, 'home.html', {'courses': sendHome, 'len': len(data)})