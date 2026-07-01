#Laboratorio sobre if, elif e else Fcc4,5.py
distance_mi = 4
is_raining  = False
has_bike = True
has_car = False
has_ride_share_app = True
## Verifica se a distância é zero
if not distance_mi:
    print(False)
# Verifica se a distância é menor ou igual a 1 milha 
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
# Verifica se a distância é maior que 1 milha e menor ou igual a 6 milhas 
elif distance_mi > 1 and distance_mi <= 6:
    if  has_bike and not is_raining:
        print(True)
    else:
        print(False)
# Verifica se a distância é maior que 6 milhas
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)