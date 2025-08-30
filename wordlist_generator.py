# Criar lista de palavras (Flags encontradas)
nano seeds.txt

# Criar a lista de palavras no Kali
mkdir -p ~/lab-wordlist
nano ~/lab-wordlist/custom_wordlist.txt

# Criar o executável em Python
nano wordlist_gen.py

#!/usr/bin/env python3
# Gera uma wordlist customizada a partir de palavras-semente (seeds.txt)
# Inclui:
# - variações de leetspeak
# - maiúsculas/minúsculas
# - sufixos comuns

import itertools

# Regras de substituição leet
leet = {
    "a": ["a", "4", "@"],
    "e": ["e", "3"],
    "i": ["i", "1", "!"],
    "o": ["o", "0"],
    "s": ["s", "5", "$"],
}

def leetspeak(word):
    combos = []
    for letters in itertools.product(*[leet.get(c.lower(), [c]) for c in word]):
        combos.append("".join(letters))
    return set(combos)

def case_variants(word):
    """Gera versões maiúsculas/minúsculas misturadas"""
    variants = set()
    variants.add(word.lower())
    variants.add(word.upper())
    variants.add(word.capitalize())
    # todas as combinações de caixa
    combos = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in word)))
    variants.update(combos)
    return variants

# Ler as seeds
with open("seeds.txt") as f:
    seeds = [line.strip() for line in f if line.strip()]

wordlist = set()
for seed in seeds:
    # para cada variação de caixa
    for variant in case_variants(seed):
        # aplicar variações leet
        leet_words = leetspeak(variant)
        wordlist |= leet_words
        # acrescentar sufixos
        for w in leet_words:
            for suffix in ["", "!", "123", "2024", "2025", "@"]:
                wordlist.add(w + suffix)

# Salvar wordlist
with open("custom_wordlist.txt", "w") as f:
    for w in sorted(wordlist):
        f.write(w + "\n")

print(f"[✓] Wordlist gerada com {len(wordlist)} palavras em custom_wordlist.txt")


#Tornar o script executável
chmod +x wordlist_gen.py

#Executar o script
python3 wordlist_gen.py
## Saída esperada 'Wordlist gerada com palavras em custom_wordlist.txt

#Verificar
head custom_wordlist.txt
wc -l custom_wordlist.txt
