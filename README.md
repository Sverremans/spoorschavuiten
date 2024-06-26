# Algoritmen en Heuristieken - RailNL
### Door Sipke de Boer, Massimo Carbone en Sverre van der Zalm a.k.a. De Spoorschavuiten

## Introductie

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

## Algoritmes

Dienstregelingen worden gegenereerd door verschillende algoritmes.
We hebben de volgende algoritmes gemaakt:
1. Random
2. Greedy
3. Depth-first
4. Greedy with lookahead
5. Hillclimber

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.12. Via de volgende instructies installeer je de packages die nodig zijn voor het runnen van onze code.

Allereerst, run je dit:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```
Voor Windows: om via matplotlib grafieken te tekenen run je:
```
sudo apt install python3-tk -y
```

### Gebruik

De algoritmes kunnen gerund worden door het aanroepen van:

```
python main.py
```

Met behulp van flags kunnen command line arguments worden toegevoegd. Specifiek kan dat als volgt:

```
options:
  -h, --help            show this help message and exit
  -a {Random,FixedRandom,Greedy,FixedGreedy,Termini_Greedy,GreedyLookAhead,HillClimber,HcStopCondition,Termini_HillClimber,DepthFirst}, --algorithm {Random,FixedRandom,Greedy,FixedGreedy,Termini_Greedy,GreedyLookAhead,HillClimber,HcStopCondition,Termini_HillClimber,DepthFirst}
                        Choose between Random, FixedRandom, Greedy, FixedGreedy, Termini_Greedy, GreedyLookAhead, HillClimber, HcStopCondition,
                        Termini_HillClimber, DepthFirst. Chooses HillClimber by default.
  -n NR_OF_RUNS, --nr_of_runs NR_OF_RUNS
                        Enter the number of runs. Chooses 1 by default.
  -s SEED, --seed SEED  Enter a seed for fixed algorithms. Chooses 1234 by default.
  -r {Holland,Nederland}, --railmap {Holland,Nederland}
                        Choose between Holland and Nederland. Chooses Holland by default.
  -tr MAX_TRAINS, --max_trains MAX_TRAINS
                        Enter the maximum number of trains. Chooses 7 for Holland and 20 for Nederland by default.
  -ti MAX_TIME, --max_time MAX_TIME
                        Enter the maximum time in minutes for the length of each train path. Chooses 120 for Holland and 180 for Nederland by default.
  -i ITERATIONS, --iterations ITERATIONS
                        Enter the number of iterations for the hillclimber algorithms. Chooses 100000 by default.
  -c CHANGES, --changes CHANGES
                        Enter the number of changes per iteration for the hillclimber algorithms. Chooses 2 by default.
  -ca CAP, --cap CAP    Enter the cap for HcStopCondition. Chooses 50000 by default.
```

Stel bijvoorbeeld dat het hillclimber algoritme met stopconditie dient te worden aangeroepen, waarbij het algoritme 200000 iteraties moet doen, tenzij er na 30000 iteraties geen verbetering is gevonden. Er worden maximaal 10 treinen ingepland, elk maximaal 100 minuten. De regio is Holland. Het algoritme moet 10 keer worden uitgevoerd, dat wil zeggen 10 keer een compleet nieuwe run. Er worden per iteratie 4 treinen opnieuw ingepland. Dit alles kan worden uitgevoerd door de volgende command line te runnen:

```
python3 main.py -a HcStopCondition -i 200000 -ca 30000 -tr 10 -ti 100 -r Holland -n 10 -c 4
```

Merk op dat het deel

```
-r Holland
```

eigenlijk overbodig is; Holland is de default value die wordt gekozen als de user niets specificeert.

## Hieronder oude README tekst
Met het bestand *distribution.py* worden het Random en Greedy algortime gerunt.
Het bestand is opgedeeld in verschillende stukjes code die resultaten genereren.
Met variabele *times* wordt aangegeven hoe vaak het algoritme herhaald moet worden, vervolgens wordt er een lege dienstergeling mee gegeven aan het algoritme.
Deze wordt daarna ingevuld door het algoritme, de score die de dienstregeling haalt wordt opgeslagen in een los bestand.
Als dit *times* keer wordt herhaald, bevat dit bestand dus ook *times* aantal behaalde scores.
Deze scores worden vervolgens gebruikt om een histogram en ee boxplot te kunnen maken.

Type in de terminal ***"python3 distribution.py"*** om deze code te laten runnen en data te genereren.
Dit zal resulteren in 4 csv bestanden:




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

