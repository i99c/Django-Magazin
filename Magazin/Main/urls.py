from django.urls import path
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', index, name='Main/base'),
]
