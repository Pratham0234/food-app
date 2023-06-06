from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUser
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method =='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username} , your account has been created')
            return redirect('login')
    else:
        form=RegisterUser()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

