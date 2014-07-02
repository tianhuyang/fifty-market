from django.shortcuts import render
from  django.views.generic import FormView, TemplateView, ListView
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


class ServiceView(CreateView):
    template_name = 'main/service.html'
    model = Contact
    exclude = ('id', 'created')
    success_url = '/main/thanks/'


class ContactListView(ListView):
    paginate_by = 2
    context_object_name = "contact_list"
    queryset = Contact.objects.all()
    template_name = "books/contact_list.html"


class ThanksView(TemplateView):
    template_name = 'main/thanks.html'

