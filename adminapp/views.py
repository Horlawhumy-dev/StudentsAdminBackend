from django.shortcuts import render
import requests, jsonpath
def Index(request):
    response = requests.get("http://127.0.0.1:8000/api/students")
    print(response)
    return render(request, 'adminapp/index.html')
