from django.urls import path, include

from .views import *

# Регистрация
# Авторизация
# Проверить актуальность почты


#
# entities/...
#   patients
#       auth/
#           signin/...
#               basic
#           signup
#   doctors
#   services
#   reception-lines
#   registers

urlpatterns = [
    path('', test),
    # path('patients', include('appointment.entities.patients')),
    # path('doctors', doctors),
    # path('services', services),
    # path('reception-lines', reception_lines),
    # path('registers', registers),


]
