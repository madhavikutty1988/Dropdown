from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"D:\Tools\Jenkins\Downloads"})

driver = webdriver.Chrome(executable_path="D:\Tools\Python\Driver\Chrome\chromedriver.exe",chrome_options = chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()
driver.implicitly_wait(15)
# to download the pdf file

driver.find_element_by_id("pdfbox").send_keys("SOME RANDOM TEXT")
# generate file button
driver.find_element_by_id("createPdf").click()
# getting download link
driver.find_element_by_id("pdf-link-to-download").click()
