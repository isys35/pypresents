from threading import Timer
import logging
import time

def thread_work():
		logging.debug("Поехали!")

if __name__=="__main__":
		logging.basicConfig(
				level=logging.DEBUG,
				format='(%(threadName)-10s) %(message)s',
			)
		my_timerl = Timer(0.3, thread_work)
		my_timerl.setName("MyTreadTimer-1")
		my_timer2 = Timer(0.3, thread_work)
		my_timer2.setName("MyTreadTimer-2")
		logging.debug("Запуск таймеров!")
		# (MainThread) Запуск таймеров!
		my_timerl.start()
		my_timer2.start()
		logging.debug(f"Задержка перед отменой
									f'выполнения {my_timer2.getName()}")
		# (MainThread) Задержка перед отменой выполнения MyTreadTimer-2
		time.sleep(0.2)
		logging.debug(f"Отмена потока - "
									f" {my_timer2.getName()}")
		# (MainThread) Отмена потока - MyTreadTimer-2
		my_timer2.cancel()
		logging.debug("Завершение")
		# (MainThread) Завершение
		# (MyTreadTimer-1) Поехали!