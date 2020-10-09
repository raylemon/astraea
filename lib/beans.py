from lib.functions import *
from lib.functions import generate_code, compute_crc


class Convert:
    def __init__(self, number: int = None, base_src: int = None, base_dst: int = None):
        self.base_src = npr.randint(2, 21) if base_src is None else base_src
        self.base_dst = npr.randint(2, 21) if base_dst is None else base_dst
        self.number = format_value(npr.randint(info8.max), self.base_src) if number is None else number

    @property
    def statement(self) -> str:
        return f"{self.number} = ? ({self.base_dst})"

    @property
    def solution(self) -> str:
        try:
            n = int(clear_string(self.number), self.base_src)
            if not info8.min < n < info8.max:
                return "OVF"
            else:
                return format_value(n, self.base_dst)
        except ValueError:
            return "IMP"


class Arith:
    def __init__(self, number1: int = None, base_src1: int = None, number2: int = None, base_src2: int = None,
                 base_dst: int = None, op: chr = None):
        self.base_src1 = get_base() if base_src1 is None else base_src1
        self.base_src2 = get_base() if base_src2 is None else base_src2
        self.base_dst = get_base() if base_dst is None else base_dst
        self.op = npr.choice(('+', '-', '×', '÷')) if op is None else op

        self.n1 = rand_byte() if number1 is None else number1
        self.n2 = rand_byte() if number2 is None else number2

        self.__number1 = format_value(self.n1, self.base_src1)
        self.__number2 = format_value(self.n2, self.base_src2)

    @property
    def number1(self) -> str:
        return self.__number1

    @number1.setter
    def number1(self, value: str):
        self.__number1 = value
        self.n1 = np.int8(int(clear_string(value), self.base_src1)).item()

    @property
    def number2(self) -> str:
        return self.__number2

    @number2.setter
    def number2(self, value):
        self.__number2 = value
        self.n2 = np.int8(int(clear_string(value), self.base_src2)).item()

    @property
    def statement(self) -> str:
        return f"{self.number1} {self.op} {self.number2} = ? ({self.base_dst})"

    @property
    def solution(self) -> str:
        try:
            res = self.compute()
            if not info8.min < res < info8.max:
                return "OVF"
            else:
                return format_value(res, self.base_dst)
        except ValueError:
            return "IMP"

    def compute(self) -> int:
        if self.op == '+':
            return self.n1 + self.n2
        elif self.op == '-':
            return self.n1 - self.n2
        elif self.op == '×':
            return self.n1 * self.n2
        elif self.op == '÷':
            if self.n1 < 0 or self.n2 < 0:
                raise ValueError
            else:
                return self.n1 // self.n2
        else:
            raise ValueError


class Ca2:
    def __init__(self, number: int = None, base_src: int = None, base_dst: int = None):
        self.base_src = choose_bin_base() if base_src is None else base_src
        self.base_dst = choose_bin_base() if base_dst is None else base_dst
        self.number = format_value(npr.randint(info8.min, info8.max), self.base_src) if number is None else number

    @property
    def statement(self) -> str:
        return f"Cà2 de {self.number} = ? ({self.base_dst})"

    @property
    def solution(self) -> str:
        n = int(clear_string(self.number), self.base_src)
        return format_value(-n, self.base_dst)


class DecimalToFloat16:
    def __init__(self, src: float = None, base_dst: int = None):
        self.src = gen_float16() if src is None else src
        self.base_dst = choose_bin_base() if base_dst is None else base_dst
        self.source = np.float16(self.src)

    @property
    def statement(self) -> str:
        return f"{self.src} => ? ({self.base_dst})"

    @property
    def solution(self) -> str:
        s = bin(self.source.view("H"))[2:].zfill(16)
        bits = int(s, 2)
        if self.base_dst == 2:
            pad = 16
        elif self.base_dst == 8:
            pad = 6
        else:
            pad = 0

        v = np.base_repr(bits, self.base_dst).zfill(pad)[::-1]
        v = ' '.join(v[i:i + 4] for i in range(0, len(v), 4))[::-1]
        if self.base_dst == 2:
            return f"b{v}"
        elif self.base_dst == 8:
            return f"0{v}"
        else:
            return f"0x{v}"


class Float16ToDecimal:
    def __init__(self, src: str = None, base_src: int = None):
        self.base_src = choose_bin_base() if base_src is None else base_src
        if src is None:
            tmp = DecimalToFloat16(base_dst=self.base_src)
            self.src = tmp.solution
            self.val = tmp.source
            del tmp
        else:
            self.src = clear_string(src)
            self.val = float_from_unsigned16(self.src, self.base_src)

    @property
    def statement(self) -> str:
        return f"{self.src} => ? (10)"

    @property
    def solution(self) -> str:
        return str(self.val)

    @property
    def polynom(self) -> str:
        if np.isneginf(self.val):
            return "-INF"
        elif np.isposinf(self.val):
            return "+INF"
        elif np.isnan(self.val):
            return "NaN"
        elif self.val == 0:
            return "0"
        else:
            signum = "-(" if self.val < 0 else "+("
            v = np.abs(self.val)
            m = int(np.log2(v))
            if 2 ** m > v:
                m = m - 1
            s = ""
            for i in range(m, m - 10, -1):
                p = 2 ** i
                if v / p >= 1:
                    s += f"+2^{i}"
                    v -= p
            return signum + s[1:] + ")"


class HammingMessage:
    def __init__(self, msg: str = None, base_src: int = None, base_dst: int = None, encoded: bool = None):
        self.base_src = choose_bin_base() if base_src is None else base_src
        self.base_dst = choose_bin_base() if base_dst is None else base_dst
        self.encoded = npr.choice((True, False)) if encoded is None else encoded

        if msg is None:
            self.bin_msg = generate_message()
            tmp = np.base_repr(int(self.bin_msg, 2), self.base_src)
            self.msg = format_message(tmp, self.base_src)
            del tmp
        else:
            self.msg = msg
            self.bin_msg = np.binary_repr(int(clear_string(msg), self.base_src))

    @property
    def statement(self) -> str:
        return f"{self.msg} à {'encoder' if self.encoded else 'décoder'} = ? ({self.base_dst})"

    @property
    def solution(self) -> str:
        if self.encoded:
            return format_message(self.encode_message(), self.base_dst)
        else:
            return format_message(self.decode_message(), self.base_dst)

    def encode_message(self) -> str:
        msg = [int(i) for i in self.bin_msg[::-1]]
        bits = generate_code(msg)
        v = ''.join(str(i) for i in bits)[::-1]
        return np.base_repr(int(v, 2), self.base_dst)

    def decode_message(self) -> str:
        power = self.parity_count()
        error = self.error_pos
        msg = [str(i) for i in reversed(self.bin_msg)]
        try:
            if error != 0:
                c = msg[error - 1]
                d = '0' if c == '1' else '1'
                msg[error - 1] = d
            for i in range(power - 1, -1, -1):
                del msg[2 ** i - 1]
        except IndexError as e:
            return f"Erreur - {e}"
        rslt = ''.join(i for i in msg[::-1])
        return np.base_repr(int(rslt, 2), self.base_dst)

    def parity_count(self) -> int:
        par = 0
        while 2 ** par <= len(self.bin_msg):
            par += 1
        return par

    @property
    def error_pos(self) -> int:
        par = self.parity_count()
        msg = [int(i) for i in reversed(self.bin_msg)]
        par = np.zeros(par, dtype=int)
        syndrome = ""
        power = 0
        while power < par:
            for i in range(len(msg)):
                k = i + 1  # extraction bit de parité
                s = np.binary_repr(k)
                bit = int((int(s) / 10 ** power) % 10)
                if bit == 1 and msg[i] == 1:
                    par[power] = int((par[power] + 1) % 2)
            syndrome = str(par[power]) + syndrome
            power += 1
        return int(syndrome, 2)


class Crc:
    def __init__(self, msg: str = None, base_src: int = None, div: str = None, base_dst: int = None,
                 encoded: bool = None):
        self.base_dst = choose_bin_base() if base_dst is None else base_dst
        self.div = generate_divisor() if div is None else div
        self.base_src = choose_bin_base() if base_src is None else base_src
        self.encoded = npr.choice((True, False)) if encoded is None else encoded

        if msg is None:
            self.bin_msg = generate_message()
            tmp = np.base_repr(int(self.bin_msg, 2), self.base_src)
            self.msg = format_message(tmp, self.base_src)
            del tmp
        else:
            self.bin_msg = np.binary_repr(int(clear_string(self.msg), self.base_src))

    @property
    def statement(self) -> str:
        return f"{self.msg} à {'encoder' if self.encoded else 'décoder'} [diviseur: {self.div}] = ? ({self.base_dst})"

    @property
    def solution(self) -> str:
        div = np.binary_repr(int(clear_string(self.div), 2))
        r = compute_crc(self.bin_msg, div)[len(self.bin_msg) + 1:]
        v = np.base_repr(int(r, 2), self.base_dst)
        return format_message(v, self.base_dst)

    @property
    def crc(self) -> str:
        div = np.binary_repr(int(clear_string(self.div), 2))
        return format_message(compute_crc(self.bin_msg, div)[len(self.bin_msg) + 1:], 2)
