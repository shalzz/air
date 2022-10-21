import re
import csv
import requests
import json

airdrops = {
    "Uniswap": "https://raw.githubusercontent.com/banteg/uniswap-distribution/master/uniswap-distribution.csv",
    "1inch": "https://gist.githubusercontent.com/banteg/12708815fb63239d9f28dec5df8641f9/raw/28a9dffe9d5681ef5f75b0ab6c39fe5ea0064712/1inch.csv",
    "Tornado": "https://raw.githubusercontent.com/tornadocash/airdrop/master/airdrop.csv",
    "Badger": "https://gist.githubusercontent.com/banteg/9ad5fdd2e169a03cc5d93478ece10a38/raw/9b14f2fd933d8a817ff6773e4d4854832b02c4b8/badger.csv",
    "Furucombo": "https://gist.githubusercontent.com/nicholashc/c96d6b41e33d1245ecdaaea33fa6fab0/raw/05d3042e034c2ea99d7084789962aa95a3330f04/combo.csv",
    "StakeDAO": "https://gist.githubusercontent.com/nicholashc/d380275aa8118e018906feeda3a92be5/raw/07f4a09dd657a27080cc75eda5e864acc030af5f/stakedao.csv",
    "Curve": "https://gist.githubusercontent.com/nicholashc/f4a34c138087195237556077ea6490d7/raw/bfdf0a9886747dfe3465a2e8ea1bfb02ae0386ac/curve.csv",
    "Digg": "https://gist.githubusercontent.com/nicholashc/c21788b0f0391d0d2d2cdcc44940a0e3/raw/0dbdc85e0ebc4d2aaa7cda49d5aaeb903fef69c7/digg.csv",
    "PoolTogether": "https://gist.githubusercontent.com/shalzz/2b278831b1444983dd5527ec89dfaf4a/raw/46dd3fb6b1389d7e588afdc082ff9c5b3594dc1c/pooltogether.csv",
    "Safe": "https://raw.githubusercontent.com/safe-global/safe-token/main/user-allocations/safes_tokens.csv",
}

hop  = "https://raw.githubusercontent.com/hop-protocol/hop-airdrop/master/src/data/finalDistribution.csv"
across = "https://raw.githubusercontent.com/across-protocol/acx-drop/main/final/final_combined.json"

my_addrs = [addr.lower() for addr in re.findall(r"0x\w{40}", open("addrs.txt").read())]
for drop, url in airdrops.items():
    print(drop)
    for addr, amount, *_ in csv.reader(requests.get(url).text.splitlines()):
        if addr.lower() in my_addrs:
            print(addr, amount)

print("Hop")
for addr, _, _, _, _, amount in csv.reader(requests.get(hop).text.splitlines()):
    if addr.lower() in my_addrs:
        print(addr, amount)

print("Across")
data = requests.get(across).json()
for key in list(data.keys()):
    if key.lower() in my_addrs:
        print(key, data[key]['total'])
