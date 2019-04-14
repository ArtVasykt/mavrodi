from django.db import models


class Client(models.Model):
    chat_id = models.CharField(max_length=25, verbose_name="Чат", default="0")
    name = models.CharField(max_length=255, default="", verbose_name="Имя")
    referer = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Реферер", null=True, blank=True)
    balance = models.IntegerField(verbose_name="Баланс", default=0)
    paid = models.BooleanField(verbose_name="Активировано", default=False)
    refered = models.ManyToManyField('self', verbose_name="Первая линия", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент (Пользователь)"
        verbose_name_plural = "Клиенты (Пользователи)"
