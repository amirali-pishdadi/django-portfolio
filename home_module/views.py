from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
import random
from django.views import View
from home_module.forms import ContactForm
from account_module.models import *
from site_module.models import SiteSetting
from django.contrib.auth.hashers import make_password
from utils.email_servies import send_email
from django.template.loader import render_to_string
from django.template import RequestContext


# Create your views here.


class MainPageBasedView(View):
    def get(self, request: HttpRequest):
        is_main_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        user: User = User.objects.filter(is_superuser=True).first()
        num_education = [user.user_education_set.count()]
        odd_education = []
        for number in num_education:
            if number % 2 != 0:
                odd_education.append(number)
        contact_form = ContactForm()
        context = {
            'is_main_setting': is_main_setting,
            'user': user,
            'odd_education': odd_education,
            'num_education': num_education,
            'contact_form': contact_form
        }

        return render(request, 'home_module/main_page.html', context)

    def post(self, request: HttpRequest):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            message = contact_form.cleaned_data['message']
            html = render_to_string('home_module/email_page.html', {
                'full_name': full_name,
                'email': email,
                'title': title,
                'message': message
            })
            email_akhar = mail.send_mail('Subject', 'Message',
                                         settings.EMAIL_HOST_USER,
                                         ['ampishdadi@outlook.com', 'amirpishdadi4@gmail.com'],
                                         html_message=html)
            print('Email sended')
            return redirect('home_page')


        else:
            return HttpResponse('error')
