import logging
import requests

class LoggingSession(requests.Session):
    def __init__(self, logger: logging.Logger):
        super().__init__()
        self.logger = logger

    def request(self, method, url, **kwargs):
        if url.startswith("https://localhost"):
            kwargs['verify'] = False
            self.logger.warning("TLS verification disabled for localhost")

        self.logger.info(f"Request: {method.upper()} {url}")
        self.logger.debug(f"Headers: {kwargs.get('headers', {})}")
        self.logger.debug(f"Params: {kwargs.get('params', {})}")
        self.logger.debug(f"Payload: {kwargs.get('json', kwargs.get('data', {}))}")
        
        response = super().request(method, url, **kwargs)
        
        self.logger.info(f"Response: {response.status_code}")
        self.logger.debug(f"Response Body: {response.text}")
        return response
