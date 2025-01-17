<img src="https://tcf.admeen.org/game/1500/1204/400x246/mastermind.jpg"  width="700"/>

# PR01-project-python
# Mastermind

Primer proyecto del modulo 1


## Contenido
- [Descripcion del juego](#Descripcion-del-juego)
- [Reglas](#Reglas)
- [Forma de jugar](#Forma-de-jugar)
- [Organizacion-Trello](#Organizacion-Trello)
- [Mas informacion](#Mas-informacion)


## Descripcion del juego
**Mastermind** es un juego de lógica que puede ser jugado por dos personas. 
El objetivo es descifrar el código de colores que creó el otro jugador. Para hacerlo necesitarás ir descartando posibilidades según las pistas que te proporcionará tu oponente.



## Reglas
Primero elegiras el nivel que quieres jugar:
    - Facil (4 colores)
    - Medio (6 colores)
    - Dificil (8 colores).
Despues elegiras cuantas oportunidades quieres jugar para ganar.
Cada turno elegirás cuatro combinaciones de colores con tres resultados posibles para cada posición. Hay que tener en cuenta que los colores se pueden repetir. El resultado sera: **"X"** si has acertado el color en su posicion. **"O"**  si has acertado el color pero no en su posicion correcta y **"/"** si el color no esta en el codigo.
Ejemplo de respuesta:
    -Es decir si aciertas los cuatro colores en su posicion la respuesta sera: XXXX
    - Si aciertas los colores pero ninguno en su posicion la respuesta sera: OOOO
    - Si no aciertas ningun color la respuesta sera: ////
    - Si aciertas dos colores en su posicion y dos colores en posicion incorrecta: XX00
    - Si aciertas un color en su posicion, otro que no este en posicion y los otros no estan: XO//
La respuesta sera devuelta totalmente ALEATORIA, es decir la X, la O o la /, estara desordenadas.
NO TIENES QUE TENER EN CUENTA LA POSICION DE LA RESPUESTA


## Forma de jugar
Descarga los archivos y ejecuta el archivo **juego.py**, sigue las instrucciones y asegurate de haber escrito bien la palabra.


## Organizacion Trello
Para realizar este proyecto, las tareas se han distribuido de la siguiente manera.
[Trello](https://trello.com/b/VMtzURyH/pr01-juego-python)


## Mas informacion
 [Enlace de interes](https://www.aboutespanol.com/aprende-a-jugar-mastermind-paso-a-paso-2077618)