class HomeWork(models.Model):
    class Types(models.IntegerChoices):
        TASK = 1, "Задача"
        REFACTOR = 2, "Рефакторинг"
        TESTS = 3, "Тесты"
        OTHER = 4

    type = models.SmallintegerField(choices=Types.choices, default=Types.TASK)