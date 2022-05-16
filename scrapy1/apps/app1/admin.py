from atexit import register
from django.contrib import admin
from apps.app1.models import Currency,Covid,History
import requests


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "country_name",
        # "total_cases",
        # "total_deaths",
        # "recovered",
        # "postcode",
        # "created_at",
    )

@admin.register(Covid)
class CovidAdmin(admin.ModelAdmin):
    list_display = (
        "country_name",
        # "currency",
    )

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display =(
        # "currency",
        "covid",
    )
    