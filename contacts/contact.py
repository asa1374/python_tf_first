# 한줄 주석
"""
이름,전화번호,이메일, 주소를 입력받아서
자료구조에 저장하는 예제
"""
class Contact:

    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def con(self):
        print("입력하신정보는 이름 {} ,전화번호 {}, 이메일 {}, 주소 {}입니다.".format(self.name
                                                                 ,self.phone
                                                                 ,self.email
                                                                 ,self.address))
    @staticmethod
    def set_contact():
        name = input("이름")
        phone = input("전화번호")
        email = input("이메일")
        address = input("주소")
        con = Contact(name,phone,email,address)
        return con

    @staticmethod
    def get_contact(ls):
        for i in ls:
            i.con()

    @staticmethod
    def del_contact(ls,name):
        for i,t in enumerate(ls):
            if t.name == name:
                del ls[i]

    @staticmethod
    def print_menu():
        print("1 연락처 입력")
        print("2 연락처 출력")
        print("3 연락처 삭제")
        print("4 종료")
        menu = input("메뉴선택")
        return int(menu)

    @staticmethod
    def run():
        ls = []
        while 1:
            menu = Contact.print_menu()
            if menu == 1:
                t = Contact.set_contact()
                ls.append(t)
            elif menu == 2:
                Contact.get_contact(ls)
            elif menu == 3:
                name = input("삭제할 이름")
                Contact.del_contact(ls,name)
            elif menu == 4:
                break

