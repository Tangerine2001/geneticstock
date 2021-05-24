import datetime
import csv


stock_list = ["SCPS", "MMAC", "CREX", "PTPI", "GVP", "SPCE", "VSTM", "KRBP", "RHE", "BTX", "JZXN", "VRTV", "APM",
                  "RCON", "XELB", "TLC", "INBX", "LBPH", "MCF", "FTK", "RNGR", "OBLN", "AINC", "RIOT", "AMC", "SBBP",
                  "JAGX", "DRTT", "GTX", "ELYS", "TDUP", "HIMX", "STEM", "MARA", "AGS", "RYB", "BWAY", "PANL", "NCSM",
                  "BFI", "RENN", "LHDX", "SKYT", "GMBL", "BYND", "BGI", "BOTJ", "DSX", "SQSP", "INZY", "MEC", "EXPR",
                  "RSVA", "NMRD", "AXR", "LBPS", "OCFT", "TGI", "CAMT", "CNEY", "PLXP", "FTCI", "BRN", "PRCH", "VIAO",
                  "GLDG", "LJPC", "IKT", "QRHC", "RAIN", "IHT", "GTIM", "SQFT", "RBLX", "CARE", "PATH", "LXEH", "PRTH",
                  "KSPN", "XYF", "KOS", "TRIB", "ICON", "SELB", "AIH", "SITM", "NTZ", "VYNT", "USDP", "FLGC", "NOVN",
                  "SB", "WSTG", "ESEA", "SKLZ", "EAST", "DKNG", "JMP", "ETWO", "MGI"]


def write_csv():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    headers = {
        'x-rapidapi-key': "0c48e7a858mshf95c38c0ff5df48p195295jsn8d917875b8ac",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    f = open("Stonks.csv", "w")
    writer = csv.writer(f, lineterminator='\n')
    historical_list = []

    writer.writerow(stocklistmaker())
    for elm in stock_list:
        time.sleep(15)
        querystring = {"symbol": elm, "region": "US"}
        stock_data = requests.request("GET", url, headers=headers, params=querystring)
        historical = stock_data.json()["prices"][::-1]

        # writer.writerow([querystring["symbol"]])
        # for past in historical:
        #     if "close" in elm.keys():
        #         writer.writerow([past["close"], datetime.datetime.fromtimestamp(past["date"])])
    f.close()


def stocklistmaker():
    newlist = []
    for elm in stock_list:
        newlist.append(elm)
        newlist.append("")
    return newlist


if __name__ == "__main__":
    write_csv()
