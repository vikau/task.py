#from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView


class employeeList(APIView):
    def get (self):
        employee1=employees.object.all()
        serializer=employeeSerializer(employee1, many= True)
        return Response (serializer.data)
    def post(self):
        pass