import asyncio
import websockets
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)

async def handler(websocket):
    async for message in websocket:
        logging.info(f"Received: {message}")
        response = f"Echo: {message}"
        await websocket.send(response)
        logging.info(f"Sent: {response}")

async def main():
    server = await websockets.serve(
        handler,
        "0.0.0.0",
        8765,
        ping_interval=5,
        ping_timeout=5
    )
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
