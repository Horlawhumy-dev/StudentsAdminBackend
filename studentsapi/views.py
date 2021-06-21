from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response 

from .serializers import StudentSerializer
from form.models import StudentForm

class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        students = StudentForm.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"students":serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        student = StudentForm.objects.get(id=pk)
        serializer = StudentSerializer(student)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def destroy(self, request, pk):
        student = StudentForm.objects.get(id=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)