class SomeQuerySet(models.QuerySet):
    # Этот метод будет перенесён
    def method(self):
        ...

    # Этот метод не будет перенесён
    def _method2(self):
        ...

    # Этот метод будет перенесён
    def _method3(self):
        ...

    _method3.queryset_only = False

    # Этот метод не будет перенесен
    def method4(self):
        ...

    _method4.queryset_only = True
