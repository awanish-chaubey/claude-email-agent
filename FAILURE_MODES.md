Failure Modes Observed in Email Agent Project

1. Silent Failure
   What I observed: Claude did not choose any tool and just replied with a text message. My database had no record of the email being processed.
   Why it matters: The system was not aware of what Claude did. There was no audit trail to prove the email was handled.
   Mitigation: Track tool usage with a flag inside the loop. If no tool was called by the end, auto-escalate to a human so every email ends with a database row.

2. Non-determinism
   What I observed: Claude sometimes chose different tools for the same email content across runs.
   Why it matters: Customers see the system as unreliable and inconsistent. The internal team cannot predict what action Claude will take for a given email.
   Mitigation: Write clear, non-overlapping tool descriptions. Lower the temperature setting (close to 0) to reduce randomness in tool selection.

3. Tool Description Overlap
   What I observed: More than one tool could apply to the same email. For example, a billing dispute email could fit create_incident_ticket, create_refund_request, or escalate_to_human.
   Why it matters: Claude may pick the wrong tool. A customer wanting a refund could end up with an incident ticket instead, causing frustration and wrong routing.
   Mitigation: Write very specific, non-overlapping tool descriptions. Add explicit instruction in the system prompt that Claude should call request_clarification or escalate_to_human whenever the right action is ambiguous.

4. Reasoning Without Action
   What I observed: Claude sometimes reasoned about what should happen and replied with text instead of calling the matching tool.
   Why it matters: Customer experience suffers — they get a conversational reply instead of a resolved action. At the system level, no tool was called, so no database row was created and there is no audit trail.
   Mitigation: Track whether any tool was picked during the response loop. If not, auto-escalate or log the event to a dedicated table so no email falls through.

5. Bounded Action Space
   What I observed: Claude can only pick from the 4 tools I defined. Emails that do not fit any tool (e.g., "set delivery to 3 PM") force Claude into clarification, escalation, or a text reply.
   Why it matters: Escalation queues grow with email types I did not plan for, reducing efficiency. Without review, the gap stays invisible and the system never improves.
   Mitigation: Periodically review all escalated and no-tool emails. Tag each with the action that should have been taken. When a pattern repeats often, promote it into a new tool.

6. Schema Contract Failure
   What I observed: Claude can pass incorrect or invalid values to tool inputs — for example picking the wrong order ID when the email mentions two, or producing a value that does not match the expected format.
   Why it matters: Wrong values flow straight into the database. A refund could be created against the wrong order, or an unrelated customer could get refunded. Data becomes untrustworthy and downstream systems inherit the corruption.
   Mitigation: Use strict enums for fields with a fixed set of values (like urgency). Add Pydantic validation on tool inputs before insert. For critical fields like order_id, verify the ID exists in the real orders table before committing the action.
