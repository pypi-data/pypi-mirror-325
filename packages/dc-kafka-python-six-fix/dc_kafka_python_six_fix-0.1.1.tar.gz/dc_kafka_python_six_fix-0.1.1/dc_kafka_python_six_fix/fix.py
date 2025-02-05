"""
dc_kafka_python_six_fix/fix.py
Fix for kafka-python's missing 'six.moves' module.
"""

import logging
import sys

def fix_six():
    """
    Fix kafka-python's missing 'six.moves' module by injecting 
    a correct reference into kafka.vendor and sys.modules.
    """
    try:
        import six
    except ImportError as e:
        raise ImportError("Error: six must be installed before applying this fix.") from e

    try:
        import kafka.vendor
    except ImportError:
        logging.debug("Kafka.vendor does not exist. Creating it...")
        import types
        sys.modules["kafka.vendor"] = types.ModuleType("vendor")

    # Ensure kafka.vendor.six exists
    if not hasattr(sys.modules["kafka.vendor"], "six"):
        logging.debug("Kafka-python six not found in vendor. Fixing it now...")
        sys.modules["kafka.vendor"].six = six  # Inject six
        logging.debug("SUCCESS: Kafka-python six issue fixed.")

    # **Critical Fix: Inject directly into sys.modules**
    if "kafka.vendor.six.moves" not in sys.modules:
        logging.debug("Injecting six.moves into sys.modules...")
        sys.modules["kafka.vendor.six.moves"] = six.moves
        logging.debug("SUCCESS: six.moves added to sys.modules.")

    logging.debug("Kafka-python six.moves issue appears to be resolved.")

# Run fix before importing Kafka
fix_six()

if __name__ == "__main__":
    print("Fix applied successfully.")

    try:
        from kafka import KafkaConsumer
        print("KafkaConsumer imported successfully.")
    except ImportError as e:
        print(f"ERROR: KafkaConsumer import failed after fix. {e}")
