from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


    # Create your views here.
def login(request):

    if request.method== 'POST':
        username=request.POST['Username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


    return render(request,"login.html")


def register(request):
    if request.method== 'POST':
        username=request.POST['Username']
        first_name=request.POST['First_name']
        last_name=request.POST['Lastname']
        email=request.POST['Email']
        password=request.POST['password']
        confirm_pass= request.POST['password1']

        if password==confirm_pass:

            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect("register")

            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"password is not match")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')