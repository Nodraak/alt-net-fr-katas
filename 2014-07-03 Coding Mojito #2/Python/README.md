## Binding en python 2.x

Je connais pas le C#, alors voici une reecriture du code en python.

Pour le moment :

* Une classe MazeCore : comme son nom l'indique : la base
* Des classes MazeBuilder : pour initialiser des laby
* Des classes MazeSolver : solver

Exemple d'utilisation (via le terminal, la fleme de faire une gui) :

````shell 
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from MazeBuilderSimple import MazeBuilder // on importe le builder
>>> from MazeSolverStupid import MazeSolverStupid // on importe le solver
>>> n=MazeSolverStupid(MazeBuilder) // on initialise le solver avec une map faite par le builder
>>> n.solve() // on solve
+-+-+-+
|X  | | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
0

+-+-+-+
|  X| | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
0

+-+-+-+
|  X| | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
1

+-+-+-+
|  X| | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
2

+-+-+-+
|X  | | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
3

+-+-+-+
|   | | 
+ +-+ +
|X    | 
+-+ +-+
|     | 
+-+-+ +
4

+-+-+-+
|   | | 
+ +-+ +
|  X  | 
+-+ +-+
|     | 
+-+-+ +
5

+-+-+-+
|   | | 
+ +-+ +
|    X| 
+-+ +-+
|     | 
+-+-+ +
6

+-+-+-+
|   |X| 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
7

+-+-+-+
|   |X| 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
8

+-+-+-+
|   |X| 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
9

+-+-+-+
|   | | 
+ +-+ +
|    X| 
+-+ +-+
|     | 
+-+-+ +
10

+-+-+-+
|   | | 
+ +-+ +
|    X| 
+-+ +-+
|     | 
+-+-+ +
11

+-+-+-+
|   | | 
+ +-+ +
|  X  | 
+-+ +-+
|     | 
+-+-+ +
12

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|  X  | 
+-+-+ +
13

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|    X| 
+-+-+ +
14

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|    X| 
+-+-+ +
15

Gagné !!
+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +
16
````

