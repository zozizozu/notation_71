# Notation 71 (0x47) - Proposition de nomenclature du sytème BibiBinaire 
## Réflexion sur la lisibilité des notations binaire, décimale et héxadécimale  

### Introduction
« Notation 71 », ou « Notation 0x47 », est une proposition de nomenclature qu’il faut voir comme une variante de la notation du BibiBinaire de Boby LAPOINTE (_Brevet d'invention no 1.569.028, Procédé de codification de l'information, Robert Jean Lapointe, délivré le 21 avril 1969_).

Injustement considéré comme une simple curiosité mathématique, le BibiBinaire apparaît comme une  réflexion profonde sur la lisibilité et la conversion d’une base à l’autre, permettant d’exprimer à la fois la valeur binaire et la valeur hexadécimale d’un chiffre.

La représentation du binaire et la notation graphique choisie par Boby LAPOINTE était cependant pour moi trop complexe, en cause un manque de connaissance des languages informatique, aussi, j’ai voulu imaginer une notation utilisant un procédé similaire en incluant un sens de lecture des bits plus accessible.

### Description
La notation des chiffres de 0 à 15 sera donc basée sur une représentation de leur valeur binaire sur 4 bits.

Afin d’utiliser un sens de lecture commun à tous, je propose de se représenter les 4 chiffres binaires comme les 4 quart d’heure d’une horloge, le bit le plus faible dans le premier quart d'heure, le 2eme bit dans le 2eme quart d’heure, ..., et le dernier bit, le plus fort, dans le 4eme quart.

Ainsi, pour le nombre 1, le binaire 0001 sera représenté <img src="/img/0001-horaire.png" width="48" height="48">

Chacun des 16 symboles sera construit avec 0, 1, 2, 3 ou 4 segments représentant la valeur de chaque bit.
 
Si le bit est positif, il sera noté par un segment tronquant le quart de cercle (le 1/4 d’heure) correspondant, si le bit est négatif, on ne note rien.

Si aucun bit n'est positif, c’est à dire pour le zéro, l’absence de segment sera marquée par un disque : <img src="/img/0.png" width="32" height="32">

Le chiffre 1 se représente donc avec un segment tronquant le quart supérieur droit: <img src="/img/0001-horaire.png" width="48" height="48"> : <img src="/img/1_nodir.png" width="32" height="32">

Le chiffre 2 se représente avec un segment tronquant le quart inferieur droit: <img src="/img/0010-horaire.png" width="48" height="48"> : <img src="/img/2_nodir.png" width="32" height="32"> 

Le 3 se représente avec les 2 segments representant le 1 et le 2 : <img src="/img/0011-horaire.png" width="48" height="48"> : <img src="/img/3.png" width="32" height="32">

Si le binaire ne comporte qu’un seul bit positif, sa représentation ne comporte qu’une seul segment. 

Il sera donc possible de confondre 2 chiffres représentés par un segment de même orientation, dont seule change la disposition, comme 1 et 4 par example.

Afin d’ éviter cette confusion, si le symbole ne comporte qu’un seul segment, on marquera la 
direction "horaire" de celui-ci (du bit le plus faible au bit le plus fort), soit respectivement pour le 1 et le 4 : <img src="/img/1.png" width="32" height="32"> et <img src="/img/4.png" width="32" height="32">


### Intérêts
Outre l’aspect pédagogique, cette notation permet de convertir très rapidement d’une base à l’autre, en assignant la valeur de chacun des 4 segments composant la figure : 

<img src="/img/8421.png" width="96" height="96">

Par exemple, la figure <img src="/img/6.png" width="32" height="32"> représente les bits 0110, soit 0 + 2 + 4 + 0

De même, la figure <img src="/img/7.png" width="32" height="32"> représente les bits 0111, soit 1 + 2 + 4 + 0

### Notes
Il ne s’agit que d'une proposition de nomenclature, une variante simplifiée de la notation du BibiBinaire.

Le nom de « Notation 71 » vient de la valeur hexadécimal de 71 qui se note 47, et se prononce « BOBI » (parceque DIBODOBIDOHE c'était trop long, mais c'est quand même vachement bien).
 

### Proposition de représentation et de notation du BibiBinaire 
![Nomenclature de la notation 71.](/img/notation.png)
	

### Exemples

71 = 0x47 = BOBI = <img src="/img/4.png" width="32" height="32"><img src="/img/7.png" width="32" height="32"> 

256 = 0x100 = HAHOHO = <img src="/img/1.png" width="32" height="32"><img src="/img/0.png" width="32" height="32"><img src="/img/0.png" width="32" height="32">

16041922 = 0xF4C7C2 = DIBODOBIDOHE = <img src="/img/15.png" width="32" height="32"><img src="/img/4.png" width="32" height="32"><img src="/img/12.png" width="32" height="32"><img src="/img/7.png" width="32" height="32"><img src="/img/12.png" width="32" height="32"><img src="/img/2.png" width="32" height="32">

20240218 = 0x134D75A = HAHIBODABIBACE = <img src="/img/1.png" width="32" height="32"><img src="/img/3.png" width="32" height="32"><img src="/img/4.png" width="32" height="32"><img src="/img/13.png" width="32" height="32"><img src="/img/7.png" width="32" height="32"><img src="/img/5.png" width="32" height="32"><img src="/img/10.png" width="32" height="32"> 


### Le Bibi du bout des doigts
Pour compter en hexadécimal sur les doigts, nous pouvons nous baser sur le sytème de numération duodécimal (base 12) des celtes, qui utilisaient le pouce pour pointer les 3 phalanges des 4 autre doigts (3 * 4), en y ajoutant le sommet de chaque doigt comme 4eme repère pour une numération hexadécimale (4 * 4 = base 16).

Le sommet de l'ongle sur le 1er doigt représente le zéro, suivent les 3 phalanges, la 1ere pour le 1, la 2eme pour le 2 et la 3eme pour le 3.

Le sommet de l'ongle sur le 2eme doigt représente le 4, la 1ere phalange du 2nd doigt représente le 5, ..., jusqu'à la dernière phalange du dernier doigt qui représente le 15. 

On passe ensuite à la 2nde main pour marquer les "seizaine", ainsi jusqu'à 255.


#### Compter 

#### Additionner

#### Multiplier




