from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [  

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^user_bizz/', include('user_bizz.urls', namespace='user_bizz')),    
    url(r'^$', 'apps.views.home'),
]
