import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Student Dropout Risk Simulator")

avg_grade = st.slider("Average Grade", 0.0, 20.0, 12.0)
absences = st.slider("Number of Absences", 0, 40, 5)
video_minutes = st.slider("Video Minutes Watched", 0, 1000, 300)
assignments = st.slider("Assignments Submitted", 0, 10, 6)

if st.button("Evaluate Risk"):
    payload = {
        "avg_grade": avg_grade,
        "absences": absences,
        "video_minutes": video_minutes,
        "assignments_submitted": assignments
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=2)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        st.error("API is not running. Start it with: uvicorn src.flask_app:app --reload")
        st.stop()
    except requests.exceptions.Timeout:
        st.error("API is taking too long to respond.")
        st.stop()
    except requests.exceptions.HTTPError:
        st.error("API returned an error.")
        st.stop()

    result = response.json()

    st.subheader(f"Risk level: {result['risk_level'].upper()}")
    st.metric("Risk score", round(result["risk_score"], 2))

    st.write("Explanation:")
    for reason in result["explanation"]:
        st.write("-", reason)