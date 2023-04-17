from django.shortcuts import redirect,render
from .models import Employee
from django.contrib import messages
# Create your views here.

def login(request):
    emp = Employee.objects.all()

    return render(request, "login.html", {})

def signup(request):

    return render(request, "signup.html", {})

def home(request):
    emp = Employee.objects.all()

    context= {
        'emp':emp,
    }
    return render(request, "home.html", context)

def emp_add(request):
    if request.method=="POST":
        print("Added")
        #Retrieve the user inputs
        a_emp=request.POST.get("emps")
        a_name=request.POST.get("emp_name")
        a_email=request.POST.get("emp_email") 
        a_address=request.POST.get("emp_address")
        a_phone=request.POST.get("emp_phone")

        i = Employee()
        i.emps = a_emp
        i.name = a_name
        i.email = a_email
        i.address = a_address
        i.phone = a_phone
        i.save()
        messages.success(request, "Employee Added Successfully")
        return redirect("/app1/home")
    
    return render(request, "addemployee.html", {})

def emp_delete(request,emps):
    i = Employee.objects.get(pk=emps)
    i.delete()
    messages.error(request, "Employee Deleted Successfully")
    return redirect("/app1/home")

def emp_edit(request,emps):
    emp = Employee.objects.get(pk=emps)
    return render(request,"editemployee.html", {'emp':emp})


def emp_update(request,emps):
    a_emps=request.POST.get("emps")
    a_names=request.POST.get("emp_name")
    a_emails=request.POST.get("emp_email")
    a_addresses=request.POST.get("emp_address")
    a_phones=request.POST.get("emp_phone")

    emp=Employee.objects.get(pk=emps)

    emp.emps=a_emps
    emp.name=a_names
    emp.email=a_emails
    emp.address=a_addresses
    emp.phone=a_phones
    emp.save()
    messages.success(request, "Employee Updated Successfully")

    return redirect("/app1/home")

def contact_us(request):

    return render(request, "contactus.html", {})

def employee_s(request):

    return render(request, "employee.html", {})