page = 1
barchar = f"https://core-api.barchart.com/v1/options/get?fields=baseSymbol%2CbaseLastPrice%2CbaseSymbolType" \
          f"%2CsymbolType%2CstrikePrice%2CexpirationDate%2CdaysToExpiration%2CbidPrice%2Cmidpoint%2CaskPrice" \
          f"%2ClastPrice%2Cvolume%2CopenInterest%2CvolumeOpenInterestRatio%2Cvolatility%2CtradeTime%2CsymbolCode" \
          f"%2ChasOptions&orderBy=volumeOpenInterestRatio&orderDir=desc&baseSymbolTypes=stock&between(" \
          f"volumeOpenInterestRatio%2C1.01%2C)=&between(volume%2C500%2C)=&between(openInterest%2C100%2C)=&in(" \
          f"exchange%2C(AMEX%2CNASDAQ%2CNYSE))=&meta=field.shortName%2Cfield.type%2Cfield.description&hasOptions=true" \
          f"&page={page}&limit=100&raw=1"
