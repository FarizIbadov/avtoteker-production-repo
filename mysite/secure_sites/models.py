from django.db import models
from django.contrib.sites.models import Site


class SecureSite(models.Model):
    site = models.OneToOneField(
        Site,
        on_delete=models.RESTRICT,
        related_name="secure_site"
    )
    is_https = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_address()

    def get_protocol(self):
        return "https" if self.is_https else "http"

    def get_address(self):
        protocol = self.get_protocol()
        return protocol + "://" + self.site.domain