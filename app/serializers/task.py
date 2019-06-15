from django.contrib import auth
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Task

User = auth.get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField('uuid', queryset=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = (
            'uuid',
            'title',
            'description',
            'is_active',
            'owner',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('uuid', 'created_at')

    def validate(self, attrs):
        if 'request' in self.context:
            attrs.update({
                'owner': self.context['request'].user
            })
        elif not attrs.get('owner'):
            raise ValidationError({"message": _("Field owner not informed.")})
        return super(TaskSerializer, self).validate(attrs)
