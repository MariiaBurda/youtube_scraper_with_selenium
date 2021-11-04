import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-grid-video-renderer")

video_list = []

for video in videos:
    title = video.find_element(By.XPATH, ".//*[@id='video-title']").text
    views = video.find_element(By.XPATH, ".//*[@id='metadata-line']/span[1]").text
    when = video.find_element(By.XPATH, "//*[@id='metadata-line']/span[2]").text

    video_item = {
        'title': title,
        'views': views,
        'posted': when
    }

    video_list.append(video_item)

pd.set_option('display.max_colwidth', None)
df = pd.DataFrame(video_list)

print(df)
