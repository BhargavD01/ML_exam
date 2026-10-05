import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Player Selection Support", page_icon="🏏", layout="wide")
ROOT=Path(__file__).parent
artifact=joblib.load(ROOT/"models/player_selection_model.pkl")
model=artifact["model"]; features=artifact["features"]; model_name=artifact["model_name"]

st.title("🏏 Player Selection Support System")
st.caption("Machine-learning decision-support prototype • final selection remains a human decision")

with st.sidebar:
    st.header("Player Performance")
    age=st.number_input("Age",18,45,25)
    matches=st.number_input("Matches Played",1,200,45)
    innings=st.number_input("Innings",1,200,40)
    not_outs=st.number_input("Not Outs",0,100,8)
    runs=st.number_input("Runs",0,20000,1800)
    batting_average=st.number_input("Batting Average",0.0,100.0,40.0,step=0.1)
    strike_rate=st.number_input("Strike Rate",0.0,200.0,90.0,step=0.1)
    centuries=st.number_input("Centuries",0,50,3)
    fifties=st.number_input("Fifties",0,100,12)
    ducks=st.number_input("Ducks",0,50,4)
    recent_form_score=st.slider("Recent Form Score",0.0,100.0,75.0)
    fitness_score=st.slider("Fitness Score",0.0,100.0,85.0)
    fielding_score=st.slider("Fielding Score",0.0,100.0,75.0)
    predict=st.button("Predict Selection",type="primary",use_container_width=True)

if predict:
    row=pd.DataFrame([{
        "age":age,"matches":matches,"innings":innings,"not_outs":not_outs,"runs":runs,"batting_average":batting_average,"strike_rate":strike_rate,"centuries":centuries,"fifties":fifties,"ducks":ducks,"recent_form_score":recent_form_score,"fitness_score":fitness_score,"fielding_score":fielding_score}],columns=features)
    pred=int(model.predict(row)[0]); prob=float(model.predict_proba(row)[0,1])
    c1,c2,c3=st.columns(3)
    c1.metric("Prediction","SELECTED" if pred else "NOT SELECTED")
    c2.metric("Selection Probability",f"{prob*100:.1f}%")
    c3.metric("Model",model_name)
    (st.success if pred else st.warning)("The model classifies this performance profile as Selected." if pred else "The model classifies this performance profile as Not Selected.")
    st.progress(prob)
    st.info("Use this result as decision support alongside coaching judgement and other contextual factors.")

st.divider()
st.subheader("Workflow")
st.write("1. Enter player-performance indicators.  2. The trained classifier processes the inputs.  3. The application returns a class and probability.  4. Human selectors interpret the output with other evidence.")
with st.expander("Dataset and limitation"):
    st.write("The included dataset is a reproducible simulated academic dataset. The Selected/Not Selected target is a documented proxy label because public performance statistics do not normally contain verified selector decisions for each player.")
