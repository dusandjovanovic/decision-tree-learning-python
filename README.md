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

#### Formirano stablo odluke

__Terminalni__ čvor treba da bude predstavljen kao:

    <klasifikacija>

Ovo je primer formiranog stabla na osnovu primera ulaznog skupa podataka:

    Sharp
        |
        ->no
        |  |
        |  ->Size
        |     |
        |      ->large
        |      |   |
        |      |   -><NO>
        |      |
        |      ->medium
        |      |    |
        |      |   ->Feet
        |      |       |
        |      |       ->no 
        |      |       |   |
        |      |       |   ->Habitat
        |      |       |       |
        |      |       |       ->land
        |      |       |       |   |
        |      |       |       |   -><NO>
        |      |       |       |
        |      |       |       ->water
        |      |       |           |
        |      |       |           -><YES>
        |      |       |
        |      |       ->yes
        |      |           |
        |      |           -><NO>
        |      |
        |      |           
        |      |
        |      ->small
        |          |
        |          -><NO>
        |
        ->yes
           |
           ->Domesticated
                |
                ->no
                |   |
                |   -><YES>
                |
                ->yes
                |   |
                |   -><NO>
                |


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

U konzolnom prozoru se nakon **formiranja stabla ono i prikazuje**. Zatim, generiše se novi objekat popunjen poput ostalih objekata dataseta. Taj objekat se **klasifikuje** i prikazuje **rezultat po formiranom stablu** - odnosno vrši se predikcija po stablu. 

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
  
def build_tree(dataframe, tree = None):
    Class = dataframe.keys()[-1]

    node = find_winner(dataframe)
    att_value = numpy.unique(dataframe[node])

    if tree is None:
        tree = {}
        tree[node] = {}

    for value in att_value:
        subtable = get_subtable(dataframe, node, value)
        cl_value, counts = numpy.unique(subtable[main_attr], return_counts = True)

        if len(counts) == 1:
            tree[node][value] = cl_value[0]
        else:
            tree[node][value] = build_tree(subtable)

    return tree
```

`buld_tree` je rekurzivna metoda koja će izgraditi stablo odluke. U svakom koraku se poziva pomoćna metoda `find_winner` za nalaženje čvora koji će se dodati u razmatranom koraku algoritma. Ova pomoćna metoda treba da pretraži sve ključeve, odnosno atribute i pronadje razliku entropije i entropije konkretnog atributa. Zatim, treba razmatrati nadjeni pobednički čvor i njegove moguće vrednosti.

```python
find_entropy(dataframe) - find_entropy_attribute(dataframe, key)
```

Nakon što se pobednički čvor pronadje, treba naći pod-tabelu koja isključuje vrednosti atributa tog čvora. Ovakva pod-tabela je zatim iskorišćena za rekurzivan poziv `buld_tree` metode.

### Nalaženje entropije i metoda `find_entropy`

```python
def find_entropy(dataframe):
    Class = dataframe.keys()[-1]
    entropy = 0
    values = dataframe[Class].unique()
    for value in values:
        fraction = dataframe[Class].value_counts()[value] / len(dataframe[Class])
        entropy += -fraction * numpy.log2(fraction)
    return entropy
```

Entropija celog skupa podataka je mera nesigurnosti tih podataka. Računa se nad celim dataset-om po dobro poznatoj formuli i obuhvata sve atribute.

### Nalaženje entropije atributa i metoda `find_entropy_attribute`

Entropija atributa odnosi se na *Information gain* vrednost, odnosno efektivnu promenu entropije nakon odlučivanja. Dobitak informacija se ogleda u relativnoj promeni entropije, pritom razmatrajući jedan od atributa.

Tehnički, predstavlja **smanjenje entropije do koga dolazi kada se dataset podeli po atributu**. Osnovna ideja formiranja stabla odluke upravo se dešava ovde. U metodi `buld_tree` se nalazi pobednički čvor za koji će se dobiti najveća povratna vrednost metode `find_entropy_attribute`, odnosno čvor sa najvećom *Information gain* vrednošću. Atribut koji definiše takav čvor će biti **sledeći odlučujući čvor**.

```python
def find_entropy_attribute(dataframe, attribute):
    Class = dataframe.keys()[-1]
    target_variables = dataframe[Class].unique()
    variables = dataframe[attribute].unique()
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(dataframe[attribute][dataframe[attribute] == variable][dataframe[Class] == target_variable])
            den = len(dataframe[attribute][dataframe[attribute] == variable])
            fraction = num / (den + epsilon)
            entropy += -fraction * numpy.log2(fraction + epsilon)
        fraction2 = den / len(dataframe)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)
```

### Klasifikacija i metoda `predict`

Predikcija, odnosno klasifikacija novonastalog objekta, može se tražiti nakon formiranja stabla. Primer predikcije je bez unošenja atributa sa ulaza, već sa predefinisanim vrednostima kao što se može videti u kodu.

Rezultat predikcije je terminalni čvor `<YES>` ili `<NO>`, različite vrednosti u zavinosti od čvorova odluke formiranog stabla. Ovo je rekurzivna metoda koja prolazi kroz celo stablo, sve do jednog od terminalnih čvorova.

```python
def predict(attributes, tree):
    node = tree
    if type(node) is dict:
        for key in node.keys():
            x = node[key]
            y = x[attributes[key]]
            predict(attributes, node[key][attributes[key]]);
    else:
        print(f'\nSample for prediction: {attributes}.')
        print(f'\nPrediction for entered values is {node}.\n')


attributes = {
    "size": "medium",
    "sharp": "no",
    "feet": "yes",
    "habitat": "land",
    "domesticated": "no"
}

predict(attributes, d3_tree)
```
