import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info(number):
    # Parse number with phonenumbers
    parsed_number = phonenumbers.parse(number)

    # Get country/region
    country = geocoder.description_for_number(parsed_number, "en")

    # Get carrier
    sim_carrier = carrier.name_for_number(parsed_number, "en")

    return country, sim_carrier