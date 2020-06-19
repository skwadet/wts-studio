from rest_framework import viewsets
from django.db.models.signals import post_save
from django.dispatch import receiver
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from .admin import AdminMethod


class HeaderAPISet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class LogoAPISet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class DescriptionAPISet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class ProsAPISet(viewsets.ModelViewSet):
    queryset = Pro.objects.all()
    serializer_class = ProsSerializer


class ServiceAPISet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class UserRequestAPISet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
    http_method_names = ['post']


class ReviewAPISet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BriefAPISet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
    http_method_names = ['post']

    @staticmethod
    @receiver(post_save, sender=Brief)
    def send_brief(instance, *args, **kwargs):
        c = instance
        AdminMethod.send_email(subject='Оставлен бриф',
                               from_='Admin',
                               from_email='wtsstudio@protonmail.com',
                               to='skwadet@gmail.com',
                               message='<p><b>Пользователь</b> {first_name} {last_name} отправил бриф:</p>'
                                       '<p><b>Тип:</b> {type}; <br>'
                                       '<b>Описание:</b> {desc}; <br>'
                                       '<b>Имеющиеся сайты:</b> {site}; <br>'
                                       '<b>Цель сайта:</b> {aim}; <br>'
                                       '<b>Задачи сайта:</b> {tasks}; <br>'
                                       '<b>Понравившиеся сайты:</b> {sites_pros}; <br>'
                                       '<b>Не понравившиеся сайты:</b> {sites_cons}; <br>'
                                       '<b>Стиль сайта:</b> {site_style}; <br>'
                                       '<b>Стиль сайта (кастомный):</b> {site_style_custom}; <br>'
                                       '<b>Приоритетная версия:</b> {version}; <br>'
                                       '<b>Приоритетная версия (кастомная):</b> {version_custom}; <br>'
                                       '<b>Дедлайн:</b> {deadline}; <br>'
                                       '<b>Эл. почта:</b> {mail}; <br>'
                                       '<b>Тел.: {phone}</p>'.format(first_name=c.first_name,
                                                                     last_name=c.last_name,
                                                                     type=c.type,
                                                                     desc=c.desc, site=c.site, aim=c.aim,
                                                                     tasks=c.tasks,
                                                                     sites_pros=c.sites_pros,
                                                                     sites_cons=c.sites_cons,
                                                                     site_style=c.site_style,
                                                                     site_style_custom=c.site_style_custom,
                                                                     version=c.version,
                                                                     version_custom=c.version_custom,
                                                                     deadline=c.deadline, mail=c.mail,
                                                                     phone=c.phone))
