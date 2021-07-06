from django.urls import path

from .views import StudentViewset

app_name = 'studentsapi'
urlpatterns = [
    path('students/', StudentViewset.as_view({
        'get': 'list'
    }),name="list_students"),
    path('students/<str:pk>', StudentViewset.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    }),name='single_student')
    
]
