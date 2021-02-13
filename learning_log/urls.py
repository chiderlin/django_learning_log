from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_log_app.urls', namespace='learning_log_app')), 
    # namespace引數讓我們能將learning_log_app的URL和其他專案URL區分開，這在專案擴充時會很有用。
    # 要在learning_log_app.urls裡面寫app_name = 'learning_log_app' namespace才會設定成功!

    # 新增login/logout/register 功能 => 連接users application
    path('users/', include('users.urls', namespace='users'))
]

