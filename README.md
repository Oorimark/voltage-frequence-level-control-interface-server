# Voltage-Frequency-Level-Control-Interface-Server

This is a server that handles request posted by an ESP8226 module through the post method also provides an interface to view the data. This Interface that displays the voltage and frequency level of a system.

## API DOCUMENTATION

### URL: http://127.0.0.1:8000/post-data

### METHOD: POST

### JSON

```
{
    "data": {
        "frequency": 50.02,
        "voltage": 50.02
    }
}

```

### SUCCESS_RESPONSE:

```
{
    "res": "data posted success"
}

```

### ERROR RESPONSE:

```
{
  "err": "please provide data or read the doc for more info."
}
```

---

### URL: http://127.0.0.1:8000/

### METHOD: GET

### SUCCESS RESPONSE: renders html page

#### NOTE: THE URL ABOVE ARE JUST DEVELOPMENT VERSION
