from django.conf.urls import url
from . import views
app_name='faunasea'

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^about$',views.about,name="about"),
    url(r'^contact$',views.contact,name="contact"),
    url(r'^info$',views.info,name="info")
    ]
