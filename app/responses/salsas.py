from typing import Dict

def salsas_response_create(salsas_current) -> Dict:
    return {
        "uuid": salsas_current.uuid,
        "name": salsas_current.name,
        "coste": salsas_current.coste,
        "status": salsas_current.status,
        "time_get": salsas_current.time_get,
        "deleted_at": salsas_current.deleted_at
    }