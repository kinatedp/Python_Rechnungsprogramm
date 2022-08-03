
class CArticles:
    art_id: str
    art_name: str
    art_unit: str
    art_price: float
    art_amount: float
    art_total_price: float


class CAbzuege(CArticles):
    def __init__(self):
        super(CArticles, self).__init__()


class CCustomer:
    cust_name: str
    cust_street: str
    cust_city: str


class CRechnung:
    strAuftragsdatum: str
    strAuftragsort: str
    strRechnungsdatum: str
    strRechnungsNum: str
    strAuftragsnummer: str
    #TODO: Check
    ###lArticles: list[CArticles]
    ###lAbzuege: list[CAbzuege]
    lArticles: CArticles
    lAbzuege: CAbzuege
    customer: CCustomer
    bAddTaxes: bool = False
