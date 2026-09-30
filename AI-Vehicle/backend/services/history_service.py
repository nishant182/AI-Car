from models.store import service_history


def get_service_history(vehicle_id: int):
    history = []

    for service in service_history:
        if service["vehicle_id"] == vehicle_id:
            history.append(service)

    return history