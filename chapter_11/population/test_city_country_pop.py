from city_country_pop_opt import city_country_pop


def test_city_country_pop():
    output_string = city_country_pop(
            'paris',
            'france',
            69_000_000,
    )
    assert output_string