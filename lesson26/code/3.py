class HomeWork(models.Model):
    TYPES = (
        ("", "Выберите тип задачи"),
        ("t", "Задача"),
        ("r", "Рефакторинг"),
        ("t", "Тесты"),
    )

    type = models.CharField(max_length=1, choices=TYPES, blank=True)