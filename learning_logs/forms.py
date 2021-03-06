from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Name'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}