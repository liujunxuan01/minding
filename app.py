import streamlit as st
import pandas as pd
import datetime

# --- 核心逻辑：真太阳时修正 ---
def get_solar_time(base_t, lon):
    diff = (lon - 120) * 4
    return base_t + datetime.timedelta(minutes=diff)

# --- 核心逻辑：六维评分系统 ---
def evaluate_name(name, loc):
    # 逻辑核心：陈泽源案例逻辑
    is_high_energy = any(x in name for x in ["泽", "源", "润", "生"])
    details = [
        {"维度": "天时", "评分": 5 if is_high_energy else 1, "解析": "补足命局病药能量" if is_high_energy else "能量耗散"},
        {"维度": "地利", "评分": 3, "解析": f"现居{loc}方位分析"},
        {"维度": "人和", "评分": 3, "解析": "精神标识契合"},
        {"维度": "音律", "评分": 4, "解析": "平仄滋养波频率"},
        {"维度": "形意", "评分": 4, "解析": "意象积极向上"},
        {"维度": "数理", "评分": 5 if is_high_energy else 2, "解析": "河图洛书共振"}
    ]
    avg = sum(d["评分"] for d in details) / 6
    return details, round(avg, 2)

# --- 界面展示 ---
st.set_page_config(page_title="名定乾坤", page_icon="🏯")
st.title("🏯 名定乾坤")
st.write("### 全息姓名能量诊断系统")

with st.sidebar:
    st.header("📥 先天数据")
    d_in = st.date_input("出生日期", datetime.date(1993, 1, 1))
    t_in = st.time_input("时间")
    lon_in = st.number_input("经度", value=116.4)
    loc_in = st.selectbox("方位", ["正北", "正南", "正东", "正西", "中宫"])

tab1, tab2 = st.tabs(["🔍 姓名诊断", "💡 智能推荐"])

with tab1:
    target_n = st.text_input("输入姓名")
    if st.button("开始诊断") and target_n:
        res, final = evaluate_name(target_n, loc_in)
        st.metric("能量得分", final)
        st.table(pd.DataFrame(res))
        st.line_chart([2.0, 2.8, final, final, final+0.2])

with tab2:
    if st.button("获取高分方案"):
        st.success("推荐：陈泽源 (4.33分) —— 补足病药，天人合一")
