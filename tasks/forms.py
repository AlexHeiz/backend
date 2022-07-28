from .models import Task
from django.forms import ModelForm, Textarea, TextInput
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }
