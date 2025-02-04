Country Flags API
============

Country Flag is a simple tool for getting the country's national flags. It returns the country's national flags.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Country Flags API](https://apiverve.com/marketplace/api/countryflags)

---

## Installation
	pip install apiverve-countryflags

---

## Configuration

Before using the countryflags API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Country Flags API documentation is found here: [https://docs.apiverve.com/api/countryflags](https://docs.apiverve.com/api/countryflags).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_countryflags.apiClient import CountryflagsAPIClient

# Initialize the client with your APIVerve API key
api = CountryflagsAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "country": "ZW",  "format": "png",  "shape": "circle" }
```

###### Simple Request

```
# Make a request to the API
result = api.execute(query)

# Print the result
print(result)
```

###### Example Response

```
{
  "status": "ok",
  "error": null,
  "data": {
    "country": "Zimbabwe",
    "countryCode": "ZW",
    "shape": "circle",
    "format": "png",
    "downloadUrl": "https://storage.googleapis.com/apiverve.appspot.com/APIResources/countryflags/circle/png/zw.png?GoogleAccessId=635500398038-compute%40developer.gserviceaccount.com&Expires=1738772197&Signature=d5DczbECBjrLDN1w3RmRhHi%2Fu3i9tNprG34zmHKjsf%2FIIonhJLlD99PazUiX7yHsEgQH%2Ff9NmbCNuW%2Bb%2F%2BzbIkeQRyj%2Bxx8gGeX9bMBfojf0NdPDpJdvy6LdSyo%2B%2FwQXeniRKjcZ15Ild8D%2B3CrVDHY%2BlYEEipbLswd40S32eSXph7PpXMEWVUruftA7tQ%2FR7pIii2phEdsMQgeFjmSN%2FI4u3iMAvSF%2BuQL6tZ%2F%2Bl%2BVr6AfBJDEHhgC6f3QJP4uFJicvbQQ1P2LGkT8F1asFuvycOS8gF6Ox4DMhL8j02hLG1POnOjBoC%2BrdIVjHg8gA7vRnytiMwENBMefzsvWhAw%3D%3D"
  },
  "code": 200
}
```

---

## Customer Support

Need any assistance? [Get in touch with Customer Support](https://apiverve.com/contact).

---

## Updates
Stay up to date by following [@apiverveHQ](https://twitter.com/apiverveHQ) on Twitter.

---

## Legal

All usage of the APIVerve website, API, and services is subject to the [APIVerve Terms of Service](https://apiverve.com/terms) and all legal documents and agreements.

---

## License
Licensed under the The MIT License (MIT)

Copyright (&copy;) 2024 APIVerve, and Evlar LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.