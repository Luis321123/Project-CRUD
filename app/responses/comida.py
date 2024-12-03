from typing import Dict

def comida_response_create(comida_current) -> Dict:
    return {
        "uuid": comida_current.uuid,
        "name": comida_current.name,
        "coste": comida_current.coste,
        "status": comida_current.status,
        "time_get": comida_current.time_get,
        "deleted_at": comida_current.deleted_at
    }