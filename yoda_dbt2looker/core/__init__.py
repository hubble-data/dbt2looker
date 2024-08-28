from .utils import configure_logging
from .config import config

# Configure logging when the package is imported
configure_logging(config.LOG_LEVEL)

# Import other necessary modules or functions
from .converter import convert
