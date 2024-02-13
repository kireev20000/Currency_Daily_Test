import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from currency_tools.models import Сurrency

from datetime import datetime


class Command(BaseCommand):
    """Кастомная management-команда для получения JSON данных курсов ЦБ."""

    def handle(self, *args, **options):
        try:
            request = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
            json_data = request.json()
            parse_date = datetime.strptime(json_data.get('Date'), '%Y-%m-%dT%H:%M:%S%z').date()
            valute = json_data.get('Valute')

            if not parse_date and valute:
                raise CommandError(
                    f'Ошибка: Данные с сайта ЦБ не были получены!'
                )

            for currency, currency_data in valute.items():
                Сurrency.objects.get_or_create(
                        date=parse_date,
                        char_code=currency,
                        name=currency_data.get('Name'),
                        value=currency_data.get('Value'),
                )
        except IntegrityError as e:
            raise CommandError(
                f'Ошибка: Запись в базу данных не выполнена!'
            )
