import pandas as pd
import pytest

from spatial_italy.data import load_population_by_municipalities


@pytest.fixture
def POSAS_2023_it_Comuni():
    return pd.DataFrame.from_dict(
        {
            "index": [
                463756,
                454070,
                66033,
                356442,
                191015,
                238125,
                525073,
                667053,
                50233,
                390401,
            ],
            "columns": [
                "Codice comune",
                "Comune",
                "Età",
                "Totale maschi",
                "Totale femmine",
            ],
            "data": [
                [56043, "Piansano", 64, 10, 16],
                [54040, "Piegaro", 68, 20, 19],
                [4169, "Piozzo", 39, 9, 8],
                [30002, "Amaro", 54, 11, 15],
                [16036, "Branzi", 71, 2, 3],
                [18052, "Confienza", 57, 13, 12],
                [63084, "Torre del Greco", 79, 236, 321],
                [81014, "Pantelleria", 75, 41, 49],
                [4012, "Barge", 49, 61, 54],
                [36038, "San Possidonio", 47, 23, 34],
            ],
            "index_names": [None],
            "column_names": [None],
        },
        orient="tight",
    )


def test_load_population_by_municipalities(mocker, POSAS_2023_it_Comuni):
    mocker.patch(
        "spatial_italy.data.request_population_by_municipalities",
        return_value=POSAS_2023_it_Comuni,
    )
    df = load_population_by_municipalities()
    assert isinstance(df, pd.DataFrame)
