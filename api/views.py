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
    # return HttpResponse(jsondata, content_type='application/json')
    jsondata = { }
    users = User.objects.all()
    doctors = Doctor.objects.all()
    for user in users:
        for doctor in doctors:
            jsondata["doctor"] = doctor.first_name
        jsondata["username"] = user.username

    # objs = Doctor.objects.all()
    # objs = Appointment.objects.all()
    # objs = Patient.objects.all()

    return JsonResponse(jsondata)
