from django.db import models


class SessionKey(models.Model):
    key = models.TextField()
    
    def __str__(self):
        return self.key

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

    use_sale = models.BooleanField(default=False)
    use_price_3_on_feeless = models.BooleanField(default=False) 

    def __str__(self):
        return "%s" % dict(self.COLORS)[self.color]



class ManatIcon(models.Model):
    image = models.ImageField(upload_to="manat")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image.name