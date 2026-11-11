from city_country_population import city_country_population


def test_city_county_population():
    formatted_name = city_country_population('osaka',
                                             'japan',
                                             5_000)
    assert formatted_name
