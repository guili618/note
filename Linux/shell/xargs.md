## xargs 笔记
***

### 

```bash

ps aux | grep PROCESS | grep -v grep | awk '{print $2}' | xargs kill -9
```