class Currency():
    def __init__(self, value, currency, convertcurrency):
        self.dic = {'US Dollars': 82.05,
                    'Euro': 89.91,
                    'British Pound': 101.99,
                    'Australian Dollars': 55.25,
                    'UAE Dirham': 22.35,
                    'New ZealandDollar': 50.96,
                    'Canadian Dollar': 61.32,
                    'Swiss Franc': 91.4,
                    'Japanese Yen': 0.6115,
                    'Saudi Riyal': 21.89,
                    'Qatari Rial': 22.54,
                    'Omani Rial': 213.16,
                    'Bahraini Dinar': 218.89,
                    'Kuwaiti Dinar': 268.21,
                    'Singapore Dollar': 61.57,
                    'Malaysian Ringgit': 18.52,
                    'Swedish Krona': 7.97,
                    'Danish Krone': 12.06,
                    'Thai Baht': 2.392,
                    'Hong Kong Dollar': 10.45,
                    'South African Rand': 4.51,
                    'Chinese Yuan': 11.94,
                    'india INR':1
                    }
        self.value = value
        self.currency = currency
        self.convertcurrency = convertcurrency

    def currenttocurrency(self):
        if self.currency in self.dic:
            self.value = self.value * self.dic[self.currency]
            return self.value

    def currencytonext(self):
        return self.value / self.dic[self.convertcurrency]

a = Currency(1045, 'india INR', 'Euro')
print('The currency value is converted into ', a.currenttocurrency())
print('The currency value which we want to convert next ',a.currencytonext())


