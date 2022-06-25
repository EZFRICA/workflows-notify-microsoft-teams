import pymsteams
import config
import uvicorn

from fastapi import FastAPI

app = FastAPI(title="Microsoft Teams Notification", version="1.0", redoc_url=None)


@app.post("/notify/", status_code=201)
async def notify(message: str):

    messageboxes = pymsteams.connectorcard(config.Microsoft_Webhook_URL)

    # Add text to the message.
    messageboxes.text(message)

    # send the message.
    messageboxes.send()

    return "Message send"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)