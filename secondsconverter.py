# Конвертирует секунды в разные единицы времени
from typing import List


class Converter:
	def __init__(self, intervals_name: List[str] = None) -> None:
		"""
		intervals_name: Должен содержать 7 элементов.
		Пример: ["сек", "мин", "часов", "дней", "недель", "месяцев", "лет"]
		"""
		if len(intervals_name) != 7:
			self.intervals_name = ["с", "м", "ч", "дн", "н", "М", "Л"]
			print('[SecondsConverter] intervals_name не получил список с 7 элементами. Был установлен стандартный.')
		else:
			self.intervals_name = intervals_name

	def seconds_to(self, seconds: int, display=2):
		"""
		seconds: Получает int секунд
		display: Получает int, сколько самых больших данных показать (макс 7)
		"""
		intervals = (
			(self.intervals_name[6], 31104000),  # 60 * 60 * 24 * 30 * 12
			(self.intervals_name[5], 2592000),  # 60 * 60 * 24 * 30
			(self.intervals_name[4], 604800),  # 60 * 60 * 24 * 7
			(self.intervals_name[3], 86400),  # 60 * 60 * 24
			(self.intervals_name[2], 3600),  # 60 * 60
			(self.intervals_name[1], 60),
			(self.intervals_name[0], 1),
		)

		result = []

		for name, count in intervals:
			value = seconds // count
			if value:
				seconds -= value * count
				if value == 1:
					name = name.rstrip('s')
				result.append("{}{}".format(value, name))
		return ' '.join(result[:display])


if __name__ == '__main__':
	# Example
	import time

	c = Converter(["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years", ])
	print(c.seconds_to(seconds=123456,
	                   display=3))
