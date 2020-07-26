Install:
```
docker-compose up -d
docker-compose exec fbk_app python manage.py migrate
```

To test on windows:

bind your server ip address with the dns record via hosts:
```
192.168.0.103	example.net
```

Check POST:
```
curl -H "Content-Type: application/json" -X POST http://example.net:8080 -d "{\"Name\":\"Test Value\"}"
```
Expected output:
```
200
```
means that request headers and body are written to the database.

Check GET:
```
curl -H "Content-Type: application/json" -X GET http://example.net:8080
```
Expected output:
```
<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.14.2</center>
</body>
</html>
```