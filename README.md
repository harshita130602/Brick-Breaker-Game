# ARCADE GAME - Brick Breaker

The game is the terminal version of brick breaker game. In this the player operates the paddle to bounce the ball to destroy the bricks.

## Installation

Colorama library:
```
pip3 install colorama
```
## Run
```
python3 main.py
```

## Controls
`a` or `A` - paddle moves towards left.
`d` or `D` - paddle moves towards right.
`<space>` - release the ball.
`x` or `X` - Quit the game.
`n` - new level jump

## Rules and Features
- Player loose one life on coming in constact with the ground.

- Player has one paddle. In the starting the player can control the ball release.

- After the ball get released. If it collides with wall it get delflected by wall in the opposite direction.

- If the ball collides with bricks, bricks looses its strength and reflect the ball.

- bricks stars falling in every 3 sec after 5 sec of start if game. If it reaches the groung the game ends there.

- Player gets poibts on hitting the brick.

- The colors of the bricks are according to strength. 
MAGENTA - 1, RED - 2, YELLOW - 3, WHITE - Unbreakable, BLUE - Explosive

- If the ball collides with the paddle it will get reflected acoording to the position of paddle.

- There are three levels of the game. On completing all three you win.

## Concept Used

The main concept used in this OOPS concept.

### Inheritance

Classes in bricks.py such as nakli_brick, sasti_brick, birla_brick, ambuja_brick, and edx_brick inherits from the parent class Brick.

### Polymorphism

Functions such as collision(), getStrength(), getColor() in bricks uses polymorphism.

### Encapsulation

Classes and objects based approach is used which makes this program more modular and hence encapsulation is used in this.

### Abstraction

Variables and Properties of classes are hidden from object and are only accessed by the methods of the class and hence follows abstraction.
