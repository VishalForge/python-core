import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()  # also prints to terminal
    ]
)

logger = logging.getLogger(__name__)

def divide(a: float, b: float) -> float | None:
    logger.info(f"Dividing {a} by {b}")
    if b == 0:
        logger.error("Cannot divide by zero")
        return None
    result = a/b
    logger.debug(f"Result: {result}")
    return result

divide(10, 2)
divide(5, 0)