from django.urls import path, include

from .views import *

# Регистрация
# Авторизация
# Проверить актуальность почты



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
    path('', PatientDetail.as_view()),
    path('auth/', include('appointment.entities.patients.auth.urls'))
]
