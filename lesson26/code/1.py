class HomeWork(models.Model):
    TYPES = (
        ("t", "Задача"),
        ("r", "Рефакторинг"),
        ("t", "Тесты"),
    )

    type = models.CharField(max_length=1, choices=TYPES, default="t")