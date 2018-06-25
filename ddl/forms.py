from django import forms
from django.db import models

from .models import Topic, Entry

'''
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

'''
'''
class EntryForm(forms.ModelForm):
#    password1 = forms.CharField(label = 'Password:', widget = forms.PasswordInput())
    text = forms.CharField(widget = forms.widgets.Select(choices=a,attrs={'class':'c1'}))
'''

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['date_ended', 'tag', 'text', 'YYYY', 'MM', 'DD']
        #fields = ['date_ended', 'text']
        labels = {'date_ended':'', 'tag':'', 'text':'', 'YYYY':'', 'MM':'', 'DD':''}
        #labels = {'date_ended':'', 'text':''}
        widgets = {'text': forms.Textarea(attrs = {'cols':80})}