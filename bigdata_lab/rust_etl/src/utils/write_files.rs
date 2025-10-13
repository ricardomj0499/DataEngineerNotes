use std::fs::File;
use std::io::{BufWriter, Write};
use std::path::Path;

/// Writes the preamble and CSV data into a new file.
pub fn write_combined_csv<P: AsRef<Path>>(
    preamble: &[String],
    data_lines: &[String],
    output_path_preamble: P,
    output_path_data: P,
) -> Result<(), Box<dyn std::error::Error>> {
    let file_preamble = File::create(output_path_preamble)?;
    let file_data = File::create(output_path_data)?;
    let mut writer = BufWriter::new(file_preamble);
    let mut writer_data = BufWriter::new(file_data);

    // Write preamble lines
    for line in preamble {
        writeln!(writer, "{}", line)?;
    }

    // Separate with a blank line if needed
    // writeln!(writer)?;

    // Write data lines
    for line in data_lines {
        writeln!(writer_data, "{}", line)?;
    }

    Ok(())
}
