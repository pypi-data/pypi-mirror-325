# aerocast/weather.py
from .api import API, __package__
from .tts_manager import TextToSpeechManager
from .converter import name_converter, distance_converter, Distance, ConverterDict
import os
import gettext, locale

# THIS CODE IS FOR IMPORTANT THE RIGHT LOCALES PATH WHEREVER THE CODER IS CALLED FROM #

try:
    __path__
except NameError:
    import importlib
    pkg = importlib.import_module(__package__)
    __path__ = pkg.__path__[0]
finally:
    pass#print(f"path: {__path__}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DEFAULT_CONVERTERS = {"name": name_converter, "visib": distance_converter}

api = API()

class WeatherManager:
    def __init__(self, airport_code, lang=None):
        self.airport_code = airport_code
        self.lang = lang

        language = locale.getlocale()[0]
        language, country = language.split('_', 2)
        chosen_language = lang or language
        locales_path = os.path.join(__path__, 'locales')

        default_lang = gettext.translation('messages', locales_path, languages=[chosen_language], fallback=True)
        default_lang.install()

        _ = default_lang.gettext

        self.tts_manager = TextToSpeechManager(lang)

    def play_text(self, text):
        self.tts_manager.play_text(text)

    @staticmethod
    def filter_by_iata(airports, airport_code: str):
        for airport in airports:
            if airport['iata'] == airport_code.upper():
                return airport
        raise ValueError(_("No airport matching %s") % airport_code)
    
    def get_weather_data(self):
        airports = api.get_metar_data(self.airport_code)
        weather_data = airports[0] if len(airports) == 1 else airports
        if not weather_data:
            raise ValueError(_("No weather data available"))
        return weather_data

    def get_airport_data(self):
        airports = api.get_airport_data(self.airport_code)
        return airports[0] if len(airports) == 1 else WeatherManager.filter_by_iata(airports, self.airport_code)

    def extract_metar_info(data: dict, converters=DEFAULT_CONVERTERS):
        # Extraire les informations directement accessibles
        for fieldname, converter in converters.items():
            data[fieldname] = converter(data[fieldname])

        return ConverterDict(data)
         
    def get_temperature(self):
        weather_data = self.get_weather_data()
        result = f"{weather_data.get('temp', 'N/A')}"
        return result

    def get_wind_speed(self):
        weather_data = self.get_weather_data()
        result = f"{weather_data.get('wind_speed', 'N/A')}"
        return result

    @staticmethod
    def traduire_abreviation(abreviation, conditions_meteo="", probabilite="", heure=""):
        abreviations = {
            "SKC": "d'un ciel dégagé",
            "CLR": "d'un ciel clair",
            "FEW": "de quelques nuages de 1 à 2 octas",
            "SCT": "de nuages épars de 3 à 4 octas",
            "BKN": _("some fragmented clouds from 5 to 7 oktas"),
            "OVC": "d'un Ciel couvert (8 octas)",
            "VV": "d'un ciel invisible en dessous de la base des nuages",
            "CB": "de cumulonimbus",
            "TCU": "de cumulus congestus",
            "CAVOK": "d'un ciel et visibilité clairs",
            "NSW": "sans précipitations importantes, pas de temps significatif",
            "FG": "de brouillard",
            "BR": "de brume",
            "HZ": "de brume sèche",
            "FU": "de fumée",
            "DU": "de poussière",
            "SA": "de sable",
            "VA": "de cendres volcaniques",
            "SQ": "de ligne de grains",
            "FC": "de tornade en formation",
            "TS": "d'orages",
            "SH": "d'averses",
            "DZ": "de bruine",
            "RA": "de pluie",
            "SN": "de neige",
            "SG": "de grésil",
            "IC": "de grésil en suspension",
            "PL": "de pluie verglaçante",
            "GR": "de grêle",
            "UP": "inconnues",
            "NSC": "sans nuages",

            "TEMPO": f"Ensuite, dès {heure} attendez-vous à des conditions temporaires {conditions_meteo} pendant une courte période.",
            "BECMG": f"Ensuite, dès {heure} prévoyez un changement et attendez-vous à des conditions temporaires {conditions_meteo} dans un avenir proche.",
            "PROB": f"Ensuite, dès {heure} il y a une probabilité de {probabilite}% {conditions_meteo} dans la période spécifiée.",
            "FM": f"Ensuite, à partir de {heure} attendez-vous à des conditions temporaires {conditions_meteo}.",
            "TL": f"Ensuite, jusqu'à {heure} attendez-vous à des conditions temporaires {conditions_meteo}.",
            "AT": f"Ensuite, à {heure} attendez-vous à des conditions temporaires {conditions_meteo}."
        }

        return abreviations.get(abreviation, "inconnue")


    def get_summarize(self):
        # Récupérer les données météorologiques
        weather_data = self.get_weather_data()

        # Préparer les parties du message avec les données récupérées ou des valeurs par défaut
        wind_direction = weather_data.get('wdir', 'N/A')
        wind_speed = weather_data.get('wspd', 'N/A')
        clouds = weather_data.get('clouds', 'N/A')
        visibility = weather_data.get('visib', 'N/A')
        temperature = weather_data.get('temp', 'N/A')
        dew_point = weather_data.get('dewp', 'N/A')
        pressure = weather_data.get('altim', 'N/A')

        # Construction du résumé clouds

        clouds_text = []

        for cloud in clouds:
            d = Distance()
            if cloud['base']:
                d.foot = cloud['base']
                clouds_text.append(f"{WeatherManager.traduire_abreviation(cloud['cover'])} à {round(d.kilometer, 2)} km d'attitude")
            else:
                clouds_text.append(f"{WeatherManager.traduire_abreviation(cloud['cover'])} sans altitude")


        # Construction du résumé météorologique
        meteo_text = [
            _("The METAR indicates a wind of %s degrees, with a speed of %s knots.") % (wind_direction, wind_speed),
            _("Cloud cover : ") + ', '.join(clouds_text),
            f"La distance de visibilité est de {visibility} kilomètres.",
            f"La température est de {temperature} degrés Celsius, et le point de rosée est de {dew_point} degrés Celsius.",
            f"La pression atmosphérique QNH est située à {pressure} hPa."
        ]

        return '\n'.join(meteo_text)