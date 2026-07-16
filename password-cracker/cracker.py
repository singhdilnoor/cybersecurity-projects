import hashlib
import os
import time
import itertools
import string

def crack_wordlist(target_hash, wordlist_path):
    with open(wordlist_path, "r") as file:
        wordlist = file.read().splitlines()

    for word in wordlist:
        guess_hash = hashlib.sha256(word.encode()).hexdigest()
        if guess_hash == target_hash:
            return word
    return None

def crack_bruteforce(target_hash, max_length):
    chars = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(chars, repeat=length):
            guess = "".join(guess_tuple)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                return guess
    return None

target_hash = input("Enter the hash to crack: ").strip()

script_dir = os.path.dirname(os.path.abspath(__file__))
wordlist_path = os.path.join(script_dir, "wordlist.txt")

start_time = time.time()

print("Trying wordlist first...")
result = crack_wordlist(target_hash, wordlist_path)

if result:
    print(f"\nPassword found (wordlist): {result}")
else:
    print("Not in wordlist. Switching to brute-force (this may take a while)...")
    result = crack_bruteforce(target_hash, max_length=4)
    if result:
        print(f"\nPassword found (brute-force): {result}")
    else:
        print("\nPassword not found.")

elapsed = time.time() - start_time
print(f"Time taken: {elapsed:.4f} seconds")