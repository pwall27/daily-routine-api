import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    class Meta:
        app_label = 'app'
        db_table = 'tasks'
        ordering = ('created_at',)
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    uuid = models.UUIDField(
        verbose_name=_('Public ID'),
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=150)

    description = models.CharField(
        verbose_name=_('Description'),
        max_length=300)

    is_active = models.BooleanField(
        verbose_name=_('Is Active?'),
        default=True)

    owner = models.ForeignKey(
        to='User',
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created Date'),
        auto_now_add=True,
        null=False,
        blank=False,
        help_text=_('Creation datetime.'))

    updated_at = models.DateTimeField(
        verbose_name=_('Updated Date'),
        auto_now=True,
        null=True,
        blank=False,
        help_text=_('Update datetime.'))

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task<{}>'.format(self.title)
