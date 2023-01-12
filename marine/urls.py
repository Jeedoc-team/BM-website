from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('product/', views.products, name = 'product'),
    path('contact/', views.contact_us, name = 'contact'),
    path('about/', views.about_us, name = 'about'),
]

