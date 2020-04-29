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
    path('patients/', include('appointment.entities.patients.urls')),
    path('doctors/', include('appointment.entities.doctors.urls')),
    path('services/', include('appointment.entities.services.urls')),
    path('reception_lines/', include('appointment.entities.reception_lines.urls')),
    path('registers/', include('appointment.entities.registers.urls')),


]
