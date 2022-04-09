import random

prime_number_1 = 277
prime_number_2 = 239

ON_low = '0x01'

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    modulus = p * q

    #Phi is the totient of n
    L = (p-1) * (q-1)
    #print("L=",L)

    #Choose an integer e such that e and L(n) are coprime
    e = random.randrange(2,L)
    #print('E=',e)

    #Use Euclid's Algorithm to verify that e and L(n) are comprime
    g = gcd(e, L)
    #print('G=',g)
    while g != 1:
        e = random.randrange(2, L)
        #print("E=",e)
        g = gcd(e, L)
        #print("G=",g)
    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, L)
    #print("D=",d)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, modulus), (d, modulus))
############################### EXERCISE 1 ###############################
def encrypt(public_key, hex_number):
    integer_value = int(hex_number, 0)
    encrypted_value = integer_value ** public_key[0]
    encrypted = encrypted_value % public_key[1]
    return encrypted
    ''' complete with necesarry code '''

############################### EXERCISE 2 ###############################
def decrypt(private_key, encrypted_msg):
    decrypted_value = encrypted_msg ** private_key[0]
    decrypted_integer = decrypted_value % private_key[1]
    decrypted_hex = hex(decrypted_integer)
    return decrypted_hex
    ''' complete with necesarry code '''

############################### EXERCISE 3 ###############################
def low_check(hex_nr):
    low = hex(hex_nr & 0xFF)[2:].zfill(2)
    low = '0x' + low
    if low == ON_low:
        return True
    else:
        return False
    ''' complete with necesarry code '''

############################### EXERCISE 4 ###############################
def number_check(hex_nr):
    high = hex(hex_nr >> 8)[2:4].zfill(2)
    low = hex(hex_nr & 0xFF)[2:].zfill(2)
    nr1 = '0x' + high[0]
    nr1_int = int(nr1, 16)
    nr2 = '0x' + high[1]
    nr2_int = int(nr2, 16)
    nr3 = '0x' + low[0]
    nr3_int = int(nr3, 16)
    nr4 = '0x' + low[1]
    nr4_int = int(nr4, 16)
    negative = [0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0]
    positive = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF]
    if positive[nr1_int] == negative[nr3_int] and positive[nr2_int] == negative[nr4_int]:
        return True
    return False
    ''' complete with necesarry code '''
