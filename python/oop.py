class account():
    def __init__(self,name,number,balance):
        self.__name = name
		self.__number = number
		self.__balance = balance
	def deposit(self,amount):
		if amount < 0:
			print('存款金额不能为负数')
		else:
			self.__balance += amount
	def withdraw(self,amount):
		if amount > self__balance:
			print('余额不足')
		else:
			self.__balance -= amount
	def __str__(self):
		return "Account('{name}','{number}','{balance}')".format(name = self.__name,number = self.__number,balance = self.__balance)


gui_acc = account('guiaixiao','198907','46000')

