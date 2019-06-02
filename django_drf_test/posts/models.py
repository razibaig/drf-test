import sys
from users.models import NewUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

sys.path.append("..")


class Post(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(_('text'), max_length=100, blank=True)
    tag = models.CharField(_('tag'), max_length=30, blank=True)
