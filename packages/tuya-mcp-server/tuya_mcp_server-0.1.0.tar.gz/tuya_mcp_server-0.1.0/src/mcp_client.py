import asyncio
import json
import time

import mcp.server.messages as messages
import mcp.server.stdio as stdio

NEWLINE = b"""\n"""

async def main():
    async with stdio.stdio_client() as (read_stream, write_stream):
        request = messages.ListResourcesRequest()
        print(f"Request: {request.model_dump_json()}")
        await write_stream.write(request.model_dump_json().encode() + NEWLINE)
        print("Request sent")
        time.sleep(0.1)
        try:
            response_bytes = await read_stream.read(1024)
            if not response_bytes:
                print("No response received")
                return
            response_line = response_bytes.decode().strip()
            print(f"Response line: {response_line}")
            response = json.loads(response_line)
            print(json.dumps(response, indent=2))
        except Exception as e:
            print(f"Error reading response: {e}")

if __name__ == '__main__':
    asyncio.run(main())
