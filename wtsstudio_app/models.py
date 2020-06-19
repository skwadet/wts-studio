from django.db import models
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField
from django.utils import timezone


class ValidationOnlyNInstance:

    @staticmethod
    def validate(obj, n):
        model = obj.__class__
        if model.objects.count() > n:
            raise ValidationError("Можно создать только {n} объект модели {name}".format(n=n + 1, name=model.__name__))


class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
    link = models.URLField()
    is_main = models.BooleanField(default=False)

    def clean(self):
        n = 0
        ValidationOnlyNInstance.validate(self, n)

    def __str__(self):
        return 'Логотип номер {id}'.format(id=self.id)


class Header(models.Model):
    text = models.CharField(max_length=120)
    link = models.CharField(max_length=250)

    def clean(self):
        n = 3
        ValidationOnlyNInstance.validate(self, n)

    def __str__(self):
        return 'Элемент хэдера {name}'.format(name=self.text)


class Description(models.Model):
    header = models.CharField(max_length=120)
    text = models.TextField(max_length=500)

    def clean(self):
        n = 0
        ValidationOnlyNInstance.validate(self, n)

    def __str__(self):
        return 'Описание номер {id}'.format(id=self.id)


class Pro(models.Model):
    header = models.CharField(max_length=120)
    image = models.ImageField(upload_to='pros/')
    text = models.TextField(max_length=250)

    def __str__(self):
        return 'Преимущество {name}'.format(name=self.header)


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return 'Работа в портфолио номер {id}'.format(id=self.id)


class Service(models.Model):
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


CALLEDSTATUS = [
    ('c', 'called'),
    ('n', 'notcalled'),

]


class UserRequest(models.Model):
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    mail = models.EmailField(default=None, null=True, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    type = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='request')
    callstatus = models.CharField(default='n', max_length=1, choices=CALLEDSTATUS)

    def __str__(self):
        return 'Запрос на {type} номер {id}'.format(type=self.type, id=self.id)


class Review(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to='reviews/')
    site_domain = models.CharField(max_length=120)

    def __str__(self):
        return 'Отзыв от клиента {name}'.format(name=self.name)


class SiteStyle(models.Model):
    style = models.CharField(max_length=250)

    def __str__(self):
        return self.style


class TargetVersion(models.Model):
    version = models.CharField(max_length=250)

    def __str__(self):
        return self.version


class Brief(models.Model):
    type = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='brief')
    desc = models.TextField(max_length=750)
    site = models.CharField(max_length=250, blank=True)
    aim = models.CharField(max_length=250)
    tasks = models.CharField(max_length=500, blank=True)
    sites_pros = models.CharField(max_length=1000)
    sites_cons = models.CharField(max_length=1000)
    site_style = models.ForeignKey(SiteStyle, on_delete=models.CASCADE, related_name='brief_style', blank=True)
    site_style_custom = models.CharField(max_length=500, blank=True)
    logo = models.ImageField(blank=True, upload_to='custom_logos')
    version_custom = models.CharField(max_length=500, blank=True)
    version = models.ManyToManyField(TargetVersion, related_name='brief_version', blank=True)
    deadline = models.DateField(blank=True, default=timezone.now)
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    mail = models.EmailField(default=None, null=True, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    comment = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return 'Бриф {type} от заказчика {name}'.format(type=self.type, name=self.first_name)
