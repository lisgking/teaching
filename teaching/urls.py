from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /teaching/
    url(r'^$', views.index, name='index'),
    # ex: /teaching/5/
    url(r'^(?P<question_id>[0-9a-z]+)/$', views.detail, name='detail'),
    # ex: /teaching/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /teaching/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # login
    url(r'^login$', views.login, name='login'),
]