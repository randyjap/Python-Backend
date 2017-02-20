from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import JsonResponse
from .models import User, Doctor, Appointment, Patient
# from django.core import serializers

# Create your views here.

def root(request):
    context = { }
    return render(request, 'api/base.html', context)

def test(request):
    # objs = User.objects.all()
    # jsondata = serializers.serialize('json', objs)
    array = []
    users = User.objects.all()
    for user in users:
        jsondata = {}
        appointments = user.appointment_set.all()
        jsondata["appointments"] = []
        for appointment in appointments:
            jsondata["appointments"].append(appointment.time)
        jsondata["username"] = user.username
        array.append(jsondata)

    # objs = Doctor.objects.all()
    # objs = Appointment.objects.all()
    # objs = Patient.objects.all()

    # return HttpResponse(jsondata, content_type='application/json')
    return JsonResponse(array, safe=False)
