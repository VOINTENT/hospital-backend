from django.http import HttpResponse
import json

from .models import ReceptionLine
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

        jsons = json.dumps(list(reception_lines), default=encode, ensure_ascii=False)

        return HttpResponse(jsons, content_type='application/json')

def registers(request):
    if request.method == 'GET':
        'ok'
    if request.method == 'POST':

        print(request.body)
