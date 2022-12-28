def Commence_Par_Majuscule(text):
    """
     Si la chaine "text" commence par une majuscule alors True sinon False
    : param text: string
    : return: Boolean
    """
    result = False
    if len(text) > 0:  # Verifier si la longueur du text est supérieur à zero
        if text[0].isupper():
            result = True

    return result


def Bonne_Ponctuation(text):
    """
    Si le dernier caractère de la chaine est ponctué par un "." ou un " !" ou un "?"
    :param text: string
    :return: Boolean
    """
    result = False
    if text[-1] in ('.', '!', '?'):
        result = True

    return result


def Espace_Validation(car_prev, car_cur, car_find, espace_accepte=False):
    """
    Contrôle de la position correcte des espaces

    :param car_prev: caractère a comparer
    :param car_cur: caractère a comparer
    :param car_find: caractère du contrôle
    :param espace_accepte: Vrai  accepte espace / Faux n'accepte pas les espaces
    :return:

    """

    result = True
    if espace_accepte:  # si j'accepte un espace
        if car_cur in car_find and car_prev != ' ':
            result = False  # le caractère precedent est différent d'espace
    else:  # si je n'accepte pas d'espace
        if car_cur in car_find and car_prev == ' ':
            result = False  # le caractère precedent est un espace

    return result


def Validation_Phrase(text):
    """
    Permet de vérifier les règles de PAO suivante :
        ● La phrase commence par une Majuscule.\n
        ● La phrase se termine par un point.\n
        ● Les mots sont séparés par un et un seul espace, excepté en cas de symbole de ponctuation
        (dans ce cas, on respecte les règles ci-après) :\n
        ● La virgule et le point sont collés au mot qui les précède et sont suivi par un espace.\n
        ● Le point-virgule, les deux points et le point d'interrogation sont entourés d'un espace.\n

    Parameters:
                   text (str): chaine caractères
    :returns:
        - Mess1 - Votre phrase ne commence pas par une Majuscule.
        - Mess2 - Votre phrase ne finis pas par un signe de ponctuation
        - Mess3 - Vous avez 2 espaces consécutifs en position X
        - Mess4 - Un signe de ponctuation doit être suivi par un espace en position X
        - Mess5 - Avant les caractères suivants (. et ,) il ne faut pas d'espace en position X
        - Mess6 - Avant les caractères suivants (: et !) il faut un espace en position X
        - Mess7 - Votre phrase est correcte
    """
    if not Commence_Par_Majuscule(text):
        return "Votre phrase ne commence pas par une Majuscule"
    if not Bonne_Ponctuation(text):
        return "Votre phrase ne finis pas par un signe de ponctuation"

    car_prev = text[0]
    counter = 0
    for car in text[1:len(text) - 1]:

        if not Espace_Validation(car_prev, car, ' ', espace_accepte=False):
            return f"Vous avez 2 espaces consécutifs en position {counter+1}"

        if not Espace_Validation(car, car_prev, (',', ':', '?', '.'), espace_accepte=True):
            return f"Un signe de ponctuation doit être suivi par un espace en position {counter+1}"

        if not Espace_Validation(car_prev, car, ('.', ','), espace_accepte=False):
            return f"Avant les caractères suivants (. et ,) il ne faut pas d'espace en position {counter+1}"

        if not Espace_Validation(car_prev, car, (':', '!'), espace_accepte=True):
            return f"Avant les caractères suivants (: et !) il faut un espace en position {counter+1}"

        car_prev = car
        counter += 1
    return "Votre phrase est correcte"


phrase = input("Entrer une phrase pour vérification")
print(Validation_Phrase(phrase))


