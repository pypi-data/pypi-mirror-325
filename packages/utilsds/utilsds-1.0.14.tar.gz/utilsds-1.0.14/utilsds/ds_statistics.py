"""
Statistics function
"""

from scipy import stats


def test_kruskal_wallis(*groups, variable, dataframe, y="y", alpha=0.02, fill_na=0):
    """
    Statistical Kruskal-Wallis test.

    Parameters
    ----------

    groups : packaging argument, pd.Dataframe
        Dataframe with one of the target groups.
    variable : str
        Column name to analyze
    dataframe : pd.Dataframe
        Dataframe with all target groups
    y : str, optional
        Target column name, by default "y"
    alpha : float, optional
        Statistical significance, by default 0.02
    fill_na : int, optional
        Fill empty rows, by default 0
    """
    krus_group = []
    for group in groups:
        group = group[variable].fillna(fill_na).to_list()
        krus_group.append(group)
    h_statistic, p_value = stats.kruskal(*krus_group)

    print("Wartość H-statystyki:", h_statistic)
    print("Wartość p-value:", p_value)

    if p_value < alpha:
        print(
            "Odrzucamy hipotezę zerową - istnieje istotnie statystycznie różnice między przynajmniej jedną parą grup. Sprawdź poniższe mediany."
        )
        return dataframe.groupby(y)[variable].median()
    print(
        "Nie ma podstaw do odrzucenia hipotezy zerowej - nie ma istotnych statystycznie różnic między grupami."
    )


def test_agosto_pearsona(column, dataframe, alpha=0.02):
    """Test for normality using D'Agostino-Pearson test.

    Parameters
    ----------
    column : str
        Column name to test for normality
    dataframe : pd.DataFrame
        Input dataframe containing the column
    alpha : float, optional
        Statistical significance level, by default 0.02
    """

    stat, p_value = stats.normaltest(dataframe[column])

    # Wyświetlenie wyników
    print(f"Wartość statystyki D'Agostino-Pearsona: {stat}")
    print(f"p-wartość: {p_value}")

    # Interpretacja wyników
    alpha = 0.05
    if p_value > alpha:
        print(
            "Nie ma podstaw do odrzucenia hipotezy zerowej: dane są zgodne z rozkładem normalnym."
        )
    else:
        print("Odrzucamy hipotezę zerową: dane nie są zgodne z rozkładem normalnym.")
