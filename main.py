import random
 
class ZeroProofProtocol:
    def __init__(self, p: int, g: int, a: int, b: int):
        self.p = p
        self.g = g
        self.a = a
        self.b = b
 
    def calculate_public_keys(self):
        # Calculate the public key for Alice: A = g^a mod p
        A = pow(self.g, self.a, self.p)
 
        # Calculate the public key for Bob: B = g^b mod p
        B = pow(self.g, self.b, self.p)
 
        return A, B
 
    def generate_challenge(self):
        # Generate a random challenge value between 1 and p-1
        challenge = random.randint(1, self.p - 1)
 
        return challenge
 
    def verify_proof(self, A: int, B: int, challenge: int):
        # Calculate the proof value for Alice: a' = (a + challenge) mod (p-1)
        a_prime = (self.a + challenge) % (self.p - 1)
 
        # Calculate the proof value for Bob: b' = (b + challenge) mod (p-1)
        b_prime = (self.b + challenge) % (self.p - 1)
 
        # Verify the proof: A^b' mod p = B^a' mod p
        if pow(A, b_prime, self.p) == pow(B, a_prime, self.p):
            return True
        else:
            return False
        

def calculate_false_proof_probability(protocol, A, B, num_attempts=1000):
        success_count = 0

        for _ in range(num_attempts):
            # Атакующая сторона выбирает случайное значение-вызов
            challenge_attempt = random.randint(1, protocol.p - 1)

            # Атакующая сторона пытается подобрать a' и b' так, чтобы условие было выполнено
            a_prime_attempt = (protocol.a + challenge_attempt) % (protocol.p - 1)
            b_prime_attempt = (protocol.b + challenge_attempt) % (protocol.p - 1)

            # Проверка условия протокола с поддельными a' и b'
            if pow(A, b_prime_attempt, protocol.p) == pow(B, a_prime_attempt, protocol.p):
                success_count += 1

        # Вероятность успешного ложного доказательства
        probability = success_count / num_attempts
        return probability


if __name__ == "__main__":
    p_value = 2048
    g_value = 5
    a_value = 1081
    b_value = 1708
    
    protocol = ZeroProofProtocol(p_value, g_value, a_value, b_value)
    A_value, B_value = protocol.calculate_public_keys()

    false_proof_probability = calculate_false_proof_probability(protocol, A_value, B_value)
    print(f"The probability of a successful false proof: {false_proof_probability}")

    print(f"The public key for Alice is {A_value}.")
    print(f"The public key for Bob is {B_value}.")
    
    challenge_value = protocol.generate_challenge()
    proof_valid = protocol.verify_proof(A_value, B_value, challenge_value)
    if proof_valid:
        print("The proof is valid.\n")
    else:
        print("The proof is not valid.\n")