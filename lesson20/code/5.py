import multiprocessing

def worker():
		"""Рабочая функция"""
		print('Worker')


if __name__ == '__main__':
		jobs = []
		for i in range(5):
				p = multiprocessing.Process(target=worker)
				jobs.append(p)
				p.start ()