def partition(symbol,length):
    print(symbol*length)

def compute_pay(h,r):
    if h > 40:
        return 40 * r + (h-40)*1.5*r

    else:
        return h * r

hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

print("Pay", compute_pay(hours, rate))

partition('*',80)


def hotel_cost(nights):
    return 140*nights

nights = int(input('Enter the no.of nights '))
print("Hotel cost", hotel_cost(nights))

partition('*',80)

def plane_ride_cost(city):

 if city == "charlotte":
     trip_cost = 183

 if city == "tampa":
     trip_cost = 220

 if city == "pittsburgh":
     trip_cost = 222

 if city == "los angeles":
     trip_cost = 475

 return trip_cost

city = str(input('Enter your city (Charlotte,Tampa,Pittsburgh,Los Angeles:) '))
city.lower()
print("Plane ride cost", plane_ride_cost(city))



partition('*',80)

def rent_car_cost(days):
    if days >= 7:
        rent = 40 * days - 50

    elif days >= 3 & days < 7:
        rent = 40 * days - 20

    else:
        rent= 40 * days

    return rent

days = int(input('Enter no.of days'))

print("Car rental cost",rent_car_cost(days))

partition('*',80)

def trip_cost(city,days):

    trip_cost= rent_car_cost(days)+plane_ride_cost(city)+hotel_cost(days)
    return trip_cost

city = str(input('Enter your city (Charlotte,Tampa,Pittsburgh,Los Angeles:) '))
city.lower()
days = int(input('Enter no.of days'))
print("Trip cost", trip_cost(city,days))

partition('*',80)

def trip_cost(city,days,spending_money):

    trip_cost= rent_car_cost(days)+plane_ride_cost(city)+hotel_cost(days)
    return trip_cost+spending_money

city = str(input('Enter your city (Charlotte,Tampa,Pittsburgh,Los Angeles:) '))
days = int(input('Enter no.of days'))
spending_money=int(input('Enter spending money'))
print("Trip cost", trip_cost(city,days,spending_money))