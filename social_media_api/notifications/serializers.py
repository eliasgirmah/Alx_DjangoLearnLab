from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_post_id = serializers.IntegerField(source='target_post.id', read_only=True)
    target_comment_id = serializers.IntegerField(source='target_comment.id', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 
                  'target_post_id', 'target_comment_id', 'read', 'timestamp']
        read_only_fields = ['recipient', 'actor', 'actor_username', 'target_post_id', 'target_comment_id', 'timestamp']
