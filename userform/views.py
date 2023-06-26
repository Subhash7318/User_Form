from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def userinput(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        phone=request.POST['phone']
        User.objects.create(name=name, email=email, dob=dob, phone=phone)
        send_mail(
            'form submition',
            'Your form has been submitted',
            'djangotrail01@gmail.com',
            [email],
        )
        return redirect('userform:read')
    return render(request,'userform/userform.html')

def Read(request):
    data=User.objects.all()
    context={'data':data}
    return render(request,'userform/read.html',context)