import os
import sys
import subprocess
from pathlib import Path


def ensure_dependencies():
    """Ensure all dependencies are installed"""
    try:
        import fastmcp
        import httpx
        import aiohttp
        # If we get here, core dependencies are installed
    except ImportError:
        print("Installing dependencies...")
        requirements_path = Path(__file__).parent / "requirements.txt"

        # Try to install uv if not present
        try:
            import uv
        except ImportError:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "uv"])

        # Install project dependencies
        subprocess.check_call(
            ["uv", "pip", "install", "-r", str(requirements_path)])

        print("Dependencies installed successfully")


def main():
    ensure_dependencies()

    # Import and run the MCP server
    from deepsearch import mcp
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
