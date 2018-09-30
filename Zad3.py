cena = float(input("Wprowadz model samochodu: "))

podatek = 157
oplataRejestracyjna = float(cena*0.19)
prowizja = 1400
dostawa = 300

print("cena samochodu po dodaniu wszystkich opłat", cena+podatek+oplataRejestracyjna+prowizja+dostawa)
