// Example of code taken from recfactoring.guru

mod game;
mod magic_maze;
mod ordinary_maze;

use magic_maze::MagicMaze;
use ordinary_maze::OrdinaryMaze;

// The game runs different with mazes depending on the concrete factory type
// it's either an ordinary maze or magic maze
// for demostration purposes, both mazes are used to contruct the game

fn main() {
    // Option 1 - game starts with Ordinary Maze
    let ordinary_maze = OrdinaryMaze::new();
    game::run(ordinary_maze);

    // Option 2 - game starts with Magic Maze
    let magic_maze = MagicMaze::new();
    game::run(magic_maze);
}
