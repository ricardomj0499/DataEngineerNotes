mod processors;
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
        let (preamble, data_lines) = processors::process_file(file_path)?;
        utils::write_files::write_combined_csv(
            &preamble,
            &data_lines,
            file_path.to_string() + "_processed_preamble.csv",
            file_path.to_string() + "_processed_data.csv",
        )?;
    }

    Ok(())
}
