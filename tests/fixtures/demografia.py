import pytest
import pandas as pd


@pytest.fixture
def POSAS_2023_it_Comuni_sample():
    # Sample: `df[(df["Età"].isin([16,74])) & (df.Comune.isin(["Milano", "Roma", "Napoli", "Castro"]))].to_dict(orient="tight")`
    return pd.DataFrame.from_dict(
        {
            "index": [
                181066,
                181124,
                193612,
                193670,
                482170,
                482228,
                521440,
                521498,
                618646,
                618704,
            ],
            "columns": [
                "Codice comune",
                "Comune",
                "Età",
                "Totale maschi",
                "Totale femmine",
            ],
            "data": [
                [15146, "Milano", 16, 6430, 5957],
                [15146, "Milano", 74, 5691, 7572],
                [16065, "Castro", 16, 4, 5],
                [16065, "Castro", 74, 11, 17],
                [58091, "Roma", 16, 13884, 13081],
                [58091, "Roma", 74, 12599, 16446],
                [63049, "Napoli", 16, 5283, 4962],
                [63049, "Napoli", 74, 4318, 5340],
                [75096, "Castro", 16, 10, 9],
                [75096, "Castro", 74, 28, 12],
            ],
            "index_names": [None],
            "column_names": [None],
        },
        orient="tight",
    )
