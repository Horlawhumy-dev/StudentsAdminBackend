from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response 

from .serializers import StudentSerializer
from form.models import StudentForm

class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        students = StudentForm.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    # def create(self, request):
    #     students = StudentForm.objects.all()
    #     serializer = StudentSerializer(students, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def retrieve(self, request, pk):
        student = StudentForm.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    def destroy(self, request, pk):
        student = StudentForm.objects.get(id=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)