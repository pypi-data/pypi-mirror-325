from . import deepsearch
import asyncio


def main():
    asyncio.run(deepsearch.main())


# Optionally expose other important items at package level
__all__ = ["main", "server"]
