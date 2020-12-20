from Crypto.Util import number

print("N")
N = int(input())

print("p")
p = int(input())

print("E")
E = int(input())

print("message")
msg = int(input())

q = N // p
L = ((p - 1) * (q - 1)) // number.GCD(p - 1, q - 1)

D = number.inverse(E, L)

def decryption(message, D, N):
    c = pow(message, D, N)
    return c

plain = decryption(msg, D, N);

def num_to_message(num):
    message = ''
    while num != 0:
        message += chr(num % 0x100)
        num >>= 8
    return message

print(num_to_message(plain)[::-1])


