import pandas as pd
import requests
from matplotlib import pyplot as plt

world_indexes = "https://github.com/ao-data/ao-bin-dumps/blob/master/formatted/world.json"
item_indexes = "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json"

main_link = "https://www.albion-online-data.com/api/v1/stats/prices/"

daily_prices = "https://www.albion-online-data.com/api/v2/stats/history/"
time_scale = "?time-scale=24"

thetford_index = "0007"
martlock_index = "3008"
lymhurst_index = "1002"
bridgewatch_index = "2004"
fortSterling_index = "4002"
black_market_index = "3003"
caerleon_market_index = "3005"
arthursRest_index = "4300"
merlynsRest_index = "1012"
morganasRest_index = "0008"

locations = f"?locations={thetford_index}, {martlock_index},{lymhurst_index},{bridgewatch_index},{fortSterling_index},{black_market_index}, {caerleon_market_index}, {arthursRest_index},{merlynsRest_index},{morganasRest_index}"
qualities = "&qualities=1"


def tier(unit):
    if unit == 0:
        return ' '
    elif unit == 1:
        return "_LEVEL1@1"
    elif unit == 2:
        return "_LEVEL2@2"
    elif unit == 3:
        return "_LEVEL3@3"
    elif unit == 4:
        return "_LEVEL4@4"


level = 3
items = f"T7_FIBER_LEVEL3@3"


def run_script():
    average_link = f"{main_link}{items}{locations}"
    daily_call = f"{daily_prices}{items}{time_scale}"

    get_average_json = create_average_call(average_link)
    get_daily_json = create_call(daily_call)

    export_to_excel(get_average_json, "datafile_average.xlsx")
    response = []

    # plt.plot(x, y)
    # plt.xlabel('X-axis')
    # plt.ylabel('Y-axis')
    # plt.title("A simple line graph")
    # plt.show()


def create_average_call(call):
    return pd.DataFrame(requests.get(call).json())


def create_call(call):
    return pd.DataFrame(requests.get(call).json())


def export_to_excel(df_json, file_name):
    writer = pd.ExcelWriter(f"{file_name}", engine="xlsxwriter")
    df_json.to_excel(writer, sheet_name='welcome', index=False)
    writer._save()


def graph_json_file(df_json):
    Locations = [df_json["location"]]
    Data = [i["item_count"] for i in df_json["data"]]
    plt.plot(Locations, Data)
    plt.show()


run_script()
