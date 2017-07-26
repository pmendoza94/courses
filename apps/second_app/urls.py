from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^addpage$', views.addpage),
    url(r'^add$', views.add),
    url(r'^show$', views.show),

]
