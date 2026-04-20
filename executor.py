from database import insert_refund
from database import insert_incident_ticket
from database import insert_clarification
from database import insert_escalation

tool_map = {
    "create_refund_request": insert_refund,
    "create_incident_ticket": insert_incident_ticket,
    "request_clarification": insert_clarification,
    "escalate_to_human": insert_escalation,
}


def execute_tool(tool_name, tool_input, email_id):
    function_to_call = tool_map.get(tool_name)
    if function_to_call is None:
        print("Tool not found")
        return None
    else:
        row_id = function_to_call(email_id=email_id , **tool_input)
        return row_id
    




