mod process;
mod schemas;
mod utils;
use std::env;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("Usage: batch_transferencias <file1> <file2> ...");
        std::process::exit(1);
    }
    println!("Processing files: {:?}", &args);
    for file_path in &args {
        process::process_file(file_path)?;
    }

    Ok(())
}
