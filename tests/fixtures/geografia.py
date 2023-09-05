import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def classificazione_sismica_comuni():
    return pd.DataFrame.from_dict(
        {
            "index": [604, 4267, 4836, 5903, 7892],
            "columns": [
                "REGIONE",
                "PROV/CITTA'_METROPOLITANA",
                "SIGLA_PROV",
                "COMUNE",
                "COD_ISTAT_COMUNE",
                "ZONA_SISMICA",
            ],
            "data": [
                ["Lombardia", "Milano", "MI", "Milano", 15146, "3"],
                ["Campania", "Napoli", np.nan, "Napoli", 63049, "2"],
                ["Lombardia", "Bergamo", "BG", "Castro", 16065, "3"],
                ["Puglia", "Lecce", "LE", "Castro", 75096, "4"],
                ["Lazio", "Roma", "RM", "Roma", 58091, "2A-3A-3B"],
            ],
            "index_names": [None],
            "column_names": [None],
        },
        orient="tight",
    )
