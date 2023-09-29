from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index),
    path('muscle/<int:muscle_id>/', show_muscle, name='muscle'),
    path('admin/', admin.site.urls),
]
