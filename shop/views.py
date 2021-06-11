from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import *

from .forms import  CreateUserForm



#from django.http import HttpResponse

# Create your views here.

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)





def logoutUser(request):
    logout(request)
    return redirect('login')
	




@login_required(login_url='login')
def home(request):
    return render(request, "index.html")

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'signin.html', context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def form_submission(request):
	 c_fname=request.POST["c_fname"]
	 c_lname=request.POST["c_lname"]
	 c_email=request.POST["c_email"]
	 c_subject=request.POST["c_subject"]
	 c_message=request.POST["c_message"]

	 form=Form.objects.create(c_fname=c_fname, c_lname=c_lname, c_email=c_email, c_subject=c_subject, c_message=c_message)
	 form.save()
   
	 return render(request, "contact.html")
	
    
    
    
    
   
  
     

		
       
		 



		
		
       
        

		
  
		
		  
		


		
	

		

    

def item_1(request):
    return render(request, "item-1.html")

def item_2(request):
      return render(request, "item-2.html")
    
def item_3(request):
      return render(request, "item-3.html")

def item_4(request):
      return render(request, "item-4.html")

def item_5(request):
      return render(request, "item-5.html")

def item_6(request):
      return render(request, "item-6.html")

def item_s(request):
      return render(request, "item-s.html")

def product(request):
      return render(request, "productPreview.html")





     
