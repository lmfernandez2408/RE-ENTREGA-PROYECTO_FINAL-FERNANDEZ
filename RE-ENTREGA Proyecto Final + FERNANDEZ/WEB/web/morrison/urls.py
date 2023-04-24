from django.urls import path, include
from morrison.urls import *
from . import views 
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('mapas', views.mapas, name='mapas'),
    path('subir', views.subir_pedido, name='subir'),
    path('editar', views.editar, name='editar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
