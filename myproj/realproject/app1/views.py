from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Donation , Funded
from .forms import Donationform , Fund
from .forms import CreateUserForm
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
 
# Create your views here.
def renderhtml(request):
    return render(request, 'app1/index.html')
def viewhtml(request):
    return render(request, 'app1/contact.html')
def homehtml(request):
    return render(request, 'app1/index.html')

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
    return render(request,'app1/main.html', {"project":Donation.objects.all()})

@login_required(login_url='login')
def createDonation(request):
    donation = Donationform(request.POST , request.FILES)
    if donation.is_valid():
        instance = donation.save(commit=False)
        instance.user = request.user
        instance.save()
        donation.save()
    else:
        print("not valid")
    return render ( request , 'app1/create.html' , {"form":Donationform})

def showDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    return render(request, 'app1/details.html',{"donation":donation})

def deleteDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    donation.delete()
    return render (request, 'app1/main.html',{"project":Donation.objects.all()})

def updateDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    form = Donationform(request.POST or None , request.FILES or None , instance=donation  )
    if form.is_valid():
        form.save()
    else:
        print("not valid")
    return render(request, 'app1/update.html',{"donation":donation,"form":form}) 

@login_required(login_url='login')
def showfundID(request,id):
    project= Donation.objects.get(pk = id)
    val=Fund(request.POST)
    if val.is_valid():
       instance = val.save(commit=False) 
       project.Targetprice=project.Targetprice+int(instance.number)  
       project.save()
       return redirect('viewDonation')
    project = Donation.objects.get(pk = id)
    return render(request,'app1/funddetails.html',{"form" : val})