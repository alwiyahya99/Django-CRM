from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')

def keuangan(request):
    template = loader.get_template('keuangan.html')
    context = {
        'name_page': 'Keuangan',
    }
    return HttpResponse(template.render(context, request))   

def pekerjaan(request):
    return render(request, 'pekerjaan.html')

def pegawai(request):
    return render(request, 'pegawai.html')