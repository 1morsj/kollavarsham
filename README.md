# Kollavarsham Date Converter

This project provides a Python script to convert Gregorian dates to Kollavarsham dates, utilizing the `kollavarsham` Python library.

## Features

- Convert Gregorian dates to Kollavarsham dates.
- Accept date input in `dd/mm/yyyy` format (defaults to midnight).
- Accept date and time input in `dd/mm/yyyy hh:mm` format.
- Use current date and time if `now` is provided as an argument.
- Default to current date at midnight if no arguments are provided.
- Output in a human-readable format using the `-H` or `--human-readable` flag.
- Output in a machine-readable (CSV-like) format by default.

## Setup

1.  **Navigate to the project directory:**

    ```bash
    cd D:/Users/sunil/Deesktop/Gits/Zerodha/kollavarsham
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows Command Prompt (cmd.exe):**

        ```bash
        .venv\Scripts\activate
        ```

    *   **On Windows PowerShell:**

        ```powershell
        .venv\Scripts\Activate.ps1
        ```

    *   **On macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The main script is `kollavarsham_converter.py`. You can run it with different arguments:

*   **Current date at midnight (no arguments, machine-readable output):**

    *   **cmd.exe:**
        ```bash
        set PYTHONIOENCODING=utf-8 && python kollavarsham_converter.py
        ```
    *   **PowerShell:**
        ```powershell
        $env:PYTHONIOENCODING="utf-8" ; python kollavarsham_converter.py
        ```

*   **Current date and time (`now` argument, human-readable output):**

    *   **cmd.exe:**
        ```bash
        set PYTHONIOENCODING=utf-8 && python kollavarsham_converter.py now -H
        ```
    *   **PowerShell:**
        ```powershell
        $env:PYTHONIOENCODING="utf-8" ; python kollavarsham_converter.py now -H
        ```

*   **Specific date at midnight (`dd/mm/yyyy`, machine-readable output):**

    *   **cmd.exe:**
        ```bash
        set PYTHONIOENCODING=utf-8 && python kollavarsham_converter.py 15/08/1947
        ```
    *   **PowerShell:**
        ```powershell
        $env:PYTHONIOENCODING="utf-8" ; python kollavarsham_converter.py 15/08/1947
        ```

*   **Specific date and time (`dd/mm/yyyy hh:mm`, human-readable output):**

    *   **cmd.exe:**
        ```bash
        set PYTHONIOENCODING=utf-8 && python kollavarsham_converter.py "29/06/2025 10:30" -H
        ```
    *   **PowerShell:**
        ```powershell
        $env:PYTHONIOENCODING="utf-8" ; python kollavarsham_converter.py "29/06/2025 10:30" -H
        ```

*   **Get help on arguments:**

    ```bash
    python kollavarsham_converter.py --help
    ```

**Note:** Ensure your terminal supports UTF-8 encoding to correctly display Malayalam characters.
