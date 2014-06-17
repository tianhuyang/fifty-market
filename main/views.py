from django.shortcuts import render
from  django.views.generic import FormView, TemplateView
from django.views.generic.edit import CreateView
from main.forms import ContactForm, Contact


class ContactView(CreateView):
    template_name = 'main/contact.html'
    model = Contact
    exclude = ('id', 'created')
    success_url = '/main/thanks/'

class TrainingView(CreateView):
    template_name = 'main/training.html'
    model = Contact
    exclude = ('id', 'created')
    success_url = '/main/thanks/'


class ContactView1(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = '/main/thanks/'


class ThanksView(TemplateView):
    template_name = 'main/thanks.html'

