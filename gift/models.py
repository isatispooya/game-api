from django.db import models
from authentication.models import User

class Gift(models.Model):
    GIFT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gift_option = models.CharField(
        max_length=10,
        choices=GIFT_CHOICES,
        default='COIN'
    )

    def __str__(self):
        return self.user.username
