from typing import Dict

def dulce_response_create(dulce_current) -> Dict:
    return {
        "uuid": dulce_current.uuid,
        "name": dulce_current.name,
        "coste": dulce_current.coste,
        "status": dulce_current.status,
        "time_get": dulce_current.time_get,
        "deleted_at": dulce_current.deleted_at
    }