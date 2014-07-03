## Binding en python 2.x

Je connais pas le C#, alors voici une reecriture du code en python.

Pour le moment :

* Une classe MazeCore : comme son nom l'indique : la base
* Une classe MazeBuilderSimple : pour initialiser un laby simple (3*3)
* Une classe MazeSolverStupid : implementation d'un solver basique


Exemple d'utilisation (via le terminal, la fleme de faire une gui) :

````shell
>>python MazeSolver.py 
+-+-+-+
|M  | | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|M    | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|M    | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|M    | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|  M  | 
+-+ +-+
|     | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|  M  | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|  M  | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|  M  | 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|    M| 
+-+-+ +

+-+-+-+
|   | | 
+ +-+ +
|     | 
+-+ +-+
|     | 
+-+-+ +

Gagné !!
````

