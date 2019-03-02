from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils.encoding import smart_text


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    people_involved = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="EventOwner"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.title)


class Transaction(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="User1"
    )
    user2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="User2"
    )
    amount = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return smart_text("{user1} owes {user2} {amount}".format(user1=self.user1, user2=self.user2, amount=self.amount))
