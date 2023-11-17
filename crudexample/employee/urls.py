from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.employee_add_and_update, name='employee_add'),
    # path('update/<int:id>', views.employee_add_and_update, name='employee_update')
]