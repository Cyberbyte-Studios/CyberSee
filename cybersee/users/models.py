# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from stdimage.models import StdImageField
from stdimage.utils import UploadToAutoSlugClassNameDir
from stdimage.validators import MinSizeValidator
from django.utils import timezone


class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    logo = StdImageField(
        upload_to=UploadToAutoSlugClassNameDir(populate_from='pk'),
        variations={
            'small': {
                "width": 250,
                "height": 250,
                "crop": True}},
        validators=[
            MinSizeValidator(250, 250)], null=True, blank=True)
    joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    community = models.ForeignKey(Community, blank=True, null=True) #TODO: remove blank and null

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
