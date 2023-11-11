# MTA Prices

## Description

> The MTA has rose the single-ride subway fare to $2.90!! Log into the admin MTA account and change the price back down to $2.75. You have already collected a partial list of the column names.
>
> http://web.csaw.io:5800/

## Write-Up

Test here

<img src="./1.png"
     alt="Markdown Monster icon"
     style="
     width: 80%;
     diplay: box;"
/>

```
jwt-cracker -t eyJlbWFpbCI6IiIsInRyYWNraW5nSUQiOiJuSjZXWUZISmlibzNZVFdFbW5abiJ9.ZQZDKQ.dczlcIlXB4uZTAVP99LXTwWIdzQ 1234567890 6
```

When seeing details of single ride

```
POST /displaydetails HTTP/1.1
Host: web.csaw.io:5800
Content-Length: 15
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://web.csaw.io:5800
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://web.csaw.io:5800/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: trackingID=p8dt2VINTHgtC1jPX1jw; session=eyJlbWFpbCI6IkVycm9yIiwidHJhY2tpbmdJRCI6IldaT3dIRnJtOFJMRTZ3V2xmOWRNIn0.ZQZTlQ.BUVb5u5OdsiHKVIxTs2682PpnB8
Connection: close

passType=single
```

After modifying query to:

```
...
passType[]=single
```

Page still works.

Moreover, when changing query to this (on whatever passtype):

```
...
passType[passType]=1
```

it gives the monthly one.




First, we need to clean the `columns_dump.txt` to get unique values :

```
sort columns_dump.txt | uniq > columns_dump_uniq.txt 
```

from there, we get less lines. After checking columns names we find that the SGBD is `MySQL` :

```
...
mysql_version
...
```




## Flag



## More Information

 
