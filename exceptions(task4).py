
import logging

# --------------------------------------
# Step 1: Configure logging
# --------------------------------------
logging.basicConfig(
    filename="auto_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# --------------------------------------
# Step 2: Create decorator for auto-logging
# --------------------------------------
def auto_log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Called function: {func.__name__}")
        logging.info(f"Arguments: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error in {func._name_}: {e}")
            raise
    return wrapper


# --------------------------------------
# Step 3: Calculator functions
# (decorator applied automatically)
# --------------------------------------

@auto_log
def add(a, b):
    return a + b

@auto_log
def subtract(a, b):
    return a - b

@auto_log
def multiply(a, b):
    return a * b

@auto_log
def divide(a, b):
    return a / b


# --------------------------------------
# Step 4: Test the functions
# --------------------------------------
print(add(10, 5))
print(subtract(20, 4))
print(multiply(3, 7))
print(divide(15, 3))