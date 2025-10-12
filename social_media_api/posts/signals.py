from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post
from notifications.models import Notification

@receiver(m2m_changed, sender=Post.likes.through)
def post_liked(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":  # When a user likes a post
        for user_id in pk_set:
            if user_id != instance.author.id:  # Don't notify if author likes own post
                Notification.objects.create(
                    recipient=instance.author,
                    actor_id=user_id,
                    verb="liked your post",
                    target_post=instance
                )
