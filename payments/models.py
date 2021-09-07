from django.db import models


MONTHS = (
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
        ('Jul', 'Jul'),
        ('Aug', 'Aug'),
        ('Sep', 'Sep'),
        ('Oct', 'Oct'),
        ('Nov', 'Nov'),
        ('Dec', 'Dec')
    )


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    month = models.CharField(max_length=5, choices=MONTHS)

    def __str__(self):
        return f'Payment #{self.id}. Date: {self.date}. Month: {self.month}'


class Accrual(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    month = models.CharField(max_length=3, choices=MONTHS)
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='accruals')

    def __str__(self):
        return f'Accrual #{self.id}. Date: {self.date}. Month: {self.month}.'
