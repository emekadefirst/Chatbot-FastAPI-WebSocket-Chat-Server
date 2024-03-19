import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.websockets import WebSocketDisconnect
from fastapi import FastAPI, WebSocket, HTTPException

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

def openai(message):
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            result = openai(data)
            await websocket.send_text(result)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        await websocket.send_text(f"Error occurred: {str(e)}")
