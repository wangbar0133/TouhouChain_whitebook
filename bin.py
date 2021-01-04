import hashlib

class Trans16To2():
    '''
    将16进制str转化为2进制str
    '''
    def __init__(self):
        self.dict_bin = {
                '0': '0000',
                '1': '0001',
                '2': '0010',
                '3': '0011',
                '4': '0100',
                '5': '0101',
                '6': '0110',
                '7': '0111',
                '8': '1000',
                '9': '1001',
                'a': '1010',
                'b': '1011',
                'c': '1100',
                'd': '1101',
                'e': '1110',
                'f': '1111'
                }
        self.listArr = ''

    def do(self, string):
        '''
        :param string:16进制str
        :return: 2进制str
        '''
        for item in string:
            dictBin = self.dict_bin
            self.listArr = self.listArr + dictBin[item]
        return self.listArr

class Encrypt():

    def __init__(self):
        pass

    def HashEncrypt(self, data_str):
        '''
        :param data_str:str
        :return: hash
        '''
        sha = hashlib.sha256()
        sha.update(data_str)
        return sha.hexdigest()

    def Sign(self, string, responsible):
        '''
        :param string: str
        :param responsible: responsible对象
        :return: responsible的签名密钥对string的签名
        '''
        SigningKey = responsible.SigningKey
        sign = SigningKey.sign(bytes(string, encoding='UTF-8'), encoding="base64")
        return str(sign)[2:-1]

def ListToStr(Lists):
    '''
    将列表转化为字符串
    :param Lists: list对象
    :return: str
    '''
    Str = '['
    for item in Lists:
        Str = Str + str(item) + ','
    Str = Str[0:-1] + ']'
    Str = Str.replace("'", '"')
    return Str