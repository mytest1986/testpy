import requests
response = requests.get("https://raw.githubusercontent.com/mytest1986/test/main/salam.txt?token=GHSAT0AAAAAAB3RIUH7WI5UVGQ5YCTWP5NSY35ZNVQ")
# response.encoding = "utf-8"
hehe = response.text
print(hehe)