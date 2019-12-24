from django.urls import path

from .views import *

urlpatterns = [
    path ('patients', patients),
    path ('doctors', doctors),
    path ('services', services),
    path ('reception-lines', reception_lines),
    path ('registers', registers),

]
