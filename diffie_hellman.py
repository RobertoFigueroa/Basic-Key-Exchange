#Reference : https://sublimerobots.com/2015/01/simple-diffie-hellman-example-python/
import random
from time import sleep

sharedPrime = 101 # n
sharedBase = random.randint(1, sharedPrime -1) # g


aliceSecret = random.randint(1, sharedPrime-1)
bobSecret =  random.randint(1, sharedPrime-1)

print("-"*20)
print("Alice secret number: {}".format(aliceSecret))
print("Bob secret number: {}".format(bobSecret))
print("-"*20)


# Begin
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime (n): " , sharedPrime )
print( "    Publicly Shared Base (g):  " , sharedBase )
 
#Alice sends bob A = g^a mod n
A = (sharedBase**aliceSecret) % sharedPrime
print("\tAlice sends by public chanel this: {}".format(A))
#Bob sends Alice B = g^b mod n
B = (sharedBase**bobSecret) % sharedPrime
print("\Bob sends by public chanel this: {}".format(B))

#simulating time
print('>'*20)
print("Sending ...")
print('<'*20)
sleep(2)

print("----- Variables calculated in private space -----")
#Alice computes shared secret: s = B ^a mod n
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("Alice's shared key: {}".format(aliceSharedSecret))

#Bob computes shared secret: s = A ^b mod n
bobSharedSecret = (A ** bobSecret) % sharedPrime
print("Bob's shared key: {}".format(bobSharedSecret))


#Attack
def search_key(sharedPrime, sharedBase, value2find):
    for i in range(sharedPrime):
        print("Intento {}".format(i))
        test = (sharedBase **i) % sharedPrime
        if test == value2find:
            print("*"*20)
            print("Founded: {}".format(i))
            print("Computed: {}".format(test))
            print("*"*20)

# For A
search_key(sharedPrime, sharedBase, A)

# For B
search_key(sharedPrime, sharedBase, B)

