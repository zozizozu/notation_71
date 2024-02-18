# Notation 71 (0x47) - Proposition de nomenclature du sytème hexadecimal 
## Réflexion sur le BibiBinaire et la lisibilité des notations binaire, décimale et héxadécimale  

### Introduction
« Notation 71 », ou « Notation 0x47 », est une proposition de nomenclature qu’il faut voir comme une variante de la notation BibiBinaire de Boby LAPOINTE.

Injustement considéré comme une simple curiosité mathématique, le BibiBinaire apparaît comme une  réflexion profonde sur la lisibilité et la conversion d’une base à l’autre, permettant d’exprimer à la fois la valeur binaire et la valeur hexadécimale d’un chiffre.

La représentation du binaire et la notation graphique choisie par Boby LAPOINTE était cependant pour moi trop complexe, en cause un manque de connaissance des languages informatique (), aussi, j’ai voulu imaginer une notation utilisant un procédé similaire en incluant un sens de lecture des bits plus accessible.

### Description
La notation des chiffres de 0 à 15 sera donc basé sur une représentation de leur valeur binaire sur 4 bits.

Afin d’utiliser un sens de lecture commun à tous, je propose de se représenter les 4 chiffres binaires comme les 4 quart d’heure d’une horloge : le 1er  bit dans le 1er quart d’heure, le 2eme bit dans le 2eme quart d’heure, etc ...

Ainsi, pour le nombre 1, le binaire 0001 sera représenté <img src="/img/0001-horaire.png" width="64" height="64">


Chacun des 16 symboles sera construit avec 0, 1, 2, 3 ou 4 segments représentant la valeur de chaque bit.
 
Si le bit est positif, il sera noté par un segment troncant le quart de cercle (le 1/4 d’heure) correspondant, si le bit est négatif, on ne note rien.

Le chiffre 1 se représente donc : <img src="/img/1_nodir.png" width="32" height="32">


Si le binaire ne comporte qu’une seul bit positif, sa représentation ne comporte qu’une seul segment. 

Il sera donc possible, surtout en écriture manuscrite, de confondre 2 chiffres représentés par un segment de même orientation, dont seule change la disposition, comme 1 et 4 par example.

Afin d’ éviter cette confusion, si le symbole ne comporte qu’un seul segment, on marquera la 
direction de celui-ci, soit respectivement pour le 1 et le 4 : <img src="/img/1.png" width="32" height="32"> <img src="/img/4.png" width="32" height="32">


A l’inverse, si le binaire ne contient aucun bit positif, c’est à dire le zéro, l’absence de segment 
sera marquée par un disque plein : <img src="/img/0.png" width="32" height="32">


### Intérêts
Outre l’aspect pédagogique, cette notation permet de convertir très rapidement d’une base à l’autre, en assignant la valeur hexadécimale de chacun des 4 segments composant la figure : 

<img src="/img/8421.png" width="96" height="96">

Par exemple, la figure <img src="/img/7.png" width="32" height="32"> représente les valeurs 4 + 2 + 1 = 7

De même, la figure <img src="/img/13.png" width="32" height="32"> représente les valeurs 8 + 4 + 1 = 13

### Notes
Il ne s’agit que d'une proposition de nomenclature, nous garderons dans cet example la prononciation parfaitement cohérente du BibiBinaire.

Le nom de « Notation 71 » vient de la valeur hexadécimal de 71 qui se note 47, et se prononce « BOBI ».
 


### Proposition de représentation et de notation du BibiBinaire 
![Nomenclature de la notation 71.](/img/notation.png)
	

### Exemples

71 = 0x47 = BOBI = <img src="/img/4.png" width="32" height="32"><img src="/img/7.png" width="32" height="32"> 

16041922 = 0xF4C7C2 = DIBODOBIDOHE = <img src="/img/15.png" width="32" height="32"> <img src="/img/4.png" width="32" height="32"> <img src="/img/12.png" width="32" height="32"> <img src="/img/7.png" width="32" height="32"> <img src="/img/12.png" width="32" height="32"> <img src="/img/2.png" width="32" height="32">

20240218 = 0x134D75A = HAHIBODABIBACE = <img src="/img/1.png" width="32" height="32"> <img src="/img/3.png" width="32" height="32"> <img src="/img/4.png" width="32" height="32"> <img src="/img/13.png" width="32" height="32"> <img src="/img/7.png" width="32" height="32"> <img src="/img/5.png" width="32" height="32"> <img src="/img/10.png" width="32" height="32"> 






