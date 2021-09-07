from django.contrib import admin

from actions.models import Account, Session, Action

admin.site.register(Account)
admin.site.register(Session)
admin.site.register(Action)
