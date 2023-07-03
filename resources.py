import pandas as pd
import requests
from matplotlib import pyplot as plt

world_indexes = "https://github.com/ao-data/ao-bin-dumps/blob/master/formatted/world.json"
item_indexes = "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json"

main_link = "https://www.albion-online-data.com/api/v1/stats/prices/"

daily_prices = "https://west.albion-online-data.com/api/v2/stats/view/"
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




level = 3


# items = f"T8_2H_CROSSBOW_CANNON_AVALON@3"

# https://west.albion-online-data.com/api/v2/stats/view/T4_BAG,T5_BAG?locations=Caerleon,Bridgewatch&qualities=2

items = [
    "T2_CLOTH",
    "T3_CLOTH",
    "T4_CLOTH",
    "T5_CLOTH",
    "T6_CLOTH",
    "T7_CLOTH",
    "T7_CLOTH_LEVEL1@1",
    "T7_CLOTH_LEVEL2@2",
    "T7_CLOTH_LEVEL3@3",
    "T7_CLOTH_LEVEL4@4",
    "T8_CLOTH",
    "T8_CLOTH_LEVEL1@1",
    "T8_CLOTH_LEVEL2@2",
    "T8_CLOTH_LEVEL3@3",
    "T8_CLOTH_LEVEL4@4"
]


def object_selector(items):
    final_object_list_string = None
    for item in items:
        if not None:
            final_object_list_string = f"{final_object_list_string},{item}"

    return final_object_list_string



def run_script():
    average_link0 = f"{main_link}{object_selector(items)}{locations}"

    get_average_json0 = create_average_call(average_link0)

    export_to_excel(get_average_json0, "datafile_average0.xlsx")


def create_item_list(item_list, tier, enchant):
    query_item_list = ""
    for item_name in item_list:
        if item_name == item_list[len(item_list) - 1]:
            query_item_list = f"{query_item_list}{tier}_{item_name}{enchant}"
        else:
            query_item_list = f"{query_item_list}{tier}_{item_name}{enchant},"
    return query_item_list


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
