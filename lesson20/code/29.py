async def waiter(name):
		for _ in range(4):
			time_to_sleep = random.randint(1, 3) / 4
			await asyncio.sleep(time_to_sleep)
			print("{} waited {} seconds".format(name, time_to_sleep))