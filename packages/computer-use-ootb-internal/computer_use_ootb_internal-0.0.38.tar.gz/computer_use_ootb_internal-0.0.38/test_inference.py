payload = {
        "uia_data": None,
        "screenshot_path": "/home/ubuntu/workspace/oymy/honkai-star-rail-menu-resized.jpg",
        "query": "Help me to complete the mission 'Buds of Memories' in Star Rail",
        "action_history": "Open the menu interface.",
        "mode": "teach",
        
        # Optional parameters
        "user_id": "star_rail",
        "trace_id": "default_trace",
        "scale_factor": "1.0x",
        "os_name": "Windows",
        "date_time": "2024-01-01",
        "llm_model": "gpt-4"
    }

import requests

response = requests.post("http://ec2-35-81-81-242.us-west-2.compute.amazonaws.com/generate_action", json=payload)
print(response.json())