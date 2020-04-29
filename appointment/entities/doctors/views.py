from django.http import HttpResponse
import json

# from .models import *
# from .serializers import encode


def test(request):
    return HttpResponse('Doctors')
