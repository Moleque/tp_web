from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hot$', views.hot, name='hot'),
    url(r'^question/(\d+)$', views.question, name='question'),
    url(r'^ask$', views.ask, name='ask'),
    url(r'^tag/(?P<tag_id>\d+)$', views.tag, name='tag'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^login$', views.login, name='login'),
    #url(r'^login_in$', views.login, name='login_in'),
    url(r'^signup$', views.signup, name='signup'),
]