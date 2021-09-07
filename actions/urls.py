from django.urls import path

from actions.views import ActionView

urlpatterns = [
    path('', ActionView.as_view())
]
