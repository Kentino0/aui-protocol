from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/context/{user_id}")
def get_context(user_id: str):
    device_context = {
        "screenWidth": 375,
        "screenHeight": 812,
        "osType": "iOS",
        "networkStatus": "wifi"
    }
    user_prefs = {
        "theme": "light",
        "plan": "free"
    }
    user_context = {
        "userId": user_id,
        "preferences": user_prefs
    }
    return {
        "deviceContext": device_context,
        "userContext": user_context
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
