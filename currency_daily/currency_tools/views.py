from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Сurrency


@api_view(['GET'])
def get_rates(request):
    """Отправляет курс валют пользователю.
         пример запроса rate/?charcode=AUD&date=2024-02-14
    """
    char_code = request.query_params['charcode']
    query_date = datetime.strptime(request.query_params['date'], '%Y-%m-%d')

    try:
        currency_object = Сurrency.objects.get(char_code=char_code, date=query_date)
        result = {
            "charcode": currency_object.char_code,
            "date": currency_object.date,
            "rate": currency_object.value,
        }

        return Response(
            {'result': result},
            status=status.HTTP_200_OK,
        )

    except Сurrency.DoesNotExist:
        return Response(
            {'error': f'По данному запросу нет данных!'},
            status=status.HTTP_400_BAD_REQUEST,
        )
