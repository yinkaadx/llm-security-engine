import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="LLM Cybersecurity Engine", layout="wide")

st.title("Serverless LLM Security Pipeline")
st.caption("Real-Time Adversarial Threat Detection & Prompt Injection Neutralization")

st.sidebar.header("Cybersecurity Configuration")
selected_endpoint = st.sidebar.selectbox("Target Enterprise LLM", ["Corporate Finance Assistant (Amazon Bedrock)", "Healthcare Triage Bot (AWS Llama)", "Internal HR Copilot (Claude)"])
attack_volume = st.sidebar.slider("Simulate Adversarial Attack Velocity", 1, 10, 5)
run_simulation = st.sidebar.button("Initialize Threat Detection Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: AWS API Gateway -> ML Threat Classifier -> LLM Inference")

if run_simulation:
    st.subheader(f"Active Zero-Trust Monitoring: {selected_endpoint}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_velocity = col1.empty()
    metric_threat = col2.empty()
    metric_latency = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(1919)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    benign_prompts = []
    malicious_prompts = []
    
    for i in range(100):
        current_benign = int(np.random.uniform(500, 1000))
        
        if i < 30:
            current_malicious = int(np.random.uniform(5, 20))
            avg_threat_score = np.random.uniform(5.0, 15.0)
            status = "STABLE"
        elif i >= 30 and i < 70:
            current_malicious = int(np.random.uniform(500, 1500) * attack_volume)
            avg_threat_score = np.random.uniform(85.0, 99.9)
            status = "ADVERSARIAL ATTACK DETECTED"
        else:
            current_malicious = int(np.random.uniform(10, 30))
            avg_threat_score = np.random.uniform(10.0, 20.0) 
            status = "ATTACK NEUTRALIZED"
            
        total_velocity = current_benign + current_malicious
        benign_prompts.append(current_benign)
        malicious_prompts.append(current_malicious)
        
        filter_latency = np.random.uniform(12.0, 18.0)
        
        metric_velocity.metric("API Ingestion Velocity", f"{total_velocity:,} Prompts/s")
        metric_threat.metric("Average Threat Score", f"{avg_threat_score:.1f}%", "Zero-Day Signatures")
        metric_latency.metric("Security Filter Latency", f"{filter_latency:.1f} ms", "In-Transit")
        
        if status == "ADVERSARIAL ATTACK DETECTED":
            metric_status.metric("Network Response", "QUARANTINING PAYLOADS", "Blocking LLM Access")
        elif status == "ATTACK NEUTRALIZED":
            metric_status.metric("Network Response", "THREAT SUPPRESSED", "System Secure")
        else:
            metric_status.metric("Network Response", "PASSING CLEAR TRAFFIC", "Normal")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=benign_prompts, mode='lines', name='Benign Traffic', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=malicious_prompts, mode='lines', name='Adversarial Prompt Injections', yaxis='y2', line=dict(color='red', dash='dot')))
        
        fig.update_layout(
            title="Large Language Model Security: Benign Traffic vs Zero-Day Prompt Injection Velocity",
            xaxis=dict(title="High-Frequency API Timeline"),
            yaxis=dict(title="Benign Prompts/sec"),
            yaxis2=dict(title="Malicious Prompts/sec", overlaying='y', side='right', range=[0, max(100, max(malicious_prompts)+1000)]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "ADVERSARIAL ATTACK DETECTED" and i == 30:
            log_placeholder.error(f"CYBERSECURITY ALERT: Massive prompt injection assault detected at {time_steps[i].strftime('%H:%M:%S')}. Serverless ML classifier intercepting and neutralizing malicious payloads. Foundation LLM protected.")
        elif status == "ATTACK NEUTRALIZED" and i == 70:
            log_placeholder.success(f"ORCHESTRATION SUCCESS: Adversarial vectors logged to cloud ledger. Network traffic returning to baseline operational limits.")
        elif status == "STABLE" and i % 5 == 0:
            log_placeholder.info(f"Log: Telemetry tick {i} ingested. Secondary ML classifier processing prompts with sub-20ms latency.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless cybersecurity pipeline successfully neutralized the adversarial machine learning attack, ensuring zero-trust protection for the Large Language Model.")
else:
    st.info("Click 'Initialize Threat Detection Engine' in the sidebar to simulate high-velocity LLM API traffic.")