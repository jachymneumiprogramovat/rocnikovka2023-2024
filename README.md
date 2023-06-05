# Rocnikovka2023-2024
Repo na sdílení dílčích pokroků pro moji ročníkovou práci
Obsahuje jednu složku na samotnou práci a druhou na simulátor.
Hlavním smyslem je simulovat míček co s nenulovou úhlovou rychlostí dopadá na povrch a od něj se odráží. Určit směr, kterým se odrazí a další vlastnosti odrazu.

# Preciznější popis:

Jaký jev pozorujeme:
Například u stolního tenisu si můžeme všimnout jednoho zajímavého jevu. Když má
míček nenulovou úhlovou rychlost může se stát, že po odrazu se jeho rychlost po
x-ové souřadnici obrátí. Nemusí mít stále stejnou velikost, ale její směr se
obrátí -> začne se vracet.

Cílem této práce je popsat jaké veličiny hrají roli v tom jestli se míček
odrazí nebo ne. Vzhledem k tomu, že úhlová rychlost je charakteristická pro
tento jev rád bych tedy vyjádřil výsledek jako:
pro tuto úhlovou rychlost musí mít míček také
-takovou rychlost
-takovýto úhel dopadu
-takovýto koeficient tření mezi ním a povrchem na který dopadá
Tedy ten fakt jestli se odrazí nebo ne formuloval jako funkci úhlové rychlosti.

Moje výzkumná metoda bude naprogramování simulátoru, který mi pomůže ověřit
mojí hypotézu. Všechny rovnice, které budou v mém simulátoru budou popsané v
teoretické části mé práce

Při zkoumání tohoto jevu je také možné,že budu schopný popsat jak y-novou tak
x-ovou složku rychlosti míčku po jeho odrazu. Ty v závěru zmínim, ale hlavním
téma práce je stále vyjádřit otočení x-ové složky pohybu po odrazu jako funkci
úhlové rychlosti.

# Roadmap

## Teoretická část:
- [ ] Motivace/pozorování
    * Pozorování tohoto efektu specificky při stolním tenisu
- [ ] Hypotéza
    * Jaké veličiny hrají roly
    * Jaké veličiny jsou přímo a jaké nepřímo uměrné
- [ ] Vliv různých veličin na tělesa v pohybu
    * Tření vzduchu
        * Statický vzduch
        * Vzduch s vlastní energií
    * Magnus efekt
- [ ] Typy odrazu
    * Deformace při odrazu
    * Přenos energie
    * Vliv rotace na odraz
- [ ] Popis simulátoru
    * Obecně simulování
      * Validita dat
    * Základní idea algoritmů
- [ ] Interpretace dat ze simulátoru
    * Obsáhlý popis celého systému
    * Potvrzení/vyvrácení hypotézy
- [ ] Závěr
    * Teorie vs. Praxe
    * Správnost hypotézy
    * Vedlejší jevy a jejich rovnice

## Praktická část:
- [ ] Dobrá kreslící knihovna
- [ ] Obecné třídy
   - [ ] Detekce kolize 
- [ ] Zrychlení a rychlost na základě sil
- [ ] Rovnice, které musí systém splňovat
- [ ] Debugging... :(


