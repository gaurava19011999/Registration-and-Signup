from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
#
#
#

#   LOGIN FUNCTION IS HERE
#
# 
# 
    
def handlelogin(request):
    
    if request.method == 'POST':
        #get the post parameters
        loginusername = request.POST['loginusername']
        password = request.POST['password']
        user = authenticate(username=loginusername,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect('profile')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('handlelogin')
    else:
        return render(request, 'login.html')



#   CONTACT FUNCTION IS HERE
#
#
#

def contact(request):
    return render(request, 'contact.html')




#   YOUR PROFILE FUNCTION IS HERE
#
#
#

def profile(request):
    return render(request, 'profile.html')



#   YOUR SIGNUP FUNCTION IS HERE
#
#
#

def signup(request):
    if request.method == 'POST':
        #get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['email']
        phone = request.POST['phone']
        newpass = request.POST['newpass']
        confirmpass = request.POST['confirmpass']

        # check for errorneous inputs
        if newpass != confirmpass:
            messages.error(request, "Your Password is not same at password and confirm password ")
            return redirect('signup')


        # Create the user
        myuser = User.objects.create_user(username,email,newpass)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone = phone
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('handlelogin')
    else:
        return render(request, 'signup.html')

   