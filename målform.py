# last inn nltk
import nltk
from nltk.corpus import udhr
nltk.download("udhr")
from nltk import word_tokenize
nltk.download("punkt")



# last ned nynorsk- og bokmålkorpus og del opp i ord/tokens

nynorsk_tokens = [ord.lower() for ord in udhr.words("Norwegian_Norsk-Nynorsk-Latin1") if ord.isalpha()]
bokmål_tokens = [ord.lower() for ord in udhr.words("Norwegian_Norsk-Bokmal-Latin1") if ord.isalpha()]



# finn vokabulær i tekstene på nynorsk og bokmål

nynorsk_vokabulær = set(nynorsk_tokens)
bokmål_vokabulær = set(bokmål_tokens)


 # Ord som berre finst i éi målform

berre_nynorsk = nynorsk_vokabulær - bokmål_vokabulær
berre_bokmål = bokmål_vokabulær - nynorsk_vokabulær



# funksjon får å finne ut om ei tekst er på nynorsk, bokmål eller om det er uvisst

def målform(tekst):
   # del opp døme i ord
   tekst_tokens = set([ord.lower() for ord in word_tokenize(tekst) if ord.isalpha()])

   antal_nynorsk = sum(1 for ord in tekst_tokens if ord in berre_nynorsk)
   antal_bokmål = sum(1 for ord in tekst_tokens if ord in berre_bokmål)
 
   if antal_nynorsk > antal_bokmål:
      print(f"Dømet {tekst} er mest sannsyleg vis nynorsk :)")
   elif antal_bokmål > antal_nynorsk:
      print(f"Dømet {tekst} er mest sannsynleg vis bokmål :)")
   else:
    print(f"Eg er ikkje sikker på om dømet{tekst} er nynorsk eller bokmål :(")


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

     


