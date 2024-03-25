from enum import Enum

# constants
class Constants:
    CANDIDATE_ID = "9a2052ea-5d27-41a1-a91d-cfa51eb7251a"
    BASE_URL = "https://challenge.crossmint.io/api/"
    MAP_URL = "https://challenge.crossmint.io/api/map/" + CANDIDATE_ID + '/goal'

class ASTRAL_OBJECTS(Enum):
    POLYANET = "POLYANET",
    LEFT_COMETH = "LEFT_COMETH",
    RIGHT_COMETH = "RIGHT_COMETH",
    UP_COMETH = "UP_COMETH",
    DOWN_COMETH = "DOWN_COMETH",
    PURPLE_SOLOON = "PURPLE_SOLOON",
    RED_SOLOON = "RED_SOLOON",
    WHITE_SOLOON = "WHITE_SOLOON",
    BLUE_SOLOON = "BLUE_SOLOON"

class Astral(Enum):
    SOLOON = "SOLOON"
    COMETH = "COMETH"
    POLYANET = "POLYANET"

class Api_Astral_Type(Enum):
    SOLOON = "soloons"
    COMETH = "comeths"
    POLYANET = "polyanets"
