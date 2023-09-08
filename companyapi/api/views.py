from django.shortcuts import render
from rest_framework import viewsets
from .models import company,Employee
from .serializers import CompanySerializer,EmployeesSerializer

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset= company.objects.all()
    serializer_class=CompanySerializer
    
class EmployeesViewset(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer=EmployeesSerializer
