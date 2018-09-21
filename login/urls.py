
from django.contrib import admin
from django.conf.urls import  include, url
#from django.views.generic import direct_to_template
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', 'loginpage.views.UserRegistration'),
   # url(r' $', direct_to_template, {'template': 'index.html'}),
    url(r'^login/$', 'loginpage.views.LoginRequest'),
    url(r'^logout/$', 'loginpage.views.LogoutRequest'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
