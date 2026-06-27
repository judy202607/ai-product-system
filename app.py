import streamlit as st
import pandas as pd

st.title("📊 AI选品系统（公开版）")

file = st.file_uploader("上传Excel文件", type=["xlsx"])

def score(row):
    title = str(row.get("标题",""))
    demand = float(row.get("想要数",0))
    exam = str(row.get("考试时间",""))

    s = 0

    # 需求权重
    s += min(demand/50, 6)

    # 热词加权
    if "真题" in title: s += 3
    if "押题" in title: s += 4
    if "2026" in title: s += 2
    if "教师招聘" in title: s += 2
    if "事业单位" in title: s += 2

    # 时间权重
    if "秋季" in exam:
        s += 3
    if "3-6月" in exam:
        s += 2

    return s


if file:
    df = pd.read_excel(file)

    df["AI评分"] = df.apply(score, axis=1)

    def level(x):
        if x >= 8:
            return "🔥爆款"
        elif x >= 5:
            return "📈潜力"
        else:
            return "💀淘汰"

    df["分层"] = df["AI评分"].apply(level)

    df = df.sort_values("AI评分", ascending=False)

    st.subheader("📊分析结果")
    st.dataframe(df)

    st.download_button(
        "下载结果Excel",
        df.to_csv(index=False),
        "分析结果.csv"
    )
