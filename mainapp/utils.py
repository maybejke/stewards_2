from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

from mainapp.models import SendContacts


def contact_us(contact_id):
    """
    send mail from form
    :param request:
    :return:
    """
    info = SendContacts.objects.get(id=contact_id)
    subject = f'Заявка с сайта Стюарды.рф от претендента {info.name}, номер {info.phone}!'
    message = f'Добрый день, \n' \
              f'Претендент - {info.name} оставил заявку на сайте:\n' \
              f'- Телефон: {info.phone} \n' \
              f'- Email: {info.email} \n' \
              f'- Сообщение: {info.description}.'
    if subject and message:
        try:
            mail_send = send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return mail_send
