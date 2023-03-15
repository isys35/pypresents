class HomeWork(models.Model):
    class Types(models.TextChoices):
        TASK = "t", "Задача"
        REFACTOR = "r", "Рефакторинг"
        TESTS = "t", "Тесты"
        OTHER = "o"

    type = models.CharField(max_length=1, choices=Types.choices, default=Types.TASK)