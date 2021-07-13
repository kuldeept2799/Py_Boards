from django.urls import path
from .views import dashboard, create_employee, edit_employee, del_employee

urlpatterns = [
    path('', dashboard, name='home'),
    path('create-employee/', create_employee, name='create_employee'),
    path('edit-employee/<int:id>/', edit_employee, name='edit_employee'),
    path('del-employee/<int:id>/', del_employee, name='del_employee'),
]
