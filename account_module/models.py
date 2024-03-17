from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
age = [MinValueValidator(0), MaxValueValidator(100)]


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/user_avatar', verbose_name='آواتار', null=True, blank=True)
    about_user_short = models.CharField(verbose_name='درباره کاربر ( خلاصه )', max_length=100, null=True, blank=True)
    about_user_long = models.TextField(verbose_name='درباره کاربر ( کامل )', null=True, blank=True)
    address = models.CharField(verbose_name='آدرس', max_length=100, null=True, blank=True)
    age = models.DecimalField(verbose_name='سن', max_digits=3, decimal_places=0,
                              validators=age, max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='شماره تلفن', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.email


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class AbilityUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام توانایی')
    Percentage = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='درصد',
                                     validators=PERCENTAGE_VALIDATOR, max_length=100)
    User = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        verbose_name = 'توانایی کاربر'
        verbose_name_plural = "توانایی های کاربر"

    def __str__(self):
        return self.name


class user_education(models.Model):
    documents = models.CharField(verbose_name='مدارک', max_length=100, null=True, blank=True)
    grade = models.CharField(verbose_name='پایه', max_length=50)
    school = models.CharField(max_length=100, verbose_name='نام دانشگاه / دبیرستان / دبستان')
    User = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='کاربر')
    date_start = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='تاریخ شروع تحصیل', null=True,
                                     blank=True)
    date_end = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='تاریخ پایان تحصیل', null=True,
                                   blank=True)

    class Meta:
        verbose_name = 'تحصیل کاربر'
        verbose_name_plural = "تحصیلات کاربران"

    def __str__(self):
        return self.school


