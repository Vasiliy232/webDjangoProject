from django.urls import path
import contact.views as contact


app_name = 'contact'

urlpatterns = [
    path('contacts/', contact.ContactFormView.as_view(), name='contact')
]
