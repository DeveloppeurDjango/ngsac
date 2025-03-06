from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, service, detail, search, about, contact, confirmation

urlpatterns = [
    path('',home, name="home"),
    path('service',service, name="service"),
    path('about',about, name="about"),    

    path('contact', contact, name='contact'),
    path('confirmation', confirmation, name='confirmation'),
    path('article/<int:id_article>', detail, name = "detail"),
    path('article/recherche', search, name = "search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
