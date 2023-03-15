class HomeWork(models.Model):
    TYPES = (
        ("Написание нового кода", (
            ("t", "Задача"),
        )),
        ("Изменение старого кода", (
            ("r", "Рефакторинг"),
            ("t", "Тесты")),
         )
    )


type = models.CharField(max_length=1, choices=TYPES, default="t")