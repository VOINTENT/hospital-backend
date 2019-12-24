from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Пользователь актуальный')

    choices = (
        ('patient', 'patient'),
        ('doctor', 'doctor')
    )
    user_type = models.CharField(max_length=7, choices=choices, default='patient')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Patient(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    snils = models.CharField(max_length=14, unique=True, verbose_name='СНИЛС')
    policy = models.CharField(max_length=16, unique=True, verbose_name='Номер страхового полиса')

    def __str__(self):
        return self.surname + ' ' + self.name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Doctor(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    speciality = models.ForeignKey('Speciality', on_delete=models.SET_NULL, null=True, verbose_name='Специальность')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name='Отделение')
    services = models.ManyToManyField('Service', verbose_name='Услуги')
    cabinets = models.ManyToManyField('Cabinet', verbose_name='Кабинеты')

    def __str__(self):
        return self.surname + ' ' + self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Speciality(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'


class Cabinet(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер кабинета')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name='Отделение')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Service(models.Model):
    category = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True, verbose_name='Категория услуги')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True)
    time = models.IntegerField(default=30, verbose_name='Время оказания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'


class Price(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')
    cost = models.IntegerField(default=0, verbose_name='Стоимость')
    date_approval = models.DateField(verbose_name='Стоимость')  # TODO:

    def __str__(self):
        return str(self.cost)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class ReceptionPlan(models.Model):
    service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='Услуга')
    doctor = models.ForeignKey('Doctor', on_delete=models.PROTECT, verbose_name='Врач')
    date = models.DateField(verbose_name='Дата приема')

    def __str__(self):
        return str(self.doctor) + ' ' + str(self.date)

    class Meta:
        verbose_name = 'План приема'
        verbose_name_plural = 'Планы приема'


class ReceptionLine(models.Model):
    reception_plan = models.ForeignKey('ReceptionPlan', on_delete=models.PROTECT, verbose_name='План приема')
    time = models.TimeField(verbose_name='Время приема')

    def __str__(self):
        return str(self.reception_plan) + ' ' + str(self.time)

    class Meta:
        verbose_name = 'Строка приема'
        verbose_name_plural = 'Строки приема'

class Register(models.Model):
    reception_line = models.ForeignKey('ReceptionLine', on_delete=models.PROTECT, verbose_name='Строка приема')
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT, verbose_name='Пациент')

    def __str__(self):
        return str(self.reception_line) + ' ' + str(self.patient)

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'


class RegisterOutPlan(models.Model):
    reception_plan = models.ForeignKey('ReceptionPlan', on_delete=models.PROTECT, verbose_name='План приема')
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT, verbose_name='Пациент')
    time = models.TimeField(verbose_name='Время приема')

    def __str__(self):
        return str(self.reception_plan) + str(self.patient) + str(self.time)

    class Meta:
        verbose_name = 'Запись вне плана'
        verbose_name_plural = 'Записи вне плана'
