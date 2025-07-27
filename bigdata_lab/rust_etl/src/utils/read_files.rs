use std::fs::{File, metadata};
use std::io;

pub fn read_file(path: &str) -> io::Result<File> {
    if !file_exists(path) {
        println!("File does not exist: {}", path);
        return Err(io::Error::new(io::ErrorKind::NotFound, "File not found"));
    }

    File::open(path)
}

fn file_exists(path: &str) -> bool {
    match metadata(path) {
        Ok(metadata) => metadata.is_file(),
        Err(_) => false,
    }
}
