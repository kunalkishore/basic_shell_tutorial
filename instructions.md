### Command 1: `pwd` (Print Working Directory)

Explanation:

- `pwd` stands for "Print Working Directory"
- It displays the current directory (folder) you're in
- This is crucial for orienting yourself in the file system
- No flags are needed for this basic command

**General Use Cases with Explained Examples:**

1. Orienting yourself in the file system:
   ```
   pwd
   ```
   Explanation: Simply typing `pwd` will display your current directory path.

2. Verifying your location before executing commands:
   ```
   pwd && ./run_analysis.sh
   ```
   Explanation: `&&` runs the second command only if the first succeeds. This ensures you're in the right directory
   before running a script.

3. Debugging scripts that depend on the current directory:
   ```
   echo "Current directory: $(pwd)"
   ```
   Explanation: `$(pwd)` is command substitution, inserting the output of `pwd` into the echo statement.

4. Constructing absolute paths in scripts or commands:
   ```
   data_dir="$(pwd)/datasets"
   ```
   Explanation: This creates a variable `data_dir` with an absolute path to a 'datasets' subdirectory of the current
   directory.

### Command 2: `ls` (List)

Explanation:

- `ls` stands for "list"
- It shows the contents of the current directory
- By default, it doesn't show hidden files (those starting with a dot)
- No flags are used here, but we'll see flags in action soon

**Command:**

```
ls
ls -a
ls -l
```

**General Use Cases with Explained Examples:**

1. Viewing the contents of directories:
   ```
   ls ~/projects/data_analysis
   ```
   Explanation: Lists contents of the specified directory. `~` is shorthand for the home directory.

2. Checking for the existence of specific files:
   ```
   ls model_v1.pkl model_v2.pkl
   ```
   Explanation: Lists only the specified files. If a file doesn't exist, ls will show an error for that file.

3. Verifying file permissions and ownership:
   ```
   ls -l confidential_data.csv
   ```
   Explanation: `-l` flag provides a long listing format, showing permissions, owner, size, and modification date.

4. Sorting files by date, size, or name:
   ```
   ls -lth
   ```
   Explanation: `-l` for long format, `-t` to sort by modification time, `-h` for human-readable sizes.

5. Quickly assessing the structure of a project or dataset:
   ```
   ls -R
   ```
   Explanation: `-R` flag recursively lists subdirectories, showing the entire directory tree.

### Command 3: `cd` (Change Directory)

Example:

```
cd DataScienceProject
```

Explanation:

- `cd` stands for "Change Directory"
- It's followed by the name of the directory you want to move into
- If the directory name contains spaces, you'd need to use quotes: `cd "Data Science Project"`
- No flags are typically used with `cd`

**Command:**

```
cd directory_name
cd ..
cd ~
```

**General Use Cases with Explained Examples:**

1. Navigating the file system:
   ```
   cd /home/user/projects/data_analysis
   ```
   Explanation: Changes to the specified absolute path.

2. Moving between different parts of a project:
   ```
   cd ../data_preprocessing
   ```
   Explanation: `..` represents the parent directory, so this moves up one level and then into 'data_preprocessing'.

3. Accessing specific directories for file operations:
   ```
   cd ~/downloads && mv dataset.csv ~/projects/current_analysis/
   ```
   Explanation: Changes to downloads directory, then moves a file. `&&` ensures the move only happens if the directory
   change is successful.

4. Setting up the working environment in scripts:
   ```
   cd "$(dirname "$0")"
   ```
   Explanation: Changes to the directory of the script being run. `$0` is the script name, and `dirname` extracts its
   directory.

### Command 4: `ls -a` (List All)

Explanation:

- The `-a` flag stands for "all"
- It tells `ls` to show all files, including hidden ones (those starting with a dot)
- Hidden files are often used for configuration and are important in many projects
- This is crucial for seeing the complete project structure

### Command 5: `cat` (Concatenate and Print)

Explanation:

- `cat` stands for "concatenate", but it's often used to display file contents
- It prints the entire content of the file to the terminal
- No flags are used here, as we're just displaying a single, small file
- For larger files, you might use `less` instead to view the content page by page

**General Use Cases with Explained Examples:**

1. Quickly viewing the contents of small text files:
   ```
   cat config.yml
   ```
   Explanation: Displays the entire content of config.yml in the terminal.

2. Combining multiple files into one:
   ```
   cat file1.csv file2.csv file3.csv > combined_data.csv
   ```
   Explanation: Concatenates the content of three files and redirects (`>`) the output to a new file.

3. Creating small text files directly from the command line:
   ```
   cat > new_file.txt << EOF
   This is a new file
   Created with cat
   EOF
   ```
   Explanation: Creates a new file and allows typing content directly. `<<EOF` defines a "here-document" until EOF is
   typed.

4. Appending content to existing files:
   ```
   cat >> log.txt << EOF
   New log entry
   Date: $(date)
   EOF
   ```
   Explanation: `>>` appends to the file instead of overwriting. `$(date)` inserts the current date.

5. Part of command pipelines to feed text into other commands:
   ```
   cat data.json | jq '.field'
   ```
   Explanation: Outputs content of data.json and pipes (`|`) it to `jq`, a JSON processor, to extract a specific field.

### Command 6: `find` (Find Files)

```
find . -name "large_dataset.csv"
```

Explanation:

- `find` is a powerful command for searching files and directories
- `.` tells find to start searching from the current directory
- `-name` is a flag that specifies we're searching by filename
- "large_dataset.csv" is the name of the file we're looking for
- The quotes around the filename are important if the name contains spaces or special characters

**General Use Cases with Explained Examples:**

1. Locating specific files in complex directory structures:
   ```
   find ~/projects -name "*.py"
   ```
   Explanation: Searches for .py files in ~/projects and all subdirectories. `-name` specifies the search is by
   filename.

2. Finding and operating on files matching certain criteria:
   ```
   find . -name "*.tmp" -delete
   ```
   Explanation: Finds all .tmp files in current directory and subdirectories, then deletes them. `-delete` action is
   applied to each found file.

3. Cleaning up old or temporary files:
   ```
   find /tmp -type f -mtime +30 -delete
   ```
   Explanation: Finds files (`-type f`) in /tmp modified more than 30 days ago (`-mtime +30`) and deletes them.

4. Creating file inventories:
   ```
   find ~/datasets -type f > dataset_inventory.txt
   ```
   Explanation: Lists all files (`-type f`) in ~/datasets and subdirectories, redirecting output to a text file.

5. As part of backup or synchronization processes:
   ```
   find ~/documents -mtime -1 -type f -print0 | xargs -0 tar czf recent_docs.tar.gz
   ```
   Explanation: Finds files modified in the last day (`-mtime -1`), prints null-separated names (`-print0`), pipes
   to `xargs` to handle spaces in filenames, then creates a tar archive.

### Command 7: `head` (View Beginning of File)

```
head -n 5 RawData/large_dataset.csv
```

Explanation:

- `head` displays the first part of a file
- `-n 5` is a flag that specifies we want to see the first 5 lines
    - `-n` stands for "number of lines"
- Without this flag, `head` would show the first 10 lines by default
- This is useful for quickly checking the structure of a CSV file, including its header

**General Use Cases with Explained Examples:**

1. Quickly inspecting the structure of data files:
   ```
   head -n 5 large_dataset.csv
   ```
   Explanation: Displays the first 5 lines of the file. `-n 5` specifies the number of lines to show.

2. Checking file headers or metadata:
   ```
   head -n 1 data_with_headers.csv
   ```
   Explanation: Shows only the first line, which is often the header in CSV files.

3. Verifying the start of log files:
   ```
   head -n 20 application.log
   ```
   Explanation: Displays the first 20 lines of the log file, useful for checking recent entries.

4. Previewing large files before full processing:
   ```
   head -c 1M large_binary_file
   ```
   Explanation: Shows the first 1 megabyte of the file. `-c 1M` specifies to output 1 megabyte of data.

5. As part of data validation pipelines:
   ```
   head -n 1000 input.csv | awk -F',' '{print NF}' | sort | uniq -c
   ```
   Explanation: Takes the first 1000 lines, uses awk to count fields in each line (assuming comma-separated), then sorts
   and counts unique field counts to check for consistency.
   `

### Command 8: `wc` (Word Count)

Example:

```
wc -l RawData/large_dataset.csv
```

Explanation:

- `wc` stands for "word count", but it can count lines, words, and characters
- `-l` flag tells `wc` to count lines only
    - This is perfect for counting records in a CSV file, assuming one record per line
- The output will be the number of lines followed by the filename

**General Use Cases with Explained Examples:**

1. Counting records in data files:
   ```
   wc -l dataset.csv
   ```
   Explanation: Counts the number of lines in the file. `-l` specifies to count only lines.

2. Verifying file sizes or content amounts:
   ```
   wc -c large_file.bin
   ```
   Explanation: Counts the number of bytes in the file. `-c` specifies to count bytes.

3. Checking the output of data processing operations:
   ```
   grep "ERROR" log.txt | wc -l
   ```
   Explanation: Counts the number of lines containing "ERROR" in the log file. `grep` finds the matching lines,
   and `wc -l` counts them.

4. Part of data quality checks in pipelines:
   ```
   [ $(wc -l < processed_data.csv) -eq $(wc -l < raw_data.csv) ] || echo "Row count mismatch!"
   ```
   Explanation: Compares line counts of two files. `$(...)` performs command substitution, `[ ... ]` is a test
   condition, `-eq` checks for equality, `||` executes the following command if the test fails.

5. Monitoring log file growth:
   ```
   watch -n 60 'wc -l /var/log/application.log'
   ```
   Explanation: Runs `wc -l` every 60 seconds using `watch`, allowing you to monitor the growth of the log file in
   real-time.

### Command 9: `awk` (Text Processing)

```
awk -F',' '{print $1","$2}' RawData/large_dataset.csv > ProcessedData/id_text.csv
```

Explanation:

- `awk` is a powerful text-processing tool
- `-F','` sets the field separator to a comma, essential for CSV files
- '{print $1","$2}' tells awk to print the first and second fields, separated by a comma
- The single quotes around the awk program are necessary
- `>` redirects the output to a new file instead of printing to the screen
- This command creates a new CSV file with only the selected columns

**General Use Cases with Explained Examples:**

1. Extracting specific columns from CSV or TSV files:
   ```
   awk -F',' '{print $2,$4}' data.csv > extracted_columns.csv
   ```
   Explanation: `-F','` sets the field separator to comma, `{print $2,$4}` prints the 2nd and 4th fields of each line.

2. Performing calculations on structured data:
   ```
   awk -F',' '{sum+=$3} END {print "Average:", sum/NR}' numeric_data.csv
   ```
   Explanation: Sums the 3rd field of each line, then prints the average. `NR` is the number of records processed.

3. Reformatting data for different applications:
   ```
   awk '{print $2,"\t",$1}' names.txt > reversed_names.txt
   ```
   Explanation: Prints the 2nd field, a tab character, then the 1st field, effectively swapping columns.

4. Generating reports from log files:
   ```
   awk '/ERROR/ {print $1,$2,$NF}' application.log
   ```
   Explanation: For lines containing "ERROR", prints the 1st, 2nd, and last fields. `$NF` represents the last field.

5. Data cleaning and transformation tasks:
   ```
   awk -F',' '$3 > 1000 {print $0}' sales.csv > high_value_sales.csv
   ```
   Explanation: Prints entire lines (`$0`) where the 3rd field is greater than 1000, effectively filtering the data.

### Command 10: `gzip` (GNU Zip)

```
gzip -d ProcessedData/compressed_data.csv.gz
```

Explanation:

- `gzip` is used for compressing and decompressing files
- `-d` flag stands for "decompress"
- This command will decompress the file, removing the .gz extension
- The original compressed file is replaced by the decompressed version

**General Use Cases with Explained Examples:**

1. Compressing large datasets to save storage space:
   ```
   gzip large_dataset.csv
   ```
   Explanation: Compresses the file, replacing it with large_dataset.csv.gz.

2. Preparing files for efficient network transfer:
   ```
   tar czf project_files.tar.gz project_directory/
   ```
   Explanation: Creates a tarball (`c`), compresses it with gzip (`z`), and specifies the output file (`f`).

3. Working with compressed log files:
   ```
   zcat log.gz | grep "ERROR"
   ```
   Explanation: `zcat` decompresses and outputs the file content, which is then piped to `grep` to find "ERROR" lines.

4. Archiving old data:
   ```
   find ./old_data -type f -mtime +365 -exec gzip {} +
   ```
   Explanation: Finds files older than 365 days and compresses each one. `{}` is replaced with each filename, and `+`
   allows multiple files to be processed in one `gzip` call.

5. Part of data backup strategies:
   ```
   mysqldump database_name | gzip > database_backup.sql.gz
   ```
   Explanation: Dumps the database and immediately compresses the output, saving disk space.

### Command 11: `grep` (Global Regular Expression Print)

```
grep "crucial" ProcessedData/compressed_data.csv
```

Explanation:

- `grep` searches for patterns in text
- "crucial" is the pattern we're searching for
- The command will print any lines containing the word "crucial"
- By default, grep is case-sensitive. Use `-i` for case-insensitive search

**General Use Cases with Explained Examples:**

1. Searching for specific data patterns in files:
   ```
   grep "Exception" application.log
   ```
   Explanation: Prints lines containing the word "Exception" from the log file.

2. Filtering log files for relevant information:
   ```
   grep -i "error" *.log > error_summary.txt
   ```
   Explanation: Searches for "error" (case-insensitive due to `-i`) in all .log files, outputting matches to a new file.

3. Counting occurrences of patterns in data:
   ```
   grep -c "404 Not Found" access.log
   ```
   Explanation: Counts lines containing "404 Not Found". `-c` outputs only the count.

4. Part of data validation processes:
   ```
   grep -v "^[0-9]\{5\}$" zipcode_column.txt
   ```
   Explanation: Finds lines that don't match exactly 5 digits. `-v` inverts the match, `^` and `$` anchor the pattern to
   the whole line.

5. Quickly checking for the presence of certain content:
   ```
   grep -q "SECRET_KEY" .env && echo "Secret key is set"
   ```
   Explanation: Quietly (`-q`) checks for "SECRET_KEY". If found, the `echo` command runs due to `&&`.

### Command 12: `find` and `grep` combination

```
find . -name "*.log" -exec grep "Processed" {} +
```

Explanation:

- This is a combination of `find` and `grep`
- `find . -name "*.log"` finds all files ending with .log
- `-exec grep "Processed" {} +` executes grep on each found file
- `{}` is replaced with each filename found
- `+` tells find to pass as many filenames as possible to grep at once, for efficiency

### Command 13: `chmod` (Change Mode)

```
chmod +x Models/train_model.py
```

Explanation:

- `chmod` changes the permissions of a file
- `+x` adds executable permissions
- This allows the script to be run directly, like a program

**General Use Cases with Explained Examples:**

1. Making scripts executable:
   ```
   chmod +x run_analysis.sh
   ```
   Explanation: Adds executable permissions (`+x`) to the script for all users.

2. Setting appropriate permissions for data files:
   ```
   chmod 644 public_data.csv
   ```
   Explanation: Sets read-write for owner (6), read-only for group (4) and others (4). In octal, 6=rw-, 4=r--.

3. Managing access control in multi-user environments:
   ```
   chmod -R g+w shared_project_folder/
   ```
   Explanation: Recursively (`-R`) adds write permission (`+w`) for the group (`g`) to all files and subdirectories.

4. Securing sensitive data or configuration files:
   ```
   chmod 600 ~/.ssh/id_rsa
   ```
   Explanation: Sets read-write permissions for the owner only (600 = rw-------), appropriate for private keys.

5. Preparing files for different types of processing:
   ```
   find . -type d -exec chmod 755 {} +
   ```
   Explanation: Finds all directories (`-type d`) and sets their permissions to 755 (rwxr-xr-x), allowing traversal but
   protecting write access.

### Command 14: `tmux` (Terminal Multiplexer)

```
tmux new -s model_training
./Models/train_model.py > Results/training_output.txt
```

Explanation:

- `tmux` allows you to run processes in the background
- `new -s model_training` creates a new session named "model_training"
- The script is run and its output is redirected to a file
- Sarah can detach from this session (Ctrl-B, d) and it will keep running

**General Use Cases with Explained Examples:**

1. Running long data processing jobs:
   ```
   tmux new -s data_processing './process_large_dataset.py'
   ```
   Explanation: Creates a new tmux session named "data_processing" and runs the Python script within it.

2. Managing multiple tasks simultaneously:
   ```
   tmux new-window -t session_name:1 -n "log_monitor" 'tail -f application.log'
   ```
   Explanation: Creates a new window in an existing session, naming it "log_monitor", and starts tailing a log file.

3. Ensuring processes continue after disconnection:
   ```
   tmux new -d -s background_job './long_running_script.sh'
   ```
   Explanation: Starts a detached (`-d`) session named "background_job", running a script that will continue even if you
   disconnect.

4. Collaborative work on shared servers:
   ```
   tmux attach -t shared_session
   ```
   Explanation: Attaches to an existing tmux session named "shared_session", useful for collaborative work or resuming
   previous work.

5. Organizing complex workflows with multiple steps:
   ```
   tmux split-window -h 'python train_model.py'
   ```
   Explanation: Splits the current window horizontally (`-h`) and runs a Python script in the new pane.


### Command 15: `sed` (Stream Editor)

```
sed 's/label/category/g' ProcessedData/compressed_data.csv > ProcessedData/relabeled_data.csv
```

Explanation:

- `sed` is used for text transformation
- `'s/label/category/g'` is a substitution command
    - `s` stands for substitute
    - `label` is the text to replace
    - `category` is the replacement text
    - `g` means global (replace all occurrences, not just the first)
- The output is redirected to a new file

**General Use Cases with Explained Examples:**

1. Find and replace operations in text files:
   ```
   sed 's/color/colour/g' document.txt > british_spelling.txt
   ```
   Explanation: Replaces all occurrences of "color" with "colour". `s/` initiates substitution, `/g` makes it global (
   all occurrences).

2. Cleaning and standardizing data formats:
   ```
   sed 's/[0-9]\{2\}-[0-9]\{2\}-\([0-9]\{4\}\)/\1/g' dates.txt
   ```
   Explanation: Extracts the year from dates in DD-MM-YYYY format. `\(...\)` captures the year, `\1` refers to the
   captured group.

3. Removing or altering specific lines in files:
   ```
   sed '/^#/d' config.ini > clean_config.ini
   ```
   Explanation: Deletes lines starting with #. `^#` matches lines starting with #, `d` is the delete command.

4. Automating text file modifications:
   ```
   sed -i 's/DEBUG/INFO/g' *.log
   ```
   Explanation: Replaces "DEBUG" with "INFO" in all .log files. `-i` performs in-place editing.

5. Part of data preprocessing pipelines:
   ```
   sed 's/,,/,NA,/g' data.csv > filled_data.csv
   ```
   Explanation: Replaces empty fields (represented by consecutive commas) with "NA" in a CSV file.


### Command 16: `awk` and pipeline

```
find RawData -name "*.csv" -exec awk -F',' '{print $1","$NF}' {} \; > ProcessedData/combined_data.csv
```

Explanation:

- This complex command combines `find`, `awk`, and output redirection
- `find RawData -name "*.csv"` finds all CSV files in RawData
- `-exec` executes a command on each found file
- `awk -F',' '{print $1","$NF}'` prints the first and last field of each CSV
- `{}` is replaced with each filename
- `\;` marks the end of the command to execute
- The result is a new CSV with data from all found files

### Command 17: `mv` (Move)

```
mv ProcessedData/combined_data.csv Results/
```

Explanation:

- `mv` moves or renames files and directories
- The first argument is the source file
- The second argument is the destination directory
- This command moves the file without changing its name

**General Use Cases with Explained Examples:**

1. Organizing files into appropriate directories:
   ```
   mv *.csv data/
   ```
   Explanation: Moves all CSV files in the current directory to a subdirectory named "data".

2. Renaming files as part of data processing:
   ```
   mv old_name.txt new_name.txt
   ```
   Explanation: Renames a file from "old_name.txt" to "new_name.txt".

3. Archiving processed data:
   ```
   mv processed_data_* ../archive/$(date +%Y%m%d)/
   ```
   Explanation: Moves all files starting with "processed_data_" to an archive directory named with today's date.

4. Staging files for different phases of analysis:
   ```
   mv raw_data.csv preprocessing/ && mv preprocessing/clean_data.csv analysis/
   ```
   Explanation: Moves a raw data file to a preprocessing directory, then moves a cleaned file to an analysis
   directory. `&&` ensures the second move only happens if the first is successful.

5. Managing file versions:
   ```
   mv model.pkl model_$(date +%Y%m%d).pkl
   ```
   Explanation: Renames a model file to include the current date, useful for version control.

### Command 18: `uniq` (Report or Omit Repeated Lines)

**General Use Cases with Explained Examples:**

1. Removing duplicate lines from a sorted file:
   ```
   sort data.txt | uniq > unique_data.txt
   ```
   Explanation: First sorts the file (uniq only works on adjacent lines), then removes duplicate lines. The result is
   redirected to a new file.

2. Counting occurrences of unique lines:
   ```
   sort data.txt | uniq -c > line_counts.txt
   ```
   Explanation: Sorts the file, then counts occurrences of each unique line. `-c` adds a count prefix to each line.

3. Finding unique values in a specific column of a CSV file:
   ```
   cut -d',' -f3 data.csv | sort | uniq
   ```
   Explanation: Extracts the third column, sorts it, then shows unique values. This pipeline combines `cut`, `sort`,
   and `uniq`.

4. Identifying duplicate entries:
   ```
   sort data.txt | uniq -d
   ```
   Explanation: `-d` option tells uniq to only print duplicate lines.

5. Finding unique combinations of values:
   ```
   cut -d',' -f2,3 data.csv | sort | uniq -c | sort -nr
   ```
   Explanation: Extracts 2nd and 3rd columns, finds unique combinations, counts occurrences, then sorts numerically in
   reverse order.

### Command 19: `cut` (Remove Sections from Each Line of Files)

**General Use Cases with Explained Examples:**

1. Extracting specific columns from a CSV file:
   ```
   cut -d',' -f1,3,5 data.csv > extracted_columns.csv
   ```
   Explanation: `-d','` sets comma as the delimiter, `-f1,3,5` selects the 1st, 3rd, and 5th fields.

2. Extracting a range of characters from each line:
   ```
   cut -c5-10 fixed_width_data.txt
   ```
   Explanation: `-c5-10` extracts characters 5 through 10 from each line.

3. Removing a specific column from a CSV file:
   ```
   cut -d',' -f2- data.csv > without_first_column.csv
   ```
   Explanation: `-f2-` selects all fields from the 2nd onwards, effectively removing the first column.

4. Extracting usernames from /etc/passwd:
   ```
   cut -d: -f1 /etc/passwd
   ```
   Explanation: Uses ':' as delimiter and extracts the first field, which is the username in /etc/passwd.

5. Combining with other commands for data analysis:
   ```
   cut -d',' -f3 data.csv | sort | uniq -c | sort -nr | head -n 5
   ```
   Explanation: Extracts 3rd column, finds unique values and their counts, sorts by frequency, shows top 5.

### Command 20: `sort` (Sort Lines of Text)

**General Use Cases with Explained Examples:**

1. Simple alphabetical sorting:
   ```
   sort names.txt > sorted_names.txt
   ```
   Explanation: Sorts lines alphabetically and saves to a new file.

2. Numerical sorting:
   ```
   sort -n numbers.txt
   ```
   Explanation: `-n` option sorts numerically instead of alphabetically.

3. Reverse sorting:
   ```
   sort -r data.txt
   ```
   Explanation: `-r` option sorts in reverse order.

4. Sorting a specific column in a CSV file:
   ```
   sort -t',' -k2 data.csv
   ```
   Explanation: `-t','` sets comma as field separator, `-k2` sorts based on the 2nd field.

5. Removing duplicates and sorting:
   ```
   sort -u combined_data.txt
   ```
   Explanation: `-u` option removes duplicate lines while sorting.

6. Sorting by multiple keys:
   ```
   sort -t',' -k2,2 -k3,3n data.csv
   ```
   Explanation: Sorts by 2nd column alphabetically, then by 3rd column numerically.

7. Sorting human-readable numbers:
   ```
   du -h | sort -h
   ```
   Explanation: `-h` option sorts human-readable numbers (like 2K, 1M, etc.).