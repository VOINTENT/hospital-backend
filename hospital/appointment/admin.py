from django.contrib import admin

from .models import User, Patient, Doctor, Department, Cabinet, Speciality
from .models import Service, ServiceCategory, Price, ReceptionPlan, ReceptionLine
from .models import Register, RegisterOutPlan


class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'email', 'phone_number')
    list_display_links = ('login',)
    search_fields = ('login',)

# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('user', 'name', 'surname', 'patronymic', 'birth_date', 'snils', 'policy')
#     list_display_links = ('login',)
#     search_fields = ('login',)

admin.site.register(User, UserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Cabinet)
admin.site.register(Speciality)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(Price)
admin.site.register(ReceptionPlan)
admin.site.register(ReceptionLine)
admin.site.register(Register)
admin.site.register(RegisterOutPlan)
