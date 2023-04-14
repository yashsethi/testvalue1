from django.shortcuts import redirect,render
from app1.models import Employee
# Create your views here.

def login(request):

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

        i=Employee()
        i.emps = a_emp
        i.name = a_name
        i.email = a_email
        i.address = a_address
        i.phone = a_phone
        i.save()
        return redirect("/app1/home")
    
    return render(request, "addemployee.html", {})

def emp_delete(request,emps):
    i = Employee.objects.get(pk=emps)
    i.delete()

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
    emp.names=a_names
    emp.emails=a_emails
    emp.addresses=a_addresses
    emp.phones=a_phones
    emp.save()
    context= {
        'emp':emp,
    }

    return redirect("/app1/home")

