from django.http import HttpResponse
from django.views.generic import View
import json


import appointment.mistakes as mistakes
from appointment.models import *
from appointment.utils import get_response_template, get_payload


class PatientDetail(View):

    def get(self, request, *args, **kwargs):
        resp = get_response_template()

        token = request.COOKIES.get('token')
        if not token:
            resp['status'] = mistakes.NOT_AUTHORIZED[0]
            resp['msg'] = mistakes.NOT_AUTHORIZED[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=401)

        payload = get_payload(token)
        if not payload:
            resp['status'] = mistakes.NOT_VALID_TOKEN[0]
            resp['msg'] = mistakes.NOT_VALID_TOKEN[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=401)
        user_id = payload['id']

        patient = Patient.objects.get(user=User.objects.get(pk=user_id))
        resp_data = {
            'user_id': patient.user.id,
            'patient_id': patient.id,
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'middle_name': patient.middle_name,
            'birth_date': patient.birth_date,
            'snils': patient.snils,
            'policy': patient.policy,
            'email': patient.user.email,
            'phone_number': patient.user.phone_number
        }

        resp['status'] = 0
        resp['msg'] = 'ok'
        resp['data'] = resp_data
        return HttpResponse(json.dumps(resp), content_type='application/json', status=200)
