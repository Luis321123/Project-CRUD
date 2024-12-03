from typing import Dict

def enlatados_response_create(enlatados_current) -> Dict:
    return {
        "uuid": enlatados_current.uuid,
        "name": enlatados_current

.name,
        "coste": enlatados_current.coste,
        "status": enlatados_current.status,
        "time_get": enlatados_current.time_get,
        "deleted_at": enlatados_current.deleted_at
    }