from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

from .models import *
from .serializers import encode

def reception_lines(request):
    if request.method == 'GET':
        date = request.GET.get('date', '')
        service_id = request.GET.get('service-id', '')
        time = request.GET.get('time', '')

        filter = {}
        if date:
            filter['reception_plan__date'] = date
        if service_id:
            filter['reception_plan__service__id'] = service_id
        if time:
            filter['time'] = time

        reception_lines = ReceptionLine.objects.filter(**filter)

        reception_lines_json = json.dumps(list(reception_lines), default=encode, ensure_ascii=False)

        return HttpResponse(reception_lines_json, content_type='application/json')


def patients(request):
    patients = Patient.objects.all()
    patients_json = json.dumps(list(patients), default=encode, ensure_ascii=False)
    return HttpResponse(patients_json, content_type='application/json')


def doctors(request):
    doctors = Doctor.objects.all()
    doctors_json = json.dumps(list(doctors), default=encode, ensure_ascii=False)
    return HttpResponse(doctors_json, content_type='application/json')


def services(request):
    services = Service.objects.all()
    services_json = json.dumps(list(services), default=encode, ensure_ascii=False)
    return HttpResponse(services_json, content_type='application/json')


@csrf_exempt
def registers(request):
    if request.method == 'GET':
        registers = Register.objects.all()
        registers_json = json.dumps(list(registers), default=encode, ensure_ascii=False)
        return HttpResponse(registers_json, content_type='application/json')

    if request.method == 'POST':

        body = json.loads(request.body)

        reception_line_id = body['reception_line_id']
        patient_id = body['patient_id']

        register = Register.objects.create(reception_line_id=reception_line_id, patient_id=patient_id)
        register_json = json.dumps(register, default=encode, ensure_ascii=False)

        return HttpResponse(register_json, content_type='application/json')
