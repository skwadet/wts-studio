from django.contrib import admin
from wtsstudio_app import models
from sendsay.api import SendsayAPI


admin.site.register(models.Logo)
admin.site.register(models.Header)
admin.site.register(models.Description)
admin.site.register(models.Pro)
admin.site.register(models.Portfolio)
admin.site.register(models.Service)
admin.site.register(models.Review)
admin.site.register(models.SiteStyle)
admin.site.register(models.TargetVersion)


class AdminMethod:
    @staticmethod
    def send_email(subject, from_, from_email, to, message):
        api = SendsayAPI(login='skwadet@gmail.com', sublogin='', password='')
        response = api.request('issue.send', {
            'sendwhen': 'now',
            'letter': {
                'subject': "{subject}".format(subject=subject),
                'from.name': "{from_}".format(from_=from_),
                'from.email': "{from_email}".format(from_email=from_email),
                'message': {
                    'html': "{message}".format(message=message)
                },
            },
            'relink': 1,
            'users.list': "{to}".format(to=to),
            'group': 'masssending',
        })
        print(response)


@admin.register(models.UserRequest)
class UserRequestCustom(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'mail', 'type', 'callstatus']
    actions = ['send_email']

    def send_email(self, request, queryset, *args):
        for c in queryset.all():
            if c.callstatus == 'n':
                AdminMethod.send_email('Здравствуйте, мы готовы сделать Ваш сайт!',
                                       'WTS? Studio', 'wtsstudio@protonmail.com', c.mail,
                                       'Здравствуйте, {name}! \n'
                                       'Мы обработали Вашу заявку '
                                       'и с радостью выполним Ваши пожелания. \n'
                                       'Пожалуйста, заполните бриф тут:'.format(name=c.first_name))
                self.message_user(request, 'Уведомление успешно отправлено!')
                queryset.update(callstatus='c')
            else:
                self.message_user(request, 'Этому клиенту уже отправлено уведомление!')


@admin.register(models.Brief)
class BriefCustom(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'mail', 'type', 'deadline']
