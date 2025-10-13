use std::fs::{File, metadata};
use std::io::{self};

pub fn read_file(path: &str) -> io::Result<File> {
    if !file_exists(path) {
        // TODO: User a better error handling strategy
        println!(
            "File does not exist or you don't have permission to access it: {}",
            path
        );
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
