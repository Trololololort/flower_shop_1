from enum import Enum


class HttpStatusCodes(Enum):

    OK = 200

    OK_NO_CONTENT = 204

    LOGIN_OCCUPIED = 409

    OUT_OF_STOCK = 400 # https://docs.commercetools.com/api/errors#outofstock
    WRONG_PRODUCT_ID = 400
