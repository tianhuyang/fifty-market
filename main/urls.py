from django.conf.urls import patterns, include, url
from main.views import ContactView, ThanksView, TrainingView, ServiceView, ContactListView


urlpatterns = patterns('',
        url(r'^contact/$', ContactView.as_view(), name='contact'),
        url(r'^training/$', TrainingView.as_view(), name='training'),
        url(r'^service/$', ServiceView.as_view(), name='service'),
        #url(r'^list/$', ContactListView.as_view(), name='list'),
        url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
)
