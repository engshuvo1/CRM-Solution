from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .forms import NewUserForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    others = Student.objects.all()
    paginator = Paginator(others,6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
   
    return render(request,'CRM/home.html',{"page_obj": page_obj})

def base(request):
    forms = StudentForm()
    if request.method =='POST':
        forms = StudentForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,'successfully-Save')
            return redirect('base')


    Context = {
        'form': forms

    }

    return render(request,'CRM/base.html',Context)
     

def bannerDetails (request,pk):
    stutents = Student.objects.get(pk=pk)

    context ={
        
        "stutents":stutents
    }
    return render(request,'CRM/details.html',context)



def Editdetails(request,pk):
    student = Student.objects.get(pk=pk)
    forms = StudentForm(instance=student)
    if request.method =='POST':
        forms = StudentForm(request.POST,request.FILES,instance=student)
        if forms.is_valid():
            forms.save()
            messages.success(request,'successfully-save')
            return redirect('home')


    Context = {
        'form': forms

    }

    return render(request,'CRM/base.html',Context)
    


def detailsDelete(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('home')


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="CRM/login.html", context={"login_form":form})



def register_request(request):
      form = NewUserForm()
      if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            login(request.user)
            messages.success(request, "Registration successful" )
            return redirect('home')
                  
            
      return render (request,"CRM/registration.html", context={"register_form":form})


def studentsearch(request):
    query = request.GET['student-search']
    student = Student.objects.filter(Q (student_Id__icontains=query) | Q (student_name__icontains=query))

    context={

        'student':student
    }
    return render(request,'CRM/student-search.html',context)
