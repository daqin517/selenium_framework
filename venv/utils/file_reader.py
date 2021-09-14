import yaml
import os
from xlrd import open_workbook
import pprint


class YamlReader():
    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yaml = yaml_file
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，则读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yaml, 'rb') as f:
                # print('转换成python值：',type(yaml.safe_load_all(f)))
                self._data = list(yaml.safe_load_all(f))  # load后面是个generator，用list组织成列表
                # print('列表：',list(yaml.safe_load_all(f)))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader():
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('该Excel文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('请使用int类型或者str类型的工作表，而不是{0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            elif type(self.sheet) == str:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dirc，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))
        return self._data


# if __name__ == '__main__':
#     y = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#     y = os.path.join(y, 'config', 'config.yml')
#     # print(y)
#     y_reder = YamlReader(y)
#     pprint.pprint(y_reder.data)
#
#     e = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#     e = os.path.join(e , 'data', 'baidu.xls')
#     print(e)
#     e_reader = ExcelReader(e, sheet='baidu', title_line=False)
#     # print(e_reader.data)
