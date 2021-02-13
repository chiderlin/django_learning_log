"Defines URL patterns for users."
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # 用系統本身的login  URL自行設定了login
    path('', include("django.contrib.auth.urls"), name="login"),

    # logout
    path('', views.logout_view, name='logout'), # 自己寫function連接
    # path('', include("django.contrib.auth.urls"), name="logout"), # Django內建登出，但是會連到後台的頁面

    # Registration page
    path('register/', views.register, name='register'),
]
