import win32com.client


def getNameNCode(market):

   
     # 연결 여부 체크
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos") # 32bit에서 작동하는듯
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()
        
    # 종목코드 리스트 구하기
    objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
   
    codeList = objCpCodeMgr.GetStockListByMarket(market) 
    result = []
    print("종목코드 길이", len(codeList))
    for i, code in enumerate(codeList):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        
        result.append({"number " :i, "code" : code, "secondCode" : secondCode, "Price" : stdPrice, 'name' : name})
    
    return result
