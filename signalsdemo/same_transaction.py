from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    User.objects.create(username="created_in_signal")

# Test
from django.contrib.auth.models import User
from django.db import transaction

try:
    with transaction.atomic():
        User.objects.create(username="main_user")
        raise Exception("Forcing rollback")
except:
    pass

print(User.objects.all().values_list("username", flat=True))
