from flowshow import create_flow_chart

# Example task data
data = {
    "task_name": "main",
    "start_time": "2025-02-01T20:21:59.984927+00:00",
    "duration": 6.530065041035414,
    "inputs": {},
    "error": None,
    "retry_count": 0,
    "end_time": "2025-02-01T20:22:06.514988+00:00",
    "logs": "yo\n10\nyeeheaw\n10\n",
    "output": None,
    "subtasks": [
        # ... your existing task data here
    ],
}

# Create and save the visualization
chart = create_flow_chart(data)
