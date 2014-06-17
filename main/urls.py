from django.conf.urls import patterns, include, url
from main.views import ContactView, ThanksView, TrainingView


urlpatterns = patterns('',
        url(r'^contact/$', ContactView.as_view(), name='contact'),
        url(r'^training/$', TrainingView.as_view(), name='training'),
        url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
)
