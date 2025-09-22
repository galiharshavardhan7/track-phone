from opencage.geocoder import OpenCageGeocode
import folium
from myphone import get_phone_info

# Replace with your own API key
API_KEY = "04491f1ec54d4bd1b953f96bba886d9b"


def main():
    phone_number = input("Enter phone number with country code (e.g. +919876543210): ")

    # Get country & carrier
    country, sim_carrier = get_phone_info(phone_number)
    print(f"Country: {country}")
    print(f"Carrier: {sim_carrier}")

    # Get coordinates of the country
    geocoder = OpenCageGeocode(API_KEY)
    results = geocoder.geocode(country)

    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f"Coordinates: {lat}, {lng}")

        # Plot map
        mymap = folium.Map(location=[lat, lng], zoom_start=4)
        folium.Marker([lat, lng], popup=country).add_to(mymap)
        mymap.save("mylocation.html")
        print("Map saved as mylocation.html")
    else:
        print("Could not fetch location")


if __name__ == "__main__":
    main()