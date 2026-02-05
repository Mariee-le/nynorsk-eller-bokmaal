# last inn nltk
import nltk
from nltk.corpus import udhr
nltk.download("udhr")
nltk.download("punkt")
from nltk import word_tokenize



# last ned nynorsk- og bokmålkorpus

nynorsk_tekst = udhr.raw("Norwegian_Norsk-Nynorsk-Latin1")
bokmål_tekst = udhr.raw("Norwegian_Norsk-Bokmal-Latin1")


# tokenize tekstene og gjere eventuelle store bokstavar til små bokstavar

nynorsk_tokens = [ord.lower() for ord in word_tokenize(nynorsk_tekst) if ord.isalpha()]
bokmål_tokens = [ord.lower() for ord in word_tokenize(bokmål_tekst) if ord.isalpha()]


# finn vokabulær i tekstene på nynorsk og bokmål

nynorsk_vokabulær = set(nynorsk_tokens)
bokmål_vokabulær = set(bokmål_tokens)


 # Ord som berre finst i éi målform

berre_nynorsk = nynorsk_vokabulær - bokmål_vokabulær
berre_bokmål = bokmål_vokabulær - nynorsk_vokabulær



# funksjon får å finne ut om ei tekst er på nynorsk, bokmål eller om det er uvisst

def målform(tekst):
   # del opp døme i ord
   tekst_vokabulær = set([ord.lower() for ord in word_tokenize(tekst) if ord.isalpha()])
   nynorsk = tekst_vokabulær & berre_nynorsk
   bokmål = tekst_vokabulær & berre_bokmål

   if nynorsk and not bokmål:
      print(f'''Dømet __{tekst}__ er på nynorsk :)''')
   elif bokmål and not nynorsk:
      print(f'''Dømet __{tekst}__ er på bokmål :)''')
   elif nynorsk and bokmål:
      print(f'''Ojsånn no blei eg usikker! Dømet __{tekst}__ kan enten vere nynorsk eller bokmål''')
   else: 
      print(f'''I dømet __{tekst}__ er der ingen tydelege markørar på verken nynorsk eller bokmål''')

# skriv inn eigne døme her:)

if __name__ == "__main__":
    while True:
        tekst = input("\nSkriv eit døme på bokmål eller nynorsk (skriv 'exit' for å avslutte): ").strip()

        if not tekst:
            print("Du må skrive ei setning.")
            continue

        if tekst.lower() == "exit":
            print("Avsluttar programmet.")
            break

        målform(tekst)

     


