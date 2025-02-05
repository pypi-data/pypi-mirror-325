from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncio
import uvicorn
from webhook_appservice import WebhookAppservice
from api import DynamicApi
from logger import AppserviceLogger

listen_port = 8228
log = AppserviceLogger()
appservice = None  # Store appservice instance globally


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage startup and shutdown lifecycle"""
    global appservice

    api = DynamicApi(app, log)
    appservice = WebhookAppservice(api, log, listen_port)

    try:
        await appservice.start()  # Start appservice
        yield  # Hand over control to FastAPI
    finally:
        log.info("Shutting down appservice...")
        if appservice:
            try:
                await appservice.stop()
                log.info("Appservice stopped.")
            except asyncio.CancelledError:
                log.info("Appservice shutdown was interrupted.")

        log.info("Lifespan shutdown complete.")


app = FastAPI(lifespan=lifespan)

async def run_uvicorn():
    """Run Uvicorn properly and handle shutdown"""
    config = uvicorn.Config(app, host="0.0.0.0", port=listen_port)
    server = uvicorn.Server(config)

    try:
        await server.serve()
    except asyncio.CancelledError:
        log.info("Uvicorn shutdown interrupted. Cleaning up...")


async def main():
    """Start Uvicorn and appservice together"""
    await run_uvicorn()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Received KeyboardInterrupt, shutting down...")
