"""
dc_kafka_python_six_fix/fix.py
Fix for kafka-python's missing 'six.moves' module.
"""

import os
import sys
import logging
import shutil
import site

def fix_six():
    """
    Fix kafka-python's missing 'six.moves' module by:
    - Removing conflicting six.py files from the virtual environment
    - Ensuring kafka.vendor.six.moves is properly injected
    """
    logging.basicConfig(level=logging.DEBUG)
    
    try:
        import six
    except ImportError:
        logging.error("six is not installed. Installing now...")
        os.system("pip install six==1.16.0")  # Install if missing

    # Step 1: Detect and remove conflicting `six.py` files
    venv_site_packages = site.getsitepackages()
    for site_pkg in venv_site_packages:
        six_path = os.path.join(site_pkg, "six.py")
        if os.path.exists(six_path):
            logging.debug(f"Removing conflicting six.py at {six_path}")
            os.remove(six_path)

        six_cache = os.path.join(site_pkg, "__pycache__", "six.cpython-*.pyc")
        if os.path.exists(six_cache):
            logging.debug(f"Removing cached six at {six_cache}")
            shutil.rmtree(six_cache)

    # Step 2: Inject six.moves into kafka.vendor
    import six
    import types

    if "kafka.vendor" not in sys.modules:
        sys.modules["kafka.vendor"] = types.ModuleType("vendor")

    sys.modules["kafka.vendor.six"] = six
    sys.modules["kafka.vendor.six.moves"] = six.moves

    logging.debug("Kafka six.moves fix applied successfully.")

# Run fix automatically
fix_six()
