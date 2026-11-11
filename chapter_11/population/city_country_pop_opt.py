def city_country_pop(city, country, pop=5_000):
    output_string = f'{city.title()}, {country.title()}'
    if pop:
        output_string += f" - population {pop}"
    return output_string
