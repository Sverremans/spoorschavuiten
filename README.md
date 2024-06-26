# Algoritmen en Heuristieken - RailNL
#### Door Sipke de Boer, Massimo Carbone en Sverre van der Zalm a.k.a. De Spoorschavuiten

## Introductie

Wij hebben gekozen om voor het vak Algoritmen en Heuristieken de case "RailNL" uit te werken.

De opdracht was simpel: creëer een zo goed mogelijke dienstregeling van spoorwegen voor twee gebieden: (Noord- en Zuid-)Holland en Nederland. Hoe goed een dienstregeling is wordt aangeduid met een doelfunctie. Des te hoger de score, des te beter. De score wordt met de volgende formule berekend:

$$S = p * 10000 - (T * 100 + min)$$

Hier is $p$ de fractie van aantal gebruikte verbindingen over totale aantal verbindingen, $T$ het aantal gebruikte trajecten en $min$ de totale duur in minuten van alle trajecten samen.

Hier volgt uitleg over de terminologie om de case te verduidelijken:
- Regio = Holland of Nederland, met alle bijbehorende stations en verbindingen.
- Verbinding = het stuk spoor tussen twee stations. Kan in beide richtingen bereden worden.
- Traject = alle verbindingen die een trein berijdt. Een traject kan niet langer duren dan de maximale tijd.
- Dienstregeling = alle trajecten in een regio bij elkaar.
- Maximale tijd = de maximale tijd die één trein mag rijden.

Verder zijn er een aantal vereisten voor de dienstregelingen, namelijk: het maximaal aantal trajecten dat gebruikt mag worden in **Holland** is **7** met een maximale duur van **120 min**. Voor **Nederland** is dit maximale aantal **20** met een maximale duur van **180 min**.

## Algoritmes

Om een zo goed mogelijke dienstregeling voor beide regio's te maken hebben we algoritmes gebruikt die deze genereren. We hebben de volgende algoritmes gemaakt:
- Random - Deze voegt trajecten toe aan de dienstregeling op een volledige willekeurige manier. Startend vanaf een random station volgt de trein een random traject van aaneengeschakelde verbindingen. 
- Greedy - Deze voegt trajecten toe aan de dienstregeling op een greedy manier. Dat betekent dat de verbindingen die gekozen worden bij voorkeur onbereden zijn. Als die niet aanwezig zijn vanaf een bepaald station, dan wordt er willekeurig een al bereden verbindingen gekozen. Startstations zijn nog steeds random gekozen.
    - Termini Greedy - Een variant van de Greedy die niet willekeurig startstations uitkiest. Eerst worden kopstations (stations met slechts één verbinding) gebruikt, daarna zal het uitkiezen weer willekeurig gaan.
- Depth-first - Een zoekalgoritme dat alle mogelijke configuraties van een traject doorzoekt en 
    de hoogst scorende toevoegt aan de dienstregeling.
    - Greedy Lookahead - Een variant van de Depth-first die een tak van configuraties voortijdig snoeit als er na het instellen van $x$ aantal verbindingen geen nieuwe verbinding wordt gekozen. Die $x$, de lookahead, stel je zelf in.
- Hillclimber - Deze neemt een ingevulde dienstregeling en plant steeds $n$ treinen opnieuw in. Slaat verbeteringen op en gooit verslechteringen weg. 
    - Hillclimber Stop Condition - Een variant van de Hillclimber die na een vast aantal iteraties waar geen verbetering is gevonden het algoritme stopt.
    - Termini Hillclimber - Een variant van de Hillclimber waarbij een Termini Greedy algoritme wordt gebruikt bij
    het inplannen van een nieuwe trein in plaats van een Greedy.
 
## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.12. Via de volgende instructies installeer je de packages die nodig zijn voor het runnen van onze code.

Allereerst dient dit command gerund te worden:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```
Voor Windows, om via matplotlib grafieken te kunnen tekenen run je:
```
sudo apt install python3-tk -y
```

### Gebruik

De algoritmes kunnen gerund worden door het aanroepen van:

```
python main.py
```

Met behulp van flags kunnen command-line arguments worden toegevoegd. Specifiek kan dat als volgt:

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
  -l LOOKAHEAD, --lookahead LOOKAHEAD
                        Enter the value of the lookahead parameter for the GreedyLookAhead algorithm. Chooses 3 by default.
```

>Bijvoorbeeld: stel dat het hillclimber-algoritme met stopconditie dient te worden aangeroepen, waarbij het algoritme *200000* *iteraties* moet doen, tenzij er na *30000* *iteraties* geen verbetering is gevonden. Er worden maximaal *10* *treinen* ingepland, elk maximaal *100 minuten*. De regio is *Holland*. Het algoritme moet *10 keer* worden uitgevoerd, dat wil zeggen *10 keer* een compleet nieuwe run. Er worden per iteratie *4* *treinen* opnieuw ingepland. Dit alles kan worden uitgevoerd door de volgende command-line te runnen:
>```
>python3 main.py -a HcStopCondition -i 200000 -ca 30000 -tr 10 -ti 100 -r Holland -n 10 -c 4
>```
>Merk op dat het deel `-r Holland` eigenlijk overbodig is; Holland is de default value die wordt gekozen als de user niets specificeert.
