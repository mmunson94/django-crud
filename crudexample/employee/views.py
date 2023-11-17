from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee/employee_list.html', context)