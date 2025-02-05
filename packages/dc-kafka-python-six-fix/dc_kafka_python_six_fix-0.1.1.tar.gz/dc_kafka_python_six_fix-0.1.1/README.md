# dc-kafka-python-six-fix

## Who Needs This?

- Mac/Linux users running kafka-python will encounter a missing six dependency when using Kafka.
- Windows users may be fine locally but will hit the same issue when deploying to cloud environments (e.g., GitHub Actions, Docker, or other Linux-based CI/CD).

## What Does this Fix Do?

- Restores compatibility without modifying existing Kafka code.
- Prevents the ModuleNotFoundError: No module named 'kafka.vendor.six.moves' issue.
- Works instantly without requiring manual virtual environment tweaks.
- Works for Kafka using kafka-python.


## How To Use This Fix 


### Step 1. Install 
Run

```
pip install dc-kafka-python-six-fix
```

OR add this dependency to requirements.txt and run with:

```
python3 -m pip install -r requirements.txt
```

## Step 2. Import & Apply The Fix

Import and apply the fix before importing from Kafka. For example:

```python
from dc_kafka_python_six_fix import fix_six
fix_six() 

from kafka import KafkaConsumer
```
## Why Is This Fix Needed?

- The kafka-python package expects six.moves inside kafka.vendor, but six is no longer included.
- This package restores six to the expected location, allowing Kafka Consumers to function without modification.
- No need to manually patch virtual environments every time we install kafka-python.

---

## Warning: kafka-python Is No Longer Maintained

- The kafka-python package is no longer actively maintained.
- Consider migrating to [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python) for all future projects.
- The migration requires minimal changes but provides long-term stability.
