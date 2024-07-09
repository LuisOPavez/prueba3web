from django.contrib import admin
from django.urls import path
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('desc_Cell1/', views.desc_Cell1, name='desc_Cell1'),
    path("accounts/", include("django.contrib.auth.urls")),
    # Agrega más rutas según sea necesario
]
