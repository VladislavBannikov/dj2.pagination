from django.conf import settings
import csv

stations_file = settings.BUS_STATION_CSV


class Stations:
    data = []

    def read_file(self):
        self.data = []
        with open(stations_file, newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append({"Name": row['Name'], "Street": row['Street'], 'District': row['District']})
