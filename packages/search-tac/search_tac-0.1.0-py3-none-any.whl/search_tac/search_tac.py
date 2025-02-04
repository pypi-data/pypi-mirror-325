import pandas as pd

_DICTIONARY_CACHE = None

def main(path='MSRPLUS20231218.xlsx', sheet_name='sh1'):
    """
    The main function that returns the 'search_tac' function.
    It will read the Excel file only once (the first time 'main' is called).
    """
    global _DICTIONARY_CACHE

    # If the cache is empty, read the file and populate the cache
    if _DICTIONARY_CACHE is None:
        df = pd.read_excel(path, sheet_name=sheet_name)
        df["TAC"] = df["TAC"].astype(str).str.zfill(8)
        _DICTIONARY_CACHE = dict(zip(df["TAC"], df["Simslot"]))

    def search_tac(tac: str):
        """Return the 'Simslot' value for the given TAC, or None if not found."""
        try:
            if (len(tac)<15 or len(tac)>17):
                raise ValueError(" La taille doit etre comprise entre 15 et 17")
                
            else :
                
                return _DICTIONARY_CACHE.get(tac[:8])
        except ValueError as e:
                raise
        

    return search_tac
