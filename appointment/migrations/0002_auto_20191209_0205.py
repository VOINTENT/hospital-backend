# Generated by Django 3.0 on 2019-12-08 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appointment.User', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appointment.User', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
