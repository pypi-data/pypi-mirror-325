import re
import json
from functools import reduce
import datetime

from .config import DEBUG, dateTimeFormatInitial, timeFormatInitial, dateFormatInitial


currentLang = 'en'
langs = ['en', 'fr']

def getLang(lang, debug = DEBUG):
    debug = debug if type(debug) == bool else DEBUG
    result = lang
    result = result if result in langs else 'fr'
    return result

def CleanName(
    value: str,
    sep: str = '_',
    regExp: str = r"[^a-zA-Z0-9_]",
    debug = DEBUG,
) -> str:
    '''
    Cette fonction permet de nettoyer un string en enlevant tous les caracteres non-alphanumeriques

        Parameters:
            value (str): element à nettoyer
            sep (str): separateur

        Returns:
            JON.Object: La reponse de la fonction
    '''
    debug = debug if type(debug) == bool else DEBUG
    if(not(
        type(value) in (str, int, float) and
        type(sep) in (str, int, float)
    )):
        return None
    value = str(value)
    sep = str(sep)
    res = sep.join(
        list(
            filter(
                lambda x: len(x) > 0,
                re.sub(
                    re.compile(regExp, re.MULTILINE),
                    sep,
                    value,
                ).split(sep),
            )
        )
    ) if len(value) > 0 else None
    return res

def preMapLoopData(
    data: any,
    parents: 'list | tuple',
    parent: 'str | int',
    debug = DEBUG,
):
    '''
    Cette fonction permet de prémapper la donnée qui devra ensuite être mappée ou pour un objet ou une liste des attributs enfants

        Parameters:
            data (any): donnée à mapé
            parents ('list | tuple'): l'ensemble des clés des parents de l'element
            parent ('str | int'): la clé du parent direct de l'element

        Returns:
            'any | list | dict': La reponse de la fonction
    '''
    debug = debug if type(debug) == bool else DEBUG
    return data
def mapLoopData(
    res: any,
    data: any,
    parents: 'list | tuple',
    parent: 'str | int',
    debug = DEBUG,
):
    '''
    Cette fonction permet de mapper la donnée ou pour un objet ou une liste des attributs enfants

        Parameters:
            data (any): donnée à parcourir
            parents ('list | tuple'): l'ensemble des clés des parents de l'element
            parent ('str | int'): la clé du parent direct de l'element

        Returns:
            'any | list | dict': La reponse de la fonction
    '''
    debug = debug if type(debug) == bool else DEBUG
    return res

def loopData2(
    data: any,
    parents: 'list | tuple' = None,
    mapFnc = mapLoopData,
    preMapFnc = preMapLoopData,
    debug = DEBUG,
):
    '''
    Cette fonction permet de parcourir une variable et d'appliquer des actions en fonction du type

        Parameters:
            data (any): donnée à parcourir
            parents ('list | tuple'): l'ensemble des clés des parents de l'element
            mapFnc (def): la fontion de mappage de la donnée ou pour un objet ou une liste des attributs enfants
            preMapFnc (def): la fontion de prémappage de la donnée qui devra ensuite être mappée ou pour un objet ou une liste des attributs enfants

        Returns:
            'any | list | dict': La reponse de la fonction
    '''
    debug = debug if type(debug) == bool else DEBUG
    preMapFnc = preMapFnc if(preMapFnc is not None and callable(preMapFnc)) else preMapLoopData
    mapFnc = mapFnc if(mapFnc is not None and callable(mapFnc)) else mapLoopData
    
    if(type(data) in (list, tuple, dict, int, float, bool, str) or data is None):
        parents = parents if type(parents) in (list, tuple) else []
        parent = parents[len(parents) - 1] if len(parents) > 0 else None

        data = preMapFnc(
            data = data,
            parents = parents,
            parent = parent,
        )
        res = data
        res = mapFnc(
            res = res,
            data = data,
            parents = parents,
            parent = parent,
        )
        if type(data) == dict:
            res = {key: loopData2(
                data = value,
                parents = [
                    *parents,
                    key,
                ],
                mapFnc = mapFnc,
                preMapFnc = preMapFnc,
                debug=debug,
            ) for key, value in res.items()}
        elif type(data) in (list, tuple):
            res = [loopData2(
                data = value,
                parents = [
                    *parents,
                    index,
                ],
                mapFnc = mapFnc,
                preMapFnc = preMapFnc,
                debug=debug,
            ) for index, value in enumerate(res)]

        return res
    return data
def loopData(
    data: any,
    parents: 'list | tuple' = None,
    mapFnc = mapLoopData,
    preMapFnc = preMapLoopData,
    initialDirection: bool = True,
    debug = DEBUG,
):
    '''
    Cette fonction permet de parcourir une variable et d'appliquer des actions en fonction du type

        Parameters:
            data (any): donnée à parcourir
            parents ('list | tuple'): l'ensemble des clés des parents de l'element
            mapFnc (def): la fontion de mappage de la donnée ou pour un objet ou une liste des attributs enfants
            preMapFnc (def): la fontion de prémappage de la donnée qui devra ensuite être mappée ou pour un objet ou une liste des attributs enfants

        Returns:
            'any | list | dict': La reponse de la fonction
    '''
    debug = debug if type(debug) == bool else DEBUG
    initialDirection = initialDirection if type(initialDirection) == bool else True
    preMapFnc = preMapFnc if(preMapFnc is not None and callable(preMapFnc)) else preMapLoopData
    mapFnc = mapFnc if(mapFnc is not None and callable(mapFnc)) else mapLoopData

    if(type(data) in (list, tuple, dict, int, float, bool, str) or data is None):
        parents = parents if type(parents) in (list, tuple) else []
        parent = parents[len(parents) - 1] if len(parents) > 0 else None

        # if(not(initialDirection == True)):
        #     data = mapFnc(
        #         res = data,
        #         data = data,
        #         parents = parents,
        #         parent = parent,
        #     )

        if(type(data) in (list, tuple)):
            res = []
            dataAction2 = [*data]
            dataAction2Keys = [*range(0, len(dataAction2), 1)]
            i = 0
            while True:
                if(not(i < len(dataAction2))):
                    break
                indexAction2 = i
                valueAction2 = dataAction2[indexAction2]

                newParents = [
                    *parents,
                    indexAction2,
                ]
                if(not(initialDirection == True) and not(type(valueAction2) in (list, tuple, dict))):
                    valueAction2 = mapFnc(
                        res = valueAction2,
                        data = valueAction2,
                        parents = parents,
                        parent = parent,
                    )
                newValue = loopData(
                    data = valueAction2,
                    parents = newParents,
                    mapFnc = mapFnc,
                    preMapFnc = preMapFnc,
                    debug=debug,
                )
                if(initialDirection and not(type(newValue) in (list, tuple, dict))):
                    newValue = mapFnc(
                        res = newValue,
                        data = valueAction2,
                        parents = parents,
                        parent = parent,
                    )
                    if(debug == True):
                        print('>-- utils | loopData - newValue (array):: ', newValue)
                res.append(newValue)

                i = i + 1
        elif(type(data) == dict):
            res = {}
            dataAction1 = {**data}
            dataAction1Keys = tuple(dataAction1.keys())
            i = 0
            while True:
                if(not(i < len(dataAction1Keys))):
                    break
                keyAction1 = dataAction1Keys[i]
                indexAction1 = i
                valueAction1 = dataAction1[keyAction1]

                newParents = [
                    *parents,
                    keyAction1,
                ]
                if(not(initialDirection == True) and not(type(valueAction1) in (list, tuple, dict))):
                    valueAction1 = mapFnc(
                        res = valueAction1,
                        data = valueAction1,
                        parents = parents,
                        parent = parent,
                    )
                newValue = loopData(
                    data = valueAction1,
                    parents = newParents,
                    mapFnc = mapFnc,
                    preMapFnc = preMapFnc,
                    debug=debug,
                )
                
                if(initialDirection and not(type(newValue) in (list, tuple, dict))):
                    newValue = mapFnc(
                        res = newValue,
                        data = valueAction1,
                        parents = parents,
                        parent = parent,
                    )
                    if(debug == True):
                        print('>-- utils | loopData - newValue (dict):: ', newValue)
                res[keyAction1] = newValue

                i = i + 1
        else :
            res = mapFnc(
                res = data,
                data = data,
                parents = parents,
                parent = parent,
            )
            

        if(type(res) in (list, tuple, dict)):
            res = mapFnc(
                res = res,
                data = data,
                parents = parents,
                parent = parent,
            )

        if(debug == True):
            print('\n')
            print('>-- utils | loopData - parents:: ', parents)
            print('>-- utils | loopData - parent:: ', parent)
            print('>-- utils | loopData - data:: ', data)
            print('>-- utils | loopData - res:: ', res)
            print('\n')

        return res
    return data