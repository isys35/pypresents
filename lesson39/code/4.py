class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Здесь можно вьmолнить какую-либо инициализацию.

    def __call__(self, request):
        # Здесь выполняется обработка клиентского запроса.

        response = self.get_response(request)

	      # Здесь выполняется обработка ответа

        return response