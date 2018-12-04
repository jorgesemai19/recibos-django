from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout

def login_vista(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            #log in the UserCreationForm
            return redirect('menu_lista:menu')
    else:
        form = AuthenticationForm()
    return render(request,'login/login.html',{'form':form})

def logout_vista(request):
    if request.method == 'POST':
        logout(request)
        return redirect('ingresar:login')
