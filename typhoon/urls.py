from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'typhoon'
urlpatterns = [
    url(r'^$', views.my_homepage_view, name='my_homepage_view'),
    url(r'^submit', views.submit_sol, name='submit'),
    url(r'^viz/$', views.visualize, name='visualize'),
    #url(r'^results/$', views.results),
    url(r'^halloffame/$', views.hallOfFame, name='halloffame'),
    url(r'^result/(\d+(?:\.\d+))/$', views.result, name='result')
    # url(r'^submit_sol/thanks/$', views.thanks)
]