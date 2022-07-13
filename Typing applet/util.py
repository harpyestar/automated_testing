
class Util():

    @classmethod
    def get_data(cls):
        datas = [
            ("", "123", "User Id不能为空"),
            ("admin", "", "password不能为空"),
            ("adminx", "123", "没有此用户"),
            ("admin", "1234", "密码错误")
        ]

        return datas

    @classmethod
    def get_data_from_file(cls, file_name):

        data_list = []
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                clear_line = line.strip("\n")
                data_list.append(clear_line.split(","))

        return data_list


if __name__ == '__main__':
    print(Util.get_data_from_file("datas.txt"))
