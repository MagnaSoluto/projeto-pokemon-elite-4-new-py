"""
Sistema de Logging
"""

import logging
import sys
from pathlib import Path
from .config import config


def setup_logger(name: str = "pokemon_elite_four", level: str = None) -> logging.Logger:
    """Configura logger para o projeto"""
    
    # Nível de log
    log_level = level or config.LOG_LEVEL
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Cria logger
    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)
    
    # Evita duplicação de handlers
    if logger.handlers:
        return logger
    
    # Handler para console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(numeric_level)
    
    # Handler para arquivo
    log_file = Path(config.OUTPUT_DIR) / "pokemon_elite_four.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(numeric_level)
    
    # Formato
    formatter = logging.Formatter(config.LOG_FORMAT)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Adiciona handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger


def log_function_call(func):
    """Decorator para log de chamadas de função"""
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("pokemon_elite_four")
        logger.debug(f"Chamando {func.__name__} com args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"{func.__name__} retornou: {result}")
        return result
    return wrapper
