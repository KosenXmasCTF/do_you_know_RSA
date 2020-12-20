from Crypto.Util import number
import os
import random

def cryption(message, E, N):
    c = pow(message, E, N)    
    return c

def get_E(L):
    E_list = [e for e in range(2, 10000) if number.GCD(e, L) == 1]
    return E_list[random.randint(0, len(E_list) - 1)]

def message_to_num(msg):
    ret = 0
    for c in msg:
        ret <<= 8
        ret += ord(c)
    return ret


def main():
    p = number.getPrime(100, os.urandom)
    q = number.getPrime(100, os.urandom)

    N = p * q
    L = ((p - 1) * (q - 1)) // number.GCD(p - 1, q - 1)

    print(f"N = {N}")
    # print(f"L = {L}")
    print(f"p = {p}")
   
    E = get_E(L)
    print(f"E = {E}")

    D = number.inverse(E, L)
    # print(D)

    c = cryption(1234, E, N)
    m = cryption(c, D, N)
   
    message = message_to_num("xm4s{dont_leak_p_and_q!!}")
    
    crypted_message = cryption(message, E, N)

    print(f"crypted message is {crypted_message}")

main()

