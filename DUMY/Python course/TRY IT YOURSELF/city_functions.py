# City, country 11-1

# city_functions.py

def format_city_country(city, country):
    """Return a formatted string representing a city and its country."""
    return f"{city.title()}, {country.title()}"


# Population 11-2

# city_functions.py

def format_city_country(city, country, population=None):
    """Return a formatted string representing a city, its country, and optional population."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
