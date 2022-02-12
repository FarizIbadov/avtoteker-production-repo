from django.db import models

class PriceColor(models.Model):
    COLORS = [
        ('r', 'Red'),
        ('y', 'Yellow'),
        ('g', 'Gray'),
    ]

    MONTHS = [
        (2, "2 month"),
        (3, "3 month"),
        (6, "6 month"),
        (9, "9 month"),
        (12,"12 month"),
    ]

    color = models.CharField(
        max_length=255, 
        choices=COLORS, 
        null=True, 
        unique=True
    )

    taksit = models.PositiveSmallIntegerField(
        choices=MONTHS, 
        null=True, 
        blank=True
    )

    kredit = models.PositiveSmallIntegerField(
        choices=MONTHS[1:-1], 
        null=True,
        blank=True
    )

    def __str__(self):
        return "%s" % dict(self.COLORS)[self.color]



