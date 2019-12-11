# Generated by Django 3.0 on 2019-12-08 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='Номер кабинета')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Отделение',
                'verbose_name_plural': 'Отделения',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('cabinets', models.ManyToManyField(to='appointment.Cabinet', verbose_name='Кабинеты')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.Department', verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('snils', models.CharField(max_length=14, unique=True, verbose_name='СНИЛС')),
                ('policy', models.CharField(max_length=16, unique=True, verbose_name='Номер страхового полиса')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.CreateModel(
            name='ReceptionLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время приема')),
            ],
            options={
                'verbose_name': 'Строка приема',
                'verbose_name_plural': 'Строки приема',
            },
        ),
        migrations.CreateModel(
            name='ReceptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата приема')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.Doctor', verbose_name='Врач')),
            ],
            options={
                'verbose_name': 'План приема',
                'verbose_name_plural': 'Планы приема',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория услуги',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Пользователь актуальный')),
                ('user_type', models.CharField(choices=[('patient', 'patient'), ('doctor', 'doctor')], default='patient', max_length=7)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('time', models.IntegerField(default=30, verbose_name='Время оказания')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.ServiceCategory', verbose_name='Категория услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='RegisterOutPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время приема')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.Patient', verbose_name='Пациент')),
                ('reception_plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.ReceptionPlan', verbose_name='План приема')),
            ],
            options={
                'verbose_name': 'Запись вне плана',
                'verbose_name_plural': 'Записи вне плана',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.Patient', verbose_name='Пациент')),
                ('reception_line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.ReceptionLine', verbose_name='Строка приема')),
            ],
            options={
                'verbose_name': 'Запись на прием',
                'verbose_name_plural': 'Записи на прием',
            },
        ),
        migrations.AddField(
            model_name='receptionplan',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.Service', verbose_name='Услуга'),
        ),
        migrations.AddField(
            model_name='receptionline',
            name='reception_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.ReceptionPlan', verbose_name='План приема'),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(default=0, verbose_name='Стоимость')),
                ('date_approval', models.DateField(verbose_name='Стоимость')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.User', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='services',
            field=models.ManyToManyField(to='appointment.Service', verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.Speciality', verbose_name='Специальность'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.User', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.Department', verbose_name='Отделение'),
        ),
    ]
