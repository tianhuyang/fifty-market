from django.conf.urls import patterns, include, url
from main.views import ContactView, ThanksView


urlpatterns = patterns('',
        url(r'^contact/$', ContactView.as_view(), name='contact'),
        url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
)
