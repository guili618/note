### 今天用virtualenv创建了一个环境，但是用pip装django包的时候，不用sudo pip 会提示Permission denied，用了sudo pip install django 发现装到了本机上，虚拟环境pip freeze依然看不到包，google了一下两个 stackoverflow的提问找到了原因



- https://stackoverflow.com/questions/19471972/how-to-avoid-permission-denied-when-using-pip-with-virtualenv
- https://stackoverflow.com/questions/14665330/pip-requirement-already-satisfied