from fastapi import FastAPI, Body
import uvicorn
import time

app = FastAPI()
feedback_events = []

@app.post("/feedback/log")
def log_feedback(event: dict = Body(...)):
    event["timestamp"] = time.time()
    feedback_events.append(event)
    return {"status": "ok", "count": len(feedback_events)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
