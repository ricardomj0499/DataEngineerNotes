use crate::schemas::transferencia::Transferencia;
use crate::utils::read_files;
use std::error::Error;
use std::io::BufRead;
use std::io::BufReader;

pub fn process_file(path: &str) -> Result<(), Box<dyn Error>> {
    println!("\nProcessing file: {}", path);

    let file = read_files::read_file(path)?;
    let reader = BufReader::new(file);

    let mut preamble = Vec::new();
    let mut data_lines = Vec::new();
    let mut is_data_section = false;

    for line_result in reader.lines() {
        let line = line_result?;
        if !is_data_section && line.contains("\"Estado\"") && line.contains("\"Fecha\"") {
            is_data_section = true;
        }
        if is_data_section {
            data_lines.push(line);
        } else {
            preamble.push(line);
        }
    }

    // Print metadata/preamble
    println!("--- Metadata (Preamble) ---");
    for line in &preamble {
        println!("{}", line);
    }

    // Parse and print data table
    println!("--- Parsed Transferencias ---");
    let csv_data = data_lines.join("\n");
    let mut rdr: csv::Reader<&[u8]> = csv::Reader::from_reader(csv_data.as_bytes());

    for result in rdr.deserialize::<Transferencia>() {
        let row = result?;
        println!("{:?}", row);
    }

    Ok(())
}
