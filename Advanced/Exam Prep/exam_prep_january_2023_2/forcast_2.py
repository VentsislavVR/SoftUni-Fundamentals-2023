def forecast(*data):
    result = []

    def add_locations(type_of_location):
        locations = list(filter(lambda x:x[1]==type_of_location,data))
        [result.append(f"{l[0]} - {type_of_location}")for l in sorted(locations)]

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")

    return '\n'.join(result)

print(forecast(

("Sofia", "Sunny"),

("London", "Cloudy"),

("New York", "Sunny")))