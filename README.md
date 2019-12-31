# Mašinsko učenje: Implementacija ID3 algoritma u programskom jeziku Python

**1. Predlog problema:**

Klasifikacija životinja prema osobinama i donošenje odluke da li je neka vrsta opasna. Očekuje se da svi ulazni podaci dataset-a budu dodati u `dataset.csv`. Potrebno je unositi vrednosti za više kolona.

#### Atributi
Atributi koji se koriste u dataset fajlovima su ograničeni i treba da budu konkretnih vrednosti. Kako se opisuju životinje, skup tih opisnih atributa dat je u u nastavku.

    size: small, medium, large
    sharp teeth: yes, no
    feet: yes, no
    habitat: land, water
    domesticated: yes, no
    dangerour: yes, no
    
*Podaci treba da budu jedinstveni i da se formiraju po potrebi* na osnovu stvarnih smislenih primera, u suprotnom algoritam neće formirati smislena stabla odluke.

#### Dataset fajlovi
Svaki fajl treba da ima listu primera gde je svaki u posebnoj liniji. Primer je skup atributa odvojenih zarezom gde svaka vrednost treba da odgovara listi atributa.

    snake:small,yes,no,land,no,yes
    bear:medium,yes,yes,land,no,yes
    deer:medium,no,yes,land,no,no
    
Redosled primera može da se menja pre pokretanja algoritma (za neke primere podataka ovo može da ima značaja na rezultat, u većini slučajeva ne).


**2. Problem za primenu ID3 algoritma:**

Primenom ID3 algoritma može se dobiti stablo odluke na osnovu priloženog skupa ulaznih podataka. Ovakvo stablo se zatim može koristiti za klasifikaciju novih objekata koji nisu u polaznom skupu. Stablo odluke je jedan od načina rešavanja ovakvih problema klasifikacija i ovaj metod se oslanja na učenje algoritma na osnovu polaznog skupa podataka.

**3. Implementacija ID3 algoritma:**

Za implementaciju algoritma koriste se samo osnovne biblioteke Python okruženja. S obzirom na složenost problema nije neophodno koristiti open-source biblioteke.

**3.1. Parametri ID3 algoritma:**

Važni ulazni argumenti algoritma su parametrizovani.

1. **main_attr** - ime kolone koja predstavlja odlučujuči atribut - *dangerous*
2. **main_dataset_csv** - ime fajla ili potpuna putanja do ulaznih podataka - *dataset.csv*

Na slikama se može videti rezultat algoritma u obliku stabla, a pre toga i skup ulaznih podataka. Skup podataka, odnosno *dataset*, učitava se iz fajla.
 
![alt text][screenshot_dataset]

[screenshot_dataset]: metadata/screenshot_dataset.png

U konzolnom prozoru se nakon **formiranja stabla ono i prikazuje**. Zatim, korisnik može da unese do tada nepostojeći objekat popunjen na isti način kao i ostali objekti dataseta. Taj objekat se **klasifikuje** i prikazuje **rezultat po formiranom stablu**. 

![alt text][screenshot_tree]

[screenshot_tree]: metadata/screenshot_tree.png

## Implementacioni detalji

### Inicijalizacija i metoda `build_tree`

Pre bilo kakve klasifikacije potrebno je formirati stablo odluke. Ulazni podaci se učitavaju iz fajla, formira se *dataframe* i prosledjuje ovo metodi. Dataframe će za svaku od kolona, odnosno atributa, imati polje niza svih dodatih vrednosti.

```python
def main():
    dataframe = pandas.read_csv(main_dataset_csv)
    d3_tree = build_tree(dataframe)
    ...
  
if __name__== "__main__":
  main()
```

### Nalaženje entropije i metoda `find_entropy`

...

### Nalaženje entropije atributa i metoda `find_entropy_attribute`

...
