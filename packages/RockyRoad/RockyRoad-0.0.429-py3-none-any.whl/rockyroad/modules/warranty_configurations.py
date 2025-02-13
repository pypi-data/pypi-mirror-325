from .module_imports import key
from uplink import (
    Consumer,
    get as http_get,
    returns,
    headers,
)


@headers({"Ocp-Apim-Subscription-Key": key})
class _Warranty_Configurations(Consumer):
    """Inteface to warranty configurations resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    @returns.json
    @http_get("warranties/configurations/roles")
    def get_roles_configuration(
        self,
    ):
        """This call will return configuration information for warranty roles."""
