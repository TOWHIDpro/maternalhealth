from django.contrib.auth.models import User

def lastusers_id():
    user = User.objects.all().last()
    return user.id