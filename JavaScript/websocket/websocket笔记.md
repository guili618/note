## Websocket笔记
---

### 基本概念
Websocket 在一个单独的持久连接上提供全双工、双向的通信，在js中创建Websocket后，会有一个http请求发送到浏览
器以发起连接，取得服务器响应后，建立的连接会从http转换为Web Socket协议

### Websocket的建立
- 必须传入绝对url
- 同源策略对Websocket不适用
- 实例化Websocket对象后，浏览器会马上尝试创建连接
```js
//新建连接
let socket = new WebSocket('ws://url' )
//用变量拼接url，并判断https
console.log(window.location);
let location = window.location;
let websocketStart = "ws://";
if (location.protocol == 'https:'){
    websocketStart = 'wss://'
}
let url = websocketStart + location.host + location.pathname + '/';
let socket = new ReconnectingWebSocket(url);

//用socket.io新建连接


//用reconnecting-websocket
<script src="https://cdnjs.cloudflare.com/ajax/libs/reconnecting-websocket/1.0.0/reconnecting-websocket.js"></script>
let ws = new ReconnectingWebSocket('ws://....');

```
### Websocket发送和接受数据
发送数据，只能发送纯文本，所以复杂的数据结构，在发送前要进行序列化，再发送到服务器
```js
let socket = new WebSocket('ws://url' );
socket.send("Hello");
//发送复杂数据
let message = {
    time:new Date(),
    text:"Hello World",
    cliendId:"12345"
};
socket.send(JSON.stringify(message));
```
服务器向客户端发来消息时，WebSocket对象会触发 message事件，这个message事件和其他传递消息的协议类似，也是把
返回的数据保存在event.data属性中
```js
socket.onmessage = function(event){
    let data = event.data; // 返回的数据也是字符串，必须手工解析
    //处理数据
};

```
### Websocket的事件
- open：在成功建立连接时触发
- error：在连接出错时触发，连接不能持续
- close：在连接关闭时触发
> WebSocket对象不支持DOM2级事件侦听器，必须使用DOM0级语法分别定义每个事件处理程序

```js
let socket = new WebSocket('ws://url' );
socket.onopen = function () {
    console.log("websocket is open"); 
};
socket.onerror = function () {
    console.log("websocket is error");
};
socket.onclose = function () {
    console.log("websocket is close");
};

//这个三个事件中，只有close和event对象有额外信息
socket.onclose = function(event){
    console.log("was clead: " +event.wasClean  + "Code: " + event.code + "Reason=" + event.reason)
};
```