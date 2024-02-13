from django.db import models


class Сurrency(models.Model):
    """Модель с данными о валюте."""
    date = models.DateField(verbose_name='Дата')
    char_code = models.CharField(max_length=3, verbose_name='Код')
    name = models.CharField(max_length=200, verbose_name='Название')
    value = models.DecimalField(max_digits=10,
                                decimal_places=5,
                                verbose_name='Курс'
                                )

    def __str__(self):
        return f"{self.date} - {self.char_code} {self.name}: {self.value}"

    class Meta:
        ordering = ["-date"]
        indexes = [
            models.Index(fields=['char_code', ]),
            models.Index(fields=['date', ])
        ]
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
