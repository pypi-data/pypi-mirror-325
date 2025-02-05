from typing import *
import asyncio
import logging
import os
import traceback
import sys
import json
import datetime
import re
import copy
import pytz
from copy import deepcopy

from .config import dateTimeFormatInitial, dateFormatInitial, timeFormatInitial
from .JON_default import JONDefaultSchema, ValidatorElement, cleanField
from .utils import getLang


log = logging.getLogger(__name__)

def ConvertStringToInitialType(self, strValue: str):
    if isObject(strValue) == True :
        return json.load(strValue)
    elif isDate(value = strValue, dateFormat = dateTimeFormatInitial) == True:
        return getDate(value = strValue, dateFormat = dateTimeFormatInitial)
    elif isNumber(value = strValue) :
        if strValue.isdigit():
            return int(strValue)
        else:
            return float(strValue)
    elif isBoolean(value = strValue) :
        return float(strValue)
    return strValue
def isObject(
    value: str,
):
    res = False
    try:
        if type(value) == dict :
            res = True
        else:
            json.load(value)
            res = True
    except Exception as err:
        res = False
    return res
def isDatetimeFormat(
    value: str,
    format: str,
):
    res = False
    try:
        datetime.datetime.strptime(value, format)
        res = True
    except Exception as err:
        res = False
    return res
def getDate(
    value: any,
    dateFormat: str = dateTimeFormatInitial,
    timezone = None,
    typeValue = None,
):
    res = None
    typesPossible = ('datetime', 'date', 'time')
    typeValue = typeValue if typeValue in typesPossible else None
    timezone = timezone if timezone is not None else None
    dateFormat = dateFormat if (
        type(dateFormat) == str and
        len(dateFormat) > 0
    ) else None

    if(
        type(value) == str and
        len(value) > 0 and
        dateFormat is not None and
        isDatetimeFormat(value, format = dateFormat)
    ):
        res = datetime.datetime.strptime(value, dateFormat)
        if(timezone is not None):
            res = res.astimezone(timezone)
        if(typeValue == 'date'):
            res = res.date()
        if(typeValue == 'time'):
            res = res.time()
    if(
        type(value) is datetime.datetime or
        type(value) is datetime.date or
        type(value) is datetime.time
    ):
        res = value
        if(
            type(value) is datetime.datetime and
            timezone is not None
        ):
            res = res.astimezone(timezone)

    return res
def isDate(
    value: any,
    typeValue: str = None,
    dateFormat: str = dateTimeFormatInitial,
) -> bool:
    dateFormat = dateFormat if (
        type(dateFormat) == str and
        len(dateFormat) > 0
    ) else None
    types: tuple = ('datetime', 'date', 'time', 'null', 'string')
    typeValue = typeValue if typeValue in types else None
    
    res = (
        (
            isDatetimeFormat(value, format = dateFormat) or
            value is None
        ) if (
            typeValue == "string" and
            type(value) == str and
            len(value) > 0 and
            dateFormat is not None
        ) else (
            (
                type(value) is datetime.datetime and (
                    typeValue in (None, 'datetime')
                )
            ) or
            (
                type(value) is datetime.time and (
                    typeValue in (None, 'time')
                )
            ) or
            (
                type(value) is datetime.date and (
                    typeValue in (None, 'date')
                )
            ) or (
                type(value) == str and
                len(value) > 0 and
                isDatetimeFormat(value, format = dateFormat) and (
                    typeValue in (None, 'string')
                )
            ) or
            (
                type(value) is None and (
                    typeValue in (None, 'null')
                )
            )
        )
    )
    return res
def isString(
    value: any,
    typeValue: str = None,
) -> bool:
    types: tuple = ('datetime', 'date', 'time', 'null', 'other')
    typeValue = typeValue if typeValue in types else None
    res = (
        (
            value is None or (
                type(value) in (str, int, float, bool, list, tuple, dict) and (
                    typeValue is None or
                    typeValue == 'other'
                )
            )
        ) or 
        (
            value is None or (
                type(value) is datetime.datetime and (
                    typeValue is None or
                    typeValue == 'datetime'
                )
            )
        ) or
        (
            value is None or (
                type(value) is datetime.time and (
                    typeValue is None or
                    typeValue == 'time'
                )
            )
        ) or
        (
            value is None or (
                type(value) is datetime.date and (
                    typeValue is None or
                    typeValue == 'date'
                )
            )
        ) or
        (
            value is None or (
                type(value) is None and (
                    typeValue is None or
                    typeValue == 'null'
                )
            )
        )
    )
    return res
def isNumber(value: any) -> bool:
    res = True
    try:
        if(value is not None):
            float(value)
    except:
        res = False
    res = (
        (res == True and type(value) in [int, float]) or
        value is None
    )
    return res
def isBoolean(
    value: any,
    valuesPossibles: list,
    strict: bool = False
) -> bool:
    res = (
        type(value) == bool or
        (
            (
                value in valuesPossibles or
                (
                    type(value) == str and
                    value.lower() in valuesPossibles
                )
            )
        ) or
        (value is None and strict == False)
    )
    return res
def convertToBoolean(
    value: any,
) -> bool:
    # value = deepcopy(value)
    defaultVal = deepcopy(value)
    valuesPossibles: list = ('true', 't', '1', 'false', 'f', '0')
    res = defaultVal
    if type(value) == bool :
        res = value
    elif value is not None and str(value).lower() in valuesPossibles:
        res = True if str(value).lower() in ('true', 't', '1') else False
    return res
def checkIfCorrectTypeSchema(value: any):
    return (
        type(value) is String or
        isinstance(type(value), String) or
        issubclass(type(value), String) or
        type(value) is Number or
        isinstance(type(value), Number) or
        issubclass(type(value), Number) or
        type(value) is Boolean or
        isinstance(type(value), Boolean) or
        issubclass(type(value), Boolean) or
        type(value) is Date or
        isinstance(type(value), Date) or
        issubclass(type(value), Date) or
        type(value) is Enum or
        isinstance(type(value), Enum) or
        issubclass(type(value), Enum) or
        type(value) is ChosenType or
        isinstance(type(value), ChosenType) or
        issubclass(type(value), ChosenType) or
        type(value) is NoInChosenType or
        isinstance(type(value), NoInChosenType) or
        issubclass(type(value), NoInChosenType) or
        type(value) is Object or
        isinstance(type(value), Object) or
        issubclass(type(value), Object) or
        type(value) is Array or
        isinstance(type(value), Array) or
        issubclass(type(value), Array) or
        type(value) is AnyType or
        isinstance(type(value), AnyType) or
        issubclass(type(value), AnyType)
    )
def convertInCorrectSchemaType(value: any):
    return value if(checkIfCorrectTypeSchema(value)) else None
def isCorrectType(
    value: any,
):
    return (
        type(value) in (list, tuple, dict, int, str, float, bool) or
        type(value) is datetime.datetime or
        type(value) is datetime.date or
        type(value) is datetime.time
    )



class String(JONDefaultSchema):
    _maxValue: str = None
    _minValue: str = None
    _lessValue: str = None
    _greaterValue: str = None
    _lengthValue: str = None
    _format: str = None
    _dateFormat: str = '%Y/%m/%d'
    _timeFormat: str = '%H:%M:%S:%f'
    
    _rule__min = None
    _rule__max = None
    _rule__less = None
    _rule__greater = None
    _rule__length = None
    _rule__regexp = None
    _rule__alphanum = None
    _rule__base64 = None
    _rule__lowercase = None
    _rule__uppercase = None
    _rule__capitalize = None
    _rule__ucFirst = None
    _rule__creditCard = None
    _rule__dataUri = None
    _rule__domain = None
    _rule__url = None
    _rule__hostname = None
    _rule__IPAddress = None
    _rule__email = None
    _rule__guid = None
    _rule__hexa = None
    _rule__binary = None
    _rule__date = None
    _rule__identifier = None

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - string --')

    def JONStringValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        
        # --> OTHERS RULES
        # --<- min
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__min, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- max
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__max, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- less
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__less, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- greater
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__greater, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- length
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__length, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- regexp
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__regexp, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- alphanum
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__alphanum, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- base64
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__base64, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- lowercase
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__lowercase, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- uppercase
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__uppercase, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- capitalize
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__capitalize, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- ucFirst
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__ucFirst, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- creditCard
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__creditCard, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- dataUri
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__dataUri, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- domain
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__domain, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- url
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__url, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- hostname
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__hostname, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- IPAddress
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__IPAddress, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- email
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__email, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- guid
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__guid, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- hexa
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__hexa, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- binary
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__binary, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- date
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__date, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- identifier
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__identifier, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())

        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONStringValidator(value)

    def init(self,):
        self._options['validationType'] = 'string'
        self._options['type'] = str
        self._options['instance'] = String
        self.set_label_type({
            'fr': 'Chaîne de caractère',
            'en': 'String'
        }[self._lang])

        self.initRule()

    def initRule(self,):
        def sanitizeFunct(value: any) -> str:
            if(value is not None):
                if(self._format is None):
                    if (
                        isString(value, typeValue = "datetime")
                    ):
                        self.changeFormat(dateTimeFormatInitial)
                    elif (
                        isString(value, typeValue = "date")
                    ):
                        self.changeFormat(self._dateFormat)
                    elif (
                        isString(value, typeValue = "time")
                    ):
                        self.changeFormat(self._timeFormat)

                if (
                    isString(value, typeValue = "other")
                ):
                    return str(value)
                elif (
                    isString(value, typeValue = "datetime") or
                    isString(value, typeValue = "date") or
                    isString(value, typeValue = "time")
                ):
                    return value.strftime(self._format)
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | String - initRule - value:: ", value)

            valid = True if (
                value is None or
                type(value) in (str, int, float, bool)
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': String,
        }
    
    def changeFormat(self,
        newFormat: str
    ):
        if (
            type(newFormat) == str and
            len(newFormat) > 0
        ):
            self._format = newFormat

        return self

    def min(self, minValue: int):
        def initFunct(value: any):
            self._minValue = minValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None
            
            # print("> JON.schemas | String - min - ruleFunct - value:: ", value)
            # print("> JON.schemas | String - min - ruleFunct - isString(value, typeValue = 'null'):: ", isString(value, typeValue = 'null'))

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and
                        len(str(value)) >= minValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._maxValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "the size of {label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être au minimum {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "the size of {label} must be at least {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__min = {
            'name': 'min',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def max(self, maxValue: int):
        def initFunct(value: any):
            self._maxValue = maxValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and
                        len(str(value)) <= maxValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._minValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                        'en': "the size of {label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être au maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                        'en': "the size of {label} must be maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__max = {
            'name': 'max',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def less(self, lessValue: int):
        def initFunct(value: any):
            self._lessValue = lessValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and
                        len(str(value)) < lessValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._greaterValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être inferieure à {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__less = {
            'name': 'less',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def greater(self, greaterValue: int):
        def initFunct(value: any):
            self._greaterValue = greaterValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and
                        len(str(value)) > greaterValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._lessValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être supérieur à {greater}".format(
                            label = labelSTR,
                            greater = greaterValue,
                        ),
                        'en': "the size of {label} must be greater than {greater}".format(
                            label = labelSTR,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__greater = {
            'name': 'greater',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def length(self, lengthValue: int):
        def initFunct(value: any):
            self._lengthValue = lengthValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and
                        len(str(value)) == lengthValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if not(valid == True):
                pass
                # print("> JON_sup - String | isString(value):: ", isString(value))
                # print("> JON_sup - String | len(str(value)):: ", len(str(value)))
                # print("> JON_sup - String | type(value):: ", type(value))
                # print("> JON_sup - String | lengthValue:: ", lengthValue)
                # print("> JON_sup - String | (len(str(value)) == lengthValue):: ", (len(str(value)) == lengthValue))


            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "la taille de {label} doit être égale à {length}".format(
                        label = labelSTR,
                        length = lengthValue,
                    ),
                    'en': "the size of {label} must be equal to {length}".format(
                        label = labelSTR,
                        length = self._lengthValue,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__length = {
            'name': 'length',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def regexp(self, ruleValue: str, flag: re.RegexFlag = None):
        # re.compile(r'\s', re.IGNORECASE | re.DOTALL)
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} ne respecte pas la rêgle appliquée".format(
                        label = labelSTR,
                    ),
                    'en': "{label} does not respect the ruleFunct applied".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__regexp = {
            'name': 'regexp',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def alphanum(self):
        ruleValue: str = r"^([\w\s])+$"
        flag: re.RegexFlag = re.MULTILINE
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        # print("> alphanum - flag:: ", flag)
        # print("> alphanum - ruleValue:: ", ruleValue)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> alphanum - bool(re.match(", ruleValue, ", ", str(value), ")):: ", bool(re.match(ruleValue, str(value))))
            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères alphanumeriques".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a string of alphanumeric characters".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__alphanum = {
            'name': 'alphanum',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def base64(self, paddingRequired: bool = True, urlSafe: bool = True):
        paddingRequired = paddingRequired if type(paddingRequired) == bool else True
        urlSafe = urlSafe if type(urlSafe) == bool else True
        
        nbr1 = '=' if paddingRequired else '(={0,1})'
        nbr2 = '(\-{1})' if urlSafe else '(+{1})'
        nbr3 = '(_{1})' if urlSafe else '(\\{1})'

        ruleValue: str = r"^(?:[A-Za-z0-9" + nbr2 + "/]{4})*(?:[A-Za-z0-9" + nbr2 + "/]{2}==|[A-Za-z0-9" + nbr2 + "/]{3}" + nbr1 + "|[A-Za-z0-9" + nbr2 + "/]{4})$"
        flag: re.RegexFlag = (re.MULTILINE)
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères de type base64".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a base64 string".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__base64 = {
            'name': 'base64',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def lowercase(self, strictMode: bool = False):
        def sanitizeFunct(value: any) -> str:
            return str(value).lower() if value is not None else None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            strictMode == False or (
                                strictMode and
                                bool(re.match(r"[A-Z]{1,}", str(value))) == False
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas en minuscule".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not lowercase".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'sanitize': sanitizeFunct,
                'valid': valid,
                'error': error,
            }

        self._rule__lowercase = {
            'name': 'lowercase',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def uppercase(self, strictMode: bool = False):
        strictMode = strictMode if type(strictMode) == bool else False
        def sanitizeFunct(value: any) -> str:
            return str(value).upper()
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            strictMode == False or (
                                strictMode and
                                bool(re.match(r"[A-Z]{1,}", str(value)))
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas en majuscule".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not uppercase".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'sanitize': sanitizeFunct,
                'valid': valid,
                'error': error,
            }

        self._rule__uppercase = {
            'name': 'uppercase',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def capitalize(self, strictMode: bool = False):
        strictMode = strictMode if type(strictMode) == bool else False
        def sanitizeFunct(value: any) -> str:
            return str(value).title() if value is not None else None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            strictMode == False or (
                                strictMode and
                                bool(re.match(r".{1,}", str(value)))
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas en lettre capitale".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not capitalized".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'sanitize': sanitizeFunct,
                'valid': valid,
                'error': error,
            }

        self._rule__capitalize = {
            'name': 'capitalize',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def ucFirst(self, strictMode: bool = False):
        strictMode = strictMode if type(strictMode) == bool else False
        def sanitizeFunct(value: any) -> str:
            return str(value).capitalize() if value is not None else None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            strictMode == False or (
                                strictMode and
                                bool(re.match(r".{1,}", str(value)))
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'a pas de première lettre en majuscule".format(
                        label = labelSTR,
                    ),
                    'en': "{label} does not have a capitalized first letter".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'sanitize': sanitizeFunct,
                'valid': valid,
                'error': error,
            }

        self._rule__ucFirst = {
            'name': 'ucFirst',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def creditCard(self, types: list = []):
        typesPossibles = ('mastercard', 'visa', 'american-express', 'discover', 'diners-club', 'jcb')
        types = types if type(types) in (tuple, list) else []
        types = tuple(
            filter(
                lambda x: x in typesPossibles,
                types,
            )
        )
        versionRegEx = {
            'visa': re.compile(r"^(4[0-9]{12}(?:[0-9]{3}))$", re.MULTILINE),
            'mastercard': re.compile(r"^((?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12})$", re.MULTILINE),
            'american-express': re.compile(r"^(3[47][0-9]{13})$", re.MULTILINE),
            'discover': re.compile(r"^(6(?:011|5[0-9]{2})[0-9]{12})$", re.MULTILINE),
            'diners-club': re.compile(r"^(3(?:0[0-5]|[68][0-9])[0-9]{11})$", re.MULTILINE),
            'jcb': re.compile(r"^((?:2131|1800|35\d{3})\d{11})$", re.MULTILINE),
        }
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            (
                                len(types) <= 0 and (
                                    bool(re.match(versionRegEx['visa'], str(value))) or
                                    bool(re.match(versionRegEx['mastercard'], str(value))) or
                                    bool(re.match(versionRegEx['american-express'], str(value))) or
                                    bool(re.match(versionRegEx['discover'], str(value))) or
                                    bool(re.match(versionRegEx['diners-club'], str(value))) or
                                    bool(re.match(versionRegEx['jcb'], str(value)))
                                )
                            ) or (
                                len(types) > 0 and (
                                    (
                                        'visa' in types and
                                        bool(re.match(versionRegEx['visa'], str(value)))
                                    ) or (
                                        'mastercard' in types and
                                        bool(re.match(versionRegEx['mastercard'], str(value)))
                                    ) or (
                                        'american-express' in types and
                                        bool(re.match(versionRegEx['american-express'], str(value)))
                                    ) or (
                                        'discover' in types and
                                        bool(re.match(versionRegEx['discover'], str(value)))
                                    ) or (
                                        'diners-club' in types and
                                        bool(re.match(versionRegEx['diners-club'], str(value)))
                                    ) or (
                                        'jcb' in types and
                                        bool(re.match(versionRegEx['jcb'], str(value)))
                                    )
                                )
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères au format d'une carte de crédit".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is a character string in the format of a credit card".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__creditCard = {
            'name': 'creditCard',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def dataUri(self):
        ruleValue: str = r"^data:([\w\/\+]+);(charset=[\w-]+|base64).*,([a-zA-Z0-9+/]+={0,2})$"
        flag: re.RegexFlag = re.MULTILINE
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne d'URI de données valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a valid data URI string".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__dataUri = {
            'name': 'dataUri',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def domain(self):
        ruleValue: str = "^(?!-)[A-Za-z0-9-]+([\\-\\.]{1}[a-z0-9]+)*\\.[A-Za-z]{2,6}$"
        flag: re.RegexFlag = re.MULTILINE
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'un domaine valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a string is in the format of a valid domain".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__domain = {
            'name': 'domain',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def url(self):
        ruleValue: str = ''.join([
            '^(https?:\\/\\/)?',
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|',
            '((\\d{1,3}\\.){3}\\d{1,3}))',
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*',
            '(\\?[;&a-z\\d%_.~+=-]*)?',
            '(\\#[-a-z\\d_]*)?$',
        ])
        flag: re.RegexFlag = re.MULTILINE
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'une url valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string is in the format of a valid url".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__url = {
            'name': 'url',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def hostname(self):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and (
                                bool(re.match(re.compile(r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$", re.MULTILINE), str(value))) or
                                bool(re.match(re.compile(r"^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$", re.MULTILINE), str(value)))
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'un nom d'hôte valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a string is in the format of a valid hostname".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__hostname = {
            'name': 'hostname',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def IPAddress(self, types: list = []):
        typesPossibles = ('ipv4', 'ipv6')
        types = types if type(types) in (tuple, list) else []
        types = tuple(
            filter(
                lambda x: x in typesPossibles,
                types,
            )
        )
        versionRegEx = {
            'ipv4': re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", re.MULTILINE),
            'ipv6': re.compile('|'.join([
                "(^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$)",
                "(^::(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}$)",
                "(^[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}$)",
                "(^[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,4}[0-9a-fA-F]{1,4}$)",
                "(^(?:[0-9a-fA-F]{1,4}:){0,2}[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,3}[0-9a-fA-F]{1,4}$)",
                "(^(?:[0-9a-fA-F]{1,4}:){0,3}[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:){0,2}[0-9a-fA-F]{1,4}$)",
                "(^(?:[0-9a-fA-F]{1,4}:){0,4}[0-9a-fA-F]{1,4}::(?:[0-9a-fA-F]{1,4}:)?[0-9a-fA-F]{1,4}$)",
                "(^(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}::[0-9a-fA-F]{1,4}$)",
                "(^(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}::$)",
            ]), re.MULTILINE),
        }
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            (
                                len(types) <= 0 and (
                                    bool(re.match(versionRegEx['ipv4'], str(value))) or
                                    bool(re.match(versionRegEx['ipv6'], str(value)))
                                )
                            ) or (
                                len(types) > 0 and (
                                    (
                                        'ipv4' in versionRegEx.keys() and
                                        bool(re.match(versionRegEx['ipv4'], str(value)))
                                    ) or (
                                        'ipv6' in versionRegEx.keys() and
                                        bool(re.match(versionRegEx['ipv6'], str(value)))
                                    )
                                )
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'une addresse IP valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string is in the format of a valid IP address".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__IPAddress = {
            'name': 'IPAddress',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def email(self):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            bool(
                                re.match(
                                    re.compile(r"^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$", re.MULTILINE),
                                    str(value)
                                )
                            ) or
                            bool(
                                re.match(
                                    re.compile(r"""^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$""", re.MULTILINE),
                                    str(value)
                                )
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'un email valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string is in the format of a valid email".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__email = {
            'name': 'email',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def guid(self, types: list = []):
        typesPossibles = ('v1', 'v2', 'v3', 'v4', 'v5')
        types = types if type(types) in (tuple, list) else []
        types = tuple(
            filter(
                lambda x: x in typesPossibles,
                types,
            )
        )
        versionRegEx = {
            'v1': re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1][0-9a-fA-F]{3}-[89AB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", re.MULTILINE),
            'v2': re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[2][0-9a-fA-F]{3}-[89AB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", re.MULTILINE),
            'v3': re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[3][0-9a-fA-F]{3}-[89AB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", re.MULTILINE),
            'v4': re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[89AB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", re.MULTILINE),
            'v5': re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[5][0-9a-fA-F]{3}-[89AB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", re.MULTILINE),
        }
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            (
                                len(types) <= 0 and (
                                    bool(re.match(versionRegEx['v1'], str(value))) or
                                    bool(re.match(versionRegEx['v2'], str(value))) or
                                    bool(re.match(versionRegEx['v3'], str(value))) or
                                    bool(re.match(versionRegEx['v4'], str(value))) or
                                    bool(re.match(versionRegEx['v5'], str(value)))
                                )
                            ) or (
                                len(types) > 0 and (
                                    (
                                        'v1' in types and
                                        bool(re.match(versionRegEx['v1'], str(value)))
                                    ) or (
                                        'v2' in types and
                                        bool(re.match(versionRegEx['v2'], str(value)))
                                    ) or (
                                        'v3' in types and
                                        bool(re.match(versionRegEx['v3'], str(value)))
                                    ) or (
                                        'v4' in types and
                                        bool(re.match(versionRegEx['v4'], str(value)))
                                    ) or (
                                        'v5' in types and
                                        bool(re.match(versionRegEx['v5'], str(value)))
                                    )
                                )
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format GUID valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string is in valid GUID format".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__guid = {
            'name': 'guid',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def hexa(self, insensitive: bool = False):
        insensitive = insensitive if type(insensitive) == bool else False
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            (
                                insensitive and
                                bool(re.match(re.compile(r"^[0-9a-fA-F]+$", re.MULTILINE), str(value)))
                            ) or 
                            (
                                not(insensitive) and
                                bool(re.match(re.compile(r"^[0-9A-F]+$", re.MULTILINE), str(value)))
                            )
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'un hexa valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string is in the format of a valid hexa".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__hexa = {
            'name': 'hexa',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def binary(self):
        ruleValue: str = r"^[0-1]{1,}$"
        flag: re.RegexFlag = None
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format binaire valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a string is in valid binary format".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__binary = {
            'name': 'binary',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def date(self, format = None):
        format = format if (
            type(format) == str and
            len(format) > 0
        ) else (
            dateTimeFormatInitial
        )
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            isDatetimeFormat(str(value), format = format)
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères est au format d'une date valide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string is in the format of a valid date".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__date = {
            'name': 'date',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def identifier(self):
        ruleValue: str = r"^[a-zA-Z]{1,}\w{0,}$"
        flag: re.RegexFlag = None
        flag = flag if (
            type(flag) is re.RegexFlag and
            flag is not None
        ) else None
        ruleValue = ruleValue if (
            type(ruleValue) == str and
            len(ruleValue) > 0
        ) else ''
        if flag is not None:
            ruleValue = re.compile(ruleValue, flag)
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isString(value, typeValue = 'null') or (
                        isString(value) and (
                            len(str(value)) > 0 and
                            bool(re.match(ruleValue, str(value)))
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} n'est pas une chaîne de caractères sous le format d'un identifiant".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is not a character string in the format of an identifier".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__identifier = {
            'name': 'identifier',
            'rule': ruleFunct,
            'schema': String,
        }

        return self
class Number(JONDefaultSchema):
    _maxValue: str = None
    _minValue: str = None
    _lessValue: str = None
    _greaterValue: str = None

    _rule__min = None
    _rule__max = None
    _rule__less = None
    _rule__greater = None
    _rule__negative = None
    _rule__positive = None
    _rule__signed = None
    _rule__integer = None
    _rule__decimal = None
    _rule__multiple = None
    _rule__TCPPort = None

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - number --')

    def init(self,):
        self._options['validationType'] = 'number'
        self._options['type'] = float
        self._options['instance'] = Number
        self.set_label_type({
            'fr': 'Nombre',
            'en': 'Number'
        }[self._lang])

        self.initRule()

    def JONNumberValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        
        # --> OTHERS RULES
        # --<- min
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__min, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- max
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__max, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- less
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__less, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- greater
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__greater, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- negative
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__negative, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- positive
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__positive, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- signed
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__signed, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- integer
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__integer, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- decimal
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__decimal, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- multiple
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__multiple, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- TCPPort
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__TCPPort, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONNumberValidator(value)

    def initRule(self,):
        def sanitizeFunct(value: any) -> str:
            if(value is not None):
                if (
                    isNumber(value) == True and
                    not(float(value).is_integer()) and
                    value is not None
                ):
                    return float(value)
                elif (
                    isNumber(value) == True and
                    float(value).is_integer() and
                    value is not None
                ):
                    return int(value)
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | Number - initRule - value:: ", value)

            valid = True if (
                isNumber(value) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Number,
        }
        
    def min(self, minValue: int):
        def initFunct(value: any):
            self._minValue = minValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        type(minValue) in (int, float) and
                        value >= minValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._maxValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "{label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être au minimum {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "{label} must be at least {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__min = {
            'name': 'min',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def max(self, maxValue: int):
        def initFunct(value: any):
            self._maxValue = maxValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        type(maxValue) in (int, float) and
                        value <= maxValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._minValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                        'en': "{label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être au maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                        'en': "{label} must be maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__max = {
            'name': 'max',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def less(self, lessValue: int):
        def initFunct(value: any):
            self._lessValue = lessValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        type(lessValue) in (int, float) and
                        value < lessValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._greaterValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être superieure à {greater} et inférieure à {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "{label} must be greater than {greater} and less than {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    })
                else:
                    err = ({
                        'fr': "{label} doit être inferieure à {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "{label} must be less than {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__less = {
            'name': 'less',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def greater(self, greaterValue: int):
        def initFunct(value: any):
            self._greaterValue = greaterValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        type(greaterValue) in (int, float) and
                        value > greaterValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._lessValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être superieure à {greater} et inférieure à {less}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                        'en': "{label} must be greater than {greater} and less than {less}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être supérieur à {greater}".format(
                            label = labelSTR,
                            greater = greaterValue,
                        ),
                        'en': "{label} must be greater than {greater}".format(
                            label = labelSTR,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__greater = {
            'name': 'greater',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def negative(self):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        value <= 0
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être un nombre negatif".format(
                        label = labelSTR,
                    ),
                    "en": "{label} must be a negative number".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__negative = {
            'name': 'negative',
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def positive(self):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        value >= 0
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être un nombre positif".format(
                        label = labelSTR,
                    ),
                    "en": "{label} must be a positive number".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__positive = {
            'name': 'positive',
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def signed(self):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and (
                            value > 0 or
                            value < 0
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être soit un nombre négatif soit un nombre positif".format(
                        label = labelSTR,
                    ),
                    "en": "{label} must be either a negative number or a positive number".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__signed = {
            'name': 'signed',
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def integer(self):
        def sanitizeFunct(value: any) -> str:
            if(value is not None):
                if (
                    isNumber(value) == True and
                    value is not None
                ):
                    return int(value)
                return value
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in (int, float)
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être un nombre entier valide".format(
                        label = labelSTR,
                    ),
                    "en": "{label} must be a valid integer number".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__integer = {
            'name': 'integer',
            'rule': ruleFunct,
            'schema': Number,
            'sanitize': sanitizeFunct,
        }

        return self
    def decimal(self):
        def sanitizeFunct(value: any) -> str:
            if value is not None:
                if (
                    isNumber(value) == True and
                    value is not None
                ):
                    return float(value)
                return value
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in (float, int)
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être un nombre décimal valide".format(
                        label = labelSTR,
                    ),
                    "en": "{label} must be a valid decimal number".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__decimal = {
            'name': 'decimal',
            'rule': ruleFunct,
            'schema': Number,
            'sanitize': sanitizeFunct,
        }

        return self
    def multiple(self, nber: float):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in (int, float) and
                        type(nber) in [int, float] and
                        value % nber == 0
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être un multiple de {nber}".format(
                        label = labelSTR,
                        nber = nber,
                    ),
                    "en": "{label} must be a multiple of {nber}".format(
                        label = labelSTR,
                        nber = nber,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__multiple = {
            'name': 'multiple',
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
    def TCPPort(self):
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        isNumber(value) and
                        type(value) in [int, float] and
                        (
                            value > 9 and
                            value <= 99999
                        )
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = ({
                    "fr": "{label} doit être au format d'un port TCP".format(
                        label = labelSTR,
                    ),
                    "en": "{label} must be in the format of a TCP port".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__TCPPort = {
            'name': 'TCPPort',
            'rule': ruleFunct,
            'schema': Number,
        }

        return self
class Boolean(JONDefaultSchema):
    _trueValues: list = ['true', 't', '1', 1, True]
    _falseValues: list = ['false', 'f', '0', 0, False]

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - boolean --')

    def JONBooleanValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONBooleanValidator(value)

    def init(self,):
        self._options['validationType'] = 'boolean'
        self._options['type'] = bool
        self._options['instance'] = Boolean
        self.set_label_type({
            'fr': 'Booleen',
            'en': 'Boolean'
        }[self._lang])

        self.initRule()

    def initRule(self,):
        def sanitizeFunct(value: any) -> str:
            valueF = convertToBoolean(value)
            # if value is not None:
            #     if (
            #         isBoolean(value, self._trueValues, True)
            #     ):
            #         valueF = True
            #     elif (
            #         isBoolean(value, self._falseValues, True)
            #     ):
            #         valueF = False
            # else:
            #     valueF = None

            return valueF
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                isBoolean(value, (self._trueValues + self._falseValues), False)
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())

                # if self.get_error() is None:
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Boolean,
        }

    def required(self, isRequired: bool = True):
        isRequired = isRequired if type(isRequired) == bool else True
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None
            
            # print("> JONschemas | Boolean - required - value:: ", value)
            # print("> JONschemas | Boolean - required - (value is not None or type(value) == bool):: ", (value is not None or type(value) == bool))

            valid = (
                value is not None or
                type(value) == bool
            )
            # print("> JONschemas | Boolean - required - valid:: ", valid)

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label() if (
                    type(self.get_label()) == str and
                    len(self.get_label()) > 0
                ) else {
                    'fr': 'l\'element',
                    'en': 'the element'
                }[self._lang])
                err = Exception({
                    'fr': "{label} est requis".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is required".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__required = {
            'name': 'required',
            'rule': ruleFunct,
            'schema': self._options['instance'],
        } if (isRequired == True) else None

        return self
    
    def trueValues(self, values: list):
        values = values if type(values) in (list, tuple) else []
        if(len(values) > 0):
            self._trueValues = values
        return self
    def falseValues(self, values: list):
        values = values if type(values) in (list, tuple) else []
        if(len(values) > 0):
            self._falseValues = values
        return self
class Date(JONDefaultSchema):
    _timezone: any = pytz.UTC
    _format: str = None
    _dateFormat: str = dateFormatInitial
    _timeFormat: str = timeFormatInitial
    _maxValue: any = None
    _minValue: any = None
    _lessValue: any = None
    _greaterValue: any = None
    _equalValue: any = None
    
    _rule__min = None
    _rule__max = None
    _rule__less = None
    _rule__greater = None
    _rule__equalTo = None
    _rule__toDate = None
    _rule__toTime = None

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - date --')

    def JONDateValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        
        # --> OTHERS RULES
        # --<- min
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__min, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- max
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__max, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- less
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__less, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- greater
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__greater, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- equalTo
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__equalTo, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- toDate
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__toDate, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- toTime
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__toTime, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())

        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONDateValidator(value)

    def init(self,):
        self._options['validationType'] = 'date'
        self._options['type'] = datetime
        self._options['instance'] = Date
        self.set_label_type({
            'fr': 'Date',
            'en': 'Date'
        }[self._lang])
        self.initRule()

    def initRule(self,):
        def sanitizeFunct(value: any) -> any:
            if(value is not None):
                if(self._format is None):
                    self.changeFormat(dateTimeFormatInitial)
                        
                if(isDate(value, typeValue="string", dateFormat=self._format)):
                    value = datetime.datetime.strptime(value, self._format)

                if(self._timezone is not None):
                    value = value.astimezone(self._timezone)

                if type(value) == str:
                    value = datetime.datetime.strptime(value, self._format)

            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | Date - initRule - value:: ", value)

            valid = True if (
                isDate(value, dateFormat = self._format) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type \"Date\" invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid \"Date\" type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

    def min(self, minValue: any):
        def initFunct(value: any):
            if(getDate(minValue, dateFormat = self._format, timezone = self._timezone) is not None):
                self._minValue = getDate(minValue, dateFormat = self._format, timezone = self._timezone)
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or (
                        isDate(value) and
                        value >= self._minValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._maxValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = self._maxValue,
                        ),
                        'en': "{label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être au minimum {min}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = self._maxValue,
                        ),
                        'en': "{label} must be at least {min}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__min = {
            'name': 'min',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self
    def max(self, maxValue: any):
        def initFunct(value: any):
            if(getDate(maxValue, dateFormat = self._format, timezone = self._timezone) is not None):
                self._maxValue = getDate(maxValue, dateFormat = self._format, timezone = self._timezone)
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or (
                        isDate(value) and
                        value <= self._maxValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._minValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = self._maxValue,
                        ),
                        'en': "{label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être au maximum {max}".format(
                            label = labelSTR,
                            max = self._maxValue,
                        ),
                        'en': "{label} must be maximum {max}".format(
                            label = labelSTR,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__max = {
            'name': 'max',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self
    def less(self, lessValue: any):
        def initFunct(value: any):
            if(getDate(lessValue, dateFormat = self._format, timezone = self._timezone) is not None):
                self._lessValue = getDate(lessValue, dateFormat = self._format, timezone = self._timezone)
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or (
                        isDate(value) and
                        value < self._lessValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._greaterValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "{label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être inferieure à {less}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "{label} must be less than {less}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__less = {
            'name': 'less',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self
    def greater(self, greaterValue: any):
        def initFunct(value: any):
            if(getDate(greaterValue, dateFormat = self._format, timezone = self._timezone) is not None):
                self._greaterValue = getDate(greaterValue, dateFormat = self._format, timezone = self._timezone)
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or (
                        isDate(value) and
                        value > self._greaterValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._lessValue is not None
                ):
                    err = ({
                        'fr': "{label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "{label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "{label} doit être supérieur à {greater}".format(
                            label = labelSTR,
                            greater = self._greaterValue,
                        ),
                        'en': "{label} must be greater than {greater}".format(
                            label = labelSTR,
                            greater = self._self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__greater = {
            'name': 'greater',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self   
    def equalTo(self, equalValue: int):
        def initFunct(value: any):
            if(getDate(equalValue, dateFormat = self._format, timezone = self._timezone) is not None):
                self._equalValue = getDate(equalValue, dateFormat = self._format, timezone = self._timezone)
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or (
                        isDate(value) and
                        value == equalValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} doit être égale à {length}".format(
                        label = labelSTR,
                        length = self._equalValue,
                    ),
                    'en': "{label} must be equal to {length}".format(
                        label = labelSTR,
                        length = self._equalValue,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__equalTo = {
            'name': 'equalTo',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self
    def toDate(self):
        def sanitizeFunct(value: any) -> any:
            if(value is not None):
                if(type(value) is datetime.datetime):
                    value = value.date()

            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or 
                    isDate(value)
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} est d'un type \"Date\" invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid \"Date\" type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__toDate = {
            'name': 'toDate',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self
    def toTime(self):
        def sanitizeFunct(value: any) -> any:
            if(value is not None):
                if(type(value) is datetime.datetime):
                    value = value.time()
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    isDate(value, typeValue = 'null') or 
                    isDate(value)
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "{label} est d'un type \"Date\" invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid \"Date\" type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__toTime = {
            'name': 'toTime',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Date,
        }

        return self  
 
    def changeFormat(self,
        newFormat: str
    ):
        if (
            type(newFormat) == str and
            len(newFormat) > 0
        ):
            self._format = newFormat

        return self
    def changeTimezone(self,
        newTimezone: any
    ):
        if (
            newTimezone is not None
        ):
            self._timezone = newTimezone

        return self
class Enum(JONDefaultSchema):
    _choices: any = []

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - enum --')

    def init(self,):
        self._options['validationType'] = 'enum'
        self._options['type'] = any
        self._options['instance'] = Enum
        self.set_label_type({
            'fr': 'Type enumeré',
            'en': 'Enumerable type'
        }[self._lang])
        
        self.initRule()

    def JONEnumValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONEnumValidator(value)

    def initRule(self,):
        # init
        def mapFunct_clean(val: any):
            resMFC = val

            resMFCString = String(self._lang).validate(val)
            resMFCDate = Date(self._lang).validate(val)
            resMFCBoolean = Boolean(self._lang).validate(val)
            resMFCNumber = Number(self._lang).validate(val)
            
            if(resMFCString['valid'] == True):
                val = resMFCString['data']
            if(resMFCDate['valid'] == True):
                resMFC = resMFCDate['data']
            elif(resMFCBoolean['valid'] == True):
                resMFC = resMFCBoolean['data']
            elif(resMFCNumber['valid'] == True):
                resMFC = resMFCNumber['data']

            return resMFC

        def enumValueIsValid(value: any):
            choiceIsNone = self._choices is None
            # print("> JON.schemas | Enum - initRule - enumValueIsValid - choiceIsNone:: ", choiceIsNone)
            # print("> JON.schemas | Enum - initRule - enumValueIsValid - value - old:: ", value)
            if choiceIsNone == True:
                return False
            else:
                self._choices = list(
                    map(
                        mapFunct_clean,
                        self._choices,
                    )
                )
                
                value = mapFunct_clean(value)
                
                # print("> JON.schemas | Enum - initRule - enumValueIsValid - self._choices:: ", self._choices)
                # print("> JON.schemas | Enum - initRule - enumValueIsValid - value:: ", value)

                if(value is None) :
                    return True
                resEVIV = (
                    (
                        type(self._choices) in (list, tuple) and
                        (
                            (
                                len(self._choices) > 0 and
                                (
                                    value in self._choices
                                )
                            ) or len(self._choices) <= 0
                        )
                    ) or
                    value is None
                )

                return resEVIV
        def cleanValue(value: any):
            if(
                not(
                    type(value) in (list, tuple, dict, str, float, int, bool)
                )
            ):
                value = self._defaultValue

            return value

        def sanitizeFunct(value: any) -> str:
            if(value is not None):
                if (
                    enumValueIsValid(value)
                ):
                    return None if value is None else mapFunct_clean(value)
                elif (
                    value is None
                ):
                    return None
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = cleanValue(value)
            valid = True if (
                enumValueIsValid(value) or
                value is None
            ) else False

            # print("> JON.schemas | Enum - initRule - ruleFunct - self._choices:: ", self._choices, ' && value:: ', value)

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Enum,
        }


    def choices(self, *values: list):
        # print("> ENUM - choices | values:: ", values)
        self._choices = copy.deepcopy(values) if (
            type(values) in (list, tuple) and
            len(values) > 0
        ) else None
        # print("> ENUM - choices | values:: ", values)
        # print("> ENUM - choices | self._choices:: ", self._choices)

        return self
    def getChoices(self,):
        return self._choices
class NotInEnum(JONDefaultSchema):
    _choices: any = []

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - notInEnum --')

    def init(self,):
        self._options['validationType'] = 'notInEnum'
        self._options['type'] = any
        self._options['instance'] = NotInEnum
        self.set_label_type({
            'fr': 'Type non enumeré',
            'en': 'No enumerable type'
        }[self._lang])
        
        self.initRule()

    def JONNotInEnumValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONNotInEnumValidator(value)

    def initRule(self,):
        # init
        def mapFunct_clean(val: any):
            resMFC = val

            resMFCString = String(self._lang).validate(val)
            resMFCDate = Date(self._lang).validate(val)
            resMFCBoolean = Boolean(self._lang).validate(val)
            resMFCNumber = Number(self._lang).validate(val)
            
            if(resMFCString['valid'] == True):
                val = resMFCString['data']
            if(resMFCDate['valid'] == True):
                resMFC = resMFCDate['data']
            elif(resMFCBoolean['valid'] == True):
                resMFC = resMFCBoolean['data']
            elif(resMFCNumber['valid'] == True):
                resMFC = resMFCNumber['data']

            return resMFC

        def notInEnumValueIsValid(value: any):
            choiceIsNone = self._choices is None
            # print("> JON.schemas | Enum - initRule - notInEnumValueIsValid - choiceIsNone:: ", choiceIsNone)
            if choiceIsNone == True:
                return True
            else:
                self._choices = list(
                    map(
                        mapFunct_clean,
                        self._choices,
                    )
                )
                
                # print("> JON.schemas | NotInEnum - initRule - notInEnumValueIsValid - value - old:: ", value)
                value = mapFunct_clean(value)
                
                # print("> JON.schemas | NotInEnum - initRule - notInEnumValueIsValid - self._choices:: ", self._choices)
                # print("> JON.schemas | NotInEnum - initRule - notInEnumValueIsValid - value:: ", value)

                resEVIV = (
                    (
                        type(self._choices) in (list, tuple) and
                        (
                            (
                                len(self._choices) > 0 and
                                (
                                    value in self._choices
                                )
                            ) or len(self._choices) <= 0
                        )
                    ) or
                    value is None
                )

                return resEVIV
        def cleanValue(value: any):
            if(
                not(
                    type(value) in (list, tuple, dict, str, float, int, bool)
                )
            ):
                value = self._defaultValue

            return value

        def sanitizeFunct(value: any) -> str:
            if(value is not None):
                if (
                    notInEnumValueIsValid(value)
                ):
                    return None if value is None else mapFunct_clean(value)
                elif (
                    value is None
                ):
                    return None
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = cleanValue(value)
            valid = True if (
                notInEnumValueIsValid(value) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': NotInEnum,
        }


    def choices(self, *values: list):
        self._choices = values if (
            not(type(values) in (list, tuple)) and
            len(values) > 0
        ) else None
        # print("> NOTINENUM - choices | values:: ", values)
        # print("> NOTINENUM - choices | self._choices:: ", self._choices)

        return self
    def getChoices(self,):
        return self._choices
class ChosenType(JONDefaultSchema):
    _choices: any = []

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - chosenType --')

    def init(self,):
        self._options['validationType'] = 'chosenType'
        self._options['type'] = any
        self._options['instance'] = ChosenType
        self.set_label_type({
            'fr': 'Type choisi',
            'en': 'Chosen type'
        }[self._lang])
        
        self.initRule()

    def JONChosenTypeValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONChosenTypeValidator(value)

    def initRule(self,):
        # init
        # print("---- JON.schemas | ChosenType - initRule ----")
        def mapFunct_clean(val: any):
            resMFC = val

            resMFCString = String(self._lang).validate(val)
            resMFCDate = Date(self._lang).validate(val)
            resMFCBoolean = Boolean(self._lang).validate(val)
            resMFCNumber = Number(self._lang).validate(val)
            
            if(resMFCString['valid'] == True):
                val = resMFCString['data']
            if(resMFCDate['valid'] == True):
                resMFC = resMFCDate['data']
            elif(resMFCBoolean['valid'] == True):
                resMFC = resMFCBoolean['data']
            elif(resMFCNumber['valid'] == True):
                resMFC = resMFCNumber['data']

            return resMFC
        def getTypeChoice(value: any):
            result = list(
                filter(
                    lambda choice: choice.isValid(value),
                    self._choices,
                )
            )
            return result[0] if len(result) > 0 else None
        def chosenTypeValueIsValid(value: any):
            choiceIsNone = value is None
            if choiceIsNone == True:
                return False
            else:
                value = mapFunct_clean(value)
                res = (
                    (
                        len(
                            list(
                                filter(
                                    lambda choice: choice.isValid(value),
                                    self._choices,
                                )
                            )
                        ) > 0
                    ) or
                    value is None
                )

                return res
        def chosenTypeErrMsg(value: any):
            lang = self.get_lang()
            value = mapFunct_clean(value)
            invalidTypes = list(
                filter(
                    lambda choice: not(choice.isValid(value) == True),
                    self._choices,
                )
            )
            
            res = Exception((
                ' or ' if lang != 'fr' else ' ou '
            ).join(
                list(dict.fromkeys(
                    list(
                        map(
                            lambda choice: '<< {0} >>'.format(str(choice.label(self.get_label()).error(value))),
                            invalidTypes,
                        )
                    )
                ))
            )) if (
                type(invalidTypes) in (list, tuple) and
                len(invalidTypes) > 0
            ) else Exception({
                'fr': "{label} est d'un type invalide".format(
                    label = json.dumps(self.get_label()),
                ),
                'en': "{label} is of an invalid type".format(
                    label = json.dumps(self.get_label()),
                ),
            }[self._lang])

            # print("> JON.schemas | ChosenType - initRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | ChosenType - initRule - ruleFunct - self.get_label():: ", self.get_label())
            # err1 = invalidTypes[0].label(self.get_label())
            
            # print("> JON.schemas | ChosenType - initRule - ruleFunct - choiceLabels:: ", err1.validate(value))

            return res
        def cleanValue(value: any):
            if(
                not(
                    value or
                    type(value) == bool or
                    value is None
                )
            ):
                value = self._defaultValue

            return value

        def sanitizeFunct(value: any) -> str:
            if value is not None:
                if (
                    chosenTypeValueIsValid(value)
                ):
                    return None if value is None else getTypeChoice(value).sanitize(value)
                elif (
                    value is None
                ):
                    return None
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | ChosenType - initRule - ruleFunct - self._choices:: ", self._choices)
            # print("> JON.schemas | ChosenType - initRule - ruleFunct - value:: ", value)

            value = cleanValue(value)
            valid = True if (
                chosenTypeValueIsValid(value) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = chosenTypeErrMsg(value)
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': ChosenType,
        }


    def choices(self, *values: list):
        self._choices = values if(
            len(
                list(
                    filter(
                        lambda val: checkIfCorrectTypeSchema(val),
                        values,
                    ),
                )
            ) > 0
        ) else None

        return self
    def getChoices(self,):
        return self._choices
class NoInChosenType(JONDefaultSchema):
    _choices: any = []

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - chosenType --')

    def init(self,):
        self._options['validationType'] = 'NoInChosenType'
        self._options['type'] = any
        self._options['instance'] = NoInChosenType
        self.set_label_type({
            'fr': 'Type choisi',
            'en': 'Chosen type'
        }[self._lang])
        
        self.initRule()

    def JONNoInChosenTypeValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONNoInChosenTypeValidator(value)

    def initRule(self,):
        # init
        # print("---- JON.schemas | NoInChosenType - initRule ----")
        def mapFunct_clean(val: any):
            resMFC = val

            resMFCString = String(self._lang).validate(val)
            resMFCDate = Date(self._lang).validate(val)
            resMFCBoolean = Boolean(self._lang).validate(val)
            resMFCNumber = Number(self._lang).validate(val)
            
            if(resMFCString['valid'] == True):
                val = resMFCString['data']
            if(resMFCDate['valid'] == True):
                resMFC = resMFCDate['data']
            elif(resMFCBoolean['valid'] == True):
                resMFC = resMFCBoolean['data']
            elif(resMFCNumber['valid'] == True):
                resMFC = resMFCNumber['data']

            return resMFC
        def chosenTypeValueIsValid(value: any):
            choiceIsNone = value is None
            if choiceIsNone == True:
                return False
            else:
                value = mapFunct_clean(value)
                resList = list(
                    filter(
                        lambda choice: (choice.isValid(value)),
                        self._choices,
                    )
                )
                # print("> JON.schemas | NoInChosenType - initRule - chosenTypeValueIsValid - resList:: ", resList)
                res = (
                    (
                        len(resList) <= 0
                    ) or
                    value is None
                )

                return res
        def chosenTypeErrMsg(value: any):
            lang = self.get_lang()
            value = mapFunct_clean(value)
            invalidTypes = list(
                filter(
                    lambda choice: (choice.isValid(value)),
                    self._choices,
                )
            )

            # print("> JON.schemas | NoInChosenType - initRule - ruleFunct - invalidTypes:: ", invalidTypes)
            
            res = Exception('Un ou plusieurs types (' + (
                ' or ' if lang != 'fr' else ' ou '
            ).join(
                list(dict.fromkeys(
                    list(
                        map(
                            lambda choice: '<< {0} >>'.format(str(choice.get_label_type())),
                            invalidTypes,
                        )
                    )
                ))
            ) + ') invalides') if (
                type(invalidTypes) in (list, tuple) and
                len(invalidTypes) > 0
            ) else Exception({
                'fr': "{label} est d'un type invalide".format(
                    label = json.dumps(self.get_label()),
                ),
                'en': "{label} is of an invalid type".format(
                    label = json.dumps(self.get_label()),
                ),
            }[self._lang])

            # print("> JON.schemas | NoInChosenType - initRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | NoInChosenType - initRule - ruleFunct - self.get_label():: ", self.get_label())
            # err1 = invalidTypes[0].label(self.get_label())
            
            # print("> JON.schemas | NoInChosenType - initRule - ruleFunct - choiceLabels:: ", err1.validate(value))

            return res
        def cleanValue(value: any):
            if(
                not(
                    value or
                    type(value) == bool or
                    value is None
                )
            ):
                value = self._defaultValue

            return value

        def sanitizeFunct(value: any) -> str:
            if value is not None:
                return value
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | NoInChosenType - initRule - ruleFunct - self._choices:: ", self._choices)
            # print("> JON.schemas | NoInChosenType - initRule - ruleFunct - value:: ", value)

            value = cleanValue(value)
            valid = True if (
                chosenTypeValueIsValid(value) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = chosenTypeErrMsg(value)
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': NoInChosenType,
        }


    def choices(self, *values: list):
        self._choices = values if(
            len(
                list(
                    filter(
                        lambda val: checkIfCorrectTypeSchema(val),
                        values,
                    ),
                )
            ) > 0
        ) else None

        return self
    def getChoices(self,):
        return self._choices
class Object(JONDefaultSchema):
    _struct: dict = {}
    _primaryStruct: bool = False
    _maxValue: str = None
    _minValue: str = None
    _lessValue: str = None
    _greaterValue: str = None
    _lengthValue: str = None

    _types: list = []
    
    _oldValueForStruct = None

    _rule__init = None
    _rule__struct = None
    _rule__typesValues = None
    _rule__regExpTypesValues = None
    _rule__notInTypesValues = None
    _rule__keys = None
    _rule__regExpKeys = None
    _rule__noKeys = None
    _rule__min = None
    _rule__max = None
    _rule__less = None
    _rule__greater = None
    _rule__length = None

    def __init__(self, lang: str = 'fr'):
        '''
        Object est un schema permettant la validation des données de type dictionnaire sous JON.

            Parameters:
                lang (str): id de la langue ('fr' ou 'en')
        '''
        super().__init__(lang)
        self.init()
        # print('-- JON - object --')

    def init(self,):
        '''
        Cette fonction permet d'effectuer une initialisation des caracteristiques primaires du schema.
        '''
        self._options['validationType'] = 'object'
        self._options['type'] = any
        self._options['instance'] = Object
        self.set_label_type({
            'fr': 'Objet',
            'en': 'Object'
        }[self._lang])
        
        self.initRule()

    def JONObjectValidator(self, value: any) -> dict:
        '''
        Cette fonction permet d'appliquer des fonctions de validation par defaut de ce schema

            Parameters:
                value (any): element à valider

            Returns:
                dict: La reponse de la fonction
        '''
        resValidator_ = self.JONvalidator(value)
        
        # --> OTHERS RULES
        # --<- struct
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__struct, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- types values
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__typesValues, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- regExp types values
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__regExpTypesValues, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- not in types values
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__notInTypesValues, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- keys
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__keys, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- regExpKeys
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__regExpKeys, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- not in keys
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__noKeys, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- min
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__min, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- max
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__max, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- less
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__less, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- greater
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__greater, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- length
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__length, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())

        return resValidator_
    def validator(self, value: any) -> dict:
        '''
        Cette fonction permet d'appliquer des fonctions de validation par defaut de ce schema (Utilise la fonction 'JONvalidator')

            Parameters:
                value (any): element à valider

            Returns:
                dict: La reponse de la fonction
        '''
        return self.JONObjectValidator(value)

    def cleanValue(self, value: any):
        '''
        Cette fonction d'appliquer une valeur par default si elle existe et si l'element à valider est de type None

            Parameters:
                value (any): element à valider

            Returns:
                dict: La reponse de la fonction
        '''
        if(
            not(
                value or
                type(value) == bool or
                value is None
            ) and
            type(self._defaultValue) == dict
        ):
            value = self._defaultValue

        return value
    def initRule(self,):
        '''
        Cette regle permet de verifier si l'element est un dictionnaire.

            Returns:
                Object: Le schema de validation
        '''
        # init
        # print("---- JON.schemas | Object - initRule ----")

        def sanitizeFunct(value: any) -> dict:
            '''
            Cette fonction permet de nettoyer l'element après validation

                Parameters:
                    value (any): element à valider

                Returns:
                    dict: Le resultat de la fonction
            '''
            return value
        def ruleFunct(value: any) -> dict:
            '''
            Cette fonction permet de verifier si l'element est valide.

                Parameters:
                    value (any): element à valider

                Returns:
                    dict: Le resultat de la fonction
            '''
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | Object - initRule - ruleFunct - self._struct:: ", self._struct)
            # print("> JON.schemas | Object - initRule - ruleFunct - value:: ", value)

            value = self.cleanValue(value)
            valid = True if (
                type(value) == dict or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Object,
        }
        
        # print("> JON.schemas | Object - initRule - rule - self._rule__init:: ", self._rule__init)

    def objectValueIsValid(self, value: dict):
        value2 = copy.deepcopy(value)
        valueIsNone = value2 is None
        value = value if type(value) == dict else {}
        # print("> JON.schemas | Object - structRule - objectValueIsValid - value2:: ", value2)
        # print("> JON.schemas | Object - structRule - objectValueIsValid - self._struct:: ", self._struct)
        # print("> JON.schemas | Object - structRule - objectValueIsValid - valueIsNone:: ", valueIsNone)
        try:
            def mapOVIV(key):
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - key:: ", key)
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - self._struct:: ", self._struct)
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - value:: ", value)
                resOVIV = self._struct[key].validate(value[key])
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - key:: ", key)
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - self._struct[key]:: ", self._struct[key])
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - value[key]:: ", value[key])
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - type(value[key]):: ", type(value[key]))
                # print("> JON.schemas | Object - structRule - objectValueIsValid - mapOVIV - resOVIV:: ", resOVIV)
                return (resOVIV['valid'] == True)
            if valueIsNone == True:
                return True
            else:
                res = (
                    valueIsNone or
                    type(self._struct) == dict and (
                        (
                            type(value) == dict and (
                                len(
                                    list(
                                        filter(
                                            lambda key: mapOVIV(key),
                                            self._struct.keys(),
                                        )
                                    )
                                ) == len(self._struct.keys()) and (
                                    (
                                        self._primaryStruct == True and
                                        len(self._struct.keys()) == len(value.keys())
                                    ) or
                                    (
                                        self._primaryStruct == False and
                                        len(self._struct.keys()) <= len(value.keys()) and
                                        len(self._struct.keys()) > 0
                                    )
                                )
                            )
                        ) or (
                            type(value) == dict and
                            len(list(self._struct.keys())) <= 0
                        )
                    )
                )

                return res
        except Exception as err:
            stack = str(traceback.format_exc())
            log.error(stack)
            return False
    def objectSanitizeRes(self, value: dict):
        # print("> JON.schemas | Object - objectSanitizeRes - value:: ", value)
        # print("> JON.schemas | Object - objectSanitizeRes - self._struct:: ", self._struct)
        # print("> JON.schemas | Object - objectSanitizeRes - type(self._struct):: ", type(self._struct))
        # print("> JON.schemas | Object - objectSanitizeRes - len(self._struct.keys()):: ", len(self._struct.keys()))
        if (
            type(self._struct) == dict and
            not(len(self._struct.keys()) > 0) and
            type(value) == dict
        ):
            return value
        elif(self.objectValueIsValid(value)):
            primaryStructValue = {}
            otherValue = {}
            resValue = {}

            if(type(value) == dict):
                for index, key in enumerate(value):
                    if(key in list(self._struct.keys())):
                        primaryStructValue[key] = self._struct[key].sanitize(value[key])
                    else:
                        otherValue[key] = value[key]

                resValue = primaryStructValue
                resValue.update(otherValue)

            return resValue
        else:
            return None
    def objectInvalidAttrs(self, value: dict):
        if self._struct is not None:
            self._struct = {keySchema: schema.label(
                f"{cleanField(self.get_label(), max = 30, reverse = True)}.{cleanField(keySchema, max = 40, reverse = True)}"
            ) for keySchema, schema in self._struct.items()}
        invalids = []
        try:
            if(type(self._struct) == dict and self._struct is not None):
                invalids = list(
                    map(
                        lambda key: self._struct[key].validate(value[key]),
                        list(self._struct.keys()),
                    )
                )
                # print("\n\n> JON.schemas | Object - objectInvalidAttrs - invalids:: ", invalids, "\n")
                invalids = list(
                    filter(
                        lambda dtaI: dtaI['valid'] == False,
                        invalids,
                    )
                )
                # print("> JON.schemas | Object - objectInvalidAttrs - invalids OLD:: ", invalids, "\n\n")
        except Exception as err:
            stack = str(traceback.format_exc())
            log.error(stack)
            invalids = []
        # print("> JON.schemas | Object - objectInvalidAttrs - value:: ", value)
        # print("> JON.schemas | Object - objectInvalidAttrs - self._struct:: ", self._struct)
        # print("> JON.schemas | Object - objectInvalidAttrs - invalids:: ", invalids)
        
        return invalids[0]['error'] if len(invalids) > 0 else None
    def structRule(self,):

        def sanitizeFunct(value: any) -> str:
            if value is not None:
                # print("> JON.schemas | Object - structRule - sanitizeFunct - value:: ", value)
                prevalueSF = self.objectSanitizeRes(value)
                valueSF = {}
                # print("> JON.schemas | Object - structRule - sanitizeFunct - prevalueSF:: ", prevalueSF)
                # print("> JON.schemas | Object - structRule - sanitizeFunct - self._oldValueForStruct:: ", self._oldValueForStruct)
                for index, key in enumerate(prevalueSF):
                    val = prevalueSF[key]
                    if(key in self._oldValueForStruct.keys()):
                        valueSF[key] = val
                # print("> JON.schemas | Object - structRule - sanitizeFunct - valueSF:: ", valueSF)
                return valueSF
            else:
                return None
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | Object - initRule - ruleFunct - value (old):: ", value)
            # self._oldValueForStruct = copy.deepcopy(value)

            if(type(value) == dict and (
                type(self._struct) == dict and
                len(self._struct.keys()) > 0 and
                type(value) == dict
            )):
                valueInt = {}
                for index, key in enumerate(self._struct):
                    if(not(key in value.keys())):
                        valueInt[key] = None
                    else:
                        valueInt[key] = value[key]
                value = valueInt

            # print("> JON.schemas | Object - initRule - ruleFunct - self._struct:: ", self._struct)
            # print("> JON.schemas | Object - initRule - ruleFunct - self._oldValueForStruct:: ", self._oldValueForStruct)

            value = self.cleanValue(value)
            self._oldValueForStruct = copy.deepcopy(value)
            valid = True if (
                self.objectValueIsValid(value) or (
                    type(self._struct) == dict and
                    not(len(self._struct.keys()) > 0) and
                    type(value) == dict
                )
            ) else False
            # print("> JON.schemas | Object - initRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - initRule - ruleFunct - valid:: ", valid)

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                # print("> JON.schemas | Object - initRule - self._label:: ", self._label)
                # print("> JON.schemas | Object - initRule - labelSTR:: ", labelSTR)
                invalidAttrs = self.objectInvalidAttrs(value)
                # print("> JON.schemas | Object - initRule - invalidAttrs:: ", invalidAttrs)
                # if invalidAttrs is not None and 'type' in tuple(value.keys()):
                #     print("> JON.schemas | Object - initRule - self._struct:: ", self._struct)
                #     print("> JON.schemas | Object - initRule - invalidAttrs:: ", invalidAttrs)
                #     print("> JON.schemas | Object - initRule - value['type']:: ", value['type'])
                #     print("> JON.schemas | Object - initRule - self._struct['type']:: ", self._struct['type'])
                err = invalidAttrs if invalidAttrs is not None else (
                    Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                )
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__struct = {
            'name': 'struct',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Object,
        }
    
    def initStruct(self, values: dict):
        struct = {}
        try:
            values = values if type(values) == dict else {}

            otherValues = {}
            #subValues
            subValues = {}
            for index, key in enumerate(values):
                if(checkIfCorrectTypeSchema(values[key])):
                    subValues[key] = values[key]
                else:
                    otherValues[key] = values[key]
            struct = subValues

            #clone
            allClones: list = list(
                filter(
                    lambda val: (
                        type(val['value']) is Clone and
                        val['key'] and
                        val['value'].getTarget() is not None and
                        val['value'].getTarget() in subValues.keys()
                    ),
                    (
                        list(
                            map(
                                lambda key: {
                                    'key': key,
                                    'value': otherValues[key],
                                },
                                otherValues.keys(),
                            )
                        )
                    )
                )
            )
            allClones = list(
                map(
                    lambda val: {
                        'key': val['key'],
                        'value': subValues[val['value'].getTarget()].label(
                            "{parent}.{child}".format(parent = self.get_label(), child = val['key'])
                        ).lang(self._lang),
                    },
                    allClones,
                )
            )
            for index, data in enumerate(allClones):
                keyAC = data['key']
                valueAC = data['value']
                struct[keyAC] = valueAC

            if struct is not None:
                struct = {keySchema: schema.label(
                    f"{cleanField(self.get_label(), max = 30, reverse = True)}.{cleanField(keySchema, max = 40, reverse = True)}"
                ) for keySchema, schema in struct.items()}

        except Exception as err:
            stack = str(traceback.format_exc())
            log.error(stack)
            struct = None
        return struct
    def struct(self, values: dict):
        self._struct = self.initStruct(values)
            
        self._primaryStruct = False

        # print("> JON.schemas | Object - struct - self._struct:: ", self._struct)
        # print("> JON.schemas | Object - struct - self._primaryStruct:: ", self._primaryStruct)

        self.structRule()

        return self
    def primaryStruct(self, values: dict):
        self._struct = self.initStruct(values)
            
        self._primaryStruct = True

        # print("> JON.schemas | Object - struct - self._struct:: ", self._struct)
        # print("> JON.schemas | Object - struct - self._primaryStruct:: ", self._primaryStruct)

        self.structRule()

        return self
    def getStruct(self,):
        return self._struct

    def typesValuesRule(self, *values: list, strict: bool = False):
        strict = strict if type(strict) == bool else False
        self._types = list(
            filter(
                lambda type: checkIfCorrectTypeSchema(type),
                values,
            ),
        ) if type(values) in (list, tuple) else None

        # print("> JON.schemas | Object - typesValues - self._types:: ", self._types)
        def dictValueHasCorrectTypes(typeData, dictValues: list):
            res = list(
                map(
                    lambda value: typeData.validate(value),
                    dictValues,
                )
            )
            valueDVHCTIsValid = (
                len(
                    list(
                        filter(
                            lambda valSVAV: not(valSVAV['valid'] == True),
                            res,
                        )
                    )
                ) < len(dictValues)
            )

            return valueDVHCTIsValid
        
        def validateDictValue(value: list):
            # print("> JON.schemas | Object - typesValuesRule - validateDictValue - value:: ", value)
            valid = False
            data = None
            error = None
            invalidElements = None
            try:
                typeIsNone = self._types is None
                if(
                    (
                        (
                            type(value) == dict and
                            len(value.values()) <= 0
                        ) or value is None
                    ) and not(typeIsNone == True)
                ):
                    data = value
                    valid = True
                    error = None
                elif(type(value) == dict and len(value.values()) > 0):
                    validatorDatas = list(
                        map(
                            lambda jonType: ({
                                'key': jonType[0] + 1,
                                'val': jonType[1],
                                'isUse': (
                                    dictValueHasCorrectTypes( typeData = jonType[1], dictValues = list(value.values()) )
                                    # and DVHCTSchema( typeData = jonType[1], value = value )
                                ),
                                'label': jonType[1].get_label_type(),
                            }),
                            enumerate(self._types),
                        )
                    )
                    invalidDatas = list(
                        filter(
                            lambda resVDIV: not(resVDIV['isUse'] == True),
                            validatorDatas,
                        )
                    )
                    validDatas = list(
                        filter(
                            lambda resVDIV: (resVDIV['isUse'] == True),
                            validatorDatas,
                        )
                    )
                    valid = (
                        value is None or (
                            not(strict == True) and
                            len(invalidDatas) < len(validatorDatas) and
                            len(validatorDatas) > 0
                        ) or (
                            strict == True and
                            len(validDatas) == len(validatorDatas) and
                            len(validatorDatas) > 0
                        )
                    )
                    
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - value.values():: ", list(value.values()))
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - invalidDatas:: ", invalidDatas)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - len(invalidDatas):: ", (
                    #     len(validatorDatas) - len(validDatas)
                    # ))
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - validDatas:: ", validDatas)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - len(validDatas):: ", len(validDatas))
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - validatorDatas:: ", validatorDatas)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - len(validatorDatas):: ", len(validatorDatas))
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - valid:: ", valid)
                    # data = list(
                    #     map(
                    #         lambda resVDIV: resVDIV['validate']['data'],
                    #         validatorDatas,
                    #     )
                    # )
                    if(
                        not(valid == True)
                    ):
                        invalidElements = list(
                            map(
                                lambda valIE: valIE['label'],
                                invalidDatas
                            )
                        ) if valid == False else None
                        invalidElements = list(
                            filter(
                                lambda element: type(element) in (dict, str, int, float),
                                invalidElements,
                            )
                        )
                        invalidElements = list(
                            map(
                                lambda element: '`{value}`'.format(
                                    value = element
                                ) if type(element) == dict else element,
                                invalidElements,
                            )
                        )
                    else:
                        data = value
                        invalidElements = None
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - invalidElements:: ", invalidElements)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - type(invalidElements):: ", type(invalidElements))
                    error = ', '.join(list(
                        map(
                            lambda val: str(val),
                            invalidElements
                        )
                    )) if (
                        invalidElements is not None
                    ) else None
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - error:: ", error)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - type(error):: ", type(error))
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - validatorDatas:: ", validatorDatas)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - valid:: ", valid)
                    # print("> JON.schemas | Object - typesValuesRule - validateDictValue - data:: ", data)
                else:
                    data = None
                    valid = False
                    error = None
            except Exception as err:
                stack = str(traceback.format_exc())
                log.error(stack)
                data = None
                valid = False
                error = str(err)
            resVAV = {
                'data': data,
                'valid': valid,
                'error': error,
                'invalidElements': invalidElements,
            }
            return resVAV

        def sanitizeFunct(value: any) -> list:
            if value is None:
                return value
            res = {}
            for key, val in value.items():
                validationValue = ChosenType(self._lang).choices(*self._types).validate(val)
                if validationValue['valid']:
                    res[key] = validationValue['data']
            return res
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)
            cnf_validateDictValue = validateDictValue(value)

            # print("> JON.schemas | Object - typesValuesRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Object - typesValuesRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - typesValuesRule - ruleFunct - cnf_validateDictValue:: ", cnf_validateDictValue)

            valid = True if (
                cnf_validateDictValue['valid']
            ) else False

            if(valid == True):
                error = None
                data = cnf_validateDictValue['data']
            else:
                labelSTR = json.dumps(self.get_label())
                invalidAttrs = cnf_validateDictValue['error']

                if(invalidAttrs is not None and len(invalidAttrs) > 0):
                    err = Exception({
                        'fr': "{label} possède un ou plusieurs types ({attrs}) non pris en charge par certains attributs".format(
                            label = labelSTR,
                            attrs = invalidAttrs,
                        ),
                        'en': "{label} has one or more types ({attrs}) not supported by certain attributes".format(
                            label = labelSTR,
                            attrs = invalidAttrs,
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__typesValues = {
            'name': 'types',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Dict,
        }
    def typesValues(self, *values: list, strict: bool = False):
        self.typesValuesRule(*values, strict = strict)

        return self
    def notInTypesValuesRule(self, *values: list, strict: bool = False):
        strict = strict if type(strict) == bool else False
        self._types = list(
            filter(
                lambda type: checkIfCorrectTypeSchema(type),
                values,
            ),
        ) if type(values) in (list, tuple) else None

        # print("> JON.schemas | Object - notInTypesValuesRule - self._types:: ", self._types)
        def dictValueHasCorrectTypes(typeData, dictValues: list):
            res = list(
                map(
                    lambda value: typeData.validate(value),
                    dictValues,
                )
            )
            valueDVHCTIsValidList = list(
                filter(
                    lambda valSVAV: (valSVAV['valid'] == True),
                    res,
                )
            )
            valueDVHCTIsValid = (
                len(
                    valueDVHCTIsValidList
                ) <= 0
            )

            # print("> JON.schemas | Object - notInTypesValuesRule - dictValueHasCorrectTypes - valueDVHCTIsValidList:: ", valueDVHCTIsValidList)
            # print("> JON.schemas | Object - notInTypesValuesRule - dictValueHasCorrectTypes - valueDVHCTIsValid:: ", valueDVHCTIsValid)
            # print("> JON.schemas | Object - notInTypesValuesRule - dictValueHasCorrectTypes - self._types:: ", self._types)

            return valueDVHCTIsValid
        
        def validateDictValue(value: list):
            # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - value:: ", value)
            valid = False
            data = None
            error = None
            invalidElements = None
            try:
                typeIsNone = self._types is None
                if(
                    (
                        (
                            type(value) == dict and
                            len(value.values()) <= 0
                        ) or value is None
                    ) and not(typeIsNone == True)
                ):
                    data = value
                    valid = True
                    error = None
                elif(type(value) == dict and len(value.values()) > 0):
                    validatorDatas = list(
                        map(
                            lambda jonType: ({
                                'key': jonType[0] + 1,
                                'val': jonType[1],
                                'isUse': (
                                    dictValueHasCorrectTypes( typeData = jonType[1], dictValues = list(value.values()) )
                                    # and DVHCTSchema( typeData = jonType[1], value = value )
                                ),
                                'label': jonType[1].get_label_type(),
                            }),
                            enumerate(self._types),
                        )
                    )
                    invalidDatas = list(
                        filter(
                            lambda resVDIV: not(resVDIV['isUse'] == True),
                            validatorDatas,
                        )
                    )
                    validDatas = list(
                        filter(
                            lambda resVDIV: (resVDIV['isUse'] == True),
                            validatorDatas,
                        )
                    )
                    valid = (
                        value is None or (
                            not(strict == True) and
                            len(invalidDatas) < len(self._types) and
                            len(self._types) > 0
                        ) or (
                            strict == True and
                            len(invalidDatas) <= 0
                        )
                    )
                    
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - validatorDatas:: ", validatorDatas)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - len(validatorDatas):: ", len(validatorDatas))
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - invalidDatas:: ", invalidDatas)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - len(invalidDatas):: ", len(invalidDatas))
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - value.values():: ", list(value.values()))
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - invalidDatas:: ", invalidDatas)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - len(invalidDatas):: ", (
                    #     len(validatorDatas) - len(validDatas)
                    # ))
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - validDatas:: ", validDatas)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - len(validDatas):: ", len(validDatas))
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - valid:: ", valid)
                    # data = list(
                    #     map(
                    #         lambda resVDIV: resVDIV['validate']['data'],
                    #         validatorDatas,
                    #     )
                    # )
                    if(
                        not(valid == True)
                    ):
                        invalidElements = list(
                            map(
                                lambda valIE: valIE['label'],
                                invalidDatas
                            )
                        ) if valid == False else None
                        invalidElements = list(
                            filter(
                                lambda element: type(element) in (dict, str, int, float),
                                invalidElements,
                            )
                        )
                        invalidElements = list(
                            map(
                                lambda element: '`{value}`'.format(
                                    value = element
                                ) if type(element) == dict else element,
                                invalidElements,
                            )
                        )
                    else:
                        data = value
                        invalidElements = None
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - invalidElements:: ", invalidElements)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - type(invalidElements):: ", type(invalidElements))
                    error = ', '.join(list(
                        map(
                            lambda val: str(val),
                            invalidElements
                        )
                    )) if (
                        invalidElements is not None
                    ) else None
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - error:: ", error)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - type(error):: ", type(error))
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - validatorDatas:: ", validatorDatas)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - valid:: ", valid)
                    # print("> JON.schemas | Object - notInTypesValuesRuleRule - validateDictValue - data:: ", data)
                else:
                    data = None
                    valid = False
                    error = None
            except Exception as err:
                stack = str(traceback.format_exc())
                log.error(stack)
                data = None
                valid = False
                error = str(err)
            resVAV = {
                'data': data,
                'valid': valid,
                'error': error,
                'invalidElements': invalidElements,
            }
            return resVAV

        def sanitizeFunct(value: any) -> list:
            if value is None:
                return None
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)
            cnf_validateDictValue = validateDictValue(value)

            # print("> JON.schemas | Object - notInTypesValuesRuleRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Object - notInTypesValuesRuleRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - notInTypesValuesRuleRule - ruleFunct - cnf_validateDictValue:: ", cnf_validateDictValue)

            valid = True if (
                cnf_validateDictValue['valid']
            ) else False

            if(valid == True):
                error = None
                data = cnf_validateDictValue['data']
            else:
                labelSTR = json.dumps(self.get_label())
                invalidAttrs = cnf_validateDictValue['error']

                if(invalidAttrs is not None and len(invalidAttrs) > 0):
                    err = Exception({
                        'fr': "{label} possède un ou plusieurs types ({attrs}) pris en charge par certains attributs".format(
                            label = labelSTR,
                            attrs = invalidAttrs,
                        ),
                        'en': "{label} has one or more types ({attrs}) supported by certain attributes".format(
                            label = labelSTR,
                            attrs = invalidAttrs,
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__notInTypesValues = {
            'name': 'not-in-types',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Dict,
        }
    def notInTypesValues(self, *values: list, strict: bool = False):
        self.notInTypesValuesRule(*values, strict = strict)

        return self
    def regExpTypesValuesRule(self, ruleValue: str, flag: re.RegexFlag = None, strict: bool = False):
        strict = strict if type(strict) == bool else False

        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)

            # print("> JON.schemas | Object - regExpTypesValuesRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Object - regExpTypesValuesRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - regExpTypesValuesRule - ruleFunct - cnf_validateDictValue:: ", cnf_validateDictValue)

            valid = True if (
                value is None or 
                (
                    not(strict == True) and
                    len(
                        list(
                            filter(
                                lambda value: String(self.lang).regexp(ruleValue=ruleValue, flag=flag).isValid(value),
                                list(value.values()),
                            )
                        )
                    ) > 0
                ) or 
                (
                    strict == True and
                    len(
                        list(
                            filter(
                                lambda value: String(self.lang).regexp(ruleValue=ruleValue, flag=flag).isValid(value),
                                list(value.values()),
                            )
                        )
                    ) == len(list(value.values())) and
                    len(list(value.values())) > 0
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                invalidDatas = list(
                    filter(
                        lambda data: not(data['isValid']),
                        [{
                            'key': key,
                            'value': value,
                            'isValid': String(self.lang).regexp(ruleValue=ruleValue, flag=flag).isValid(value),
                        } for (key, value) in value.items()],
                    )
                )

                if(not(len(list(value.values())) > 0)):
                    err = Exception({
                        'fr': "{label} ne possede aucune valeur à verifier pour la validation".format(
                            label = labelSTR,
                        ),
                        'en': "{label} has no value to check for validation".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                elif(invalidDatas is not None and len(invalidDatas) > 0):
                    err = Exception({
                        'fr': "{label} possède une ou plusieurs valeurs au format invalide dont les clés sont : {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda data: '"{0}"'.format(data['key']),
                                    invalidDatas
                                )
                            )),
                        ),
                        'en': "{label} has one or more invalidly formatted values ​​whose keys are : {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda data: '"{0}"'.format(data['key']),
                                    invalidDatas
                                )
                            )),
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__regExpTypesValues = {
            'name': 'regExptypes',
            'rule': ruleFunct,
            'schema': Dict,
        }
    def regExpTypesValues(self, ruleValue: str, flag: re.RegexFlag = None, strict: bool = False):
        self.regExpTypesValuesRule(ruleValue = ruleValue, flag = flag, strict = strict)

        return self
    def keysRule(self, *keys: list, strict: bool = False):
        strict = strict if type(strict) == bool else False
        keys = list(
            filter(
                lambda key: type(key) == str,
                keys,
            )
        ) if type(keys) in (list, tuple) else []
        
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)

            # print("> JON.schemas | Object - keysRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Object - keysRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - keysRule - ruleFunct - cnf_validateDictValue:: ", cnf_validateDictValue)

            valid = True if (
                value is None or 
                (
                    not(strict == True) and
                    len(
                        list(
                            filter(
                                lambda key: key in value.keys(),
                                keys,
                            )
                        )
                    ) > 0
                ) or 
                (
                    strict == True and
                    len(
                        list(
                            filter(
                                lambda key: key in value.keys(),
                                keys,
                            )
                        )
                    ) == len(keys) and
                    len(keys) > 0
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                invalidKeys = list(
                    filter(
                        lambda key: not(key in value.keys()),
                        keys,
                    )
                )

                if(not(len(keys) > 0)):
                    err = Exception({
                        'fr': "{label} ne possede aucune clé à verifier pour la validation".format(
                            label = labelSTR,
                        ),
                        'en': "{label} has no key to check for validation".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                elif(invalidKeys is not None and len(invalidKeys) > 0):
                    err = Exception({
                        'fr': "{label} possède une ou plusieurs clés indefinis: {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda key: '"{0}"'.format(key),
                                    invalidKeys
                                )
                            )),
                        ),
                        'en': "{label} has one or more undefined keys: {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda key: "'{0}'".format(key),
                                    invalidKeys
                                )
                            )),
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__keys = {
            'name': 'keys',
            'rule': ruleFunct,
            'schema': Dict,
        }
    def keys(self, *keys: list, strict: bool = False):
        self.keysRule(*keys, strict=strict)

        return self
    def regExpKeysRule(self, ruleValue: str, flag: re.RegexFlag = None, strict: bool = False):
        strict = strict if type(strict) == bool else False
        
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)

            # print("> JON.schemas | Object - regExpKeysRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Object - regExpKeysRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - regExpKeysRule - ruleFunct - cnf_validateDictValue:: ", cnf_validateDictValue)

            valid = True if (
                value is None or 
                (
                    not(strict == True) and
                    len(
                        list(
                            filter(
                                lambda key: String(self.lang).regexp(ruleValue=ruleValue, flag=flag).isValid(key),
                                list(value.keys()),
                            )
                        )
                    ) > 0
                ) or 
                (
                    strict == True and
                    len(
                        list(
                            filter(
                                lambda key: String(self.lang).regexp(ruleValue=ruleValue, flag=flag).isValid(key),
                                list(value.keys()),
                            )
                        )
                    ) == len(list(value.keys())) and
                    len(list(value.keys())) > 0
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                invalidKeys = list(
                    filter(
                        lambda key: not(String(self.lang).regexp(ruleValue=ruleValue, flag=flag).isValid(key)),
                        list(value.keys()),
                    )
                )

                if(not(len(list(value.keys())) > 0)):
                    err = Exception({
                        'fr': "{label} ne possede aucune clé à verifier pour la validation".format(
                            label = labelSTR,
                        ),
                        'en': "{label} has no key to check for validation".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                elif(invalidKeys is not None and len(invalidKeys) > 0):
                    err = Exception({
                        'fr': "{label} possède une ou plusieurs clés au format invalide: {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda key: '"{0}"'.format(key),
                                    invalidKeys
                                )
                            )),
                        ),
                        'en': "{label} has one or more invalidly formatted keys: {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda key: "'{0}'".format(key),
                                    invalidKeys
                                )
                            )),
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__regExpKeys = {
            'name': 'regExpKeys',
            'rule': ruleFunct,
            'schema': Dict,
        }
    def regExpKeys(self, ruleValue: str, flag: re.RegexFlag = None, strict: bool = False):
        self.regExpKeysRule(ruleValue = ruleValue, flag = flag, strict = strict)

        return self
    def noKeysRule(self, *keys: list, strict: bool = False):
        strict = strict if type(strict) == bool else False
        keys = list(
            filter(
                lambda key: type(key) == str,
                keys,
            )
        ) if type(keys) in (list, tuple) else []
        
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)

            # print("> JON.schemas | Object - noKeysRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Object - noKeysRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Object - noKeysRule - ruleFunct - cnf_validateDictValue:: ", cnf_validateDictValue)

            valid = True if (
                value is None or 
                (
                    not(strict == True) and
                    len(
                        list(
                            filter(
                                lambda key: not(key in value.keys()),
                                keys,
                            )
                        )
                    ) > 0
                ) or 
                (
                    strict == True and
                    len(
                        list(
                            filter(
                                lambda key: not(key in value.keys()),
                                keys,
                            )
                        )
                    ) == len(keys) and
                    len(keys) > 0
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                invalidKeys = list(
                    filter(
                        lambda key: (key in value.keys()),
                        keys,
                    )
                )

                if(not(len(keys) > 0)):
                    err = Exception({
                        'fr': "{label} ne possede aucune clé à verifier pour la validation".format(
                            label = labelSTR,
                        ),
                        'en': "{label} has no key to check for validation".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                elif(invalidKeys is not None and len(invalidKeys) > 0):
                    err = Exception({
                        'fr': "{label} possède une ou plusieurs clés definis: {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda key: '"{0}"'.format(key),
                                    invalidKeys
                                )
                            )),
                        ),
                        'en': "{label} has one or more defined keys: {attrs}".format(
                            label = labelSTR,
                            attrs = ', '.join(list(
                                map(
                                    lambda key: "'{0}'".format(key),
                                    invalidKeys
                                )
                            )),
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__noKeys = {
            'name': 'not-in-keys',
            'rule': ruleFunct,
            'schema': Dict,
        }
    def noKeys(self, *keys: list, strict: bool = False):
        self.noKeysRule(*keys, strict=strict)

        return self

    def min(self, minValue: int):
        def initFunct(value: any):
            self._minValue = minValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None
            
            # print("> JON.schemas | Object - min - ruleFunct - value:: ", value)

            valid = True if (
                (
                    value is None or (
                        type(value) == dict and
                        len(value.keys()) >= minValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._maxValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "the size of {label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être au minimum {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "the size of {label} must be at least {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__min = {
            'name': 'min',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def max(self, maxValue: int):
        def initFunct(value: any):
            self._maxValue = maxValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) == dict and
                        len(value.keys()) <= maxValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._minValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                        'en': "the size of {label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être au maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                        'en': "the size of {label} must be maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__max = {
            'name': 'max',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def less(self, lessValue: int):
        def initFunct(value: any):
            self._lessValue = lessValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) == dict and
                        len(value.keys()) < lessValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._greaterValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être inferieure à {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__less = {
            'name': 'less',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def greater(self, greaterValue: int):
        def initFunct(value: any):
            self._greaterValue = greaterValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) == dict and
                        len(value.keys()) > greaterValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._lessValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être supérieur à {greater}".format(
                            label = labelSTR,
                            greater = greaterValue,
                        ),
                        'en': "the size of {label} must be greater than {greater}".format(
                            label = labelSTR,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__greater = {
            'name': 'greater',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def length(self, lengthValue: int):
        def initFunct(value: any):
            self._lengthValue = lengthValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) == dict and
                        len(value.keys()) == lengthValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "la taille de {label} doit être égale à {length}".format(
                        label = labelSTR,
                        length = lengthValue,
                    ),
                    'en': "the size of {label} must be equal to {length}".format(
                        label = labelSTR,
                        length = self._lengthValue,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__length = {
            'name': 'length',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
class Array(JONDefaultSchema):
    _maxValue: str = None
    _minValue: str = None
    _lessValue: str = None
    _greaterValue: str = None
    _lengthValue: str = None
    _types: list = []
    
    _rule__init = None
    _rule__types = None
    _rule__min = None
    _rule__max = None
    _rule__less = None
    _rule__greater = None
    _rule__length = None

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - array --')

    def init(self,):
        self._options['validationType'] = 'array'
        self._options['type'] = any
        self._options['instance'] = Array
        self.set_label_type({
            'fr': 'Tableau',
            'en': 'Array'
        }[self._lang])
        
        self.initRule()

    def JONObjectValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        
        # --> OTHERS RULES
        # --<- types
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__types, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- min
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__min, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- max
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__max, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- less
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__less, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- greater
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__greater, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        # --<- length
        resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__length, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())

        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONObjectValidator(value)

    def cleanValue(self, value: any):
        if(
            not(
                value or
                type(value) == bool or
                value is None
            ) and
            type(self._defaultValue) in (list, tuple)
        ):
            value = self._defaultValue

        return value
    def initRule(self,):
        # init
        # print("---- JON.schemas | Array - initRule ----")

        def sanitizeFunct(value: any) -> str:
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JON.schemas | Array - initRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Array - initRule - ruleFunct - value:: ", value)

            value = self.cleanValue(value)
            valid = True if (
                type(value) in (list, tuple) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Array,
        }

    def typesRule(self,):
        def mapFunct_clean(val: any):
            resMFC = val

            resMFCString = String(self._lang).validate(val)
            resMFCDate = Date(self._lang).validate(val)
            resMFCBoolean = Boolean(self._lang).validate(val)
            resMFCNumber = Number(self._lang).validate(val)
            
            if(resMFCString['valid'] == True):
                val = resMFCString['data']
            if(resMFCDate['valid'] == True):
                resMFC = resMFCDate['data']
            elif(resMFCBoolean['valid'] == True):
                resMFC = resMFCBoolean['data']
            elif(resMFCNumber['valid'] == True):
                resMFC = resMFCNumber['data']

            return resMFC
        def getTypeChoice(value: any):
            result = list(
                filter(
                    lambda choice: choice.isValid(value),
                    self._types,
                )
            )
            return result[0] if len(result) > 0 else None
        def arrayValueIsValid(value: any):
            choiceIsNone = value is None
            if choiceIsNone == True:
                return False
            else:
                value = mapFunct_clean(value)
                res = (
                    (
                        len(
                            list(
                                filter(
                                    lambda choice: choice.isValid(value),
                                    self._types,
                                )
                            )
                        ) > 0
                    ) or
                    value is None
                )

                return res
        def arrayErrMsg(value: any):
            if self._types is not None:
                self._types = [value.label(f"{self.get_label()}") for indexValue, value in enumerate(self._types)]
            lang = self.get_lang()
            value = mapFunct_clean(value)
            invalidTypes = list(
                filter(
                    lambda choice: not(
                        value is None or
                        choice.isValid(value) == True
                    ),
                    self._types,
                )
            )
            # print("> JON.schemas | Array - typesRule - arrayErrMsg - invalidTypes:: ", invalidTypes)
            # print("> JON.schemas | Array - typesRule - arrayErrMsg - value:: ", value)
            
            res = Exception((
                ' or ' if lang != 'fr' else ' ou '
            ).join(
                list(dict.fromkeys(
                    list(
                        map(
                            lambda choice: '<< {0} >>'.format(cleanField(choice.label(self.get_label()).error(value))),
                            invalidTypes,
                        )
                    )
                ))
            )) if (
                type(invalidTypes) in (list, tuple) and
                len(invalidTypes) > 0
            ) else None

            # print("> JON.schemas | Array - initRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Array - initRule - ruleFunct - self.get_label():: ", self.get_label())
            # err1 = invalidTypes[0].label(self.get_label())
            
            # print("> JON.schemas | Array - initRule - ruleFunct - choiceLabels:: ", err1.validate(value))

            return res
        def cleanValue(value: any):
            if(
                not(
                    value or
                    type(value) == bool or
                    value is None
                )
            ):
                value = self._defaultValue

            return value

        def singleValidateArrayValue(valueSVAV):
            res = list(
                map(
                    lambda type: type.validate(valueSVAV),
                    self._types,
                )
            )
            valueSVAVIsValid = (
                len(
                    list(
                        filter(
                            lambda valSVAV: not(valSVAV['valid'] == True),
                            res,
                        )
                    )
                ) <= 0
            )

            return list(
                filter(
                    lambda valSVAV: valSVAV['valid'] == True,
                    res,
                )
            )[0] if valueSVAVIsValid else res[0]
        def validateArrayValue(value: list):
            # print("> JON.schemas | Array - typesRule - validateArrayValue - value:: ", value)
            valid = False
            data = None
            error = None
            invalidElements = None
            try:
                typeIsNone = self._types is None
                if(
                    (
                        (
                            type(value) in (list, tuple) and
                            len(value) <= 0
                        ) or value is None
                    ) and not(typeIsNone == True)
                ):
                    data = value
                    valid = True
                    error = None
                elif(type(value) in (list, tuple) and len(value) > 0):
                    validatorDatas = list(
                        map(
                            lambda val: {
                                'val': val,
                                'validate': singleValidateArrayValue(val),
                            },
                            value,
                        )
                    )
                    valid = (
                        len(
                            list(
                                filter(
                                    lambda resVDIV: not(resVDIV['validate']['valid'] == True),
                                    validatorDatas,
                                )
                            )
                        ) <= 0
                    )
                    data = list(
                        map(
                            lambda resVDIV: resVDIV['validate']['data'],
                            validatorDatas,
                        )
                    )
                    if(
                        type(invalidElements) in (str, tuple) and
                        len(invalidElements) > 0
                    ):
                        invalidElements = list(
                            map(
                                lambda valIE: valIE['val'],
                                (
                                    list(
                                        filter(
                                            lambda resVDIV: not(resVDIV['validate']['valid'] == True),
                                            validatorDatas,
                                        )
                                    )
                                )
                            )
                        ) if valid == False else None
                        invalidElements = list(
                            filter(
                                lambda element: type(element) in (dict, str, int, float),
                                invalidElements,
                            )
                        )
                        invalidElements = list(
                            map(
                                lambda element: cleanField(element) if type(element) == dict else element,
                                invalidElements,
                            )
                        )
                    else:
                        invalidElements = None
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - invalidElements:: ", invalidElements)
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - type(invalidElements):: ", type(invalidElements))
                    error = ', '.join(invalidElements) if (
                        invalidElements is not None
                    ) else None
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - error:: ", error)
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - type(error):: ", type(error))
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - validatorDatas:: ", validatorDatas)
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - valid:: ", valid)
                    # print("> JON.schemas | Array - typesRule - validateArrayValue - data:: ", data)
                else:
                    data = None
                    valid = False
                    error = None
            except Exception as err:
                stack = str(traceback.format_exc())
                log.error(stack)
                data = None
                valid = False
                error = str(err)
            resVAV = {
                'data': data,
                'valid': valid,
                'error': error,
                'invalidElements': invalidElements,
            }
            return resVAV

        def sanitizeElFunct(value: any):
            if value is not None:
                if (
                    arrayValueIsValid(value)
                ):
                    return None if value is None else getTypeChoice(value).sanitize(value)
                elif (
                    value is None
                ):
                    return None
            else:
                return None
        def sanitizeFunct(value: any) -> list:
            return list(
                map(
                    lambda dt: sanitizeElFunct(dt),
                    value,
                )
            ) if value is not None else value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            value = self.cleanValue(value)
            # cnf_validateArrayValue = validateArrayValue(value)

            # print("> JON.schemas | Array - initRule - ruleFunct - self._types:: ", self._types)
            # print("> JON.schemas | Array - initRule - ruleFunct - value:: ", value)
            # print("> JON.schemas | Array - initRule - ruleFunct - cnf_validateArrayValue:: ", cnf_validateArrayValue)

            # valid = True if (
            #     cnf_validateArrayValue['valid']
            # ) else False
            valid = True if (
                value is None or (
                    type(value) in (list, tuple) and
                    len(value) == len(list(
                        filter(
                            lambda dt: arrayValueIsValid(dt),
                            value,
                        )
                    ))
                ) or
                value is None
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                # print("> JON.schemas | Array - initRule - ruleFunct - self._label:: ", self._label)
                initialInvalidAttrs = [{
                    'index': indexDt,
                    'error': arrayErrMsg(dt),
                    'value': dt,
                    'label': f"{cleanField(self.get_label(), max = 30, reverse = True)}[{cleanField(indexDt, max = 10, reverse=True)}] = `{cleanField(dt)}`",
                } for indexDt, dt in enumerate(value)]

                invalidAttrs = list(
                    filter(
                        lambda data: (
                            type(data['error']) is Exception or
                            isinstance(type(data['error']), Exception) or
                            issubclass(type(data['error']), Exception)
                        ),
                        initialInvalidAttrs
                    )
                )
                # print("> JON.schemas | Array - initRule - ruleFunct - initialInvalidAttrs:: ", initialInvalidAttrs)
                # print("> JON.schemas | Array - initRule - ruleFunct - invalidAttrs:: ", invalidAttrs)
                invalidAttrs = list(
                    map(
                        lambda dt: dt['label'],
                        invalidAttrs,
                    )
                )
                # print("> JON.schemas | Array - initRule - ruleFunct - invalidAttrs:: ", invalidAttrs)

                if(invalidAttrs is not None and len(invalidAttrs) > 0):
                    err = Exception({
                        'fr': "{label} ({attrs}) possède une ou plusieurs valeurs invalides".format(
                            label = labelSTR,
                            attrs = cleanField(', '.join(invalidAttrs), max = 50),
                        ),
                        'en': "{label} ({attrs}) has one or more invalid values".format(
                            label = labelSTR,
                            attrs = cleanField(', '.join(invalidAttrs), max = 50),
                        ),
                    }[self._lang])
                else:
                    err = Exception({
                        'fr': "{label} est d'un type invalide".format(
                            label = labelSTR,
                        ),
                        'en': "{label} is of an invalid type".format(
                            label = labelSTR,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__types = {
            'name': 'types',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Array,
        }
    def types(self, *values: list):
        self._types = list(
            filter(
                lambda type: checkIfCorrectTypeSchema(type),
                values,
            ),
        ) if type(values) in (list, tuple) else None
        if self._types is not None:
            self._types = [value.label(f"{self.get_label()}") for indexValue, value in enumerate(self._types)]
        # print("> JON.schemas | Array - types - self._types:: ", self._types)

        self.typesRule()

        return self
    def getTypes(self,):
        return self._types

    def min(self, minValue: int):
        def initFunct(value: any):
            self._minValue = minValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None
            
            # print("> JON.schemas | Object - min - ruleFunct - value:: ", value)

            valid = True if (
                (
                    value is None or (
                        type(value) in (list, tuple) and
                        len(value) >= minValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._maxValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "the size of {label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être au minimum {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                        'en': "the size of {label} must be at least {min}".format(
                            label = labelSTR,
                            min = minValue,
                            max = self._maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__min = {
            'name': 'min',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def max(self, maxValue: int):
        def initFunct(value: any):
            self._maxValue = maxValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) in (list, tuple) and
                        len(value) <= maxValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._minValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être compris entre {min} et {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                        'en': "the size of {label} must be between {min} and {max}".format(
                            label = labelSTR,
                            min = self._minValue,
                            max = maxValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être au maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                        'en': "the size of {label} must be maximum {max}".format(
                            label = labelSTR,
                            max = maxValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__max = {
            'name': 'max',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def less(self, lessValue: int):
        def initFunct(value: any):
            self._lessValue = lessValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) in (list, tuple) and
                        len(value) < lessValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._greaterValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être inferieure à {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less}".format(
                            label = labelSTR,
                            less = lessValue,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__less = {
            'name': 'less',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def greater(self, greaterValue: int):
        def initFunct(value: any):
            self._greaterValue = greaterValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) in (list, tuple) and
                        len(value) > greaterValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                if(
                    self._lessValue is not None
                ):
                    err = ({
                        'fr': "la taille de {label} doit être inférieure à {less} et superieure à {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                        'en': "the size of {label} must be less than {less} and greater than {greater}".format(
                            label = labelSTR,
                            less = self._lessValue,
                            greater = greaterValue,
                        ),
                    }[self._lang])
                else:
                    err = ({
                        'fr': "la taille de {label} doit être supérieur à {greater}".format(
                            label = labelSTR,
                            greater = greaterValue,
                        ),
                        'en': "the size of {label} must be greater than {greater}".format(
                            label = labelSTR,
                            greater = self._greaterValue,
                        ),
                    }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__greater = {
            'name': 'greater',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self
    def length(self, lengthValue: int):
        def initFunct(value: any):
            self._lengthValue = lengthValue
            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        type(value) in (list, tuple) and
                        len(value) == lengthValue
                    )
                ) and (
                    self._rule__init is not None
                )
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                
                err = ({
                    'fr': "la taille de {label} doit être égale à {length}".format(
                        label = labelSTR,
                        length = lengthValue,
                    ),
                    'en': "the size of {label} must be equal to {length}".format(
                        label = labelSTR,
                        length = self._lengthValue,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__length = {
            'name': 'length',
            'init': initFunct,
            'rule': ruleFunct,
            'schema': String,
        }

        return self

class AnyType(JONDefaultSchema):

    def __init__(self, lang: str = 'fr'):
        super().__init__(lang)
        self.init()
        # print('-- JON - AnyType --')

    def JONAnyTypeValidator(self, value: any) -> dict:
        resValidator_ = self.JONvalidator(value)
        return resValidator_
    def validator(self, value: any) -> dict:
        return self.JONAnyTypeValidator(value)

    def init(self,):
        self._options['validationType'] = 'any'
        self._options['type'] = bool
        self._options['instance'] = Any
        self.set_label_type({
            'fr': 'Booleen',
            'en': 'Boolean'
        }[self._lang])

        self.initRule()

    def initRule(self,):
        def sanitizeFunct(value: any) -> str:

            return value
        def ruleFunct(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            valid = True

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())

                # if self.get_error() is None:
                err = Exception({
                    'fr': "{label} est d'un type invalide".format(
                        label = labelSTR,
                    ),
                    'en': "{label} is of an invalid type".format(
                        label = labelSTR,
                    ),
                }[self._lang])
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__init = {
            'name': 'init',
            'sanitize': sanitizeFunct,
            'rule': ruleFunct,
            'schema': Boolean,
        }

class Clone :
    _target: str = None
    _lang: str = 'fr'

    def __init__(self, target: str, lang: str = 'fr') -> None:
        self._lang = getLang(lang)

        self._target = target

    def getTarget(self,):
        return self._target
    def setTarget(self, target: str):
        self._target = target if (
            type(target) == str and
            len(target) > 0
        ) else None