# NLP Project - Password Strength Checker

## Project Setup

1. Install UV for dependency management.\
   Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"` \
   macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Install Python & dependencies: `uv sync`
3. Download the dataset: `uv run download_dataset.py` \
   The dataset used contains breached passwords: `https://github.com/danielmiessler/SecLists`
4. Calculate the password strength using `zxcvbn` which is a well-known password checker by Twitter.\
   Run `uv run tag_dataset.py`
5. Run the Jupyter notebook to check passwords using NLP, and print a report against zxcvbn's results.
