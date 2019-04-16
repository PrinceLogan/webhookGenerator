# webhookGenerator

Intended for use with [webhookCounter](https://github.com/PrinceLogan/webhookCounter).

1. arg 1 - source value in payload
2. arg 2 - destination url
3. arg 3 - wait time between sends

## Docker Example
docker run -e SOURCEVALUE="red" -e DESTINATION="https://enz9yjah5e6hn.x.pipedream.net" -e WAITTIME="1" uuid-sender3

