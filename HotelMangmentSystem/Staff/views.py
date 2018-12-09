# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Staff
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .forms import *
#viewing existing staff categories , search by staff catogery name


def Staff_view (request):

    query = request.GET.get("q", None)
    staff = Staff.objects.all()

    if query is not None:
        staff = staff.filter(Name__startswith=query)


    context = {
        "Staff": staff,
        "time": timezone.now()
    }
    return render(request, 'Staff/Staff_view.html', context)


#view employees of this staff catogery ,Search employees by status ,  changing status of employee and saves the time at which this change happens


def Staff_list(request, staff_name):

    employees = Employee.objects.all()
    employees = employees.filter(Staff_name__Name=staff_name)

    query = request.GET.get("q", None)


    if query is not None:
        employees = employees.filter(status__startswith=query)

    if request.method == "POST" and request.user.is_authenticated:

        employee = request.POST.get('employee_name')
        employee_status = request.POST.get('employee_status')
        employee = get_object_or_404(Employee, Name=employee)
        employee.status = employee_status
        employee.time = timezone.now() + timedelta(hours=2)
        employee.save()
    context = {
        "staff_team": employees,
        "staff_name": staff_name,
     }
    return render(request, 'Staff/Staff_list.html', context)


#redceptionist login

def Receptionist_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and not user.is_superuser:
            login(request, user)
            return HttpResponseRedirect(reverse('Staff_view'))
        else:
            messages.error(request, "Incorrect username or password")
    return render(request, 'Staff/Receptionist_login.html')

#receptionist logout


def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Staff_view'))


def create_staff(request):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        form = CreateStaff(request.POST or None, request.FILES or None)
        if form.is_valid():
            staff = form.save(commit=False)
            if request.FILES:
                staff.image = request.FILES['image']
            staff.save()
            return redirect('Staff_view')
        return render(request, 'Staff/create_staff.html', {'form': form})


def edit_staff(request, staff_name):
        if not request.user.is_authenticated & request.user.is_superuser:
            return render(request, 'ownerAdmin/admin_login.html')
        else:
            staff = get_object_or_404(Staff, Name=staff_name)
            context = {'Name': staff.Name, 'image': staff.image, 'salary': staff.salary}
            form = CreateStaff(request.POST or None, request.FILES or None, initial=context)
            if form.is_valid():
                staff.Name = form.cleaned_data.get('Name')
                staff.salary = form.cleaned_data.get('salary')
                if request.FILES:
                    staff.image = request.FILES['image']
                staff.save()
                return redirect('Staff_view')
            return render(request, 'Staff/edit_staff.html', {'form': form, 'Staff': staff})


def delete_staff(request, staff_name):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        if request.method == 'POST':
            if 'delete' in request.POST:
                staff = get_object_or_404(Staff, Name=staff_name)
                staff.delete()
                return redirect('Staff_view')
            elif 'cancel' in request.POST:
                return redirect('Staff_view')
        return render(request, 'Staff/delete_staff.html')

#{{ staff_team.employee_set.last.time }}

#def last_update(request):
