from typing import *
import asyncio
import logging
import traceback
import sys
import json
import copy
from copy import deepcopy
from .utils import getLang

log = logging.getLogger(__name__)

def InitialMapFunct(value: any):
    return value

def cleanField(value: str, max: int = 15, reverse: bool = False):
    reverse = reverse if type(reverse) == bool else False
    max = max if (
        type(max) == int and
        max > 0
    ) else 15
    res = str(value)
    if len(res) > max:
        res = f"...{res[max:]}" if reverse else f"{res[:max]}..."
    return res
def defaultMapError( value, error, ruleName = None, label = None, lang = 'fr' ):
    res = error
    # print("\n>----------------------")
    # print("-- JON - defaultMapError | error:: ", error)
    # print("-- JON - defaultMapError | value:: ", value)
    # print("-- JON - defaultMapError | ruleName:: ", ruleName)
    # print("-- JON - defaultMapError | label:: ", label)
    # print("-- JON - defaultMapError | lang:: ", lang)
    # print("\n")
    # print("-- JON - defaultMapError | error:: ", error)
    # print("-- JON - defaultMapError | res:: ", res)
    # print("-------------------------<")
    return res
def ValidatorElement(
    valueVE: any,
    rule,
    customError: Exception = None,
    errorMsgs: dict = {},
    label: str = None,
    lang: str = 'fr',
    mapError: any = defaultMapError,
):
    try:
        import inspect
        mapError = mapError if (
            callable(mapError) and 
            len((inspect.getfullargspec(mapError)).args) <= 5
        ) else defaultMapError
        errorMsgs = {keyValue: value for keyValue, value in list(
            map(
                lambda keyDt: [keyDt, errorMsgs[keyDt]],
                list(
                    filter(
                        lambda keyDt: (
                            (
                                type(errorMsgs[keyDt]) == str and
                                len(errorMsgs[keyDt]) > 0
                            ) or
                            isinstance(type(errorMsgs[keyDt]), Exception) or
                            issubclass(type(errorMsgs[keyDt]), Exception)
                        ),
                        tuple(errorMsgs.keys()),
                    )
                ),
            )
        )} if type(errorMsgs) == dict else {}
        resVE = valueVE
        
        if(
            (
                rule is not None and
                type(rule) == dict
            ) and resVE['valid'] == True
        ):
            if(
                'init' in rule.keys() and
                rule['init'] and
                callable(rule['init']) and
                rule['init'] is not None
            ):
                resVE['data'] = rule['init'](resVE['data'])
            if(
                'rule' in rule.keys() and
                rule['rule'] and
                callable(rule['rule']) and
                rule['rule'] is not None
            ):
                resVE = rule['rule'](resVE['data'])
            resVE['data'] = rule['sanitize']( resVE['data']) if (
                type(rule) == dict and
                'sanitize' in rule.keys() and
                rule['sanitize'] and
                callable(rule['sanitize']) and
                rule['sanitize'] is not None
            ) else  resVE['data']
            # print("-- JON - ValidatorElement | resVE['data']:: ", resVE['data'])
            # resVE['data'] = removeAttributesOfObject(resVE['data'])

        # print("-- JON - ValidatorElement | errorMsgs:: ", errorMsgs)
        if (
            customError is not None and
            type(customError) == Exception and
            'error' in tuple(resVE.keys()) and
            resVE['error'] is not None
        ):
            resVE['error'] = str(customError)
        elif(
            'error' in tuple(resVE.keys()) and
            resVE is not None and
            type(rule) == dict and
            'name' in tuple(rule.keys()) and
            rule['name'] is not None and
            str(rule['name']).upper() in tuple(errorMsgs.keys()) and
            type(errorMsgs[str(rule['name']).upper()]) == Exception
        ):
            resVE['error'] = str(errorMsgs[str(rule['name']).upper()])
        if(
            resVE['error'] is not None and
            rule is not None
        ):
            errorSubMessage = {
                'fr': f"la valeur qui génère l'erreur: `{cleanField(valueVE['data'])}`",
                'en': f"the value generating the error: `{cleanField(valueVE['data'])}`",
            }[lang]
            errorSubMessage = ''#'\n'# + errorSubMessage
            resVE['error'] = f"{str(resVE['error'])}{errorSubMessage}"
            mapErrorLength = len((inspect.getfullargspec(mapError)).args)
            # print("-- JON - ValidatorElement | mapErrorLength:: ", mapErrorLength)
            resVE['error'] = mapError(
                valueVE['data'],
                resVE['error'],
                str(rule['name']).upper(),
                label,
                lang
            )

        return resVE
    except Exception as err:
        stack = traceback.format_exc()
        log.error(stack)
        return {
            'data': None,
            'valid': False,
            'error': 'unknown error',
        }

class JONDefaultSchema():
    '''
    JONDefaultSchema est la super class 'schema' permettant la validation des données sous JON
    '''
    _label__type: str = 'default'
    _label: str = None
    _lang: str = 'fr'
    _options: dict = {
        'validationType': 'any',
        'type': 'any',
        'instance': None,
        'rules': [],
    }
    _defaultValue = None
    _finalError: Exception = None
    _customError: Exception = None
    map = None
    preMap = None
    
    _mapError = {
        'map': defaultMapError,
    }
    _errMsgs = None

    _rule__init = None
    _rule__required = None
    _rule__enum = None
    _rule__enumNot = None
    _rule__applyApp = None
    _rule__applyApp2 = None
    _rule__applyApp3 = None
    _rule__applyApp4 = None
    _rule__applyApp5 = None
    _rule__applyApp6 = None
    _rule__applyApp7 = None
    _rule__applyApp8 = None
    _rule__applyApp9 = None
    _rule__applyApp10 = None
    _rule__applyApp11 = None
    _rule__applyApp12 = None
    _rule__applyApp13 = None
    _rule__applyApp14 = None
    _rule__applyApp15 = None
    _rule__applyApp16 = None
    _rule__applyApp17 = None
    _rule__applyApp18 = None
    _rule__applyApp19 = None
    _rule__applyApp20 = None

    def __init__(self, lang: str = 'fr'):
        self.set_lang(lang)
        self.set_finalError()
        # print(('-- JONDefaultSchema --')
        # print(('-- JONDefaultSchema | self._lang:: ', self._lang)


    def JONApplyAppValidator(self,
        resValidator_: any
    ) -> dict:
        '''
        Cette fonction d'ajouter des fonctions supplementaires de validation

            Parameters:
                resValidator_ (dict): autre reponse de validation

            Returns:
                dict: La reponse de la fonction
        '''
        try:
            # if resValidator_['data'] is not None and type(resValidator_['data']) == bool:
            #     print("> JONschemas | JONApplyAppValidator - resValidator_:: ", resValidator_)
            # --<- applyApp
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp2
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp2, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp3
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp3, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp4
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp4, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp5
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp5, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp6
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp6, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp7
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp7, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp8
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp8, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp9
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp9, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp10
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp10, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp11
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp11, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp12
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp12, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp13
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp13, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp14
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp14, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp15
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp15, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp16
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp16, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp17
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp17, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp18
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp18, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp19
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp19, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- applyApp20
            resValidator_ = ValidatorElement(resValidator_, customError=self._customError, rule=self._rule__applyApp20, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
        except Exception as err:
            stack = traceback.format_exc()
            resValidator_ = {
                'data': None,
                'valid': False,
                'error': str(stack),
            }
            
            log.error(stack)

        # print("> JONschemas | JONDefaultSchema - JONApplyAppValidator - resValidator_:: ", resValidator_)
        return resValidator_
    def JONvalidator(self,
        value: any
    ) -> dict:
        '''
        Cette fonction permet d'appliquer des fonctions de validation par defaut de JON

            Parameters:
                value (any): element à valider

            Returns:
                dict: La reponse de la fonction
        '''
        # value = deepcopy(value)
        resValidator = {
            'data': None,
            'valid': None,
            'error': None
        }

        try:
            if(value is None):
                value = self._defaultValue
            # print("> JONDefaultSchema.JONvalidator ", self.get_label(), " self._defaultValue : ", self._defaultValue)
            # print("> JONDefaultSchema.JONvalidator ", self.get_label(), " value : ", value)
            if(self._rule__init is not None and type(self._rule__init) == dict):
                if(
                    'init' in self._rule__init.keys() and
                    self._rule__init['init'] and
                    callable(self._rule__init['init'])
                ):
                    resValidator['data'] = self._rule__init['init'](value)
                else:
                    resValidator['data'] = value
                resValidator = self._rule__init['rule'](resValidator['data'])
                resValidator['data'] = self._rule__init['sanitize']( resValidator['data']) if (
                    'sanitize' in self._rule__init.keys() and
                    callable(self._rule__init['sanitize'])
                ) else  resValidator['data']
            # --> OTHERS RULES
            # --<- required
            resValidator = ValidatorElement(resValidator, customError=self._customError, rule=self._rule__required, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            """if(
                'init' in self._rule__required.keys() and
                self._rule__required['init'] and
                callable(self._rule__required['init'])
            ):
                resValidator['data'] = self._rule__required['init'](resValidator['data'])
            resValidator = self._rule__required['rule'](resValidator['data'])
            resValidator['data'] = self._rule__required['sanitize']( resValidator['data']) if (
                type(self._rule__required) == dict and
                'sanitize' in self._rule__required.keys() and
                self._rule__required['sanitize'] and
                callable(self._rule__required['sanitize'])
            ) else  resValidator['data']"""
            # --<- enum
            resValidator = ValidatorElement(resValidator, customError=self._customError, rule=self._rule__enum, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())
            # --<- enumNot
            resValidator = ValidatorElement(resValidator, customError=self._customError, rule=self._rule__enumNot, errorMsgs=self._errMsgs, label=self.get_label(), lang = self._lang, mapError=self.getMapError())

            if(resValidator['valid'] is None):
                resValidator = {
                    'data': None,
                    'valid': False,
                    'error': str({
                        'fr': "aucune règle n'est appliquée",
                        'en': "no rule is applied",
                    }[self._lang]),
                }
        except Exception as err:
            stack = traceback.format_exc()
            resValidator = {
                'data': None,
                'valid': False,
                'error': str(stack),
            }
            
            log.error(stack)

        # print("> JONschemas | JONDefaultSchema - JONvalidator - resValidator:: ", resValidator)

        return resValidator
    def validator(self,
        value: any
    ) -> dict:
        '''
        Cette fonction permet d'appliquer des fonctions de validation par defaut de JON (Utilise la fonction 'JONvalidator')

            Parameters:
                value (any): element à valider

            Returns:
                dict: La reponse de la fonction
        '''
        # value = deepcopy(value)
        return self.JONvalidator(value)
    def validate(self, value: any) -> dict :
        '''
        Cette fonction permet d'appliquer des fonctions de validation par defaut de JON applicable sur des types de données specifiques

            Parameters:
                value (any): element à valider

            Returns:
                dict: La reponse de la fonction
        '''
        # value = deepcopy(value)
        try:
            # self.init()
            # print("""> JONschemas | JONDefaultSchema - validate - self._options['validationType']:: """, self._options['validationType'])
            # print("""> JONschemas | JONDefaultSchema - validate - self._options['type']:: """, self._options['type'])
            # print("""> JONschemas | JONDefaultSchema - validate - self._options['instance']:: """, self._options['instance'])
            # print("""> JONschemas | JONDefaultSchema - validate - self._options['rules']:: """, self._options['rules'])

            if(self._options['validationType'] in ['any', 'number', 'string', 'boolean', 'date', 'file', 'enum', 'notInEnum', 'chosenType', 'NoInChosenType', 'object']):
                if(self.preMap is not None and callable(self.preMap)):
                    value = self.preMap(value)
                resV = self.validator(value)
                # if type(resV['data']) == bool:
                #     print("""> JONschemas | JONDefaultSchema - validate - self.validator(value):: """, resV)
                resV = self.JONApplyAppValidator(resV)
                # print("""> JONschemas | JONDefaultSchema - validate - self.JONApplyAppValidator(deepcopy(resV)):: """, resV)
                resV['data'] = None if (
                    (
                        (
                            type(resV['data']) == dict and
                            len(resV['data'].keys()) <= 0
                        ) or 
                        (
                            type(resV['data']) in (list, tuple) and
                            len(resV['data']) <= 0
                        )
                    ) and not(resV['valid'] == True)
                ) else resV['data']
                # resV['error'] = str(resV['error']) if resV['error'] is not None else None
                resV['error'] = resV['error'] if resV['error'] is not None else None
                if(resV['valid'] == True and self.map is not None and callable(self.map)):
                    # print("---- ICI ----")
                    resV['data'] = self.map(resV['data'])
                return resV

            return {
                'data': None,
                'valid': False,
                'error': str(self.get_error()),
            }
        except Exception as err:
            code = str(type(err))
            msg = str(err)
            stack = str(traceback.format_exc())
            
            log.error(stack)
            return {
                'data': None,
                'valid': False,
                'error': 'unknown error during validation',
            }

    def ruleNames(self,) -> list:
        '''
        Cette fonction retourne l'ensemble des regles (noms) applicables à un schema JON

            Returns:
                'tuple|list': La reponse de la fonction
        '''
        return list(
            map(
                lambda data: data['name'],
                self._options['rules'],
            )
        )
        

    def error(self, value: any) -> Exception:
        '''
        Cette fonction retourne l'erreur survenue apres une validation à l'aide d'un schema JON

            Parameters:
                value (any): element à valider

            Returns:
                Exception: La reponse de la fonction
        '''
        return (self.validate(value))['error']
    def isValid(self, value: any) -> bool :
        '''
        Cette fonction verifie si un element à valider à l'aide d'un schema JON respecte les regles du dit schema.

            Parameters:
                value (any): element à valider

            Returns:
                bool: La reponse de la fonction
        '''
        return (self.validate(value))['valid']
    def sanitize(self, value: any) -> any :
        '''
        Cette fonction la donnée nettoyée apres une validation à l'aide d'un schema JON

            Parameters:
                value (any): element à valider

            Returns:
                any: La reponse de la fonction
        '''
        return (self.validate(value))['data']

    def get_rules(self,):
        '''
        Cette fonction retourne l'ensemble des regles applicables à un schema JON

            Returns:
                'tuple|list': La reponse de la fonction
        '''
        return self._options['rules']
    def set_rules(self, rules: list):
        '''
        Ce setter permet d'ajouter un nouvel ensemble de regles applicables à un schema JON

            Parameters:
                rules ('list|tuple'): nouvelles regles
        '''
        self._options['rules'] = rules
    def get_label_type(self,):
        '''
        Ce getter retourne le nom du schema JON

            Returns:
                str: La reponse de la fonction
        '''
        return self._label__type
    def set_label_type(self, label: str):
        '''
        Ce setter modifie le nom du schema JON

            Parameters:
                label (str): nouveau nom
        '''
        self._label__type = label
    def get_lang(self,):
        '''
        Ce getter retourne la langue utilisée par un schema JON

            Returns:
                str: La reponse de la fonction
        '''
        return self._lang
    def set_lang(self, lang: str):
        '''
        Ce setter modifie la langue utilisée par un schema JON

            Parameters:
                lang (str): langue
        '''
        self._lang = getLang(lang)
    def get_label(self,):
        '''
        Ce setter retourne le label du schema JON

            Returns:
                str: La reponse de la fonction
        '''
        labelF = self._label if (
            type(self._label) in [str] and
            len(self._label) > 0
        ) else {
            'fr': 'l\'element',
            'en': 'the element'
        }[self._lang]
        return cleanField(labelF, max = 30, reverse = True)
    def set_label(self, label: any):
        '''
        Ce setter permet de modifier le label d'un schema JON

            Parameters:
                label (any): nouveau label
        '''
        self._label = label if (
            type(label) in [str] and
            len(label) > 0
        ) else None
    def get_error(self,):
        '''
        Ce getter retourne l'erreur generée lors d'une validation

            Returns:
                Exception: La reponse de la fonction
        '''
        if self._customError is not None :
            return self._customError
        return self._finalError
        # if self._finalError is not None :
        #     return self._finalError
        # return self._customError
    def set_finalError(self, finalError: any = None):
        '''
        Ce setter permet de modifier l'erreur generée en cas d'une exception inconnue ou non definie

            Parameters:
                finalError (any): message d'erreur
        '''
        try:
            self._finalError = Exception(
                finalError[self._lang] if(
                    type(finalError) == dict and
                    self._lang in finalError.keys()
                ) else finalError
            ) if type(finalError) is not Exception else finalError
        except:
            self._finalError = Exception(
                {
                    'fr': 'erreur interne inconnue',
                    'en': 'unknown internal error',
                }[self._lang]
            )
    def set_error(self, errorValue: any = None):
        '''
        Ce setter permet de definir une erreur à afficher en cas de resultat negatif lors d'une validation

            Parameters:
                erreur ('dict|str'): message d'ereur
        '''
        try:
            self._customError = Exception(
                errorValue[self._lang] if(
                    type(errorValue) == dict and
                    self._lang in errorValue.keys()
                ) else errorValue
            )
        except:
            self._customError = Exception(
                {
                    'fr': 'erreur interne inconnue',
                    'en': 'unknown internal error',
                }[self._lang]
            ) if type(errorValue) is not Exception else errorValue
    def get_customError(self,):
        '''
        Ce getter permet de retourner l'erreur de base

            Returns:
                Exception: La reponse de la fonction
        '''
        return self._customError
            
    def get_defaultValue(self,):
        '''
        Ce getter retourne la valeur par defaut si l'element à valider est undefini ou nul

            Returns:
                any: La reponse de la fonction
        '''
        return self._defaultValue
    def set_defaultValue(self, defaultValue: any):
        '''
        Ce setter definie la valuer par defaut de l'element à valider

            Parameters:
                defaultValue (any): valeur par defaut de l'element à valider
        '''
        self._defaultValue = defaultValue

    def label_type(self, label: str):
        '''
        Ce setter modifie le nom du schema JON

            Parameters:
                label (str): nouveau nom
        '''
        self.set_label_type(label)
        return self
    def lang(self, value: str):
        '''
        Cette fonction definit la langue qui sera utilisée par le schema JON

            Parameters:
                value (str): id de la langue ('fr' ou 'en')
        '''
        self.set_lang(value)
        return self
    def label(self, value: any):
        '''
        Cette fonction definit le label du schema JON

            Parameters:
                value (str): nouveau label
        '''
        self.set_label(value)
        return self
    def default(self, value: any):
        '''
        Cette fonction definit la valeur par defaut que prendra l'element à valider s'il est indefini ou null

            Parameters:
                value (any): valeur par defaut
        '''
        self.set_defaultValue(value)
        return self
    def defaultError(self, defaultErr: any):
        '''
        Cette fonction permet de definir le message d'erreur par defaut qui sera retourné après validation negative

            Parameters:
                defaultErr (any): element à valider
        '''
        self.set_error(defaultErr)
        # self.set_finalError(defaultErr)
        # print("> JONschemas | defaultSchema - set_error - self._customError:: ", self._customError)
        # print("> JONschemas | defaultSchema - set_error - self._finalError:: ", self._finalError)
        return self
    def required(self, isRequired: bool = True):
        '''
        Cette regle verifie si l'element à valider n'est pas null ou indefini
            Parameters:
                isRequired: Valeur determinant si elle est requise ou pas

            Returns:
                self: La classe de validation
        '''
        isRequired = isRequired if type(isRequired) == bool else True
        def ruleFunct(value: any) -> dict:
            '''
            Fonction de validation de la regle

                Parameters:
                    value (any): element à valider

                Returns:
                    dict: resultat de la fonction
            '''
            data: any = None
            valid: bool = False
            error: any = None
            
            valid = (
                value is not None
            )

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
    def enum(self, *choices: any):
        '''
        Cette regle verifie si l'element à valider se trouve dans les choix predefinis

            Parameters:
                choices ('list|tuple'): les choix de validation

            Returns:
                self: La classe de validation
        '''
        choices = choices if type(choices) in (list, tuple) else None
        choiceIsNone = choices is None
        def ruleFunct(value: any) -> dict:
            '''
            Fonction de validation de la regle

                Parameters:
                    value (any): element à valider

                Returns:
                    dict: resultat de la fonction
            '''
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        value in choices
                    )
                ) and (
                    self._rule__init is not None
                ) and not(choiceIsNone == True)
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} correspond à aucun choix défini".format(
                        label = labelSTR,
                    ),
                    'en': "{label} correspond to any defined choice".format(
                        label = labelSTR,
                    ),
                })
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__enum = {
            'name': 'enum',
            'rule': ruleFunct,
            'schema': self._options['instance'],
        }

        return self
    def enumNot(self, *choices: any):
        '''
        Cette regle verifie si l'element à valider ne se trouve pas dans les choix predefinis

            Parameters:
                choices ('list|tuple'): les choix de validation

            Returns:
                self: La classe de validation
        '''
        choices = choices if type(choices) in (list, tuple) else []
        choiceIsNone = choices is None
        def ruleFunct(value: any) -> dict:
            '''
            Fonction de validation de la regle

                Parameters:
                    value (any): element à valider

                Returns:
                    dict: resultat de la fonction
            '''
            data: any = None
            valid: bool = False
            error: any = None

            valid = True if (
                (
                    value is None or (
                        not(value in choices)
                    )
                ) and (
                    self._rule__init is not None
                ) and not(choiceIsNone == True)
            ) else False

            if(valid == True):
                error = None
                data = value
            else:
                labelSTR = json.dumps(self.get_label())
                err = Exception({
                    'fr': "{label} ne correspond à aucun choix défini".format(
                        label = labelSTR,
                    ),
                    'en': "{label} does not correspond to any defined choice".format(
                        label = labelSTR,
                    ),
                })
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        self._rule__enumNot = {
            'name': 'enumNot',
            'rule': ruleFunct,
            'schema': self._options['instance'],
        }

        return self
    
    def getMapError(self, ):
        self._mapError = self._mapError if (
            type(self._mapError) == dict
        ) else {}
        return self._mapError['map'] if (
            'map' in tuple(self._mapError.keys())
        ) else defaultMapError
    def initMapError(self,
        mapError: any                 
    ):
        import inspect
        self._mapError = self._mapError if (
            type(self._mapError) == dict
        ) else {}
        self._mapError['map'] = mapError if (
            callable(mapError) and 
            len((inspect.getfullargspec(mapError)).args) <= 5
        ) else defaultMapError
        return self
    def initExceptions(self,
        msgs: dict,
    ):
        # print("> JONschemas | defaultSchema - initExceptions - msgs OLD:: ", msgs)
        msgs = {keyValue: value for keyValue, value in list(
            map(
                lambda keyDt: [keyDt, Exception(msgs[keyDt])],
                list(
                    filter(
                        lambda keyDt: (
                            (
                                type(msgs[keyDt]) == str and
                                len(msgs[keyDt]) > 0
                            ) or
                            isinstance(type(msgs[keyDt]), Exception) or
                            issubclass(type(msgs[keyDt]), Exception)
                        ),
                        tuple(msgs.keys()),
                    )
                ),
            )
        )} if type(msgs) == dict else {}
        # print("> JONschemas | defaultSchema - initExceptions - msgs:: ", msgs)
        self._errMsgs = self._errMsgs if type(self._errMsgs) == dict else {}
        self._errMsgs = {
            **self._errMsgs,
            **msgs,
        }
        # print("> JONschemas | defaultSchema - initExceptions - self._errMsgs:: ", self._errMsgs)
        return self


    def applyAppInit(self,
        name: str = 'applyApp',
        init = (lambda data: data),
        rule = (lambda data: not(not(data))),
        sanitize = (lambda data: data),
        exception = None
    ):
        '''
        Cette fonction permet de definir une regle personnalisée

            Parameters:
                name (str): le nom de la regle
                init (any): la fonction d'initialisation
                rule (any): la fonction de validation de la regle
                sanitize (any): la fonction nettoyage apres validation positive
                exception ('dict|str'): l'exception de la regle

            Returns:
                self: La classe de validation
        '''
        if type(exception) == dict and self._lang in exception.keys():
            exception = exception[self._lang]
        if type(exception) == str:
            exception = Exception(exception)
                
        def ruleF(value: any) -> dict:
            data: any = None
            valid: bool = False
            error: any = None

            # print("> JONschemas | defaultSchema - applyAppInit - ruleF - value:: ", value)
            # print("> JONschemas | defaultSchema - applyAppInit - ruleF - rule:: ", rule)
            # print("> JONschemas | defaultSchema - applyAppInit - ruleF - value['password']:: ", value['password'])
            # print("> JONschemas | defaultSchema - applyAppInit - ruleF - value['confirmpassword']:: ", value['confirmpassword'])
            # print("> JONschemas | defaultSchema - applyAppInit - ruleF - (value['password'] == value['confirmpassword']):: ", (value['password'] == value['confirmpassword']))

            valid = True if (
                (
                    value == None or (
                        callable(rule) and
                        rule(value) == True
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
                err = (Exception({
                    'fr': "la condition appliquéé à {label} est invalide".format(
                        label = labelSTR,
                    ),
                    'en': "the condition applied to {label} is invalid".format(
                        label = labelSTR,
                    ),
                }) if exception is None else exception)
                error = err
                data = None

            return {
                'data': data,
                'valid': valid,
                'error': error,
            }

        return {
            'name': name if (
                type(name) == str and
                len(name) > 0
            ) else 'applyApp',
            'rule': ruleF,
            'sanitize': sanitize if callable(sanitize) else None,
            'init': init if callable(init) else None,
        }
    def applyApp(self,
        name: str = 'applyApp',
        init = (lambda data: data),
        rule = (lambda data: not(not(data))),
        sanitize = (lambda data: data),
        exception = None
    ):
        '''
        Cette fonction permet de definir la premiere regle personnalisée

            Parameters:
                name (str): le nom de la regle
                init (any): la fonction d'initialisation
                rule (any): la fonction de validation de la regle
                sanitize (any): la fonction nettoyage apres validation positive
                exception ('dict|str'): l'exception de la regle

            Returns:
                self: La classe de validation
        '''
        self._rule__applyApp = self.applyAppInit(
            name=name,
            init=init,
            rule=rule,
            sanitize=sanitize,
            exception=exception,
        )

        return self
    def applyApp2(self,
        name: str = 'applyApp2',
        init = (lambda data: data),
        rule = (lambda data: not(not(data))),
        sanitize = (lambda data: data),
        exception = None
    ):
        '''
        Cette fonction permet de definir la deuxieme regle personnalisée

            Parameters:
                name (str): le nom de la regle
                init (any): la fonction d'initialisation
                rule (any): la fonction de validation de la regle
                sanitize (any): la fonction nettoyage apres validation positive
                exception ('dict|str'): l'exception de la regle

            Returns:
                self: La classe de validation
        '''
        self._rule__applyApp2 = self.applyAppInit(
            name=name,
            init=init,
            rule=rule,
            sanitize=sanitize,
            exception=exception,
        )

        return self
    def applyApp3(self,
        name: str = 'applyApp3',
        init = (lambda data: data),
        rule = (lambda data: not(not(data))),
        sanitize = (lambda data: data),
        exception = None
    ):
        '''
        Cette fonction permet de definir la troisième regle personnalisée

            Parameters:
                name (str): le nom de la regle
                init (any): la fonction d'initialisation
                rule (any): la fonction de validation de la regle
                sanitize (any): la fonction nettoyage apres validation positive
                exception ('dict|str'): l'exception de la regle

            Returns:
                self: La classe de validation
        '''
        self._rule__applyApp3 = self.applyAppInit(
            name=name,
            init=init,
            rule=rule,
            sanitize=sanitize,
            exception=exception,
        )

        return self
    def applyApp4(self,
        name: str = 'applyApp4',
        init = (lambda data: data),
        rule = (lambda data: not(not(data))),
        sanitize = (lambda data: data),
        exception = None
    ):
        '''
        Cette fonction permet de definir la quatrième regle personnalisée

            Parameters:
                name (str): le nom de la regle
                init (any): la fonction d'initialisation
                rule (any): la fonction de validation de la regle
                sanitize (any): la fonction nettoyage apres validation positive
                exception ('dict|str'): l'exception de la regle

            Returns:
                self: La classe de validation
        '''
        self._rule__applyApp4 = self.applyAppInit(
            name=name,
            init=init,
            rule=rule,
            sanitize=sanitize,
            exception=exception,
        )

        return self
    def applyApp5(self,
        name: str = 'applyApp5',
        init = (lambda data: data),
        rule = (lambda data: not(not(data))),
        sanitize = (lambda data: data),
        exception = None
    ):
        '''
        Cette fonction permet de definir la dernière regle personnalisée

            Parameters:
                name (str): le nom de la regle
                init (any): la fonction d'initialisation
                rule (any): la fonction de validation de la regle
                sanitize (any): la fonction nettoyage apres validation positive
                exception ('dict|str'): l'exception de la regle

            Returns:
                self: La classe de validation
        '''
        self._rule__applyApp5 = self.applyAppInit(
            name=name,
            init=init,
            rule=rule,
            sanitize=sanitize,
            exception=exception,
        )

        return self

    def applyPreMapping(self, map = InitialMapFunct):
        '''
        Cette fonction permet d'appliquer un mapping personnalisé avant les etapes de validations

            Parameters:
                map (any): fonction de mapping

            Returns:
                self: La classe de validation
        '''
        self.preMap = map
        return self
    def applyMapping(self, map = InitialMapFunct):
        '''
        Cette fonction permet d'appliquer un mapping personnalisé après une validation positive

            Parameters:
                map (any): fonction de mapping

            Returns:
                self: La classe de validation
        '''
        self.map = map
        return self