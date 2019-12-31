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

Svi ulazni argumenti algoritma su parametrizovani.

1. **xyz** -
2. **xyz** -
3. **xyz** -
4. **xyz** -
5. **xyz** -
6. **xyz** -
7. **xyz** -

Na slikama se može videti rezultat algoritma u obliku stabla, a pre toga i skup ulaznih podataka. Skup podataka, odnosno *dataset*, učitava se iz fajla.
 
![alt text][screenshot_dataset]

[screenshot_tree]: metadata/screenshot_dataset.png

U konzolnom prozoru se nakon **formrianja stabla ono i prikazuje**.

![alt text][screenshot_tree]

[screenshot_dataset]: metadata/screenshot_tree.png

## Implementacioni detalji
