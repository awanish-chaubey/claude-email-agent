create_refund_tool = {
    "name": "create_refund_request",
    "description": "Use this when the customer is clearly asking for a refund on a specific order.",
    "input_schema": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "string",
                "description": "The order number the customer wants refunded"
            },
            "reason": {
                "type": "string",
                "description": "Short summary of why the customer wants a refund"
            }
        },
        "required": ["order_id", "reason"]
    }
}
## create_incident_ticket

create_incident_ticket ={
"name":"create_incident_ticket",
"description":"Use this when there is any technical problem or bug and an incident needs to be created",
"input_schema":{
"type":"object",
"properties":{
"order_id" :{
    "type":"string",
    "description":"The order number if available",
},
"reason":{
    "type":"string",
    "description":"short summary of the complain"
},


},
"required" : ["reason"]
}
}

# request_clarification

request_clarification = {
"name":"request_clarification",
"description":"Use this when the customer's email is ambiguous and you need to ask them a clarifying question before taking action.",
"input_schema":{
    "type":"object",
    "properties": {
        "order_id":{
            "type":"string",
            "description": "The order id number if available",
        },

        "needed_clarity":{
            "type":"string",
            "description":"details of the clarification needed by customer "
        }
    },
    "required":["needed_clarity"]
}
}

##escalate_to_human

escalate_to_human = {
"name":"escalate_to_human",
"description": "Use this tool when customer want to esclate or there is an urgency ",
"input_schema":{
    "type":"object",
    "properties":{
        "order_id":{
            "type":"string",
            "description": "The order id number if available",
        },
        "reason":{
    "type":"string",
    "description":"summary of the complain"
},
"urgency":{
    "type":"string",
    "enum": ["low", "medium", "high", "legal_risk"],
    "description":"What is the urgency"
},
"action_point":{
    "type":"string",
    "description":"What is the action point for the human"
}
    },
    "required":["reason","urgency","action_point"]

}

}

all_tools = [
    create_refund_tool,
    create_incident_ticket,
    request_clarification,
    escalate_to_human,
]