import pandas as pd


def 정제(df):
    # 원본을 바꾸지 않도록 데이터프레임을 복사한다.
    result = df.copy()

    # 점수가 비어 있는 행을 삭제한다.
    result = result.dropna(subset=["점수"])
    result["점수"] = result["점수"].astype("int64")
    print("점수 비어 있는 행 삭제 후:", len(result))

    # 모든 열의 값이 같은 중복 행을 하나만 남긴다.
    result = result.drop_duplicates()
    print("완전 중복 행 제거 후:", len(result))

    # 반과 과목의 앞뒤 공백을 제거한다.
    result["반"] = result["반"].str.strip()
    result["과목"] = result["과목"].str.strip()
    print("반과 과목 공백 제거 후:", len(result))

    # 점수가 0 이상 100 이하인 행만 남긴다.
    result = result[(result["점수"] >= 0) & (result["점수"] <= 100)]
    print("점수 범위 필터링 후:", len(result))

    return result

df = 정제(pd.read_csv("scores_2026.csv"))

print(sorted(df["반"].unique()))
print(sorted(df["과목"].unique()))

수학_df = df[df["과목"] == "수학"]; print(len(수학_df))
수학90_df = df[(df["반"] == "1반") & (df["점수"] >= 90)]
print(len(수학90_df))

과목반별평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목반별평균)


def 반별평균(df):
    # 반별로 개수, 평균, 중앙값, 최댓값을 한 표로 만든다.
    표 = df.groupby("반").agg(
        개수=("점수", "size"),
        평균=("점수", "mean"),
        중앙값=("점수", "median"),
        최댓값=("점수", "max"),
    ).round(2)
    print(표)
    return 표["평균"]


반별평균(df)

print(df.groupby("반")["점수"].sum().sum())
print(df["점수"].sum())
print(df.groupby("반")["점수"].count().sum())
print(len(df))
print(df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"])

미니 = 정제(pd.read_csv("mini.csv"))
print( 반별평균( 미니))