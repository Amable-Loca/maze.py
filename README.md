# El Laberinto

Este código implementa un *juego de laberinto en Pygame*, donde el jugador controla un personaje que debe navegar a través de un conjunto de paredes hasta llegar a la meta.

### *Descripción del juego*
- *Movimiento del jugador:* Usa las teclas *W, A, S, D* para moverse por el laberinto.
- *Paredes:* Se han definido varias paredes (Wall) que forman un recorrido desafiante.
- *Fondo y visualización:* Se carga una imagen de fondo (background.jpg) y una pantalla de victoria (vict.jpg).
- *Colisiones:* Si el jugador choca con una pared, aparece la pantalla de victoria y el juego termina.

### *Estructura del código*
1. *Clases principales*  
   - GameSprite: Clase base para los elementos del juego.  
   - Player: Permite mover el jugador en la pantalla.  
   - Wall: Representa las paredes del laberinto.

2. *Inicialización y lógica*  
   - Se crea un grupo de paredes (sprite.Group()).  
   - Se configura el *bucle principal*, que dibuja el fondo, el jugador y las paredes.  
   - Se revisa si el jugador *colisiona* con alguna pared.
