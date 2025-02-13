import enum


class CreationType(enum.IntEnum):
    FILE_UPLOADING = 1
    MANUAL_CREATION = 2

class ConsumptionType(enum.IntEnum):
    STATIC = 1
    DYNAMIC = 2


class OrderStatus(enum.IntEnum):
    NEW = 1
    PENDING = 2
    FILLED = 3
    CANCELED = 4


class RestMethod(enum.Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"


class Blockchain(enum.Enum):
    TRON = "tron"
    BTC = "btc"
