import time

from django.http import HttpResponse
from django.template.loader import get_template

from django.http import HttpResponse
from django.http import JsonResponse

from switcher.settings import PIN
from switcher.relay import Switch

s = Switch(PIN)

def on(request):
    s.on()
    return HttpResponse(status=200)

def off(request):
    s.off()
    return HttpResponse(status=200)

def switch(request):
    if s.get_state() == 1:
        s.on()
        return HttpResponse("Switched on", status=200)
    else:
        s.off()
        return HttpResponse("Switched off", status=200)

def state(request):
    state = s.get_state()
    if state == 0:
        return HttpResponse('<img src=/static/pictures/lamp_on.png>', status = 200)
    else:
        return HttpResponse('<img src=/static/pictures/lamp_off.png>', status = 200)

def show(request):
    template = get_template('switch.html')
    html = template.render({ "state": s.get_state() })
    return HttpResponse(html)