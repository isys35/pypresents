from multiprocessing import Process, current_process, cpu_count, Pool

def square(data):
		return data * data


def start_process():
		print(f'Старт процесса - '
					f'{current_process().name}')


if __name__ == '__main__':
		inputs = list(range(10))
		print(f'Начальный список: {inputs}')
		builtin_map = map(square, inputs)
		print(f'Встроенная функция map: '
					f' {list(builtin_map)}')
		pool_size = cpu_count() * 2
		print(f'Количество ядер у процессора: '
					f' {cpu_count()}')
		print(f'Количество запускаемых процессов: '
					f' {pool_size}')
		pool = Pool(
					processes=pool_size,
					initializer=start_process,
			)
		pool_map = pool.map(square, inputs)
		pool.close()
		pool.join()
		print(f'Результат работы пула процессов:
					f'{pool_map}')