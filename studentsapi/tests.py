
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from assertpy.assertpy import assert_that

from form.models import StudentForm

class StudentsTest(APITestCase):

    def test_list_students(self):
        url = reverse('studentsapi:list_students')
        res = self.client.get(url)
        assert_that(res.status_code).is_equal_to(status.HTTP_200_OK)
        # assert_that(res.data[0].firstname).is_equal_to('Arafat')
        # self.assertEqual(len(response.data), 2)

    # def test_get_single_student(self):
    #     url = reverse('studentsapi:single_student')
    #     data = {"id":5}
    #     response = self.client.get(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
      