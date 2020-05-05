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
    path('login/basic', LoginBasic.as_view()),
    path('signup', SignUp.as_view()),
    # path('doctors', doctors),
    # path('services', services),
    # path('reception-lines', reception_lines),
    # path('registers', registers),


]
