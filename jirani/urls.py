from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static







urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search_profile, name='search_project'),
    url(r'^signup/', views.register, name='signup'),
    url(r'^edit/', views.edit_profile, name='edit_profile'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^post/$', views.upload_post, name='upload_post'),

]
