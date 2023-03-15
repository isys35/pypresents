class Types(models.TextChoices):
    TASK = "t", "Задача"
    REFACTOR = "r", "Рефакторинг"
    TESTS = "t", "Тесты"
    OTHER = "o"
    __empty__ = "Выберите тип задачи"