import random

class Prover:
    def __init__(self, p, A, x):
        self.p = p
        self.A = A
        self.x = x

    def generate_proof(self):
        self.r = random.randint(0, self.p - 2)
        h = pow(self.A, self.r, self.p)
        return h

    def respond_to_challenge(self, b):
        s = (self.r + (b * self.x)) % (self.p - 1)
        return s

class Verifier:
    def __init__(self, p, A, B):
        self.p = p
        self.A = A
        self.B = B

    def challenge_prover(self):
        b = random.getrandbits(1)
        return b

    def verify_proof(self, h, s):
        left_side = pow(self.A, s, self.p)
        right_side = (h * pow(self.B, self.b, self.p)) % self.p
        return left_side == right_side

class Attacker:
    def __init__(self, p, A, B):
        self.p = p
        self.A = A
        self.B = B

    def generate_fake_proof(self, potential_x):
        r_fake = random.randint(0, self.p - 2)
        h_fake = pow(self.A, r_fake, self.p)
        b_fake = random.getrandbits(1)
        s_fake = (r_fake + (b_fake * potential_x)) % (self.p - 1)
        return h_fake, s_fake


if __name__ == "__main__":
    p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
    A = 2
    x = 6
    B = pow(A, x, p)

    prover = Prover(p, A, x)
    verifier = Verifier(p, A, B)

    h = prover.generate_proof()
    verifier.b = verifier.challenge_prover()
    s = prover.respond_to_challenge(verifier.b)
    result_prover = verifier.verify_proof(h, s)
    print("Prover Zero-Knowledge Proof Verification Result:", result_prover)

    # - - - - - - - - - - - ATTACK  - - - - - - - - - - - #

    attacker = Attacker(p, A, B)

    potential_x = 0
    max_attempts = 1000

    count_success = 0
    for _ in range(max_attempts):
        fake_h, fake_s = attacker.generate_fake_proof(potential_x)
        result_attacker = verifier.verify_proof(fake_h, fake_s)

        if result_attacker:
            count_success += 1

        potential_x += 1

    print(f"Probability of successful attack: {count_success / max_attempts * 100} %")
