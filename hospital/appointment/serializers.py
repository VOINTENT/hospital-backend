import json

from .models import ReceptionLine, ReceptionPlan, Service, ServiceCategory, Doctor

def encode(object):
    if isinstance(object, ReceptionLine):
        return {
            'id': object.id,
            'reception_plan': encode(object.reception_plan),
            'time': str(object.time)
        }

    elif isinstance(object, ReceptionPlan):
        return {
            'id': object.id,
            'service': encode(object.service),
            'doctor': encode(object.doctor),
            'date': str(object.date)
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

    elif isinstance(object, Doctor):
        return {
            'id': object.id,
            'name': object.name,
            'surname': object.surname,
            'patronymic': object.patronymic,
            'birth_date': str(object.birth_date),
            'speciality': str(object.speciality),
            'department': str(object.department),
        }

    else:
        type_name = object.__class__.__name__
        raise TypeError(f'Object of type "{type_name}" is not JSON serializable')
