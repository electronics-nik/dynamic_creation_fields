from django.db import models
from django.contrib.auth.models import AbstractUser

from .utilities import get_timestamp_path


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Activated')
    send_messages = models.BooleanField(default=True, verbose_name='Send message about new comments')

    class Meta(AbstractUser.Meta):
        pass


class Question(models.Model):
    question = models.CharField(max_length=1024, verbose_name='Question')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Image')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Author')
    single_answer = models.BooleanField(default=True, verbose_name='Is single answer?')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Question is active?')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Questions'
        verbose_name = 'Question'
        ordering = ['-created']


class Answer(models.Model):
    answer = models.CharField(max_length=1024, verbose_name='Answer')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Image')
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='Question')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Author')
    correct = models.BooleanField(default=False, verbose_name='Correct ansver')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Answer is active?')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name_plural = 'Answers'
        verbose_name = 'Answer'
        ordering = [
            'question',
            '-correct',
            '-created'
        ]
