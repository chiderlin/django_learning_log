"Defines URL patterns for learning_log_app."
from django.urls import path
from . import views


app_name = "learning_log_app" #for urls.py辨認application用
urlpatterns = [
    # Home page
    path("index/", views.index, name="index"), # 前面URL可以自取名稱,中間引數連接views function名稱, 
                                               # 第三引數:指定URL模式名稱，讓我們能在程式碼其他部分引用它
                                               # html做連結時都會使用這個名稱而不是直接寫出URL
    # Show all topics
    path("topics/", views.topics, name="topics"),

    # Detail page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),

    # Page for adding a new topic
    path("newtopic/", views.new_topic, name="new_topic"), # 二三的引數名稱最好一致

    # Page for adding a new entry
    path("newentry/<int:topic_id>/", views.new_entry, name="new_entry"),

    # Page for editing an entry
    path("editentry/<int:entry_id>", views.edit_entry, name="edit_entry"),
]
