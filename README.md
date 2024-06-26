# Algoritmen en Heuristieken - RailNL
### Spoorschavuiten: Sipke de Boer, Massimo Carbone en Sverre van der Zalm

### Introductie

Wij hebben gekozen om voor het vak Algoritmen en Heuristieken, de case RailNL uit te werken.

De opdracht was simpel, creeër een dienstregeling voor de spoorwegen in Holland en Nederland met een zo'n hoog mogelijke score.
Om dit te doen wordt er gebruik gemaakt van een bepaalde terminologie:
- dienstregeling = alle trajecten in een regio bij elkaar
- regio = Holland of Nederland, en alles stations en verbindingen die zeze bevat.
- traject = alle verbindingen die een trein berijdt, een traject kan niet langer duren dan de maximale tijd.
- verbinding = het stuk spoor tussen twee stations
- maximale tijd = de maximale tijd die een trein mag rijden, voor Holland is dit 120 minuten, voor Nederland is dit 180 minuten.

Deze score wordt met de volgende formule berekent:

**S = p * 10000 - (T * 100 + min)**

Voor **'p'** wordt een fractie van het aantal gebruikte verbindingen gebruikt.

Voor **'T'** wordt het aantal gebruikte treinen in gevuld. 
Het maximaal aantal treinen dat mag gebruikt worden in Holland is 7, voor Nederland is dit maximale aantal 20 treinen.

Als laatste wordt voor **'min'** het totale aantal minuten ingevoerd dat alle gebruikte treinen bezig zijn om alle verbindingen in hun traject te berijden.


Door gebruik te maken van verschillende algoritmes worden mogelijke dienstregelingen gemaakt en er wordt een score berekend.

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```

### Gebruik

Een voorbeeldje kan gerund worden door aanroepen van:

```
python main.py
```

Het bestand geeft een voorbeeld voor gebruik van de verschillende functies.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de bokeh code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren


Wij werken met verschillende scripts om de verschillende algoritmen te laten runnen.


Met het bestand *distribution.py* worden het Random en Greedy algortime gerunt.
Het bestand is opgedeeld in verschillende stukjes code die resultaten genereren.
Met variabele *times* wordt aangegeven hoe vaak het algoritme herhaald moet worden, vervolgens wordt er een lege dienstergeling mee gegeven aan het algoritme.
Deze wordt daarna ingevuld door het algoritme, de score die de dienstregeling haalt wordt opgeslagen in een los bestand.
Als dit *times* keer wordt herhaald, bevat dit bestand dus ook *times* aantal behaalde scores.
Deze scores worden vervolgens gebruikt om een histogram en ee boxplot te kunnen maken.

Type in de terminal ***"python3 distribution.py"*** om deze code te laten runnen en data te genereren.
Dit zal resulteren in 4 csv bestanden:
- 



In *run_hillclimber.py* wordt het Hill Climber algoritme gerunt.
Ook hier is gebruik gemaakt van verschillende blokjes code om verschillende resultaten te gegereren.
Als eerst wordt een random dienstregeling gemaakt door middel van het Random algoritme.
Deze dienstregeling wordt vervolgens meegegeven aan het Hill Climber algoritme.
De eerste twee blokjes code maken gebruitk van het Hill Climber Stop Condition algoritme.
Dit algortime gaat op zoek naar een verbeterde dienstregeling door een vooraf aangegeven aantal treinen uit de dienstregeling te verwijderen.
Hierna worden deze treinen opnieuw ingepland, als de nieuwe score hoger is word de nieuwe dienstregeling opgeslagen, als de nieuwe score niet hoger wordt de oude dienstregeling bewaard.
Vervolgens wordt dit opnieuw gedaan, het Hill Climber Stop Condition algoritme stop wanneer het algoritme 10000 (of een zelf gekozen aantal iteraties) iteraties geen verbetering van het schema heeft gevonden.

Het laatste blokje code gebruikt het Hill Climber algoritme.
Deze werkt hetzelfde aleen stop deze nadat het algoritme *1000000* (of zelf nader te bepalen) iteraties is uitgevoerd.

Van alle resultaten wordt de output, score en routes opgeslagen in losse bestanden. Deze data kan vervolgens worden gebruikt om de kaart met alle treinen te tekenen, of te laten zien op welke iteraties het Hill Climber algoritme een verbeterig heeft gevonden.

Type in de terminal ***"python3 run_hillclimber.py"*** om deze code te laten runnen en data te genereren.

In *run_depthfirst.py*

Random Algoritme

Greedy Algoritme

Hill Climber Algoritme

Depth First Algoritme

