# Le modèle de Von Neumann

## Historique

La machine de Von Neumann à été créée en juin 1945 par John von Neumann (un
mathématicien) en travaillant sur le projet EDVAC, qui était un des tout
premiers ordinateurs éléctroniques, conçu comme l'ENIAC pour répondre aux besoins
du laboratoire de recherche en balistique de l'US Army.

## Architecture

L’architecture de von Neumann décompose l’ordinateur en 4 parties distinctes :

* L'unité arithmétique et logique ( ou unité de traitement ) dont le rôle est
d'effectuer les opérations de base.

* L’unité de contrôle, chargée du « séquençage » des opérations.

* La mémoire qui contient à la fois les données et les instructions qui indiquera
à l’unité de contrôle quels sont les calculs à faire sur ces données.
La mémoire se divise entre mémoire volatile (programmes et données en cours de
fonctionnement) et mémoire permanente (programmes et données de base de la machine).

* Les dispositifs d’entrée-sortie, qui permettent de communiquer avec le monde
extérieur.

De nos jour, longtemps après son invention, le modèle d’architecture de
von Neumann régit toujours l’architecture des ordinateurs.

## Evolution

On peut cependant noter deux évolution:

* Les ordinateurs possèdent maintenant de multiples processeurs, qu'ils s'agisse
de "coeurs" à l'intérieur d'une même puce ou d'unités séparées, ce qui a permis
d'atteindre une puissance globale de calcul élevée.

* Les entrées-sorties, sont depuis le début des années 1960 sous le contrôle
de processeurs autonomes. Associée à la multiprogrammation (partage de la mémoire
entre plusieurs programmes), cette organisation a notamment permis le développement
des systèmes en temps partagé.

Ces deux évolutions font que la mémoire prenne plus d'importance, mais ne remettent
pas en cause les principes de base que sont la séparation entre traitement et
commande.
