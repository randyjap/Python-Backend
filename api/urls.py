from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.root, name='root'),
    url(r'^test/', views.test, name='test'),
]
