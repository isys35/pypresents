def simple_middleware(get_response):
    # Здесь можно вьmолнить какую-либо инициализацию

    def middleware(request):
        # Здесь выполняется обработка клиентского запроса

        response = get_response(request)

        # Здесь выполняется обработка ответа

        return response

    return middleware