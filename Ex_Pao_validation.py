def commence_par_majuscule(text):
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


def bonne_ponctuation(text):
    """
    Si le dernier caractère de la chaine est ponctué par un "." ou un "!" ou un "?"
    :param text: string
    :return: Boolean
    """
    result = False
    if text[-1] in ('.', '!', '?'):
        result = True

    return result


def espace_validation(car_prev, car_cur, car_find, espace_accepte=False):
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


def validation_phrase(text):
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
        - Mess1 - Veuillez corriger votre phrase selon les indications données.
        - Mess2 - Votre phrase est correcte.
    """
    fail_count = 0
    if not commence_par_majuscule(text):
        fail_count += 1
        print("Votre phrase ne commence pas par une Majuscule")
    if not bonne_ponctuation(text):
        fail_count += 1
        print("Votre phrase ne finis pas par un signe de ponctuation")

    car_prev = text[0]
    counter = 0
    for car in text[1:]:

        if not espace_validation(car_prev, car, ' ', espace_accepte=False):
            fail_count += 1
            print(f"Vous avez 2 espaces consécutifs en position {counter+1}")

        if not espace_validation(car, car_prev, (',', ':', '?', '.'), espace_accepte=True):
            fail_count += 1
            print(f"Un signe de ponctuation doit être suivi par un espace en position {counter+1}")

        if not espace_validation(car_prev, car, ('.', ','), espace_accepte=False):
            fail_count += 1
            print(f"Avant les caractères suivants (. et ,) il ne faut pas d'espace en position {counter+1}")

        if not espace_validation(car_prev, car, (':', '!', '?'), espace_accepte=True):
            fail_count += 1
            print(f"Avant les caractères suivants (: et !) il faut un espace en position {counter+1}")

        car_prev = car
        counter += 1
    if fail_count != 0:
        return "Veuillez corriger votre phrase selon les indications données."
    else:
        return "Votre phrase est correcte."


phrase = input("Entrer une phrase pour vérification :\n")
print(validation_phrase(phrase))
