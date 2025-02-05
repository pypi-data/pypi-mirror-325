# This file makes this folder an importable package.

# Import the function from Python file in the same directory
from .fix import fix_six

# Inject six into kafka.vendor so kafka-python can find it
import sys
import six

if "kafka.vendor" not in sys.modules:
    import types
    sys.modules["kafka.vendor"] = types.ModuleType("vendor")

sys.modules["kafka.vendor.six"] = six
sys.modules["kafka.vendor.six.moves"] = six.moves

# Define what is available when using from this import *
__all__ = ["fix_six"]
