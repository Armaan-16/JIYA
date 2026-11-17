# JIYA Architecture

## Vision

JIYA is an offline-first AI Operating System designed to help with learning, engineering, coding, automation, research, and everyday productivity while keeping user data private.

---

## Core Principles

- Offline First
- Privacy First
- Modular Architecture
- Separation of Concerns
- Scalable Design
- Easy Model Replacement

---

## System Architecture

User
│
▼
main.py
│
▼
Brain
│
▼
LLM Service
│
▼
AI Model (Qwen / GPT / Claude / etc.)

---

## Responsibilities

### main.py

Starts the application.

---

### Brain

Makes decisions.

Never communicates directly with AI models.

---

### LLM Service

Handles all communication with language models.

Responsible for:

- Sending prompts
- Receiving responses
- Switching between AI models
- Error handling

---

### Memory

Stores user information and previous conversations.

---

### Voice

Speech Recognition

Text To Speech

Wake Word

---

### Vision

Image understanding

OCR

PCB Analysis

Diagram Understanding

---

### Automation

Windows Automation

Task Scheduling

Application Control

File Management

---

## Design Philosophy

Every module should have one responsibility.

High-level modules should never depend on low-level implementations.

Changing an AI model should require modifying only one service.