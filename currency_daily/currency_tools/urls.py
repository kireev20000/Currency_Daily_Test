from django.urls import path

from currency_tools.views import get_rates

app_name = 'Currecy Tools'

urlpatterns = [
    path('rate/', get_rates)
]