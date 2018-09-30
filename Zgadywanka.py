import random
liczba = random.randint(1,10)
odp = input("Jaka liczba od 1 do 49 zostala wylosowana")

if liczba == int(odp):
	print("Poprawna odpowiedz.")
else:
	print("Niepoprawna odpowiedz.")
