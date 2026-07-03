class yasvanth_school:
    def classten(self):
        return "tenth class 50 students"
    def classeleven(self):
        return "class eleven 46 students"
    def classtwelve(self):
        return "class twelve 42 students"

class management:
    def __init__(self,std:str,sports_winner:str,sec:str):
        self.name="yes public international school"
        self.std=std
        self.sports=sports_winner
        self.sec=sec
    def sports_winner(self):
        return f"{self.name} participated in {self.std} section {self.sec} sports {self.sports}"


class tenth_class(management):
    def __init__(self, std, sports_winner, sec):
        super().__init__(std, sports_winner, sec)


class eleventh_class(management):
    def __init__(self, std, sports_winner, sec):
        super().__init__(std, sports_winner, sec)


class twelth_class(management):
    def __init__(self, std, sports_winner, sec):
        super().__init__(std, sports_winner, sec)


#driving eligible or not

class driving:
    def __init__(self,age:int,name:str):
        self.age=age
        self.name=name
        self.age_list=[13,14,23,7,35]
        
    def eligible_or_not(self):
        if self.age>=18:
            return f"{self.name} eligible for licence" 
        else:
            return f"{self.name} not eligible for licence"

    def count_eligible(self):
        count=0
        for i in self.age_list:
            if i >18:
                count+=1

        return count

        