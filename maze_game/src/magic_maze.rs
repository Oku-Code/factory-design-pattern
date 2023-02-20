use super::game::{MazeGame, Room};

#[derive(Clone)]
pub struct MagicRoom {
    title: String,
}

impl MagicRoom {
    pub fn new(title: String) -> Self {
        MagicRoom { title }
    }
}

impl Room for MagicRoom {
    fn render(&self) {
        println!("Magic room: {}", self.title)
    }
}

pub struct MagicMaze {
    rooms: Vec<MagicRoom>,
}

impl MagicMaze {
    pub fn new() -> Self {
        MagicMaze {
            rooms: vec![
                MagicRoom::new("Infinite Room".into()),
                MagicRoom::new("Red room".into()),
            ],
        }
    }
}

impl MazeGame for MagicMaze {
    type RoomImpl = MagicRoom;

    fn rooms(&self) -> Vec<Self::RoomImpl> {
        self.rooms.clone()
    }
}
