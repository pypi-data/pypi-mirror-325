import pandas as pd
import importlib.resources as pkg_resources
from pathlib import Path

_DICTIONARY_CACHE = None

def main(sheet_name='sh1'):
    """
    Load the Excel file from the package and return the 'search_tac' function.
    """
    global _DICTIONARY_CACHE

    # Locate the Excel file inside the package
    with pkg_resources.as_file(pkg_resources.files("search_tac").joinpath("MSRPLUS20231218.xlsx")) as path:
        if _DICTIONARY_CACHE is None:
            df = pd.read_excel(path, sheet_name=sheet_name)
            df["TAC"] = df["TAC"].astype(str).str.zfill(8)
            _DICTIONARY_CACHE = dict(zip(df["TAC"], df["Simslot"]))

    def search_tac(tac: str):
        """Return the 'Simslot' value for the given TAC, or None if not found."""
        try:
            if len(tac) < 15 or len(tac) > 17:
                raise ValueError("La taille doit être comprise entre 15 et 17")
            return _DICTIONARY_CACHE.get(tac[:8])
        except ValueError as e:
            print(f"An error occurred: {e}")

    return search_tac
