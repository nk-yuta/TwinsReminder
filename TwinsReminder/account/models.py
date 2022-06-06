from django.conf import settings
from django.core.mail import EmailMessage
from django.db import models
from django.template.loader import render_to_string

class EmailPush(models.Model):
    """メールでのプッシュ先を表す"""
    email = models.EmailField('メールアドレス', unique=True)
    is_active = models.BooleanField('有効フラグ', default=False)

    def __str__(self):
        return self.email
    
    def email_push(self, request):
        """記事をメールで通知"""
        context = {
            'post': self,
        }
        #subject = render_to_string('account/notify_subject.txt', context, request)
        #message = render_to_string('account/notify_message.txt', context, request)
        subject="題名"
        message="本文"
        from_email = settings.DEFAULT_FROM_EMAIL
        bcc = [settings.DEFAULT_FROM_EMAIL]
        for mail_push in EmailPush.objects.filter(is_active=True):
            bcc.append(mail_push.email)
        email = EmailMessage(subject, message, from_email, [], bcc)
        email.send()