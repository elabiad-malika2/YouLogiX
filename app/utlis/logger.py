import sys
import os
from loguru import logger

LOG_FILE = "logs/youexpress.log"

if not os.path.exists("logs"):
    os.makedirs("logs")

#  nettoiage la configuration par défaut de Loguru
logger.remove()


logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
    level="INFO"
)


logger.add(
    LOG_FILE,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    level="INFO",
    rotation="500 MB",  
    retention="10 days", 
    compression="zip"    
)

#  exporte le logger pour l'utiliser ailleurs
__all__ = ["logger"]