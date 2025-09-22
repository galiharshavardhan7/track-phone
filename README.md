#“**Track Phone Number Location in Python | Harsha’s GitHub Project**”
 phone number -> region -> map (educational)
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/57d3b90b-71a3-41ad-8f80-a8d1d85ebe23" />

**Queries this project answers**

How to track a phone number location with Python
Phone number location tracker using Python (GitHub)
Python code to get coordinates from a phone number’s country code
Phone number validation in Python
Get approximate location (country/region) using Python libraries
How to use OpenCage API + phonenumbers in Python
** About this project**
This project was created for educational purposes only.

**👉 What it does:**

Takes a phone number as input
Extracts the country information based on the country calling code (e.g., +91 → India, +880 → Bangladesh) using the phonenumbers library
Uses the OpenCage Geocoding API to fetch the coordinates of that country/region
Displays the location on a map using Folium

**👉 What it does not do:**
It does not track the exact live location of a person’s phone.
That is not possible with public libraries or APIs.

**⚠️ Important note from OpenCage**

OpenCage cannot convert a phone number directly into a precise GPS location.
What actually happens is:
phonenumbers extracts the country/region from the number
OpenCage converts that country name into approximate coordinates (center of the country/region)
Example:

Input: +91... → Output: India

OpenCage returns coordinates: 22.3511148, 78.6677428 (center of India, not where the phone really is).

So, this project is for fun, practice, and learning Python libraries — not real tracking.

Source: https://blog.opencagedata.com/post/we-can-not-convert-a-phone-number-into-a-location-sorry

**Properties Used**


Phonenumbers Python Library: https://pypi.org/project/phonenumbers/

OpenCage Geocoding Module for Python: https://pypi.org/project/opencage/

OpenCage Geocoding API: https://opencagedata.com/

Folium: https://pypi.org/project/folium/

PyCharm (Code Editor): https://www.jetbrains.com/pycharm/
