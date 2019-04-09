from django.conf.urls import url

from . import views

app_name = 'threads'
urlpatterns = [
    # ex: /b/
    url(
        r'^(?P<section_name>[a-z]+)/$', views.section_view, name='section_url'
    ),
    # ex: /b/thr/1003
    url(
        r'^(?P<section_name>[a-z]+)/thr/(?P<thread_id>\d+)/$',
        views.thread_view, name='thread_url'
    ),
    # ex: /
    url(r'^$', views.IndexView.as_view(), name='main'),
]
