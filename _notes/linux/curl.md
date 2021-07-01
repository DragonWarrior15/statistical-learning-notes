---
title: cURL
---

## `cURL`
`curl` command can be used to query urls from the command lines, and also allows sending form data, saving reponses to files etc.

### Fetching websites
`curl https://www.google.com` will return the entire html data of [google.com](https://www.google.com)

### REST APIs
`curl https://reqres.in/api/users/2` demonstrates how to test a REST API with curl. It returns the following json data (the returned data is not automatically formated)
```json
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
```

Adding the `-i` flag will print the response header as well `curl -i https://reqres.in/api/users/2` (the raw output is pasted below)
```json
HTTP/1.1 200 OK
Date: Thu, 01 Jul 2021 18:22:07 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 280
Connection: keep-alive
X-Powered-By: Express
Access-Control-Allow-Origin: *
Etag: W/"118-pbdwwFo9SKNhD3Lx5iHJyngpq00"
Via: 1.1 vegur
Cache-Control: max-age=14400
CF-Cache-Status: HIT
Age: 132
Accept-Ranges: bytes
cf-request-id: 0b04e799f100004b17879e8000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v2?s=T6JBJVWbubBKy8LHXsP8NEX2Ogo%2F3M%2Bmaj1Y%2Bq8XK5IrEPZ3BrT6owkPwWuNNHtL5HIBr21Eu4TR7eXFxfFjd%2BreTNZvzogCjq%2FQNJ7LS%2B%2BOQKgknh5p"}],"group":"cf-nel","max_age":604800}
NEL: {"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6681a86fea034b17-HYD
alt-svc: h3-27=":443"; ma=86400, h3-28=":443"; ma=86400, h3-29=":443"; ma=86400, h3=":443"; ma=86400

{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
```

`-i` is a shorthand for `--include`

### Posting data
Data can be posted using the `-d` flag which is shorthand for `--data`.

`curl -d "key1=value1&key2=value2" https://jsonplaceholder.typicode.com/posts` returns and prints
```json
{
  "key1": "value1",
  "key2": "value2",
  "id": 101
}
```

This uses the POST method by default.

To update the data, we add the `-X PUT` flag as `curl -X PUT -d "key1=value1&key2=value2" https://jsonplaceholder.typicode.com/posts/1` which returns and prints
```json
{
  "key1": "value1",
  "key2": "value2",
  "id": 101
}
```

To delete data, use `-X DELETE` as `curl -X DELETE https://jsonplaceholder.typicode.com/posts/1`

### Authentication
Authentication for username and password can be done with the `-u` flag in the format `curl -u username:password site_address`. The username and password are separated by a `:`.

### Download binary data
Binary data can be downloaded with the `-o` flag which is short for `--output`. `curl -o test.jpg https://www.python.org/static/apple-touch-icon-144x144-precomposed.png` will download a wallpaper image file and save it as test.jpg

Using a captial `-O` instead will save the file to the same name as the one with which its hosted online `curl -O https://www.python.org/static/apple-touch-icon-144x144-precomposed.png` saves the file to the location `apple-touch-icon-144x144-precomposed.png`.

### Save json data to disk
`curl -o test.json https://reqres.in/api/users/2` will save the response to a file `test.json`.

#### References
* [Linux/Mac Terminal Tutorial: How To Use The cURL Command](https://youtu.be/WxUVU0b95Oc)
