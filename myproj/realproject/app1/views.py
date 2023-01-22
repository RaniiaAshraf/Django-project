from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Donation
from .forms import Donationform
from .forms import CreateUserForm
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
 
# Create your views here.
def renderhtml(request):
    return render(request, 'app1/index.html')
def viewhtml(request):
    return render(request, 'app1/contact.html')

def registerPage(request):
    form = CreateUserForm()
    context ={'form':form}
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    return render(request,'app1/register.html',context)


def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('viewDonation')
    return render(request,'app1/login.html')

def viewDonation(request):
    return render(request,'app1/main.html', {"cars":Donation.objects.all()})

def createDonation(request):
    donation = Donationform(request.POST , request.FILES)
    if donation.is_valid():
        donation.save()
    else:
        print("not valid")
    return render ( request , 'app1/create.html' , {"form":Donationform})

def showDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    # print(car)
    return render(request, 'app1/details.html',{"donation":donation})

def deleteDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    donation.delete()
    return render (request, 'app1/main.html',{"cars":Donation.objects.all()})

def updateDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    form = Donationform(request.POST or None , request.FILES or None , instance=donation  )
    if form.is_valid():
        form.save()
    else:
        print("not valid")
    return render(request, 'app1/update.html',{"donation":donation,"form":form}) 

    