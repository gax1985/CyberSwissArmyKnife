# Cyber Swiss Army Knife: System Architecture

This document outlines the architecture of the "Cyber Swiss Army Knife" project, a local-first, highly specialized personal AI infrastructure.

## 1. Core Philosophy
The project is inspired by Daniel Miessler's "markdown-first" philosophy, where the primary knowledge base is a collection of structured markdown files. This ensures portability, longevity, and easy integration with various tools. The system is designed to be a Pentesting Swiss Army Knife, categorizing MITRE ATT&CK tactics and processing penetration testing logs.

## 2. Infrastructure Overview
The infrastructure is a hybrid environment bridging a Windows host with a WSL (Ubuntu) backend.

*   **Host Environment:** Windows, running PyCharm as the primary IDE.
*   **Backend Environment:** Ubuntu on WSL for Linux-native tooling.
*   **Local LLMs:** Ollama serves local, air-gapped models (e.g., `qwen3.5:0.8b`) for privacy and offline capability.
*   **Orchestration:** Langflow, running via its desktop application, exposes a local API at `http://localhost:7860` for pipeline execution.
*   **Secure Remote Access:** OpenClaw is configured on a Tailscale network (Tailnet), with a Telegram Bot for administrative control and notifications.
*   **IDE Integration:** MCP (Multi-Capability Peripheral) servers are used to bridge the IDE (PyCharm) with the underlying system, enabling file system operations and tool execution.

## 3. Data Flow
1.  Local documents (e.g., pentesting logs) are read by a Python script.
2.  The script sends the document content to the Langflow API.
3.  Langflow processes the text using the Ollama-hosted LLM.
4.  The output is a structured markdown file written to an Obsidian vault, typically as a `SKILLS.md` payload.