from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"] # 表單只有在text欄位
        labels = {"text": ""} # 不要在text欄位加上標籤 (label =>應該是HTML上的)
        widgets = {"public": forms.CheckboxInput()}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols":80})} # 多行文字方塊，文字區塊寬度:80
