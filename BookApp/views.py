from django.shortcuts import render, redirect
from BookApp.models import UsedBooks, RegisteredUsers
from django.contrib import messages

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

        if (RegisteredUsers.objects.filter(email=useremail).exists()) or (RegisteredUsers.objects.filter(username=username).exists()) or (RegisteredUsers.objects.filter(mobile_no=usermobile).exists()):
            messages.warning(request, "User Already Exists!")

            return redirect("/PageTurn")
        else:
            user_data=RegisteredUsers(full_name=userfullname, mobile_no=usermobile, email=useremail, username=username, password=userpasswd)
            user_data.save()
            messages.success(request, "User Registered Successfully!!")

            return render(request,"index.html")
        

        
    else:
        return render(request, "register.html")
