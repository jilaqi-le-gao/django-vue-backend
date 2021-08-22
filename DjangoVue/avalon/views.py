from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
# Create your views here.


def TestSession(requests):
    requests.session['info'] = 'Hello session'
    requests.session['number'] = np.random.rand()
    print(requests.session['number'])
    return HttpResponse('You got session!')


def ShowSession(requests):
    return HttpResponse(f'Your Rand Number is {requests.session["number"]}')


def DelSession(requests):
    del requests.session['info']
    del requests.session['number']
    return HttpResponse(f'Your Session info is deleted!')
