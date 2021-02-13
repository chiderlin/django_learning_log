from django.shortcuts import render
from django.http import HttpResponseRedirect # logout, register
from django.urls import reverse # logout
from django.contrib.auth import logout # logout, register

from django.contrib.auth import login, authenticate # register
from django.contrib.auth.forms import UserCreationForm # register


def logout_view(request): # logout寫一個views功能導回index就行
    "Let user logout."
    logout(request)
    return HttpResponseRedirect(reverse("learning_log_app:index"))


def register(request):
    "register a new user."
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # new_user => print是註冊者帳號 , type是class django.contrib.auth.models.User
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # request.POST有password1 & password2 (因為頁面上有兩行輸入密碼確認的地方)
            # new_user.username => 屬性印出的是註冊者帳號
            # authenticate_user 驗證出來OK後變數也是顯示註冊者帳號
            login(request, authenticate_user) # 這會為新使用者建立有效對話(session)階段。
            return HttpResponseRedirect(reverse("learning_log_app:index"))
    context = {'form': form}
    return render(request, "registration/register.html", context)
