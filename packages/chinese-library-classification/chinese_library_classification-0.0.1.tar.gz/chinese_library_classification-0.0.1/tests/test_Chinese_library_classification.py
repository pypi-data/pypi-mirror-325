from chinese_library_classification import Chineselibraryclassification

def test_initialization():
    # 测试类的初始化
    CLC = Chineselibraryclassification()
    value = CLC.num2info('D432.0')
    print(value)
    assert value['level'] == 5
    