from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()

@app.post("/ui/generate")
def generate_ui(context: dict = Body(...)):
    device_ctx = context.get("deviceContext", {})
    user_ctx = context.get("userContext", {})

    # Simple logic
    is_mobile = device_ctx.get("screenWidth", 1024) < 600
    user_plan = user_ctx.get("preferences", {}).get("plan", "free")

    layout_type = "vertical-stack" if is_mobile else "horizontal-stack"
    layout = {
        "type": layout_type,
        "children": [
            {"type": "text", "props": {"content": f"Hello {user_ctx.get('userId')}!"}},
            {"type": "button", "props": {"label": "Click Me"}}
        ]
    }

    if user_plan == "premium":
        layout["children"].append({"type": "badge", "props": {"label": "Premium"}})

    return {
        "version": "1.0",
        "layout": layout,
        "styles": {
            "theme": user_ctx.get("preferences", {}).get("theme", "light")
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
