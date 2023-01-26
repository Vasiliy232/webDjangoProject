from django import forms
from .tasks import send_email_job
import django_rq
from drumtraining.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    subject = forms.CharField(label='Тема', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }), required=True)

    def send_email(self):
        queue = django_rq.get_queue()
        queue.enqueue(
            send_email_job,
            self.cleaned_data.get('subject'),
            f'Отправлено сообщение "{self.cleaned_data.get("message")}" с адреса {self.cleaned_data.get("from_email")}',
            DEFAULT_FROM_EMAIL,
            RECIPIENTS_EMAIL
        )
        queue.enqueue(
            send_email_job,
            self.cleaned_data.get('subject'),
            'Ваша заявка принята. Спасибо за обращение к нашим услугам.',
            DEFAULT_FROM_EMAIL,
            self.cleaned_data.get('from_email')
        )

