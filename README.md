# Kriptovalute
## Projektna naloga pri predmetu UVP
### O projektu
Namen uporabe te projektne naloge je, da uporabniku omogoča ustvarjanje portfeljev, na katere dodaja resnične kripto kovance.
Program je sposoben iz interneta prebrati trenutno trgovalno ceno kovancev, ki jih je uporabnik dodal na svoje portfelje in 
izračunati trenutne vrednosti količin kovancev kot tudi vrednost celotnega portfelja uporabnika.

### Navodila za uporabo
- Pred prvo uporabo programa je potrebno namestiti modul yahoofinancials, kar najlažje storite z ukazom pip. Podobnejša navodila najdete na strani: https://pypi.org/project/yahoofinancials/
- Uporabnik naj iz githuba prenese vse datoteke iz repozitorija in odpre ter požene datoteko tekstovni_vmesnik.py. V terminalu se bo začelo izvajanje programa, tam pa bodo tudi vidna nadaljna navodila kao uporabljati program.
- Ko uporabnik zaključi z izvajanjem programa se narejene spremembe shranijo v json datoteko in so uporabniku vidne ob naslednji uporabi.

### Neprijetnosti ob uporabi
Posledica tega, da program podatke o trenutnih cenah pridobiva iz interneta je, da mora uporabnik (relativno dolgo) čakati na prikaz vrednosti portfeljev. 

Program je bil zamišljen z dodelanim spletnim vmesnikom, ki bi bil uporabniku bolj prijazen, vendar tega nisem do konca izvedel. Če ima kdo izrecno željo lahko pobrska po repozitoriju in poišče datoteko spletni_vmesnik.py in pripadajoče datoteke ter jo požene in vidi delujoče preprostejše funkcije programa.