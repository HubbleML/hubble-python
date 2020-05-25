# Hubble Python Client

The python client for [Hubble](https://docs.gethubble.io).

Docs: https://docs.gethubble.io

Contact: support@gethubble.io

Monitor your machine learning models in real-time by integrating
this client with your ML code. Hubble captures the data flowing in
and out of your model and allows you to visualise it in real-time.

Sign up for an account at https://gethubble.io

## Getting started

**Installation**

```bash
pip install hubble-client
```

**Send an event**
```python
import hubble

hubble.write_key = 'YOUR WRITE KEY'

# Send a features event
hubble.features([
  {
    "name": "pet",
    "featureType": "categorical",
    "category": "lizard",
  },
])
```
