from django.db import transaction

@transaction.non_atomic_requests
def my_view(request):
		# В этом контроллере действует режим обработки транзакций по умолчанию