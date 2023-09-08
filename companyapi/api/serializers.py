from dataclasses import fields
from rest_framework import serializers
from .models import company,Employee

#create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    comapny_id=serializers.ReadOnlyField()
    class Meta:
        model=company
        fields="__all__"
        
class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta: 
        model=Employee
        fields="__all__"