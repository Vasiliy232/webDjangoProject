from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    name = forms.CharField(label='Название курса', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    started_at = forms.DateField(label='Дата начала курса', widget=forms.DateInput(attrs={
        'placeholder': 'YYYY-MM-DD',
    }))
    duration = forms.CharField(label='Длительность курса', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '3 месяца',
    }))
    price = forms.CharField(label='Стоимость курса', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '6000 рублей',
    }))
    description = forms.CharField(label='Описание курса', widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))
    img = forms.ImageField(label='', widget=forms.FileInput(attrs={
        'class': 'form-control',
        'id': 'image'
    }))

    class Meta:
        model = Course
        fields = [
            'name',
            'started_at',
            'duration',
            'price',
            'description',
            'img'
        ]
