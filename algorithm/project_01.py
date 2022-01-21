my_station=['야탑','모란','이매','선릉','한티','왕십리']

def station_list(list):
    for station in list:
        print(station)

print('station_list 함수 결과')
station_list(my_station)


def station_point(list):
    for station in list:
        if station=='선릉':
            print(station)


print('\nstation_point 함수 결과')
station_point(my_station)