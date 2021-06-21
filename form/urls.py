from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('form/', views.Form, name="studentsform")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
