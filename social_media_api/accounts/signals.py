from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.conf import settings
from notifications.models import Notification

User = settings.AUTH_USER_MODEL

@receiver(m2m_changed, sender=User.following.through)
def user_followed(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":  # When someone follows a user
        for followed_id in pk_set:
            if followed_id != instance.id:
                Notification.objects.create(
                    recipient_id=followed_id,
                    actor=instance,
                    verb="started following you"
                )
