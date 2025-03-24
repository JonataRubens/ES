from django.urls import path
from . import views
from .views import lista_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.index, name='index'),
     path('', views.lista_posts, name='lista_posts'), 
    path('post/<int:id>/',view.test_link, name= 'Post')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)