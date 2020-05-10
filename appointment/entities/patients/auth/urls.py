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
    path('logout', Logout.as_view()),
    path('restore-password', RestorePassword.as_view()),
]
