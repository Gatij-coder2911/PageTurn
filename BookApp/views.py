from django.shortcuts import render, redirect
from BookApp.models import UsedBooks, RegisteredUsers
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    # fetch UsedBooks details from database
    bookobjs=UsedBooks.objects.all()
    
    return render(request,"index.html",{'ubook':bookobjs})

def register(request):

    if request.method=="POST":
        userfullname=request.POST['userfullname']
        usermobile=request.POST['usermobile']
        useremail=request.POST['useremail']
        username=request.POST['username']
        userpasswd=request.POST['userpasswd']

        if (RegisteredUsers.objects.filter(email=useremail).exists()) or (RegisteredUsers.objects.filter(mobile_no=usermobile).exists()):
            messages.warning(request, "User Already Exists!")

            return redirect("/PageTurn")
        
        elif (RegisteredUsers.objects.filter(username=username).exists()):
            messages.warning(request, "User with same Username already Exists!")

            return redirect("/PageTurn")

        else:
            user_data=RegisteredUsers(full_name=userfullname, mobile_no=usermobile, email=useremail, username=username, password=userpasswd)
            user_data.save()
            messages.success(request, "User Registered Successfully!!")

            # subject = 'Welcome to PageTurn'
            # message = 'Hi {}, thank you for registering in PageTurn'.format(username)
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [useremail, ]
            # send_mail( subject, message, email_from, recipient_list )

            return redirect("/PageTurn")

def login(request):

    if request.method=="POST":
        username=request.POST['username']
        userpasswd=request.POST['userpasswd']

        if (RegisteredUsers.objects.filter(username=username,password=userpasswd)):
            messages.success(request, "Login Successful!")

            return render(request, "login.html")
        else:
            messages.warning(request, "User not Found!")

            return render(request, "login.html")
    else:
        return render(request, "login.html")

def whyuse(request):
    return render(request, "whyuse.html")

def mostlybought(request):
    return render(request, "mostlybought.html")

def aboutus(request):
    return render(request, "aboutus.html")

def termsconditions(request):
    return render(request, "terms.html")

def privacypolicy(request):
    return render(request, "privacy.html")

def safetytips(request):
    return render(request, "safety.html")

def helpline(request):
    return render(request, "helpline.html")

def sellbooks(request):
    return render(request, "sell.html")