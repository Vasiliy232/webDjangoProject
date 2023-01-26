from django.urls import reverse
from django.views.generic import FormView
from .forms import ContactForm
from education.views import PageTitleMixin


class ContactFormView(PageTitleMixin, FormView):
    page_title = 'Contacts'
    template_name = 'contact/contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact:contact')

