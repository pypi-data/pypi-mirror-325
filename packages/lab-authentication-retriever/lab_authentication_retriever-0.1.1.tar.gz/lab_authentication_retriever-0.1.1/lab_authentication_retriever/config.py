import json

import tornado
from jupyter_server.base.handlers import APIHandler
from qbraid_core import QbraidSession


from .config_logger import get_logger

logger = get_logger(__name__)


class UserConfigHandler(APIHandler):
    """Handler for managing user configurations and other local data."""

    @tornado.web.authenticated
    def get(self):
        """Get user's qBraid credentials and available Python executables."""
        credentials = self.default_action()
        
        config = {**credentials}
        self.finish(json.dumps(config))
    
    def default_action(self):
        try:    
            """Configure qBraid CLI options."""
            session = QbraidSession()
            email = session.get_config("email")
            token = session.get_config("refresh-token")
            api_key = session.get_config("api-key")
            url = session.get_config("url")
        except Exception as e:
            logger.error(f"Error while retrieving user configuration: {e}")
            email = None
            token = None
            api_key = None
            url = None
        
        return {
            "email": email,
            "refreshToken": token,
            "apiKey": api_key,
            "url":url
        }
        

