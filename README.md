# Claude Email Agent

An AI-powered email triage agent that uses Claude's tool-use feature to automatically route customer support emails to the right action — refund, incident ticket, clarification request, or human escalation.

Built as part of learning CLAUDE

## What it does

When an email arrives, Claude reads it and picks one of four tools:

- `create_refund_request` — clear refund asks
- `create_incident_ticket` — bug reports and technical issues
- `request_clarification` — ambiguous emails needing follow-up
- `escalate_to_human` — legal threats, urgent issues, angry customers

The chosen action is executed against a local SQLite database with full audit trail.

## Architecture

- `tools.py` — tool definitions for Claude
- `database.py` — SQLite schema and insert functions
- `executor.py` — routes tool calls to database functions (dispatch table pattern)
- `agent.py` — main loop, sends emails to Claude, handles responses
- `sample_emails.py` — test emails

## Fail-safe pattern

If Claude replies with text instead of picking a tool, the agent automatically escalates to a human so every email ends with a database record. This prevents silent failures.

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install: `pip install anthropic pydantic python-dotenv`
5. Create a `.env` file with:
   ANTHROPIC_API_KEY=your-key-here
   CLAUDE_MODEL=claude-haiku-4-5

6. Initialise the database: `python database.py`
7. Run the agent: `python agent.py`

## Learnings

See `FAILURE_MODES.md` for 6 production failure modes observed while building this, including silent failure, non-determinism, and schema contract failure.

## Tech stack

- Python 3.x
- Anthropic Python SDK
- SQLite (built-in)
- python-dotenv
