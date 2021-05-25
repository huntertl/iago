import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import StringIO

url = 'https://forecast.predictwind.com/tracking/display/SV_Freya'

os.environ['PATH'] = os.getcwd() + ':' + os.environ['PATH']

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


outputdir = "logs"
service_log_path = "{}/chromedriver.log".format(outputdir)
service_args = ['--verbose']
driver = webdriver.Chrome(service_args=service_args,
													service_log_path=service_log_path)


driver.get(url)
now = datetime.utcnow()
driver.get_screenshot_as_file('screenshots/{}.png'.format(now))


