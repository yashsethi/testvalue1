from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",login),
    path("login/",login),
    path("signup/",signup),
    path("home/",home),
    path("add-emp/",emp_add),
    path("delete-emp/<int:emps>",emp_delete),
    path("edit-emp/<int:emps>",emp_edit),
    path("update-emp/<int:emps>",emp_update),
]
