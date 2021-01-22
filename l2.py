from functools import reduce
from string import ascii_lowercase




def find_ioc_from_frec_file():
    with open("frecv.txt", 'r') as frecfile:
        frecs = [float(line.split(': ')[1]) / 100 for line in frecfile]

        ioc = reduce(lambda sum, probability: probability * probability + sum, frecs, 0)
        print("IOC for English is: ", ioc)
        return frecs


english_frequencies = []


def question_1():
    print("Question 1: ")
    global english_frequencies
    english_frequencies = find_ioc_from_frec_file()



def find_counts(input_text: str):
    freq_dict = {}
    count = 0
    for char in ascii_lowercase:
        freq_dict[char] = 0
    for char in input_text.lower():
        if char in ascii_lowercase:
            if char in freq_dict.keys():
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
            count += 1
    for letter in ascii_lowercase:
        freq_dict[letter] /= count
    return freq_dict


def find_index_from_cipher(frec_dict_cipher):
    ioc = 0
    for num, letter in enumerate(ascii_lowercase):
        ioc += frec_dict_cipher[letter] * english_frequencies[num]
    return ioc

def question_2():
    print("\nQuestion2:")
    chall1 = "GCUA VQ DTGCM"
    chall2 = "LGEGJJGO OW OADD ESJUZ GF HSFLZWJ VAFAFY"
    chall3 = "GO QOD K YB NOKDR"

    def shift_letter(letter, key) -> chr:
        if letter not in ascii_lowercase:
            return letter
        return chr((ord(letter) - ord('a') + 26 + key) % 26 + ord('A'))

    def shift_text(string: str, key) -> str:
        return "".join([shift_letter(ch, key) for ch in list(string.lower())])



    #for letter in ascii_lowercase:
    #    english_frequencies[letter] * decoded_freqs[letter]
    # one liner to replicate verification bash script
    def brute_force(challenge):
        ioc, key = max([(find_index_from_cipher(find_counts(shift_text(challenge, i))), i) for i in range(26)])
        print(shift_text(challenge, key), ioc)

    brute_force(chall1)
    brute_force(chall2)
    brute_force(chall3)


def vignere_enc_shift(plain, key):
    return chr((ord(plain) + ord(key) - ord('a') * 2 + 26) % 26 + ord('A'))


def vignere_dec_shift(cipher, key):
    return chr((ord(cipher) - ord(key) + 26) % 26 + ord('a'))


def vignere_encode(plaintext, key):
    to_shift = 0
    res = ""
    for ch in plaintext.lower():
        res += vignere_enc_shift(ch, key[to_shift])
        to_shift = (to_shift + 1) % len(key)
    return res


def vignere_decode(cipertext, key):
    to_shift = 0
    res = ""
    for ch in cipertext.lower():
        res += vignere_dec_shift(ch, key[to_shift])
        to_shift = (to_shift + 1) % len(key)
    return res


def question_3():
    print("\nQuestion 3: ")
    print(vignere_encode("Plaintext", "key"))
    print(vignere_decode("ZPYSRROBR", "key"))


def question_4():
    print("\nQuestion 4: ")
    challenge = """CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBW
RVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAK
LXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELX
VRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHR
ZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJT
AMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBI
PEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHP
WQAIIWXNRMGWOIIFKEE"""
    for length in range(1,10):
        print(find_index_from_cipher(find_counts(vignere_decode(challenge, 'z' * length))))
    print("NYI")


question_1()
question_2()
question_3()
question_4()
