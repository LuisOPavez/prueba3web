"""
URL configuration for paginaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('desc_Cell1/', views.desc_Cell1, name='desc_Cell1'),
    path('compras/', views.compras, name='compras'), 
    path('desc_TV1/', views.desc_TV1, name='desc_TV1'),
    path('desc_TV2/', views.desc_TV2, name='desc_TV2'), 
    path('desc_Cell2/', views.desc_Cell2, name='desc_Cell2'),
    path('desc_Micro1/', views.desc_Micro1, name='desc_Micro1'),
    path('desc_Micro2/', views.desc_Micro2, name='desc_Micro2'),
    path('desc_Pc1/', views.desc_Pc1, name='desc_Pc1'),
    path('desc_Pc2/', views.desc_Pc2, name='desc_Pc2'),    
    path('desc_Pc3/', views.desc_Pc3, name='desc_Pc3'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('items/', include('items.urls')),  
    path('', include('productos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
