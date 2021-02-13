from django.db import models
from django.contrib.auth.models import User # for登入者


class Topic(models.Model):
    "A topic that user is learning about."
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE) # 建立外部鍵 連接到User模型，裡面記錄著所有註冊過的使用者資料
    # public = models.BooleanField()

    def __str__(self):
        "return a string representation of the model."
        return self.text  # 網頁上要顯示什麼字 (上面定義名是text)


class Entry(models.Model): #每個類別新增日誌
    "Somethig specific learned aboout topic."
    topic = models.ForeignKey(Topic, models.CASCADE) # 把每個紀錄項目關連到特定主題(Topic)
    text = models.CharField(max_length=500) # 新版本不能不限制長度，這邊先設500
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta: # 儲存用來管理模型的額外資訊
        verbose_name_plural = 'entries' # 設定後台顯示名稱

    def __str__(self):
        "return a string representation of the model."
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text


