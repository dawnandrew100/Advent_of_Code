use std::fs::File;
use std::io::{self, prelude::*};
use std::path::PathBuf;
use std::usize;

fn main() -> std::io::Result<()> {
    let file_contents = file_contents_to_string("../input.txt");
    let contents = match file_contents {
        Ok(c) => c,
        Err(e) => {
            eprintln!("{e}");
            return Ok(());
        }
    };

    // Parse ranges into numbers with Vec<(start, end)>
    let ranges = {
        let mut temp_ranges = Vec::new();
        let range_list = contents.split(',');
        for range in range_list {
            // Remove registered nurses with trim
            let parts: Vec<&str> = range.trim().split('-').collect();
            let first = parts[0];
            let last = parts[1];
            temp_ranges.push((first, last));
        }
        temp_ranges
    };

    let mut invalid_nums: Vec<usize> = Vec::new();
    for (start, end) in &ranges {
        // Invalid numbers are numbers that are repeated exactly
        // For example: 55 is a repeated 5 and 113113 is a repeated 113
        // Numbers with an odd length cannot be perfectly repeated and can therefore be ignored
        // This won't be true for part 2
        // SO REMEMBER TO MODIFY THIS LINE
        if start.len() == end.len() && !start.len().is_multiple_of(2) {
            continue;
        }
        let curr = start.parse::<usize>().unwrap_or(0);
        let upper_lim = end.parse::<usize>().unwrap_or(0);
        // There's probably a clever way to skip a bunch of numbers
        // but I'm feeling kind of brute forcey right now
        for num in curr..=upper_lim {
            if is_invalid_num(num) {
                invalid_nums.push(num);
            }
        }
    }
    println!("{invalid_nums:?}");
    println!("Solution = {}", invalid_nums.iter().sum::<usize>());

    Ok(())
}

fn file_contents_to_string(path_to_file: &str) -> Result<String, io::Error> {
    // Path to Cargo.toml directory (crate root)
    let manifest_dir = env!("CARGO_MANIFEST_DIR");
    // File path relative to project root
    let file_path = PathBuf::from(manifest_dir).join(path_to_file);

    let mut file = File::open(&file_path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    Ok(contents)
}

fn is_invalid_num(num: usize) -> bool {
    let num_str: Vec<char> = num.to_string().chars().collect();
    if !num_str.len().is_multiple_of(2) {
        return false;
    }
    let half = num_str.len() / 2;
    let first_half: String = num_str.iter().take(half).collect();
    let last_half: String = num_str.iter().skip(half).collect();
    if first_half == last_half {
        return true;
    }
    false
}
