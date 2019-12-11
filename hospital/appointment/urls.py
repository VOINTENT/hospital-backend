from django.urls import path

from .views import reception_lines, registers

urlpatterns = [
    path ('reception-lines/', reception_lines),
    path ('registers/', registers),
]
