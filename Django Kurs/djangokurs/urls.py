from django.contrib import admin
from django.urls import path
from core import views #importujemy nasz widok

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #strona główna
    path('o-nas/', views.about, name='about'),
    path('dodaj-usluge/', views.add_service, name='add_service'),
]
