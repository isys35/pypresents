if "counter" in request.COOKIES:
		cnt = int(request.COOKIES['counter']) + 1
else:
		cnt = 1