# 将json格式字典写入文件
data = {
  "a": 'Hello World'
}

with open('test.txt', 'w') as f:
  # 需要将字典转为字符串写入
  f.write(str(data))

# 读取到的数据是字符串格式，使用时需要转为字典类型
with open('test.txt', 'r') as f:
  _data = f.read()
# eval 将字符串格式的数据转为字典格式
print(eval(_data)['a'])
