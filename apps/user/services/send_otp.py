# Django
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

SUBJECT = {
    "EN": "Your account verification code",
    "RU": "Код подтверждения вашей учетной записи",
    "UZ": "Elektron pochta tasdiqlovchi kod"
}


def get_message(otp_code, lang):
    MESSAGE = {
        "EN": "Hellooooo!!!\n\n"
              "Wowwee! Thanks for registering an account with Medicalka! You're the coolest person in all the land."
              "Before we get started, we'll need to verify your email.\n\n"
              "Your verify code is:\n\n\n"
              f"\t\t\t\t{otp_code}\n\n\n\n"
              f"Thank you for your trust\n"
              f"Welcome to Medicalka!\n",
        "RU": "Приветоооо!!!\n\n"
              "Спасибо за регистрацию учетной записи в Medicalka! Ты самый крутой человек на всей земле."
              "Прежде чем мы начнем, нам необходимо подтвердить вашу электронную почту.\n\n"
              "Ваш код подтверждения:\n\n\n"
              f"\t\t\t\t{otp_code}\n\n\n\n"
              f"Спасибо за ваше доверие\n"
              f"Добро пожаловать в Medicalka!\n",
        "UZ": "Salommm!!!\n\n"
              "Medicalka da akkauntni ro'yxatdan o'tkazganingiz uchun tashakkur! Siz butun mamlakatdagi eng zo'r odamsiz."
              "Ishni boshlashdan oldin elektron pochta manzilingizni tekshirishimiz kerak.\n\n"
              "Tasdiqlash kodingiz:\n\n\n"
              f"\t\t\t\t{otp_code}\n\n\n\n"
              f"Ishonchingiz uchun rahmat\n"
              f"Medicalkaga xush kelibsiz!\n",
    }

    return MESSAGE[lang]


def make_email_verify_msg(code, lang='EN'):
    message = get_message(code, lang)
    subject = SUBJECT.get(lang, SUBJECT['EN'])
    return {
        "subject": subject,
        "otp_code": code,
        "message": message
    }


def update_user_obj(user_obj, code) -> bool:
    try:
        user_obj.otp = code
        user_obj.save()
        return True
    except Exception as ex:
        return False


def send_otp_code_via_email(email, code, lang) -> bool:
    try:
        message = make_email_verify_msg(code=code, lang=lang)
        email_from = settings.EMAIL_FROM
        user_obj = User.objects.get(email=email)

        send_mail(
            f"{message['subject']}",
            f"{message['message']}",
            email_from,
            [user_obj.email],
            fail_silently=False
        )

        return update_user_obj(user_obj, code)
    except Exception as ex:
        return False
