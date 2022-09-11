from typing import Union

def multiplication(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
	return a * b


if __name__ == '__main__':
	while True:
		print(multiplication(float(input('a:')), float(input('b:'))))
