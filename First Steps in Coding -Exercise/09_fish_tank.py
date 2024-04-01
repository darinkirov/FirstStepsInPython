duljina =  int(input())
shirochina = int(input())
visochina = int(input())
percent = float(input())

obem_akvarium = duljina * shirochina * visochina
obem_liters = obem_akvarium/1000
zaeto_prostranstvo = percent/100
liters_aquarium =  obem_liters*(1 - zaeto_prostranstvo)
print(liters_aquarium)