"""hackaton_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hackaton_test import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^typhoon/', include("typhoon.urls"))
    # url(r'^$', views.my_homepage_view),
    # url(r'^submit', views.submit_sol),
    # url(r'^viz/$', views.visualize),
    # url(r'^results/$', views.results)
    # url(r'^submit_sol/thanks/$', views.thanks)
]
