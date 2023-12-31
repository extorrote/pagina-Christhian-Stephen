"""
URL configuration for aprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('inicio/', views.inicio, name="inicio"),
    path('', views.inicio, name="inicio"),#CUANDO DEJO LAS COMILLAS SIN NADA ADENTRO QUEDA COMO LA PAGINA PRINCIPAL Y ASI NO TENGO QUE PONER NADA EN EL NAVEGADOR, 
    path('mundo/',views.noticias_del_mundo, name="mundo"),
    path('colombia/', views.noticias_colombia, name="colombia"),
    path('mexico/', views.noticias_mexico, name="mexico"),
    path ('ecuador/', views.noticias_ecuador, name="ecuador"),
    path('crear-articulo/', views.crear_articulo, name="crear"),
    
    path('ver-articulos/', views.ver_todos_los_articulos, name="ver-articulos"),
    path('ver-video/', views.ver_video, name="ver_video"),
    path('años-pares/',views.años_pares, name="años-pares"),
    path ('contacto/' , views.contacto, name="contacto"),
    path ('ver-articulo/' , views.ver_un_articulo, name="tu-articulo"),
    path('editar-articulo/<int:id>/', views.editar_articulo, name="editar"),
    path('delete/<int:id>/',views.eliminar,name="Delete"),
   
    path('crear-articulo-formulario/', views.create_article_with_form, name="crear-articulo-formulario"),
    path('save-article/', views.create_article, name='save'),

    path('form-class/', views.crear_articulo_con_class, name="form-class") ,
    
    
]