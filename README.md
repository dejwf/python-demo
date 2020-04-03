# README for Pavel

## na instalaci vsech zavislosti (knihoven a tak), pouzij nasledujici prikaz
### (ten dollar $ se pise, aby bylo jasne, ze se to ma pustit z prikazoveho radku, konkretne z bash'e, tj typ prikazoveho radku, ktery je implementovany pro linux, ale pokud neni receno jinak, tak to funguje i pro windows cmd)
$ pip install -r requirements.txt

## po dotazeni zavislosti staci pustit 
$ behave

## a jak to vlastne funguje:
kdyz se podivas do struktury toho projektu, tak bys mel videt priblizne tohle

geckodriver-v0.26.0-win64
README.md
requirements.txt
features\search.feature
features\steps\google.py


vlastne to dela to samy, co ti delal ten main.py, ale ted je to trochu rozhazene,
aby to odpovidalo nejake stabni kulture (slysel jsi nekdy o cucumber'u? Jestli jo, tak 'behave' je implementace
cucumber'u pro python). Ten behave jako takovy, zadny zazraky nedela, ale slouzi k tomu, aby se v tom spolupracovnici
lepe orientovali. No a tohleto ma jeste jednu vyhodu v tom, ze testovaci scenare jsou napsane "lidsky" (koukni na soubor features\search.feature ), tj ne-technicky kolega by tomu mel taky rozumet. Ten text z .feature souboru se hleda v souborech v features\steps\* , kde zrovna v tomto pripade ve features\steps\google.py najde nejakou funkci (v pythonu zacinaji funkce keywordem "def" jako definition),  ktera ma anotaci @step(), kdy ten @step ma v sobe string, ktery je shodny s tim puvodnim textem. No a ten behave prikaz vi poradi kroku ve scenari a postupne pousti funkce s odpovidajici anotaci.

Tak, tady v tom miste by te mozna mohlo zajimat, ze to Selenium v tom zas tak velkou roli nehraje. To je tim, ze testovani browseru neni to jednine, co se automatizuje a spis by se dalo rict, ze i kdyz to tak nevypada, tak se prevazne automatizuji APIcka, data processing (transformace dat), ruzne vnitrni komponenty softwareu (napr. modul XY ma vstup pro CSV soubor a vystupem ma byt obrazek) a pod. No a prave proto je to Selenium v tomto projekte doinstalovane a neni puvodni soucasti toho behave. Ty, jakozto QA, si uz pak rozhodnes, co vlastne chces automatizovat.... 

Ty browsery byvaji nejsnaze pochopitelne, takze to dela vetsina QA automatizatoru, ale je to peknej voser a kdyz to jde udelat pres API, tak se to dost casto dela tak, ze udelas nejaky smoke test na uspesny login, nejakou snazsi interakci a tak a pak zbytek toho, co jde, se pokusis udelat pres API cally a ruzne DB machinace a tak ( zalezi, co ti ve firme projde)


