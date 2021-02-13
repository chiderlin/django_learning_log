from django.shortcuts import render
from django.http import HttpResponseRedirect # form
from django.urls import reverse # form # 舊版from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required # 裝飾器
from django.http import Http404
from django.shortcuts import get_object_or_404 # 引發404例外

from .models import Topic, Entry
from .forms import TopicForm, EntryForm  # form

def index(request):
    "Home page for learning log."
    return render(request, "learning_log_app/index.html")

@login_required #讓python執行topics前先執行login_required函式 # 檢測使用者是否已登入，登入成功才可到這個topics頁面
def topics(request):
    "Show all topics."
    # topics = Topic.objects.order_by("date_added") #QuerySet
    topics = Topic.objects.filter(owner=request.user).order_by("date_added") # 修改成 => 限制只能存取屬於自己的主題
    context = {"topics": topics} #把內容以json方式傳到html那邊做處裡
    return render(request, "learning_log_app/topics.html", context)

@login_required
def topic(request, topic_id):
    # topic = Topic.objects.get(id=topic_id) #先指定哪個topic
    topic = get_object_or_404(Topic, id=topic_id) # 請求不存在的主題就會404錯誤
    # Make sure the topic belongs to the current user!
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by("date_added") #得到特定topic裡面的所有文章
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_log_app/topic.html", context)

@login_required
def new_topic(request):
    "Add a new topic."
    if request.method != "POST": # 第一次請求頁面時瀏覽器是會傳送GET請求
        form = TopicForm() # 回傳空表單，不會引起錯誤
    else:
        form = TopicForm(data=request.POST) # 使用者傳送表單料時才是POST請求
        if form.is_valid():
            new_topic = form.save(commit=False) # 如果直接儲存會有owner_id不可為NULL的錯誤，所以這邊先不commit
            new_topic.owner = request.user # 設定完owner是登入者後再save到DB
            new_topic.save()
            return HttpResponseRedirect(reverse("learning_log_app:topics")) # 頁面redirect但是資料會繼續往下傳
    
    context = {"form": form}
    return render(request, "learning_log_app/new_topic.html", context)  

@login_required
def new_entry(request, topic_id):
    "Add a new entry for a particular topic."
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # commit=False先不儲存進DB中
            # print(new_entry) # 新增的文字內容 是class
            # print(new_entry.topic) # 原來裡面是沒有東西 列印會報錯
            new_entry.topic = topic # 存進去之後
            # print(new_entry.topic) # 才印得出來
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_log_app:topic", args=[topic_id])) # args串列中放入URL中所有的引數(這個URL目前只有topic_id一個引數)
    context = {"topic": topic, "form": form}
    return render(request, "learning_log_app/new_entry.html", context)

@login_required
def edit_entry(request, entry_id): # entry_id => 每一篇文章的號碼
    "Edit an existing entry."
    # entry = Entry.objects.get(id=entry_id) # 得到特定的entry text文章內容
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic # 得到該topic名稱
    check_topic_owner(topic, request) # 另外寫一個驗證函式
    if request.method != "POST":
        form = EntryForm(instance=entry) #instance把entry匯入才可以在修改方塊中瀏覽到內容!否則會空白
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_log_app:topic",args=[topic.id])) # args要給的引數是前面URL所需要的引數，而非此函數的引數!!!
    
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_log_app/edit_entry.html", context)


def check_topic_owner(topic_obj, request):
    if topic_obj.owner != request.user:
        raise Http404