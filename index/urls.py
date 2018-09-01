# urls.py
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^login/$', login_views, name='login'),
    url(r'^register/$', register_views, name='register'),
    url(r'^regverify/$', regverify_views),
    url(r'^register/save/$', saveinfo_views),
    url(r'^register/lookup/$', queryinfo_views),
    url(r'^register/regmsg/$', regmsg_views),
    url(r'^oto/$', oto_views),
    url(r'^qfruit', qfruit_views),
    url(r'^06_forms/$', form_views),
    url(r'^register_forms/$', registerForm_views),
    url(r'^index/$', index_views),
    url(r'^getSource/$', getSource_views),
]

urlpatterns += [
    url(r'^quit/$', quitlogin_views),
    url(r'^check_login/$', check_login_views),
    url(r'^add_cart/$', add_cart_views),
]