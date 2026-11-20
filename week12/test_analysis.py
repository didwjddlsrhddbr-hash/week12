import pandas as pd
from analysis import 정제, 반별평균


scores_df = pd.read_csv("scores_2026.csv")
mini_df = pd.read_csv("mini.csv")
cleaned_df = 정제(scores_df)
cleaned_mini_df = 정제(mini_df)


def test_scores_cleaned_row_count():
    assert len(cleaned_df) == 100


def test_cleaned_class_values():
    assert set(cleaned_df["반"].unique()) == {"1반", "2반"}


def test_class_score_sums_match_total():
    class_sum = cleaned_df.groupby("반")["점수"].sum().sum()
    total_sum = cleaned_df["점수"].sum()
    assert class_sum == total_sum


def test_mini_class_one_average():
    averages = 반별평균(cleaned_mini_df)
    assert averages["1반"] == 80.0