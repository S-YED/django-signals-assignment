import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Test
from django.contrib.auth.models import User
print(f"Caller thread ID: {threading.get_ident()}")
User.objects.create(username="thread_test")
