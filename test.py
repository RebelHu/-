import csv
import ast
from product import Product

#with open("account.csv") as csvfile:
#    csv_reader = csv.reader(csvfile)
#    header = next(csv_reader)
#    account_dict = {}
#    for row in csv_reader:
#        account_dict[row[1]] = row[2]

#print(account_dict)


'''
def write_in_csv(filename, account_c, password_c):
    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([len(account_dict)+1, account_c, password_c])
write_in_csv("account.csv","xzh","123456" )

with open("account.csv") as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    header = next(csv_reader)        # 读取第一行每一列的标题
    account_dict = {}
    for row in csv_reader:
        account_dict[row[1]] = row[2]

print(account_dict)
'''

'''
def read_stock():
    with open("stock.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        project_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            chara = ast.literal_eval(row[7])
            pro_cur = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], chara)
            project_list.append(pro_cur)
    return project_list

project_l = read_stock()
'''

'''
item_index = 6
r = csv.reader(open('stock.csv', encoding='gbk'))
lines = list(r)
for line in lines:
    if line[0] == str(item_index):
        lines.remove(line)
        break
writer = csv.writer(open('stock.csv', 'w', encoding='gbk'))
writer.writerows(lines)
'''

'''
def read_admin_account():
    with open("admin_account.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)
        admin_account_dict = {}
        for row in csv_reader:
            if row[1] == "用户名":
                continue
            admin_account_dict[row[1]] = row[2]

    return admin_account_dict

print(read_admin_account())
'''
from user import User
def read_user_w():
    '''
    :return: 列表
    '''
    with open("account_waiting.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        user_w_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            user_cur = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            user_w_list.append(user_cur)
    return user_w_list

def read_last_id(filename):
    '''
    读取csv文件中最后一行的id
    :return:
    '''
    with open(filename, encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        li = []
        for row in csv_reader:
            li.append(row[0])
        if li == ['id']:
            return 0
        else:
            return li[-1]


def read_type():
    with open('types.csv', encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        type_dict = {}
        for row in csv_reader:
            cha_l = row[1].split(sep='，')
            type_dict[row[0]] = cha_l
    return type_dict

print(read_type())