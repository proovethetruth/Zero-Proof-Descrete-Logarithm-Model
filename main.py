import random
 
class ZeroProofProtocol:
    """
    Class to implement the Zero-Proof Protocol for discrete logarithm for Alice and Bob.
 
    Attributes:
    - p: int
        The prime number representing the modulo.
    - g: int
        The base number for the discrete logarithm.
    - a: int
        The private key for Alice.
    - b: int
        The private key for Bob.
    """
 
    def __init__(self, p: int, g: int, a: int, b: int):
        """
        Constructor to instantiate the ZeroProofProtocol class.
 
        Parameters:
        - p: int
            The prime number representing the modulo.
        - g: int
            The base number for the discrete logarithm.
        - a: int
            The private key for Alice.
        - b: int
            The private key for Bob.
        """
 
        self.p = p
        self.g = g
        self.a = a
        self.b = b
 
    def calculate_public_keys(self):
        """
        Calculates the public keys for Alice and Bob.
 
        Returns:
        - int, int:
            The public keys for Alice and Bob respectively.
        """
 
        # Calculate the public key for Alice: A = g^a mod p
        A = pow(self.g, self.a, self.p)
 
        # Calculate the public key for Bob: B = g^b mod p
        B = pow(self.g, self.b, self.p)
 
        return A, B
 
    def generate_challenge(self):
        """
        Generates a random challenge value for Alice and Bob.
 
        Returns:
        - int:
            The challenge value.
        """
 
        # Generate a random challenge value between 1 and p-1
        challenge = random.randint(1, self.p - 1)
 
        return challenge
 
    def verify_proof(self, A: int, B: int, challenge: int):
        """
        Verifies the proof of Alice and Bob.
 
        Parameters:
        - A: int
            The public key of Alice.
        - B: int
            The public key of Bob.
        - challenge: int
            The challenge value.
 
        Returns:
        - bool:
            True if the proof is valid, False otherwise.
        """
 
        # Calculate the proof value for Alice: a' = (a + challenge) mod (p-1)
        a_prime = (self.a + challenge) % (self.p - 1)
 
        # Calculate the proof value for Bob: b' = (b + challenge) mod (p-1)
        b_prime = (self.b + challenge) % (self.p - 1)
 
        # Verify the proof: A^b' mod p = B^a' mod p
        if pow(A, b_prime, self.p) == pow(B, a_prime, self.p):
            return True
        else:
            return False

p_value = 107
g_value = 2
a_value = 15
b_value = 20
 
protocol = ZeroProofProtocol(p_value, g_value, a_value, b_value)
 
A_value, B_value = protocol.calculate_public_keys()
print(f"The public key for Alice is {A_value}.")
print(f"The public key for Bob is {B_value}.")
 
for i in range(100000000):
    challenge_value = protocol.generate_challenge()
    proof_valid = protocol.verify_proof(A_value, B_value, challenge_value)
    if proof_valid:
        print("The proof is valid.\n")
    else:
        print("The proof is not valid.\n")