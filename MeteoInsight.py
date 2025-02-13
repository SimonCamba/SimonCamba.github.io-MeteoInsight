import csv

datiMeteo = []
with open('climate_change_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        datiMeteo.append(row)
print(datiMeteo[0])

country=sorted(set(el[2] for el in datiMeteo[1:]))

def get_temperature_stats(country_name):
    T=[float(el[3]) for el in datiMeteo[1:] if el[2]==country_name]
    tempMin=min(T)
    tempMean=sum(T)/len(T)
    tempMax=max(T)
    return tempMin, tempMean, tempMax
print(f"La temperatura MINIMA, quella MEDIA e quella MASSIMA per l'Italia sono rispetivamente {get_temperature_stats('Italy')}")

with open("temperature.csv","w",newline="") as mycsv:
    temperature_data = []
    for stato in country:
        temps = get_temperature_stats(stato)
        temperature_data.append([stato, temps[0], temps[1], temps[2]])
    scrittore = csv.writer(mycsv, delimiter=",")
    intestazione= ['stato', 'temp_minima', 'temp_media', 'temp_massima']
    scrittore.writerow(intestazione)
    for row in temperature_data:
        scrittore.writerow(row)
