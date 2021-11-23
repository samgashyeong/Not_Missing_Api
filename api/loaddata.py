import requests

esntlId = '10000420'
authKey = '5bdbdfb411ee4e3b'
def parsingData(page):
    url = "https://www.safe182.go.kr/api/lcm/amberList.do"
    datas = {
        'esntlId' : esntlId,
        'authKey' : authKey,
        'rowSize' : '100',
        'page' : page
    }
    return requests.post(url, datas)


def safeLoadData(pageIndex):
    url = "https://www.safe182.go.kr/api/lcm/safeMap.do"
    datas = {
        'esntlId' : esntlId,
        'authKey' : authKey,
        'pageIndex' : pageIndex,
        'pageUnit' : '100'
    }
    return requests.post(url, datas)