def __digraf_to_new_latin(word):  # noqa ŌōḠḡŞşÇçŊŋ
    # Converts Uzbek digraphs (e.g., O‘, G‘, SH, CH, NG) to corresponding new Latin Unicode characters.

    # Replace various representations of 'O‘' with 'Ō'
    word = word.replace("O'", 'Ō')
    word = word.replace("O`", 'Ō')
    word = word.replace("Oʻ", 'Ō')
    word = word.replace("Oʼ", 'Ō')
    word = word.replace("O‘", 'Ō')
    word = word.replace("O’", 'Ō')

    # Replace various representations of 'o‘' with 'ō'
    word = word.replace("o'", 'ō')
    word = word.replace("o`", 'ō')
    word = word.replace("oʻ", 'ō')
    word = word.replace("oʼ", 'ō')
    word = word.replace("o‘", 'ō')
    word = word.replace("o’", 'ō')

    # Replace various representations of 'G‘' with 'Ḡ'
    word = word.replace("G'", 'Ḡ')
    word = word.replace("G`", 'Ḡ')
    word = word.replace("Gʻ", 'Ḡ')
    word = word.replace("Gʼ", 'Ḡ')
    word = word.replace("G‘", 'Ḡ')
    word = word.replace("G’", 'Ḡ')

    # Replace various representations of 'g‘' with 'ḡ'
    word = word.replace("g'", 'ḡ')
    word = word.replace("g`", 'ḡ')
    word = word.replace("gʻ", 'ḡ')
    word = word.replace("gʼ", 'ḡ')
    word = word.replace("g‘", 'ḡ')
    word = word.replace("g’", 'ḡ')

    # Replace digraphs for 'SH', 'CH', and 'NG'
    word = word.replace("SH", 'Ş').replace("Sh", 'Ş').replace("sH", 'Ş').replace("sh", 'ş')
    word = word.replace("CH", 'Ç').replace("Ch", 'Ç').replace("cH", 'Ç').replace("ch", 'ç')
    word = word.replace("NG", 'Ŋ').replace("Ng", 'Ŋ').replace("nG", 'Ŋ').replace("ng", 'ŋ')

    return word


def __new_latin_to_digraf(word):  # noqa ŌōḠḡŞşÇçŊŋ
    # Converts new Latin Unicode characters back to Uzbek digraphs.

    word = word.replace('Ō', "O‘")
    word = word.replace('ō', "o‘")
    word = word.replace('Ḡ', "G‘")
    word = word.replace('ḡ', "g‘")
    word = word.replace('Ş', "SH").replace('ş', "sh")
    word = word.replace('Ç', "CH").replace('ç', "ch")
    word = word.replace('Ŋ', "NG").replace('ŋ', "ng")

    return word


def tokenize(word):
    # If the text is not a word, it will be returned by itself.
    if not isinstance(word, str) or not word.isalpha():
        return str(word)

    # Convert Uzbek digraphs to new Latin Unicode characters
    word = __digraf_to_new_latin(word)

    vowels = "AaEeIiOoUuŌō"
    consonants = "BbDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxYyZzḠḡŞşÇçŊŋ"

    # Dictionary of words with predefined syllabifications
    exceptions = {  # (18 units)
        "abstrakt": "abs-trakt",
        "agglyutinativ": "ag-glyu-ti-na-tiv",
        "ansambl": "an-sambl",
        "aviaekspress": "a-vi-a-eks-press",
        "aviakonstruktor": "a-vi-a-ko-nstruk-tor",
        "avstraliya": "avs-tra-li-ya",
        "bae'tibor": "ba-e'-ti-bor",
        "bee'tibor": "be-e'-ti-bor",
        "eksklyuziv": "eks-klyu-ziv",
        "ekstremizm": "eks-tre-mizm",
        "elektrlampa": "e-lektr-lam-pa",
        "inflyatsiya": "in-flyat-si-ya",
        "instruksiya": "ins-truk-si-ya",
        "mototransport": "mo-to-trans-port",
        "pisht": "pisht",
        "zoologiya": "zoo-lo-gi-ya",
        "silindrik": "silin-drik",
        "monografiya": "mo-no-gra-fi-ya",
        "transport": "tran-sport"
    }

    if word.lower() in exceptions:
        return exceptions[word.lower()]

    # Remove leading and trailing spaces
    word = word.strip()

    # If the word does not contain a vowel, return as is
    if not any(char in vowels for char in word):
        return word

    syllables = []
    current_syllable = ""
    i = 0

    # Process the word character by character
    while i < len(word):
        current_syllable += word[i]

        if word[i] in vowels:
            next_char = word[i + 1] if i + 1 < len(word) else ""
            next_next_char = word[i + 2] if i + 2 < len(word) else ""

            # If next two characters are consonants, end syllable here
            if next_char in consonants and next_next_char in consonants:
                current_syllable += next_char
                syllables.append(current_syllable)
                current_syllable = ""
                i += 1
            else:
                syllables.append(current_syllable)
                current_syllable = ""

        i += 1

    # Add any remaining characters to syllables
    if current_syllable:
        if len(current_syllable) == 1 and syllables:
            syllables[-1] += current_syllable
        else:
            syllables.append(current_syllable)

    # Convert back to Uzbek digraphs
    clean_syllables = [__new_latin_to_digraf(syllable) for syllable in syllables]

    return "-".join(clean_syllables)
