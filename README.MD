# Access Camera Login Scanner

## Summary
 This tool uses the Requests library to make HTTP reqeusts with basic Digest Authentication to a list of targets specified in a file passed as the only argument. It is currently in early development.

## Usage
```
python3 axis-login.py {TARGETS FILE}
```

Targets file should be a list of base URLS (IE http://10.10.10.10/), with or without a slash at the end.

## Additional Information
From the environment I was testing, the AXIS cameras use a variety of endpoint URLs for authentication. I've compiled a list of three of them that I have seen, and the script will loop through each one until it either receives a 401 or a 200, indicating failure or success. If a 404 is received, the script moves on to the next endpoint. If any other HTTP status code is returned, an error is logged with all of the relevant request and response information to the file specified in the script.

If no valid login endpoint is found it will alert you. I'd recommend accessing the device management web service manually while proxying through Burp to identify the login endpoint and ensure it's using the same HTTP Digest Authentication method that this script utilizes.

## Other stuff
Only use this on things you have been given permission to test yadda yadda. I can't guarantee what will happen when you run this script. It may also miss things.
