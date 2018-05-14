## cURL学习笔记
***
### curl向http接口post json数据
```bash
$ curl -H "Accept: application/json" -H "Content-type: application/json" -X POST  -d   '{"txn": {"reqseq": "1504167510190","posid": "1","mchntid": "456","batchid": "789"},"head": {"ERRDISP": "","TXNTYPE": "0900","VERSION": "1.0","TXNDATE": "20170901","ERRCODE": "","TXNTIME": "102200"}}' http://10.101.251.148:5000/card


```