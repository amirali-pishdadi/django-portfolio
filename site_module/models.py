from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت', null=True, blank=True)
    site_url = models.CharField(max_length=100, verbose_name='دامنه سایت', null=True, blank=True)
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='تلفن', null=True, blank=True)
    address = models.CharField(verbose_name='آدرس', max_length=100, null=True, blank=True)
    copy_right = models.CharField(verbose_name='متن کپی رایت', max_length=100)
    site_logo = models.ImageField(upload_to='static/images/site_setting', verbose_name='لوگو سایت', null=True, blank=True)
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی هست / نیست', default=False, null=True, blank=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام', null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی لینک های پایین صفحه'
        verbose_name_plural = 'دسته بندی های لینک های پایین صفحه'

    def __str__(self): return self.title


class FooterLink(models.Model):
    title = models.CharField(verbose_name='نام', max_length=100, null=True, blank=True)
    url = models.CharField(verbose_name='لینک', max_length=100, null=True, blank=True)
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = "لینک پایین صفحه"
        verbose_name_plural = "لینک های پایین صفحه"

    def __str__(self):
        return self.title


class HeaderPage(models.Model):
    title = models.CharField(verbose_name='نام', max_length=100, null=True, blank=True)
    url = models.CharField(verbose_name='لینک', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "لینک سر صفحه"
        verbose_name_plural = "لینک های سر صفحه ها"

    def __str__(self):
        return self.title
