"""
dc_kafka_python_six_fix/fix.py
Fix for kafka-python's missing 'six.moves' module.
"""

import logging
import sys
import types

def fix_six():
    """
    Fix kafka-python's missing 'six.moves' module by injecting 
    a correct reference into kafka.vendor and sys.modules.
    """
    logging.basicConfig(level=logging.DEBUG)  # Enable logging for debug messages

    try:
        import six
    except ImportError as e:
        raise ImportError("Error: six must be installed before applying this fix.") from e

    # Ensure kafka.vendor exists
    if "kafka.vendor" not in sys.modules:
        logging.debug("Creating kafka.vendor module...")
        sys.modules["kafka.vendor"] = types.ModuleType("vendor")

    # Inject six into kafka.vendor
    if not hasattr(sys.modules["kafka.vendor"], "six"):
        logging.debug("Injecting six into kafka.vendor...")
        sys.modules["kafka.vendor"].six = six  # Inject six

    # Inject six.moves into sys.modules
    if "kafka.vendor.six.moves" not in sys.modules:
        logging.debug("Injecting six.moves into kafka.vendor.six...")
        sys.modules["kafka.vendor.six.moves"] = six.moves

    # Force reload to make sure Kafka sees the change
    if "kafka" in sys.modules:
        logging.debug("Reloading Kafka module to ensure it sees six...")
        import importlib
        importlib.reload(sys.modules["kafka"])

    logging.debug("Kafka-python six.moves fix applied successfully.")

# Run the fix automatically when the package is imported
fix_six()
