from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static







urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search_profile, name='search_project'),
    url(r'^signup/', views.register, name='signup'),

]
