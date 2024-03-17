from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from utils.email_servies import *


# Create your views here.


def send_mail(request):
    name = str(request.GET.get('name'))
    email = str(request.GET.get('email'))
    subject = str(request.GET.get('subject'))
    message = str(request.GET.get('message'))
    context = {
        'name': name,
        'email': email,
        'subject': subject,
        'message': message
    }
    to = 'ampishdadi@outlook.com'
    # send_email(subject=subject, template='AmirWeb/contact_me.html', context=context, to_email=to)
    return HttpResponse(f'{subject} <br> {email} <br> {name} <br> {message}')
