import asyncio
import pymsteams
import config

from fastapi import FastAPI

app = FastAPI(title="Microsoft Teams Notification", version="1.0", redoc_url=None)


@app.post("/notify/")
async def notify(message: str):
    loop = asyncio.get_event_loop()

    # the async_connectorcard object is used instead of the normal one.
    messageboxes = pymsteams.async_connectorcard(config.Microsoft_Webhook_URL)

    # all formatting for the message should be the same
    messageboxes.text(message)

    # to send the message, pass to the event loop
    loop.run_until_complete(messageboxes.send())
    return "Message send"
