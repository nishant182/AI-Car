def get_notifications(vehicle_id: int):
    
    notifications = [
        {
            "id": 1,
            "vehicle_id": vehicle_id,
            "type": "Service Reminder",
            "message": "Your vehicle service is due soon.",
            "status": "Unread"
        },
        {
            "id": 2,
            "vehicle_id": vehicle_id,
            "type": "Maintenance",
            "message": "Engine oil inspection is recommended.",
            "status": "Unread"
        },
        {
            "id": 3,
            "vehicle_id": vehicle_id,
            "type": "Tyre Reminder",
            "message": "Please inspect your tyre condition.",
            "status": "Unread"
        }
    ]

    return notifications