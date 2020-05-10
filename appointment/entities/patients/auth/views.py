from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import View
import json

import appointment.mistakes as mistakes
from appointment.models import User, Patient
from appointment.serializers import encode
from appointment.utils import get_token, get_response_template

import hashlib

# from .models import *
# from .serializers import encode


def test(request):
    return HttpResponse('Auth')

# Проверить, адекватены ли все значения
# Проверить существование уникальных значений


"""
    {
        last_name: ...,
        first_name: ...,
        middle_name: ...,
        email: ...,
        phone_number: ...,
        password: ...
    }
    =============================
    {
        status: ...,
        msg: ...,
        data: ...,
    }
    status:
    -1 - не введен email
"""


class SignUp(View):

    def post(self, request, *args, **kwargs):
        resp = get_response_template()
        data = request.POST

        # Валидация TODO
        if not data.get('last_name'):
            resp['status'] = mistakes.NOT_LAST_NAME[0]
            resp['msg'] = mistakes.NOT_LAST_NAME[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if not data.get('first_name'):
            resp['status'] = mistakes.NOT_FIRST_NAME[0]
            resp['msg'] = mistakes.NOT_FIRST_NAME[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if not data.get('middle_name'):
            resp['status'] = mistakes.NOT_MIDDLE_NAME[0]
            resp['msg'] = mistakes.NOT_MIDDLE_NAME[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if not data.get('email'):
            resp['status'] = mistakes.NOT_EMAIL[0]
            resp['msg'] = mistakes.NOT_EMAIL[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if not data.get('phone_number'):
            resp['status'] = mistakes.NOT_PHONE_NUMBER[0]
            resp['msg'] = mistakes.NOT_PHONE_NUMBER[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if not data.get('password'):
            resp['status'] = mistakes.NOT_PASSWORD[0]
            resp['msg'] = mistakes.NOT_PASSWORD[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        # Проверка наличия уникальных записей в БД
        if User.objects.filter(email=data['email']).exists():
            resp['status'] = mistakes.EMAIL_EXISTS[0]
            resp['msg'] = mistakes.EMAIL_EXISTS[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if User.objects.filter(phone_number=data['phone_number']).exists():
            resp['status'] = mistakes.PHONE_NUMBER_EXISTS[0]
            resp['msg'] = mistakes.PHONE_NUMBER_EXISTS[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        user = User.objects.create(
            password=hashlib.sha512(data['password'].encode('utf-8')).hexdigest(),
            email=data['email'],
            phone_number=data['phone_number']
        )

        patient = Patient.objects.create(
            user=user,
            last_name=data['last_name'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            birth_date=None,
            snils=None,
            policy=None
        )

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

        response = HttpResponse(
            json.dumps(resp, default=encode),
            content_type='application/json',
            status=201)
        response.set_cookie('token', get_token(user))
        return response


class LoginBasic(View):

    def post(self, request, *args, **kwargs):
        resp = get_response_template()
        data = request.POST

        # Валидация
        if not data.get('email_or_phone'):
            resp['status'] = mistakes.NOT_EMAIL_OR_PHONE_NUMBER[0]
            resp['msg'] = mistakes.NOT_EMAIL_OR_PHONE_NUMBER[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        if not data.get('password'):
            resp['status'] = mistakes.NOT_PASSWORD[0]
            resp['msg'] = mistakes.NOT_PASSWORD[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        hash_password = hashlib.sha512(data['password'].encode('utf-8')).hexdigest()
        q = (Q(email=data['email_or_phone']) | Q(phone_number=data['email_or_phone'])) & Q(password=hash_password)

        user = User.objects.filter(q).first()
        if not user:
            resp['status'] = mistakes.WRONG_EMAIL_OR_PHONE_NUMBER[0]
            resp['msg'] = mistakes.WRONG_EMAIL_OR_PHONE_NUMBER[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=400)

        patient = Patient.objects.get(user=user)
        resp_data = {
            'user_id': user.id,
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

        response = HttpResponse(
            json.dumps(resp, default=encode, ensure_ascii=False),
            content_type='application/json',
            status=200)
        response.set_cookie('token', get_token(user))
        return response


class Logout(View):

    def delete(self, request, *args, **kwargs):
        resp = get_response_template()

        token = request.COOKIES.get('token')
        if not token:
            resp['status'] = mistakes.NOT_AUTHORIZED[0]
            resp['msg'] = mistakes.NOT_AUTHORIZED[1]
            return HttpResponse(json.dumps(resp), content_type='application/json', status=401)

        resp['status'] = 0
        resp['msg'] = 'ok'
        response = HttpResponse(json.dumps(resp), content_type='application/json', status=200)
        response.delete_cookie('token')
        return response


class RestorePassword(View):

    def post(self, request, *args, **kwargs):
        resp = get_response_template()

        resp['status'] = 0
        resp['msg'] = 'ok'
        return HttpResponse(json.dumps(resp), content_type='application/json', status=200)
