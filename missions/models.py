from django.db import models
from authentication.models import User

class Missions(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    puzzle_done = models.BooleanField(default=False , null=True , blank=True)
    puzzle_score = models.IntegerField(default=0 )
    puzzle_end_date = models.DateTimeField(null=True)
    sejam_done = models.BooleanField(default=False , null=True , blank=True)
    sejam_score = models.IntegerField(default=0)
    sejam_end_date = models.DateTimeField(null=True)
    broker_done = models.BooleanField(default=False , null=True , blank=True)
    broker_score = models.IntegerField(default=0)
    broker_end_date = models.DateTimeField(null=True)
    test_question_done = models.BooleanField(default=False , null=True , blank=True)
    test_question_score = models.IntegerField(default=0)
    test_question_end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username

