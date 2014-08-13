from django.db import models

# Create your models here.

# class Event(models.Model):
#     title = models.CharField(_('title'), max_length=200, help_text=_('Title'))
#     description = models.CharField(_('description'), max_length=300, help_text=_('Short description'))
#     text = models.TextField(_('text'), help_text=_('Full text'))
#     is_hero = models.BooleanField(_('hero'), default=False,
#         help_text=_('Designates whether this post should take attention'))
#     is_featured = models.BooleanField(_('featured'), default=False,
#         help_text=_('Designates whether this post should take attention'))
#     is_published = models.BooleanField(_('published'), default=True,
#         help_text=_('Designates whether post is published'))
#     publish_date = models.DateTimeField(_('date published'), default=timezone.now)
#     photo = models.ImageField(_('photo'), null=True, blank=True, upload_to='events')
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = _('event')
#         verbose_name_plural = _('events')
#
#     def image_tag(self):
#         return u'<img src="%s" style="max-height:200px;max-width:200px;"/>' % self.photo.url
#     image_tag.short_description = _('photo')
#     image_tag.allow_tags = True