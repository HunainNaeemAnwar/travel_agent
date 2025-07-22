# 🧳 AI Travel Designer Agent

An AI-powered multi-agent system that plans personalized travel experiences using the OpenAI Agent SDK and Chainlit UI.

---

## ✨ Description

This project simulates an intelligent travel planner that suggests destinations, books mock hotels and flights, and helps explore local attractions. It uses multiple specialized agents and tool calling via OpenAI's Agent SDK, while the user interface is built using **Chainlit**.

---

## 🚀 Features

- Mood-based destination suggestions
- Mock hotel and flight booking
- Local food and attraction recommendations
- Native language output (multilingual support)
- Agent handoff and tool-based architecture
- Real-time conversational UI with **Chainlit**

---

## 🧠 Architecture Overview

### 🧩 OrchestratorAgent
Main coordinator handling user flow and agent delegation.

**Tools:**
- `get_native_language(language: str)` → Translates output to user’s preferred language.

**Hands Off To:**
- `DestinationAgent`
- `BookingAgent`
- `ExploreAgent`

---

### 🌍 DestinationAgent
Suggests destinations based on mood or interest.

---

### 🏨 BookingAgent
Handles hotel and flight mock bookings.

**Tools:**
- `get_all_hotels(city: str)`
- `get_all_flights(origin: str, destination: str)`

---

### 🗺️ ExploreAgent
Recommends attractions and food in the chosen destination.

---

## 🧰 Tech Stack

| Component         | Tool/Framework         |
|------------------|------------------------|
| Agent Platform    | OpenAI Agent SDK       |
| UI Interface      | Chainlit               |
| Programming Lang  | Python                 |
| Data              | Mock data (in-memory)  |



