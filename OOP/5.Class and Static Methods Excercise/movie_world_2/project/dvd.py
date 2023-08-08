import datetime


class DVD:
    def __init__(self,name: str, id: int,creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    @classmethod
    def from_date(cls,id: int, name: str, date: str, age_restriction: int):

        day,month_number_as_str,year = date.split(".")
        monthinteger = int(month_number_as_str)
        month = datetime.date(1900,monthinteger,1).strftime('%B')
        return cls(name,id,int(year),month,age_restriction)

    def __repr__(self) ->str:
        rented = 'rented' if self.is_rented else 'not rented'
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})"
                f" has age restriction {self.age_restriction}. Status: {rented}")











