from bmi_calc.bmi import Bmi

def main():
    bmi = Bmi(input("이름을 입력하세요")
              ,float(input("키를 입력하세요"))
              ,float(input("몸무게를 입력하세요")))

    bmi.bmi()

if __name__ == '__main__':
    main()