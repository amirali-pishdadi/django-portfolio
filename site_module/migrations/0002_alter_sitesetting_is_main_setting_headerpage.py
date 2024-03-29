# Generated by Django 4.1.2 on 2022-11-01 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='is_main_setting',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تنظیمات اصلی هست / نیست'),
        ),
        migrations.CreateModel(
            name='HeaderPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'صفحات سر صفحه',
                'verbose_name_plural': 'صفحات سر صفحه ها',
            },
        ),
    ]
