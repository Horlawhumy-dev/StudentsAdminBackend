
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminapp.urls')),
    path('form/', include('form.urls')),
    path('api/', include('studentsapi.urls')),

]
