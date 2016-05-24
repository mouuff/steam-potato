
import re
from potato.constants import MARKET_URL

def item_list(json_list):
	html = json_list["results_html"]
	expr = r"href=\"{market_url}/(.*?)\" id=\"resultlink_.\">"
	expr = expr.format(market_url=MARKET_URL)
	regex = re.compile(expr)
	print(regex.findall(html))
