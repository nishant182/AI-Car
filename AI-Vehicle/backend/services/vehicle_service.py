from models.store import vehicles


def get_all_vehicles():
    return vehicles


def get_vehicle_by_id(vehicle_id: int):

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            return vehicle

    return None


def add_vehicle(vehicle_data):

    new_vehicle = {
        "id": len(vehicles) + 1,
        **vehicle_data
    }

    vehicles.append(new_vehicle)

    return new_vehicle