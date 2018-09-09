"""
This is the code that will try to get the data and send it for the workers
to process


Try to look into probabilties and truth table

Finish setting up the Redis Queue


"""
import requests

from .Models import Barchart


def get_top_pages():
    for i in range(2, 6):
        page = i
        barchar = f"https://core-api.barchart.com/v1/options/get?fields=baseSymbol%2CbaseLastPrice%2CbaseSymbolType" \
                  f"%2CsymbolType%2CstrikePrice%2CexpirationDate%2CdaysToExpiration%2CbidPrice%2Cmidpoint%2CaskPrice" \
                  f"%2ClastPrice%2Cvolume%2CopenInterest%2CvolumeOpenInterestRatio%2Cvolatility%2CtradeTime%2CsymbolCode" \
                  f"%2ChasOptions&orderBy=volumeOpenInterestRatio&orderDir=desc&baseSymbolTypes=stock&between(" \
                  f"volumeOpenInterestRatio%2C1.01%2C)=&between(volume%2C500%2C)=&between(openInterest%2C100%2C)=&in(" \
                  f"exchange%2C(AMEX%2CNASDAQ%2CNYSE))=&meta=field.shortName%2Cfield.type%2Cfield.description&hasOptions=true" \
                  f"&page={page}&limit=100&raw=1"
        options = requests.get(barchar)
        new_row = Barchart()
        new_row.data = options.json()
        new_row.data["page"] = page
        new_row.save()
