from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ---------------------------
# Request schema
# ---------------------------
class StudentInput(BaseModel):
    avg_grade: float
    absences: int
    video_minutes: int
    assignments_submitted: int


# ---------------------------
# Response schema
# ---------------------------
class PredictionOutput(BaseModel):
    risk_score: float
    risk_level: str
    explanation: list[str]


# ---------------------------
# Manual scoring logic
# ---------------------------
def manual_risk_score(data: StudentInput):
    score = 0.0
    reasons = []

    # Absences
    if data.absences > 20:
        score += 0.4
        reasons.append("High number of absences")
    elif data.absences > 10:
        score += 0.2
        reasons.append("Moderate number of absences")

    # Grades
    if data.avg_grade < 10:
        score += 0.3
        reasons.append("Low average grade")
    elif data.avg_grade < 13:
        score += 0.15
        reasons.append("Moderate grades")

    # Engagement
    if data.video_minutes < 200:
        score += 0.2
        reasons.append("Low video engagement")

    # Assignments
    if data.assignments_submitted < 5:
        score += 0.2
        reasons.append("Low assignment submission")

    score = min(score, 1.0)

    if score > 0.6:
        level = "high"
    elif score > 0.3:
        level = "medium"
    else:
        level = "low"

    return score, level, reasons


# ---------------------------
# API endpoint
# ---------------------------
@app.post("/predict", response_model=PredictionOutput)
def predict_dropout(student: StudentInput):
    score, level, reasons = manual_risk_score(student)

    return {
        "risk_score": score,
        "risk_level": level,
        "explanation": reasons
    }
