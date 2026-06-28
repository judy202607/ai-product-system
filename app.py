import streamlit as st
import pandas as pd

st.title("V4智能选品系统")

st.write("📂 上传Excel文件（必须包含：标题 / 链接 / 时间）")

uploaded_file = st.file_uploader("选择Excel文件", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        st.subheader("📊 原始数据预览")
        st.dataframe(df)

        # 自动检查列
        required_cols = ["标题", "链接", "时间"]
        missing = [col for col in required_cols if col not in df.columns]

        if missing:
            st.error(f"缺少列：{missing}，请检查Excel表头")
        else:
            df = df.sort_values(by="时间", ascending=False)

            st.subheader("🔥 按时间排序结果")
            st.dataframe(df)

    except Exception as e:
        st.error(f"读取失败：{e}")
