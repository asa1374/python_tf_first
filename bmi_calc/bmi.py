class Bmi:
    def __init__(self,name,t,h):
        self.name = name
        self.t = t
        self.h =h

    def bmi(self):
        res = (self.h/(self.t*self.t))*10000
        if res >=40 :
            return print("{}님은 비만입니다.".format(self.name))
        elif res >=30 and res < 40:
            return print("{}님은 경도비만입니다.".format(self.name))
        elif res >= 25 and res <30:
            return print("{}님은 과체중입니다.".format(self.name))
        elif res >= 18.5 and res < 25:
            print("{}님은 정상입니다.".format(self.name))
        else:
            print("{}님은 저체중입니다.".format(self.name))
