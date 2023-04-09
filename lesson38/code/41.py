>>> from bboard.models import Rubric
>>> # Получаем набор записей, возвращенный методом get_queryset()
>>> Rubric.objects.all()
<QuerySet [ <Rubric : Транспорт> , <Rubric : Недвижимость > ,
<Rubric : Мебель > , <Rubric : Бытовая техника > , <Rubric : Сантехника > ,
<Rubric : Растения> , <Rubric : Сель хозинвентарь > ] >
>>> # Получаем набор записей , возвращенный вновь добавленным методом
>>> # order_by_bb_count()
>>> Rubric.objects.order_by_bb_count()
<QuerySet [ <Rubric : Недвижимость > , <Rubric : Транспорт> ,
<Rubric : Бытовая техника> , <Rubric : Сельхозинвентарь > ,
<Rubric : Мебель > , <Rubric : Сантехника> , <Rubric : Растения> ] >