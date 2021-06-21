from django.db.models import fields
from rest_framework import serializers

from form.models import StudentForm

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = '__all__'