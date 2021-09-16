import csv

with open('data2.csv', 'w', newline='') as fichiercsv:
    writer=csv.writer(fichiercsv)
    writer.writerow(['Temperature', 'Humidite', 'Temps'])
    writer.writerow(['20', '55', '1'])
    writer.writerow(['21', '60', '2'])
    writer.writerow(['23', '58', '3'])
    writer.writerow(['19', '62', '4'])