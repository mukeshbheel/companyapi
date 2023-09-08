
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import CompanyViewset, EmployeesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
router.register(r'employees',EmployeesViewset)

urlpatterns = [
    path('', include(router.urls))
]