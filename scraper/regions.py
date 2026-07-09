"""Europe location filter.

Location strings come in 16+ ATS-specific shapes ("London, UK", "Novara,
Piedmont, ITA", "Remote - EMEA", "Warsaw", ...). Per string the check is:

1. explicit NON-European country -> not European (this must run first, so
   "London, Ontario, Canada", "Cambridge, MA, USA" and "New South Wales,
   AUS" don't match on a European city/region name)
2. explicit European country / ISO3 code / Europe-EMEA keyword -> European
3. well-known European city -> European
4. otherwise -> not European (unknown/empty locations are excluded)

A job counts as European when ANY of its locations passes.
"""
import re


def _rx(words):
    return re.compile(r"\b(" + "|".join(words) + r")\b", re.IGNORECASE)


EU_COUNTRIES = _rx([
    "United Kingdom", "UK", "England", "Scotland", "Wales", "Northern Ireland",
    "Ireland", "Germany", "Deutschland", "France", "Netherlands", "Spain",
    "Italy", "Poland", "Sweden", "Denmark", "Norway", "Finland", "Switzerland",
    "Austria", "Belgium", "Czechia", "Czech Republic", "Portugal", "Greece",
    "Hungary", "Romania", "Bulgaria", "Croatia", "Slovakia", "Slovenia",
    "Estonia", "Latvia", "Lithuania", "Luxembourg", "Iceland", "Serbia",
    "Ukraine", "Turkey", "Türkiye", "Cyprus", "Malta", "Europe", "EMEA",
    # ISO3 codes (Amazon-style "City, Region, ITA")
    "GBR", "IRL", "DEU", "FRA", "NLD", "ESP", "ITA", "POL", "SWE", "DNK",
    "NOR", "FIN", "CHE", "AUT", "BEL", "CZE", "PRT", "GRC", "HUN", "ROU",
    "BGR", "HRV", "SVK", "SVN", "EST", "LVA", "LTU", "LUX", "ISL", "SRB",
    "UKR", "TUR", "CYP", "MLT",
])

NON_EU_COUNTRIES = _rx([
    "United States", "USA", "U\\.S\\.", "Canada", "Mexico", "Brazil",
    "Argentina", "Chile", "Colombia", "Peru", "Costa Rica", "India", "China",
    "Japan", "Singapore", "Australia", "New Zealand", "South Korea", "Korea",
    "Israel", "United Arab Emirates", "Dubai", "Saudi Arabia", "Qatar",
    "Hong Kong", "Taiwan", "Malaysia", "Indonesia", "Thailand", "Vietnam",
    "Philippines", "South Africa", "Egypt", "Nigeria", "Kenya", "Morocco",
    "CAN", "MEX", "BRA", "ARG", "CHL", "COL", "PER", "CRI", "IND", "CHN",
    "JPN", "SGP", "AUS", "NZL", "KOR", "ISR", "ARE", "SAU", "QAT", "HKG",
    "TWN", "MYS", "IDN", "THA", "VNM", "PHL", "ZAF", "EGY",
])

EU_CITIES = _rx([
    "London", "Dublin", "Cork", "Edinburgh", "Glasgow", "Manchester", "Leeds",
    "Bristol", "Reading", "Cambridge", "Oxford", "Belfast",
    "Berlin", "Munich", "München", "Hamburg", "Frankfurt", "Cologne",
    "Köln", "Stuttgart", "Dresden", "Aachen", "Karlsruhe", "Nürnberg",
    "Nuremberg", "Düsseldorf",
    "Paris", "Grenoble", "Toulouse", "Lyon", "Nice", "Sophia Antipolis",
    "Amsterdam", "Eindhoven", "Rotterdam", "Utrecht", "The Hague",
    "Zurich", "Zürich", "Geneva", "Basel", "Lausanne", "Zug",
    "Stockholm", "Gothenburg", "Lund", "Copenhagen", "Aarhus", "Oslo",
    "Helsinki", "Espoo", "Tampere",
    "Madrid", "Barcelona", "Malaga", "Málaga", "Valencia",
    "Milan", "Milano", "Rome", "Roma", "Turin", "Torino", "Novara", "Pisa",
    "Warsaw", "Krakow", "Kraków", "Wroclaw", "Wrocław", "Gdansk",
    "Gdańsk", "Poznan", "Poznań",
    "Prague", "Brno", "Vienna", "Wien", "Budapest", "Bucharest", "Cluj",
    "Timisoara", "Timișoara", "Iasi", "Iași",
    "Lisbon", "Lisboa", "Porto", "Brussels", "Ghent", "Antwerp",
    "Athens", "Thessaloniki", "Sofia", "Zagreb", "Ljubljana", "Bratislava",
    "Belgrade", "Tallinn", "Riga", "Vilnius", "Reykjavik", "Kyiv",
    "Istanbul", "Ankara", "Nicosia",
])


def _is_european_location(text):
    if NON_EU_COUNTRIES.search(text):
        return False
    if EU_COUNTRIES.search(text):
        return True
    return bool(EU_CITIES.search(text))


def is_european_job(locations):
    return any(_is_european_location(loc) for loc in locations if loc)
