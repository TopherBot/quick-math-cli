# quick‑math‑cli

**quick‑math‑cli** is a minimal Python utility that evaluates a single arithmetic expression supplied on the command line.

## Installation
```bash
# Clone the repo and install (no dependencies required)
git clone https://github.com/yourname/quick-math-cli.git
cd quick-math-cli
chmod +x calc.py
```

## Usage
```bash
./calc.py "2 + 3 * (4 - 1)"
# => 11

./calc.py "(2**3) / 4"
# => 2.0
```

The script prints the result or an error message if the expression cannot be parsed.

## Features
- Zero‑dependency, pure Python 3
- Supports `+`, `-`, `*`, `/`, `**`, parentheses
- Safe evaluation using `ast.literal_eval`-like node whitelist

## License
MIT – see LICENSE file.
