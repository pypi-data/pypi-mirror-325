scada-tuna
=================================

Generic PLC client.

Usage
------------

main.py


.. code:: python

    from scada_tuna import Tuna
    # 用法总结：
    tuna = Tuna('modbus://10.8.7.6:502?timeout=5.0&series=H5U').connect()
    # tuna = Tuna('mc_3e://172.16.1.153:8100?timeout=5.0&series=L').connect()
    print(tuna)
    # 单次写入各种类型的数据
    tuna.write('R100', 'int', 87)
    tuna.write('D100', 'int', 86)
    tuna.write('D200', 'long', 50054)
    tuna.write('D205', 'float', [23.23, 34.56])
    tuna.write('D210', 'string', 'hello world!')
    print(tuna.read('R100', 'int'))
    print(tuna.read('D100', 'int'))
    print(tuna.read('D200', 'long'))
    print(tuna.read('D205', 'float', 2))
    print(tuna.read('D210', 'string', 12))
    # 批量写入多种类型的数据
    buffer = Buffer().append(89, 'int').append(12.23, 'float').append("hello world")
    tuna.write('D500', None, buffer)
    print(tuna.read('D500', 'int'))
    print(tuna.read('D502', 'float'))
    print(tuna.read('D504', 'string', 11))
    # 批量读取多种类型的数据
    buffer = tuna.read('D500', None, 20)
    print(buffer.read('D500', datatype='int'))
    print(buffer.read('D502', datatype='float'))
    print(buffer.read('D504', datatype='string', length=11))