
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminapp.urls')),
    path('students/', include('form.urls')),
    path('studentsapi/', include('studentsapi.urls'))
]
