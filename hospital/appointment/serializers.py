import json

from .models import *

def encode(object):
    if isinstance(object, User):
        return {
            'id': object.id,
            'login': object.login,
            'password': object.password,
            'email': object.email,
            'phone_number': object.phone_number,
            'date_creation': str(object.date_creation),
            'is_active': object.is_active,
        }

    elif isinstance(object, Patient):
        return {
            'id': object.id,
            'user': encode(object.user),
            'name': object.name,
            'surname': object.surname,
            'patronymic': object.patronymic,
            'birth_date': str(object.birth_date),
            'snils': object.snils,
            'policy': object.policy,
        }

    elif isinstance(object, Doctor):
        return {
            'id': object.id,
            'name': object.name,
            'surname': object.surname,
            'patronymic': object.patronymic,
            'birth_date': str(object.birth_date),
            'speciality': encode(object.speciality),
            'department': encode(object.department),
            'services': [encode(service) for service in object.services.all()],
            'department': encode(object.department),

        }

    elif isinstance(object, Speciality):
        return {
            'id': object.id,
            'name': object.name
        }

    elif isinstance(object, Department):
        return {
            'id': object.id,
            'name': object.name
        }

    elif isinstance(object, Cabinet):
        return {
            'id': object.id,
            'number': object.number,
            'department': encode(object.department)
        }

    elif isinstance(object, Service):
        return {
            'id': object.id,
            'category': encode(object.category),
            'name': object.name,
            'description': object.description,
            'time': str(object.time)
        }

    elif isinstance(object, ServiceCategory):
        return {
            'id': object.id,
            'name': object.name
        }

    elif isinstance(object, Price):
        return {
            'id': object.id,
            'service': encode(object.service),
            'cost': object.cost,
            'date_approval': object.date_approval,
        }

    elif isinstance(object, ReceptionPlan):
        return {
            'id': object.id,
            'service': encode(object.service),
            'doctor': encode(object.doctor),
            'date': str(object.date)
        }

    elif isinstance(object, ReceptionLine):
        return {
            'id': object.id,
            'reception_plan': encode(object.reception_plan),
            'time': str(object.time)
        }

    elif isinstance(object, Register):
        return {
            'id': object.id,
            'reception_line': encode(object.reception_line),
            'patient': encode(object.patient)
        }

    else:
        type_name = object.__class__.__name__
        raise TypeError(f'Object of type "{type_name}" is not JSON serializable')
