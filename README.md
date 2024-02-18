# Notation 71 - Proposition de nomenclature du sytème hexadecimal 
## Réflexion sur le BibiBinaire et la lisibilité des notations binaire, décimale et héxadécimale  

« Notation 71 » est une proposition de nomenclature qu’il faut voir comme une extension du BibiBinaire de Boby LAPOINTE.

Injustement considéré comme une simple curiosité mathématique, le BibiBinaire apparaît comme une  réflexion profonde sur la lisibilité et la conversion d’une base à l’autre, permettant d’exprimer à la fois la valeur binaire et la valeur hexadécimale d’un chiffre.

La notation graphique choisie par Boby LAPOINTE était cependant pour moi trop complexe et pas assez intuitive, aussi, j’ai voulu imaginer une notation en utilisant le même procédé, mais en y intégrant deux contraintes :
- Le sens de lecture des bits du binaire doit être intuitif
- La représentation symbolique d’un chiffre doit en exprimer clairement la valeur

La notation des chiffres de 0 à 15 sera donc basé sur une représentation de leur valeur binaire sur 4 bits.

Afin d’utiliser un sens de lecture commun à tous, je propose de se représenter les 4 chiffres binaires comme les 4 quart d’heure d’une horloge : le 1er  bit dans le 1er quart d’heure, le 2eme bit dans le 2eme quart d’heure,  le 3eme bit dans le 3eme quart d’heure, et le 4eme bit dans le 4eme quart d’heure.

Ainsi, pour le nombre 1, le binaire 0001 sera représenté <img src="/img/0001-horaire.png" width="64" height="64">


Chacun des 16 symbôles sera représenté par 0 à 4 segments, eux même représentant la valeur de chaque bit.
 
Si le bit est positif, il sera noté par un segment troncant le quart d’heure correspondant, si le bit est
 négatif, on ne note rien, ainsi le 1 se représente : <img src="/img/1_nodir.png" width="32" height="32">


Si le binaire ne comporte qu’une seul bit positif, sa représentation ne comporte qu’une seul segment. 

Il sera donc possible, surtout en écriture manuscrite, de confondre 2 chiffres représentés par un segment de même orientation, dont seule change la disposition, comme 1 et 4 par example.

Afin d’ éviter cette confusion, si le symbôle ne comporte qu’un seul segment, on marquera la 
direction de celui-ci, soit, respectivement pour le 1  et le 4 : <img src="/img/1.png" width="64" height="64"> <img src="/img/4.png" width="64" height="64">


A l’inverse, si le binaire ne contient aucun bit positif, c’est à dire le zéro, l’absence de segment 
sera marqué par un disque plein : <img src="/img/0.png" width="64" height="64">



Outre l’aspect pédagogique, une telle notation permet de convertir très rapidement d’une base à l’autre, en assignant la valeur hexadécimale de chacun des 4 segments composant la figure : <img src="/img/8421.png" width="64" height="64">

Par example, la figure <img src="/img/7.png" width="64" height="64"> vaudra  4 + 2 + 1 = 7

De même, la figure <img src="/img/13.png" width="64" height="64"> vaudra  8 + 4 + 1 = 13


Encore une fois, il ne s’agit que de nomenclature, la prononciation du BibiBinaire étant parfaitement cohérente.

Le nom de « Notation 71 » vient de la valeur hexadécimal de 71 qui se note 47, et se prononce « BOBI ».
 



Proposition de représentation et de notation du BibiBinaire 
![Nomenclature de la notation 71.](/img/notation.png)
	

