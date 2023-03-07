from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render

User = get_user_model()


def Signup(request):


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('accueil')

    return render(request, 'accounts/signup.html')


def Login_user(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('accueil')
    return render(request, 'accounts/login.html')

def Logout_user(resquest):
    logout(resquest)
    return redirect('accueil')