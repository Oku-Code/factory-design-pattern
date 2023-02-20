// Maze room that is going to be instantiated with a factory method
pub trait Room {
    fn render(&self);
}

// Maze game has a factory method to producing differents rooms
pub trait MazeGame {
    // Type to define the behaviour of the room
    type RoomImpl: Room;

    // The factory method to create a room
    fn rooms(&self) -> Vec<Self::RoomImpl>;

    fn play(&self) {
        for room in self.rooms() {
            room.render()
        }
    }
}

// The client code initializes resources and others to the preparations
// then it uses a factory to construct and run the game
pub fn run(maze_game: impl MazeGame) {
    println!("Loading resources...");
    println!("Starting the game...");
    maze_game.play();
}
