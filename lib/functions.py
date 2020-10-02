import re

import numpy as np
import numpy.random as npr

info8 = np.iinfo(np.int8)


def clear_string(msg: str) -> str:
    """
  Suppression des éléments de formatage
  :param msg : le message à nettoyer.
  :return : le message nettoyé de ses éléments de formatage
  """
    msg = re.sub("^(b|0x?)", "", msg)
    msg = re.sub("(\\(\\d*\\))$", "", msg)
    msg = re.sub("\\s", "", msg)
    return msg


def format_message(msg: str, base: int) -> str:
    """
    Formate un message en espaçant les blocs de 4 et en ajoutant la base
    :param msg: le message à formater
    :param base: la base de travail
    :return: le message formaté et espacé.
    """
    msg = msg[::-1]
    v = ' '.join(msg[i:i + 4] for i in range(0, len(msg), 4))[::-1]
    if base == 2:
        return f"b{v}"
    elif base == 8:
        return f"O{v}"
    elif base == 16:
        return f"0x{v}"
    else:
        return f"{v}({base})"


def format_value(value: int, base: int) -> str:
    """
    Formate une valeur numérique et vérifie l’overflow
    :param value: La représentation décimale d’une valeur binaire
    :param base: La base de travail
    :return: la valeur formatée
    """
    if not -256 < value < 255:
        return "OVF"
    value = np.uint8(value)
    if base == 2:
        v = np.binary_repr(value, width=8)
    else:
        v = np.base_repr(value, base)
    return format_message(v, base)


def choose_bin_base() -> int:
    """
    Renvoie une base binaire
    :return: Une base binaire
    """
    return npr.choice((2, 8, 16))


def generate_message() -> str:
    """
    Génère un message binaire aléatoire
    :return: un message binaire aléatoire
    """
    v = npr.randint(2, size=(4,))
    return ''.join(str(e) for e in v.tostring())[:15]


def generate_divisor() -> str:
    """
    Renvoie un diviseur positif
    :return: Un diviseur en binaire formaté
    """
    return format_message(np.binary_repr(npr.randint(0, 100)), 2)


def get_base() -> int:
    """
    Choisit une base aléatoirement entre les bases binaires et décimales
    :return: Renvoie une base choisie entre 2,8,10 et 16
    """
    return npr.choice((2, 8, 10, 16))


def rand_byte() -> int:
    """
    Génère un byte aléatoire
    :return: Renvoie un byte sous forme décimale
    """
    return npr.randint(info8.min, info8.max, dtype="int8").item()


def gen_float16() -> float:
    """
    Génère aléatoirement un nombre flottant sur 16 bits
    :return: Un nombre généré aléatoirement sur 16 bits.
    """
    mini = -32768
    maxi = 32767
    f = (maxi - mini) * npr.random() + mini
    return np.float16(np.around(f))
