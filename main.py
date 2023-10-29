import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="SushiXswap On Avalanche",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

text_1 = '<p style="font-family:sans-serif; color:#48b0ae; font-size: 20px;">SushiXSwap is Sushi’s cross-chain AMM (automated market maker) that enables users to execute swaps across chains without any additional lockup period or fees. It leverages LayerZero’s Stargate protocol to quickly and effectively swap assets between multiple ecosystems.</p>'

text_2 = '<p style="font-family:sans-serif; color:#48b0ae; font-size: 20px;">This dashboard aims to offer a view into the usage of SushiXswap on Avalanche.</p>'

text_3 = '<p style="font-family:sans-serif; color:#48b0ae; font-size: 20px;">The data used for this dashboard is from <a href="https://flipsidecrypto.xyz/">Flipside Crypto</a>. Queries: <a href="https://flipsidecrypto.xyz/edit/queries/d1ec94a0-77e1-4090-b5cb-affe3976b737">1</a>, <a href="https://flipsidecrypto.xyz/edit/queries/a3af8f8f-ef2b-4214-8dd4-d2645e098c99">2</a>, <a href="https://flipsidecrypto.xyz/edit/queries/be69a572-e074-48bc-bd24-a5f2f6a8e2f3">3</a>, <a href="https://flipsidecrypto.xyz/edit/queries/266a32a4-168d-418d-a069-734c92ab2284">4</a>, <a href="https://flipsidecrypto.xyz/edit/queries/e43fc057-59a7-4a71-9144-96916a29da38">5</a>, <a href="https://flipsidecrypto.xyz/edit/queries/c088118e-3855-470f-88c5-9d3e53149908">6</a>. Special thanks to <a href="https://flipsidecrypto.xyz/Herotat">Herotat</a> whose <a href="https://flipsidecrypto.xyz/Herotat/sushi-xswap-stats--GB0-t">work</a> helped in decoding the event logs.</p>'

text_4 = '<p style="font-family:sans-serif; color:#48b0ae; font-size: 20px;">This dashboard is hosted on <a href="https://streamlit.io/cloud/">Streamlit Cloud</a>, the repo is available <a href="https://github.com/OOlajide/sushixswap-on-avalanche">here</a>.</p>'

st.markdown(f'<h1 style="color:#d1cc2c;font-size:60px;text-decoration:underline;text-align:center;">{"SushiXswap On Avalanche"}</h1>', unsafe_allow_html=True)
st.markdown(text_1, unsafe_allow_html=True)
st.markdown(text_2, unsafe_allow_html=True)
st.markdown(text_3, unsafe_allow_html=True)
st.markdown(text_4, unsafe_allow_html=True)

# swaps from avalanche to other chains
url_1 = "https://api.flipsidecrypto.com/api/v2/queries/d1ec94a0-77e1-4090-b5cb-affe3976b737/data/latest"
df_1 = pd.read_json(url_1)

# swaps from other chains to avalanche
url_2 = "https://api.flipsidecrypto.com/api/v2/queries/a3af8f8f-ef2b-4214-8dd4-d2645e098c99/data/latest"
df_2 = pd.read_json(url_2)

# totals: avalanche to other chains
url_3 = "https://api.flipsidecrypto.com/api/v2/queries/be69a572-e074-48bc-bd24-a5f2f6a8e2f3/data/latest"
df_3 = pd.read_json(url_3)

# totals: other chains to avalanche
url_4 = "https://api.flipsidecrypto.com/api/v2/queries/266a32a4-168d-418d-a069-734c92ab2284/data/latest"
df_4 = pd.read_json(url_4)

# weekly stats from avalanche
url1 = "https://api.flipsidecrypto.com/api/v2/queries/c088118e-3855-470f-88c5-9d3e53149908/data/latest"
df1 = pd.read_json(url1)

# sushixswap users on avalanche
url2 = "https://api.flipsidecrypto.com/api/v2/queries/e43fc057-59a7-4a71-9144-96916a29da38/data/latest"
df2 = pd.read_json(url2)

st.warning("As confirmed by the developers, there was a period of inactivity on SushiXswap during the rollout of Version 2 of the protocol.", icon="⚠️")
st.image("pic.png")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.header("Weekly Stats From Avalanche To Other Chains")
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

fig1 = px.bar(df1, x="WEEK", y="USD_VOLUME", color="VERSION", title="Weekly USD Volume (Avalanche To Other Chains)")
fig1.update_layout(hovermode="x unified")

fig2 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig2.add_trace(
    go.Line(x=df1["WEEK"], y=df1["AVG_VOLUME"], name="weekly_average_volume"),
    secondary_y=False,
)
fig2.add_trace(
    go.Line(x=df1["WEEK"], y=df1["MEDIAN_VOLUME"], name="weekly_median_volume"),
    secondary_y=True,
)
# Add figure title
fig2.update_layout(
    title_text="Weekly Average & Median USD Volume (Avalanche To Other Chains)"
)
# Set x-axis title
fig2.update_xaxes(title_text="Week")

# Set y-axes titles
fig2.update_yaxes(title_text="weekly_average_volume", secondary_y=False)
fig2.update_yaxes(title_text="weekly_median_volume", secondary_y=True)
fig2.update_layout(hovermode="x unified")

fig3 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig3.add_trace(
    go.Line(x=df1["WEEK"], y=df1["ACTIVE_USERS"], name="weekly_active_users"),
    secondary_y=False,
)
fig3.add_trace(
    go.Line(x=df1["WEEK"], y=df1["TXN_COUNT"], name="weekly_txn_count"),
    secondary_y=True,
)
# Add figure title
fig3.update_layout(
    title_text="Weekly Active Users & Txn Count (Avalanche To Other Chains)"
)
# Set x-axis title
fig3.update_xaxes(title_text="Week")

# Set y-axes titles
fig3.update_yaxes(title_text="weekly_active_users", secondary_y=False)
fig3.update_yaxes(title_text="weekly_txn_count", secondary_y=True)
fig3.update_layout(hovermode="x unified")

fig4 = px.pie(df2, values='TXN_COUNT', names='LABEL_TYPE', title='Share Of Avalanche SushiXswap Users Activities')

col_a, col_b = st.columns(2)
with col_a:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
with col_b:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

col_c, col_d = st.columns(2)
with col_c:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
with col_d:
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

st.markdown("""
<p>
  <ul>
    <li>Adoption of SushiXswap on Avalanche started gradually, with a significant uptick in April 2023, marked by a surge in weekly volume and active users. However, by mid-July, this trend reversed."</li>
    <li>During the period of increased activity, the average and median USD volume showed a declining trend.</li>
    <li>48 percent of SushiXswap users hang around the defi section of Avalanche.</li>
  </ul>
</p>""", unsafe_allow_html=True)

col_1, col_2 = st.columns(2)
with col_1:
    colored_header(
    label="",
    description="",
    color_name="gray-70",
)
    st.header("Avalanche To Other Chains")
    colored_header(
    label="",
    description="",
    color_name="gray-70",
)
    st.metric("Total USD Volume", millify(df_1["USD_VOLUME"].sum(), precision=2))

    fig_a1 = px.bar(df_1, x="WEEK", y="USD_VOLUME", color="DESTINATION_CHAIN", title="Weekly USD Volume")
    fig_a1.update_layout(hovermode="x unified")
    st.plotly_chart(fig_a1, theme="streamlit", use_container_width=True)

    fig_a2 = px.bar(df_1, x="WEEK", y="ACTIVE_USERS", color="DESTINATION_CHAIN", title="Weekly Active Users")
    fig_a2.update_layout(hovermode="x unified")
    st.plotly_chart(fig_a2, theme="streamlit", use_container_width=True)

    st.write("In terms of weekly volume and active users, Arbitrum emerges as the preferred destination for swaps from Avalanche, especially during the surge that began in April, with Polygon following closely in second place.")
    fig_a3 = px.bar(df_1, x="WEEK", y="TXN_COUNT", color="DESTINATION_CHAIN", title="Weekly Transaction Count")
    fig_a3.update_layout(hovermode="x unified")
    st.plotly_chart(fig_a3, theme="streamlit", use_container_width=True)

    fig_a4 = px.line(df_1, x="WEEK", y="AVG_VOLUME", color="DESTINATION_CHAIN", title="Weekly Average Volume")
    fig_a4.update_layout(hovermode="x unified")
    st.plotly_chart(fig_a4, theme="streamlit", use_container_width=True)

    st.markdown("""
    <p>
    <ul>
        <li>Arbitrum is also the leading chain for swaps from Avalanche in terms of weekly number of swaps.</li>
        <li>For weekly average volume, Ethereum stands out as the leader. At its peak in early February 2023, Ethereum reached a weekly average volume of $30,000. In comparison, the second-highest weekly average volume for swaps from Avalanche to other chains is Polygon, with $5,675.</li>
    </ul>
    </p>""", unsafe_allow_html=True)

    colored_header(
    label="",
    description="",
    color_name="gray-70",
)
    st.header("Avalanche To Other Chains")
    colored_header(
    label="",
    description="",
    color_name="gray-70",
)

    col_1a, col_2a = st.columns(2)
    with col_1a:
        pie_a1 = px.pie(df_3, values='USD_VOLUME', names='DESTINATION_CHAIN', title='Share Of USD Volume')
        st.plotly_chart(pie_a1, theme="streamlit", use_container_width=True)
    with col_2a:
        pie_a2 = px.pie(df_3, values='AVG_VOLUME', names='DESTINATION_CHAIN', title='Share Of Average Volume')
        st.plotly_chart(pie_a2, theme="streamlit", use_container_width=True)
    col_3a, col_4a = st.columns(2)
    with col_3a:
        pie_a3 = px.pie(df_3, values='ACTIVE_USERS', names='DESTINATION_CHAIN', title='Share Of Active Users')
        st.plotly_chart(pie_a3, theme="streamlit", use_container_width=True)
    with col_4a:
        pie_a4 = px.pie(df_3, values='TXN_COUNT', names='DESTINATION_CHAIN', title='Share Of Transaction Count')
        st.plotly_chart(pie_a4, theme="streamlit", use_container_width=True)

with col_2:
    colored_header(
    label="",
    description="",
    color_name="gray-70",
)
    st.header("Other Chains To Avalanche")
    colored_header(
    label="",
    description="",
    color_name="gray-70",
)
    st.metric("Total USD Volume", millify(df_2["USD_VOLUME"].sum(), precision=2))

    fig_b1 = px.bar(df_2, x="WEEK", y="USD_VOLUME", color="SOURCE_CHAIN", title="Weekly USD Volume")
    fig_b1.update_layout(hovermode="x unified")
    st.plotly_chart(fig_b1, theme="streamlit", use_container_width=True)

    fig_b2 = px.bar(df_2, x="WEEK", y="ACTIVE_USERS", color="SOURCE_CHAIN", title="Weekly Active Users")
    fig_b2.update_layout(hovermode="x unified")
    st.plotly_chart(fig_b2, theme="streamlit", use_container_width=True)

    st.write("On the flip side (no pun intended), Arbitrum stands out as the primary source for swaps from other blockchains to Avalanche, with BSC and Polygon also commanding significant shares in terms of weekly users and volume.")

    fig_b3 = px.bar(df_2, x="WEEK", y="TXN_COUNT", color="SOURCE_CHAIN", title="Weekly Transaction Count")
    fig_b3.update_layout(hovermode="x unified")
    st.plotly_chart(fig_b3, theme="streamlit", use_container_width=True)

    fig_b4 = px.line(df_2, x="WEEK", y="AVG_VOLUME", color="SOURCE_CHAIN", title="Weekly Average Volume")
    fig_b4.update_layout(hovermode="x unified")
    st.plotly_chart(fig_b4, theme="streamlit", use_container_width=True)

    st.markdown("""
    <p>
    <ul>
        <li>The same trend applies in the other direction—when moving from other chains to Avalanche. Ethereum leads with the highest weekly average volume, while Arbitrum narrowly surpasses Polygon to secure the second spot</li>
        <li>it's notable that Ethereum consistently maintains a dominant position in terms of weekly average volume in both directions, emphasizing its pivotal role in Avalanche's DeFi ecosystem.</li>
    </ul>
    </p>""", unsafe_allow_html=True)

    colored_header(
    label="",
    description="",
    color_name="gray-70",
)
    st.header("Other Chains To Avalanche")
    colored_header(
    label="",
    description="",
    color_name="gray-70",
)

    col_1a, col_2a = st.columns(2)
    with col_1a:
        pie_b1 = px.pie(df_4, values='USD_VOLUME', names='SOURCE_CHAIN', title='Share Of USD Volume')
        st.plotly_chart(pie_b1, theme="streamlit", use_container_width=True)
    with col_2a:
        pie_b2 = px.pie(df_4, values='AVG_VOLUME', names='SOURCE_CHAIN', title='Share Of Average Volume')
        st.plotly_chart(pie_b2, theme="streamlit", use_container_width=True)
    
    col_3a, col_4a = st.columns(2)
    with col_3a:
        pie_b3 = px.pie(df_4, values='ACTIVE_USERS', names='SOURCE_CHAIN', title='Share Of Active Users')
        st.plotly_chart(pie_b3, theme="streamlit", use_container_width=True)
    with col_4a:
        pie_b4 = px.pie(df_4, values='TXN_COUNT', names='SOURCE_CHAIN', title='Share Of Transaction Count')
        st.plotly_chart(pie_b4, theme="streamlit", use_container_width=True)

# st.markdown("""
# <p>
# <ul>
#     <li></li>
#     <li></li>
#     <li></li>
# </ul>
# </p>""", unsafe_allow_html=True)