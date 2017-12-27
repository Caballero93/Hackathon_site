from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.my_homepage_view),
    url(r'^submit', views.submit_sol),
    url(r'^viz/$', views.visualize),
    url(r'^results/$', views.results),
    url(r'^halloffame/$', views.hallOfFame)
    # url(r'^submit_sol/thanks/$', views.thanks)
]