class Contact:
    loc= "germ"
    email_service="@gmail.com"
    Germ_prefix= "+49(0)"

    def __init__(self,first,mid,last,day,month,year,location,Country,prog_language,mobile):
        self.first = first
        self.mid = mid
        self.last = last
        self.e_mail = first+Contact.loc + Contact.email_service
        self.day = day
        self.month = month
        self.year = year
        self.location = location
        self.country = Country
        self.prog_language = prog_language
        self.mobile = mobile

    def full_name(self):
        return f"{self.first} {self.mid} {self.last}"
    def birthday(self):
        return f"{self.day}.{self.month}.{self.year}"
    def locate(self):
        return f"{self.location} {self.country}"
    def mobile_number(self):
        return f"{Contact.Germ_prefix}{self.mobile}"

    def display(self):
        print(f"My name is {self.full_name()}")
        print(f"I am born in {self.birthday()}")
        print(f"I live in {self.locate()}")
        print(f"Phone number: {self.mobile_number()}")
        print(f"E-mail address: {self.e_mail.lower()}")
        print(f"Programming language: {self.prog_language}")


me = Contact("Radu","Florin","Ardelean",19,"april",1991,"Neuhausen","Germany","Python","1774426103")

if __name__ == "__main__":
    Contact.display(me)
