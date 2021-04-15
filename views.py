from django.shortcuts import render, redirect
from .models import Registeration
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    
    if request.method =="POST":
        firestname     = request.POST['firestname']
        lastname       = request.POST['lastname']          
        fullname       = request.POST['fullname']        
        fathername     = request.POST['fathername']      
        mobileno       = request.POST['mobileno']
        email          = request.POST['email']
        tempadd        = request.POST['tempadd']
        pin_temp            = request.POST['pin_temp']
        permadd        = request.POST['permadd']
        pin_per           = request.POST['pin_per']
        password1       = request.POST['password1']
        password2       = request.POST['password2']
        aadhar         = request.POST['aadhar']
        pan            = request.POST['pan']
        bankNo         = request.POST['bankNo']
        Holder_name    = request.POST['Holder_name']
        bankno         = request.POST['bankno']
        ifsccode        = request.POST['ifsccode']
        bankname       = request.POST['bankname']
        
        
        user = User.objects.create_user(username= username, password = password, email= email,firestname = firestname,lastname = lastname, fathername = fathername, 
                                        mobileno =mobileno, tempadd=tempadd,pin_temp =pin_temp ,permadd =permadd, pin_per= pin_per,aadhar=aadhar,pan= pan,bankNo =bankNo,Holder_name= Holder_name,
                                        bankno =bankno,ifsccode =ifsccode, bankname= bankname)
        user.save();
        print("User Created")
        return redirect('/')
    else:
        return render(request, "register.html")