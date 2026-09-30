from models.store import service_centers


def get_all_service_centers():
    return service_centers


def get_service_center_by_id(service_id: int):
    for service in service_centers:
        if service["id"] == service_id:
            return service

    return None