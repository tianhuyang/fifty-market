from django.conf.urls import patterns, include, url
from django.contrib import admin
from market.views import IndexView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
