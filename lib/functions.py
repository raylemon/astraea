import re

import numpy
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


def float_from_unsigned16(src: str, base_src: int) -> float:
    n = int(src, base_src)
    assert 0 <= n < 2 ** 16
    sign = n >> 15
    exp = (n >> 10) & 0b011111
    fraction = n & (2 ** 10 - 1)
    if exp == 0:
        if fraction == 0:
            return -0.0 if sign else 0.0
        else:
            return (-1) ** sign * fraction / 2 ** 10 * 2 ** (-14)  # subnormal
    elif exp == 0b11111:
        if fraction == 0:
            return float("-inf") if sign else float("inf")
        else:
            return float("nan")
    else:
        return (-1) ** sign * (1 + fraction / 2 ** 10) * 2 ** (exp - 15)


def parity(bits, power):
    par = 0
    for i in range(len(bits)):
        if bits[i] != 2:
            # si la case ne contient pas 2, on récupère l’index en binaire
            s = np.binary_repr(i + 1)
            x = int((int(s) / 10 ** power) % 10)
            if x == 1 and bits[i] == 1:
                par = int((par + 1) % 2)
    return par


def generate_code(msg):
    i = 0
    par = 0
    while i < len(msg):  # recherche nb bits à ajouter
        if 2 ** par == i + par + 1:
            par += 1
        else:
            i += 1
    bits = np.zeros(len(msg) + par, dtype=int)  # tableau de Hamming
    i, j, k = 1, 0, 0
    while i <= len(bits):
        if 2 ** j == i:
            bits[i - 1] = 2  # remplissage des inconnus
            j += 1
        else:
            bits[k + j] = msg[k]
            k += 1
        i += 1
    i = 0
    while i < par:
        bits[2 ** i - 1] = parity(bits, i)
        i += 1
    return bits


def compute_crc(dividend, divisor):
    def divide(d,r):
        curr = 0
        while not (len(r) - curr < len(d)):
            for i in range(len(d)):
                r[curr+i] = np.bitwise_xor(r[curr+i],d[i])
            while r[curr] ==0 and curr != len(r):
                curr+=1
        return r

    divis = [int(i) for i in divisor]
    #calcul
    div = [int(i) for i in dividend]
    for i in range(len(divis)):
        div.append(0)
    rem = list(div)
    rem = divide(divis,rem)
    crc = np.bitwise_xor(div,rem)
    return ''.join(str(i) for i in crc)