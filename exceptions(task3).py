
import logging

# ---------------------------------------------------
# Step 3: Configure logging settings
# ---------------------------------------------------

logging.basicConfig(
    filename="calc_script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# ---------------------------------------------------
# Step 2: Calculator function with logging
# ---------------------------------------------------

def calculator(a, b, operation):
    logging.info(f"Calculator called with a={a}, b={b}, operation='{operation}'")

    try:

        if operation == "add":
            result = a + b
            logging.info(f"Addition successful: {a} + {b} = {result}")
            return result

        elif operation == "sub":
            result = a - b
            logging.info(f"Subtraction successful: {a} - {b} = {result}")
            return result

        elif operation == "mul":
            result = a * b
            logging.info(f"Multiplication successful: {a} * {b} = {result}")
            return result

        elif operation == "div":
            if b == 0:
                logging.error("Division Error: Cannot divide by zero")
                return None
            
            result = a / b
            logging.info(f"Division successful: {a} / {b} = {result}")
            return result

        else:
            logging.warning(f"Invalid operation '{operation}' received")
            return None

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None


# ---------------------------------------------------
# Step 4 & 5: Test the calculator and create logs
# ---------------------------------------------------

def test_logging():
    calculator(10, 5, "add")
    calculator(10, 5, "sub")
    calculator(10, 5, "mul")
    calculator(10, 0, "div")      # division by zero
    calculator(10, 5, "mod")      # invalid op

    print("\n✔ Script executed. Check 'calc_script.log' for log entries.")


if __name__ == "_main_":
    test_logging()