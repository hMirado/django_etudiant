from django.urls import path, re_path

from . import views

app_name = 'retard'

urlpatterns = [
    path('', views.retard, name='retard'),
    re_path('^(?P<retard_id>[A-Z-0-9]+)/$', views.detail, name="detail")
]
