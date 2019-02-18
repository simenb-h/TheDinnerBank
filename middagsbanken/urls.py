from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^middager', include('middager.urls')),
    # url(r'^$', include('middager.urls')),
    # url(r'^add', include('middager.urls')),
    # url(r'^insp', include('middager.urls'))
    #path('middager/', include('middager.urls')),
    path('', include('middager.urls')),
    path('add/', include('middager.urls')),
    path('insp/', include('middager.urls'))
]

