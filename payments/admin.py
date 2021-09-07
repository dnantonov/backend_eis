from django.contrib import admin

from payments.models import Accrual, Payment

admin.site.register(Payment)
admin.site.register(Accrual)
