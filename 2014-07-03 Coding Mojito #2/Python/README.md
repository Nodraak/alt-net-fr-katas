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
>>> from MazeSolverStupid import MazeSolver // on importe le solver
>>> n=MazeSolver(MazeBuilder) // on initialise le solver avec une map faite par le builder
>>> n.solve() // on solve
+-+-+-+
|  X| | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|  X| | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|  X| | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|X  | | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|X    | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|  X  | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|    X| 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   |X| 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   |X| 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   |X| 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|    X| 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|    X| 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|  X  | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|  X  | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|    X| 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|    X| 
+-+-+ +

Gagné !!
````

