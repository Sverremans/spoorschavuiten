# Spoorschavuiten 
#### Sipke "achternaam", Massimo "achternaam" en Sverre van der Zalm
## Algoritmen en Heuristieken - RailNL

Wij hebben gekozen om voor het vak Algoritmen en Heuristieken, de case RailNL uit te werken.

De opdracht was simpel, creeër een dienstregeling voor de spoorwegen in Holland en Nederland.


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

