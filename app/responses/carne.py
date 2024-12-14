from typing import Dict

def carne_response_create(carne_current) -> Dict:
    return {
        "uuid": carne_current.uuid,
        "name": carne_current.name,
        "coste": carne_current.coste,
        "status": carne_current.status,
        "time_get": carne_current.time_get,
        "deleted_at": carne_current.deleted_at
    }