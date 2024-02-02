from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pydub import AudioSegment
from pydub.generators import Sine
import simpleaudio as sa
import io
# Set the path to the WebDriver

# Generate a 1-second sine wave tone at 440 Hz
toneSuccess = Sine(440).to_audio_segment(duration=30000)
counter = 0

while (True):
    print(f'Number of tries: {counter}')
    counter = counter + 1
    driver = webdriver.Chrome()

    driver.get('https://termine.staedteregion-aachen.de/auslaenderamt/')
    driver.minimize_window()

    driver.find_element("id", 'cookie_msg_btn_no').click()

    driver.find_element("name", 'Aufenthaltsangelegenheiten').click()

    time.sleep(1)

    driver.find_element("id", 'header_concerns_accordion-115').click()

    time.sleep(1)

    driver.find_element("id", 'button-plus-227').click()
    time.sleep(1)

    driver.find_element("id", 'WeiterButton').click()
    time.sleep(1)

    driver.find_element("id", 'OKButton').click()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1)
    element = driver.find_element("xpath", "//input[@aria-label='Ausländeramt Aachen, 2. Etage auswählen']")
    element.click()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 400);")
    
    
    if 'Kein freier Termin verfügbar' in driver.page_source:
        print("Text is present")
        time.sleep(10)
        driver.quit()
    else:
        print("Text is not present")
        break

print("NEW STUFF ONLINE")
#wave_obj = sa.WaveObject(toneSuccess.raw_data, num_channels=toneSuccess.channels, bytes_per_sample=toneSuccess.sample_width, sample_rate=toneSuccess.frame_rate)
#play_obj = wave_obj.play()
#play_obj.wait_done()

input("Press Enter to quit...")
driver.quit()