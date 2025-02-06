import aiohttp
from diskcache import Cache
import os
from .const import BASE_URL, VARIABLES_URL
from .exceptions import BadRequestError, ForbiddenError, TooManyRequestsError, InternalServerError, UnknownAPIError

class MeteocatVariables:
    """Clase para interactuar con la lista de variables de la API de Meteocat."""

    def __init__(self, api_key: str):
        """
        Inicializa la clase MeteocatVariables.

        Args:
            api_key (str): Clave de API para autenticar las solicitudes.
        """
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }

    async def get_variables(self):
        """
        Obtiene la lista de variables desde la API de Meteocat.

        Returns:
            list: Datos de las variables.
        """

        # Hacer la solicitud a la API para obtener las variables
        url = f"{BASE_URL}{VARIABLES_URL}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=self.headers) as response:
                    if response.status == 200:
                        variables = await response.json()
                        return variables

                    # Gestionar errores según el código de estado
                    if response.status == 400:
                        raise BadRequestError(await response.json())
                    elif response.status == 403:
                        error_data = await response.json()
                        if error_data.get("message") == "Forbidden":
                            raise ForbiddenError(error_data)
                        elif error_data.get("message") == "Missing Authentication Token":
                            raise ForbiddenError(error_data)
                    elif response.status == 429:
                        raise TooManyRequestsError(await response.json())
                    elif response.status == 500:
                        raise InternalServerError(await response.json())
                    else:
                        raise UnknownAPIError(f"Unexpected error {response.status}: {await response.text()}")
            
            except aiohttp.ClientError as e:
                raise UnknownAPIError(
                    message=f"Error al conectar con la API de Meteocat: {str(e)}",
                    status_code=0,
                )

            except Exception as ex:
                raise UnknownAPIError(
                    message=f"Error inesperado: {str(ex)}",
                    status_code=0,
                )
