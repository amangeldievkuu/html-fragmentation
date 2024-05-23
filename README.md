# HTML Fragment Splitter

This script splits an HTML file into smaller fragments of a specified maximum length. It's useful for processing large HTML documents and ensuring they can be handled more easily by other tools or processes.

## Features

- Splits an HTML file into fragments of a specified maximum length.
- Uses `BeautifulSoup` to parse and manage HTML content.
- Provides colored console output to differentiate between fragments.

## Requirements

- Python 3.x
- `beautifulsoup4==4.12.3`
- `typing`
- `click`
- `colorama`

## Installation

1. Clone the repository or download the script file.

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script from the command line, specifying the path to the HTML file and optionally the maximum length of each fragment:

    ```bash
    python msg_split.py <filepath> [--max-len MAX_LEN]
    ```

    - `<filepath>`: Path to the HTML file you want to split.
    - `--max-len`: Optional. Maximum length of each fragment. Default is 4096 characters.

    For example:

    ```bash
    python msg_split.py --max-len=3072 ./source.html
    ```

2. The script will print each fragment to the console, showing the fragment number and its length.

## Example Output

```plaintext
-- fragment #1: 4096 chars! --
<fragment content here>

-- fragment #2: 3500 chars! --
<fragment content here>
