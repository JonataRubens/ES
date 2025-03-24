from django.urls import path
from . import views
from .views import lista_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.index, name='index'),
     path('', views.lista_posts, name='lista_posts'), 
    path('post/<int:pk>/',view.lista_posts, name= 'lista_posts')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)