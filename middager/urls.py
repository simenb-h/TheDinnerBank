from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings 


urlpatterns = [
    # url(r'^middager', views.index,name='middager'),
    # url(r'^$', views.index, name='middager'),
    # url(r'^add', views.add, name='add'),
    # url(r'^insp', views.insp, name='insporation')
    #path('middager', views.index,name='middager'),
    path('', views.index, name='middager'),
    path('add/', views.add, name='add'),
    path('insp/', views.insp, name='insporation'),
    url(r'^details/(?P<id>\w{0,50})/$',views.details, name='details')

    #path('success', views.success, name = 'succsess')
]

#if settings.DEBUG:
        #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)