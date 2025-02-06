# http_utils.py

import certifi
import json
import http.client
import socket
import ssl

from bancointer.utils.bancointer_validations import BancoInterValidations
from bancointer.utils.exceptions import ErroApi, BancoInterException, Erro
from bancointer.utils.token_utils import TokenUtils


class HttpUtils(object):

    def __init__(self, host, client_id, client_secret, cert, conta_corrente=None):
        """Method constructor"""
        self.host = host
        self.client_id = client_id
        self.client_secret = client_secret
        self.cert = cert
        self.conta_corrente = conta_corrente
        self.headers = {"Content-Type": "application/json"}
        self.bearer_token = {}
        self.token_util = TokenUtils(
            client_id, client_secret, cert, conta_corrente, host
        )

    def add_header_authorization(self, value):
        self.headers["Authorization"] = f"Bearer {value}"
        if self.conta_corrente is not None and self.conta_corrente is not "":
            if BancoInterValidations.validate_x_conta_corrente(self.conta_corrente):
                self.headers["x-conta-corrente"] = str(self.conta_corrente)
            else:
                erro = Erro(404, "Formato de conta corrente inválido")
                raise BancoInterException("add_header_authorization.Exception", erro)

    def add_custom_header(self, name: str, value: str):
        self.headers[name] = value

    def __create_connection(self):
        # Define the client certificate settings for https connection
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.context.load_verify_locations(certifi.where())
        self.context.load_cert_chain(certfile=self.cert[0], keyfile=self.cert[1])
        # Create a connection to submit HTTP requests
        # print(f"Host ::::: {self.host}")
        self.connection = http.client.HTTPSConnection(
            self.host, port=443, context=self.context, timeout=5.0
        )

    def __close_connection(self):
        self.connection.close()  # close the active connection

    def make_request(
        self, method, path, payload: dict, custom_headers_dict=None
    ) -> dict:
        """Make http method, execute the request.

        Args:
            method (str): Http method, GET, POST, DELETE, etc.
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data, if exceptions occurs or no response, `{}` is returned.
        """
        self.__create_connection()

        if custom_headers_dict is not None:
            # print(f"Custom HEADERS::::: {custom_headers_dict.values()}")
            self.headers.update(custom_headers_dict)

        if payload is not None:
            payload = json.dumps(payload)

        # print(f"Payload ::::: {payload}")
        # print(f"HEADERS ::::: {self.headers}")
        # print(f"Method ::::: {method}")
        # print(f"Path ::::: {path}")

        data_response: str = ""
        response: http.client.HTTPResponse | None = None
        try:
            # Use connection to submit a HTTP POST request
            self.connection.request(
                method=method, url=path, headers=self.headers, body=payload
            )

            # Print the HTTP response from the IOT service endpoint
            response = self.connection.getresponse()

            print(response.status, response.reason)
            data_response = response.read().decode("utf-8")
            # print(f"data_response: {data_response}")

        except TimeoutError:
            self.__close_connection()
            erro = Erro(408, "Banco inter API request timeout.")
            raise BancoInterException(
                "BancoInterException.HttpUtils.make_request", erro
            )
        except socket.gaierror as e:
            self.__close_connection()
            # Captura o erro de nome de host
            print(f"Host {self.host} - Erro: {e}")
            erro = Erro(502, f"Connection Error: {self.host}")
            raise BancoInterException(
                "BancoInterException.HttpUtils.make_request", erro
            )
        except Exception as e:
            print(f"make_request.Exception: {e}")
            self.__close_connection()

        if response is not None and (
            response.status < 200 or response.status > 299
        ):  # ! Error 200, SUCCESS
            data_response = json.loads(data_response)
            if "message" in data_response:
                data_response = data_response["message"]
            erro = Erro(response.status, data_response)
            if 399 < response.status < 500:  # Error 400
                self.token_util.save_token_to_file()
                raise BancoInterException(
                    "BancoInterException.HttpUtils.make_request", erro
                )
            else:
                raise BancoInterException(
                    "BancoInterException.HttpUtils.make_request", erro
                )

        # Convert bytes to JSON
        json_data = {}
        try:
            json_data = json.loads(
                data_response
            )  # Decodes the bytes and loads them as JSON

            if "title" in json_data:
                raise ErroApi(**json_data)

        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
        finally:
            self.__close_connection()

        return json_data

    def make_request_with_token(
        self, method, path, payload: dict, custom_headers_dict: dict = None
    ):
        """Make http method. Invoke the make request.

        Args:
            method (str): Http method, GET, POST, DELETE, etc.
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data.
        """
        # get api token
        self.add_header_authorization(self.token_util.get_api_token())
        return self.make_request(method, path, payload, custom_headers_dict)

    def make_get(self, path, payload: dict = None, custom_headers_dict: dict = None):
        """Make http GET method. Invoke the make request with token.

        Args:
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data.
        """
        return self.make_request_with_token("GET", path, payload, custom_headers_dict)

    def make_post(self, path, payload: dict, custom_headers_dict: dict = None):
        """Make http POST method. Invoke the make request with token.

        Args:
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data.
        """
        return self.make_request_with_token("POST", path, payload, custom_headers_dict)

    def make_delete(self, path, payload: dict = None, custom_headers_dict: dict = None):
        """Make http DELETE method. Invoke the make request with token.

        Args:
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data.
        """
        return self.make_request_with_token(
            "DELETE", path, payload, custom_headers_dict
        )

    def make_put(self, path, payload: dict, custom_headers_dict: dict = None):
        """Make http PUT method. Invoke the make request with token.

        Args:
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data.
        """
        return self.make_request_with_token("PUT", path, payload, custom_headers_dict)

    def make_patch(self, path, payload: dict, custom_headers_dict: dict = None):
        """Make http PATCH method. Invoke the make request with token.

        Args:
            path (str): String path to endpoint.
            payload (dict): Payload data to send to api.
            custom_headers_dict (dict): Custom data headers.

        Returns:
            dict object response data.
        """
        return self.make_request_with_token("PATCH", path, payload, custom_headers_dict)
