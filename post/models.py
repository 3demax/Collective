from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(_('name'),  max_length=200, help_text=_('Name of category'))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(_('title'), max_length=200, help_text=_('Title'))
    text = models.TextField(_('text'), help_text=_('Full text'))
    is_published = models.BooleanField(_('published'), default=True,
        help_text=_('Designates whether post is published'))
    publish_date = models.DateTimeField(_('date published'), default=timezone.now)
    author = models.ForeignKey(User, related_name='author')
    category = models.ForeignKey(Category, related_name='category')

    def get_absolute_url(self):
        return '/'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')