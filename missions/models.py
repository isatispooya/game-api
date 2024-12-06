from django.db import models
from authentication.models import User

class Missions(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    puzzle_done = models.BooleanField(default=False , null=True , blank=True)
    puzzle_score = models.IntegerField(default=0 )
    puzzle_end_date = models.DateTimeField(null=True , blank=True   )
    sejam_done = models.BooleanField(default=False , null=True , blank=True)
    sejam_score = models.IntegerField(default=0)
    sejam_end_date = models.DateTimeField(null=True , blank=True)
    broker_done = models.BooleanField(default=False , null=True , blank=True)
    broker_score = models.IntegerField(default=0)
    broker_end_date = models.DateTimeField(null=True , blank=True)
    test_question_1_done = models.BooleanField(default=False , null=True , blank=True)
    test_question_1_score = models.IntegerField(default=0)
    test_question_1_end_date = models.DateTimeField(null=True , blank=True)
    test_question_2_done = models.BooleanField(default=False , null=True , blank=True)
    test_question_2_score = models.IntegerField(default=0)
    test_question_2_end_date = models.DateTimeField(null=True , blank=True)
    test_question_3_done = models.BooleanField(default=False , null=True , blank=True)
    test_question_3_score = models.IntegerField(default=0)
    test_question_3_end_date = models.DateTimeField(null=True , blank=True)
    test_question_4_done = models.BooleanField(default=False , null=True , blank=True)
    test_question_4_score = models.IntegerField(default=0)
    test_question_4_end_date = models.DateTimeField(null=True , blank=True)
    coffee_done = models.BooleanField(default=False , null=True , blank=True)
    coffee_score = models.IntegerField(default=0)
    coffee_end_date = models.DateTimeField(null=True , blank=True)
    photo = models.FileField(upload_to='photos/' , null=True , blank=True)
    upload_photo_done = models.BooleanField(default=False , null=True , blank=True)
    upload_photo_score = models.IntegerField(default=0)
    upload_photo_end_date = models.DateTimeField(null=True , blank=True)

    def __str__(self):
        return self.user.username

