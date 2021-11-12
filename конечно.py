import sqlite3
import csv

result = []


def prediction(*titles):
    con = sqlite3.connect('ocean_weather.db')
    cur = con.cursor()
    result = cur.execute("""SELECT Places.latitude, Places.longitude, Winds.wind FROM Places
    INNER JOIN winds
    ON places.wind_id = winds.wind
    WHERE location in ?""", (titles,)).fetchall()
    print(result)
    con.close()


with open('path_weather.csv', 'w', newline='') as csvfile:
    write = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in result:
        write.writerow(i[2])


v = ["Saint-Petersburg", "Lisbon", "Malaga", "Le Havre"]
prediction(*v)