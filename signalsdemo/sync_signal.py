import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(3)
    print("Signal handler finished")

# Test
from django.contrib.auth.models import User
start = time.time()
User.objects.create(username="moin_test")
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")
