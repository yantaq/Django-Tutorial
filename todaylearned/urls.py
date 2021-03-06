from django.conf.urls import url

from . import views

app_name = 'todaylearned'
urlpatterns = [
    # ex: /entry/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_id>[0-9]+)/$', views.details, name='details'),
]
