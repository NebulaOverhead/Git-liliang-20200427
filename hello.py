def func1(name):
    if name == 'stranger':
        print('''Sorry stranger,This door is not for you.:( ''')
    else:
        print('Hello,'+name.upper())
        
    print('*'*(10+10))


func1('stranger')
func1('python')
func1('陌生人')
