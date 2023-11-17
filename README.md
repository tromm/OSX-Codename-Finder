# OSX Codename Finder

## Overview

This script is designed to determine the codename of your current macOS version. It reads the
macOS version of your system and compares it with a list of current macOS versions and their
codenames on the Apple Support page.

## Prerequisites

- Python 3.x
- Libraries: `requests`, `bs4` (BeautifulSoup 4)
Install missing libraries with:

```bash
pip3 install requests bs4
```

## Installation

Clone the repository or download the script directly:

```bash
git clone https://github.com/tromm/OSX-Codename-Finder.git
```

## Usage

The script can be executed with various parameters:

- Without parameters: Determines the codename of the current macOS version.

```bash
python3 getosxcodename.py
```

- `--version`: Only returns the macOS product version.

```bash
python3 getosxcodename.py --version
```

- `--codename`: Only returns the codename of the current macOS version.

```bash
python3 getosxcodename.py --codename
```

- `--list-versions`: Lists all macOS versions and codenames found on the Apple support page.

```bash
python3 getosxcodename.py --list-versions
```

- `--debug`: Provides detailed debugging output including data found on the Apple support page.

```bash
python3 getosxcodename.py --debug
```

### Notes

- Ensure you have an internet connection when using the script without the `--version` parameter.
- For systems with Python versions lower than 3.x, it is recommended to use a virtual environment
with Python 3.x. For more information on setting up a virtual environment, please visit [Python's
venv documentation](https://docs.python.org/3/library/venv.html).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
