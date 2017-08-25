from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'profile/(\d+)', views.profile),
    url(r'remove/(\d+)', views.remove),
    url(r'add/(\d+)', views.add),
    url(r'^', views.dashboard),
]