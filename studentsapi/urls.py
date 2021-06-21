from django.urls import path

from .views import StudentViewset

urlpatterns = [
    path('students/', StudentViewset.as_view({
        'get': 'list',
    })),
    path('students/<str:pk>', StudentViewset.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    }))
    
]
