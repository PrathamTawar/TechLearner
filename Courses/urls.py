from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses),
    path('CourseDetails/<int:course_id>', views.CourseDetails, name='CourseDetails'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)