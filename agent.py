import os
from dotenv import load_dotenv
from anthropic import Anthropic

from tools import all_tools
from executor import execute_tool
from sample_emails import sample_emails

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
model = os.getenv("CLAUDE_MODEL")


client = Anthropic(api_key=api_key)

def process_email(email):
    email_id = email["id"]
    email_body = email["body"]

    print(f"\nProcessing {email_id}")
    print(f"Email: {email_body}")

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        tools=all_tools,
        messages=[
            {"role": "user", "content": email_body}
        ]
    )

    print(f"Stop reason: {response.stop_reason}")
    tool_was_called = False
    for block in response.content:
        if block.type == "tool_use":
            tool_name = block.name
            tool_input = block.input
            print(f"Claude picked tool: {tool_name}")
            print(f"With inputs: {tool_input}")

            row_id = execute_tool(tool_name, tool_input, email_id)
            print(f"Saved to DB with row_id: {row_id}")
            tool_was_called = True
        elif block.type == "text":
            print(f"Claude said: {block.text}")
    if not tool_was_called:
        tool_input = {"reason": "No tools selected by Claude", "urgency": "high", "action_point": "Review"}
        row_id = execute_tool("escalate_to_human", tool_input, email_id)
        print(f" ⚠️ AUTO-ESCALATION: No tool selected by Claude. Escalating to human. Row saved: {row_id}")
if __name__ == "__main__":
    for email in sample_emails:
        process_email(email)