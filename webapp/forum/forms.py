from django.forms import ModelForm
from django import forms
from .models import Topic, Message

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_theme']
        labels = {
            'topic_theme': 'Введите название'
        }
        widgets = {
            'topic_theme': forms.TextInput(attrs={
                'class': 'form-control'

            })

        }

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["message_text"]
        labels = {
            'message_text': 'Введите сообщение'
        }
        widgets = {
            'message_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            })
        }

