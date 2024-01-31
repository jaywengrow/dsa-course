import random


class DivisionHasher:

    def __init__(self, array_length):
        self.array_length = array_length

        # Choose a random prime number:
        p = random.randint(10007, 99991)
        while not self.is_prime(p):
            p = random.randint(10007, 99991)
    
        self.prime = p

    def hash(self, key):
        return key % self.prime % self.array_length

    # Fermat's Primality Test
    def is_prime(self, number):
        for _ in range(100):
            a = random.randint(1, number - 1)
            if pow(a, number - 1, number) != 1:
                return False
        
        return True
