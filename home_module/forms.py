from django import forms
from account_module import models


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='نام و نام خانوادگی',
                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد فرمایید'},
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل', error_messages={'required': 'لطفا ایمیل خود را وارد فرمایید'},
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'ایمیل'}))

    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'عنوان'
    }))
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'متن پیام',
        'id': 'message'

    }))
