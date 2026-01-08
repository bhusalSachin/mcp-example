# MCP Client–Server Example

This repository demonstrates a complete **MCP (Model Context Protocol)** setup with both a **server** and a **client** implemented in Python and running together from a single project.

The project uses **uv** for dependency management and execution.

---

## 📦 Project Structure

```
.
├── client/
│   └── main.py        # MCP client entrypoint
├── server/
│   └── main.py        # MCP server entrypoint
├── start.sh           # Startup script
├── pyproject.toml     # Project & dependency configuration
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **uv** installed

If you don’t have `uv` yet:

```bash
pip install uv
```

---

## ▶️ Running the Project

The easiest way to run both the MCP server and client is using the provided startup script.

### 1. Make the script executable

```bash
chmod +x start.sh
```

### 2. Start the application

```bash
./start.sh
```

What this does:

1. Installs and syncs all dependencies
   ```bash
   uv sync
   ```
2. Starts both the MCP client and server
   ```bash
   uv run client/main.py server/main.py
   ```

---

## 🧠 How It Works

- The **MCP Server** (`server/main.py`) exposes tools, resources, or prompts via the Model Context Protocol.
- The **MCP Client** (`client/main.py`) connects to the server and interacts with it using MCP APIs.
- Both components are launched together to simplify local development and testing.

---

## 🛠 Development

### Install dependencies only

```bash
uv sync
```

### Run components manually

```bash
uv run server/main.py
```

```bash
uv run client/main.py
```

---

## 📄 start.sh

```bash
#!/usr/bin/env bash

# 1. Install dependencies
uv sync

# 2. Run the application
uv run client/main.py server/main.py
```

---

## 🧪 Use Cases

- Learning MCP client–server architecture
- Prototyping MCP tools or resources
- Local development and experimentation

---

## 📌 Notes

- Intended for **local development**
- Adjust ports or transports (stdio / HTTP) as needed
- Ensure server readiness if running separately

---

## 🙌 Acknowledgements

- https://modelcontextprotocol.io/
- https://github.com/astral-sh/uv
