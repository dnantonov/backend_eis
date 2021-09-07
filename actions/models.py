from django.db import models


class Account(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.number}'


class Session(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    session_id =models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.session_id}'


class Action(models.Model):
    ACTIONS = (
        ('Read', 'Read'),
        ('Create', 'Create'),
        ('Update', 'Update'),
        ('Delete', 'Delete'),

    )

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='actions')
    action_type = models.CharField(max_length=100, choices=ACTIONS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.action_type}'
