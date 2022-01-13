class Contact:
    loc= "germ"
    email_service="@gmail.com"
    prefix= {"Afghanistan": "+93", "Albania": "+355", "Algeria": "+213","Argentina": "+54","Armenia": "+347","Australia":"+61","Australian External Territories":"+672","Austria":"+43","Azerbaijan":"+994","Bahamas":"+1-242","Bahrain":"+973","Bangladesh":"+880","Barbados":"+1-246","Belarus":"+375","Belgium":"+32","Belize":"+501","Bermuda":"+1-441*","Bolivia":"+591","Bosnia & Herzegovina":"+387","Botswana":"+267","Brazil":"+55","British Virgin Islands":"+1-284*","Bulgaria":"+359",
             "Cambodia":"+855","Cameroon":"+237","Canada":"+1","Cape Verde Islands":"+238","Cayman Islands":"+1-345*","Central African Republic":"+236","Chad":"+235","Chatham Islands (New Zealand)":"+64","Chile":"+56","China":"+86","Congo":"+242","Costa Rica":"+506","Cote d'Ivoire":"+225","Croatia":"+385","Cuba":"+53","Cyprus":"+357","Czech Republic":"+420","Denmark":"+45","Ecuador":"+593","Egypt":"+20","Estonia":"+372","Finland":"+358","France":"+33","Gambia":"+220",
             "Georgia":"+995","Germany":"+49","Greece":"+30","Guinea Bissau":"+245","Haiti":"+509","Honduras":"+504","Hungary":"+36","Iceland":"+354","India":"+91","Indonesia":"+62","Iran":"+98","Iraq":"+964","Ireland":"+353","Israel":"+972","Italy":"+39","Jamaica":"+1-876*","Japan":"+81","North Korea":"+850","South Korea":"+82","Kuwait":"+965","Liechtenstein":"+423","Lithuania":"+370","Luxembourg":"+352","Macedonia":"+389","Maldives":"+960","Malta":"+356","Mexico":"+52","Moldova":"+373",
             "Monaco":"+377","Netherlands":"+31","Nigeria":"+234","Norway":"+47","Pakistan":"+92","Panama":"+507","Paraguay":"+595","Peru":"+51","Philippines":"+63","Poland":"+48","Portugal":"+351","Romania":"+40","Rusia":"+7",
             "Saudi Arabia":"+966","Serbia & Montenegro":"+381","Slovak Republic":"+421","Slovenia":"+386","South Africa":"+27","Spain":"+34","Sri Lanka":"+94","Sudan":"+249","Swaziland":"+268","Sweden":"+46","Switzerland":"+41",
             "Turkey":"+90","Turkmenistan":"+993","Ukraine":"+380","United Arab Emirates":"+971","United Kingdom":"+44","USA Area Codes":"+1","US Virgin Islands":"+1-340*","Uruguay":"+598","Vietnam":"+84","Venezuela":"+58"}


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
        return f"{self.location}, {self.country}"
    def mobile_number(self):
        if self.country in Contact.prefix.keys():
            return f"{Contact.prefix[self.country]} (0){self.mobile}"

    def display(self):
        print(f"My name is {self.full_name()}")
        print(f"I am born in {self.birthday()}")
        print(f"I live in {self.locate()}")
        print(f"Phone number: {self.mobile_number()}")
        print(f"E-mail address: {self.e_mail.lower()}")
        print(f"Programming language: {self.prog_language}")
        print("____________________________________________")


me = Contact("Radu","Florin","Ardelean",19,"April",1991,"Neuhausen","Germany","Python","1774426103")

if __name__ == "__main__":
    Contact.display(me)



