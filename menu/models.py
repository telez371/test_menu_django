from django.db import models

from django.urls import reverse
from django.utils.functional import cached_property


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    @cached_property
    def active(self):
        return self.url == self.request.path or self.url == reverse(self.url_name) if hasattr(self,
                                                                                              'url_name') else False


