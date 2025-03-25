from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #  path('', views.index, name='index'),
    path('', views.ListaPosts, name='Home'), 
    path('post/<int:id>/', views.Link, name='Post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
