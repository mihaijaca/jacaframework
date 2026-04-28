import base64
import random
import requests
from seleniumbase import SB

def main():
    geo_data = requests.get("http://ip-api.com/json/").json()
    proxy_str = False

    latitude = geo_data["lat"]
    longitude = geo_data["lon"]
    timezone_id = geo_data["timezone"]
    language_code = geo_data["countryCode"].lower()

    name = "YnJ1dGFsbGVz"
    fulln = base64.b64decode(name).decode("utf-8")

    urlt = f"https://www.twitch.tv/{fulln}"
    urly = f"https://www.reddit.com/r/{fulln}"

    while True:
        with SB(uc=True, locale="en", ad_block=True,
                chromium_arg='--disable-webgl', proxy=proxy_str) as formwww:

            rnd = random.randint(450, 800)

            formwww.activate_cdp_mode(urly, tzone=timezone_id, geoloc=(latitude, longitude))
            formwww.sleep(2)

            formwww.cdp.open('https://kick.com/brutalles')
            formwww.sleep(10)

            formwww.cdp.open('https://www.twitch.tv/brutalles/clip/HumbleStrangeKuduJonCarnage-xTG7nQKnhrSA-BZk')
            formwww.sleep(10)

            formwww.cdp.open(urlt)
            formwww.sleep(2)

            if formwww.is_element_present('button:contains("Accept")'):
                formwww.cdp.click('button:contains("Accept")', timeout=4)

            formwww.sleep(12)

            if formwww.is_element_present('button:contains("Start Watching")'):
                formwww.cdp.click('button:contains("Start Watching")', timeout=4)
                formwww.sleep(10)

            if formwww.is_element_present('button:contains("Accept")'):
                formwww.cdp.click('button:contains("Accept")', timeout=4)

            if formwww.is_element_present("#live-channel-stream-information"):

                if formwww.is_element_present('button:contains("Accept")'):
                    formwww.cdp.click('button:contains("Accept")', timeout=4)

                formwww2 = formwww.get_new_driver(undetectable=True)
                formwww2.activate_cdp_mode(urlt, tzone=timezone_id, geoloc=(latitude, longitude))
                formwww2.sleep(10)

                if formwww2.is_element_present('button:contains("Start Watching")'):
                    formwww2.cdp.click('button:contains("Start Watching")', timeout=4)
                    formwww2.sleep(10)

                if formwww2.is_element_present('button:contains("Accept")'):
                    formwww2.cdp.click('button:contains("Accept")', timeout=4)

                formwww.sleep(rnd)

            else:
                break


if __name__ == "__main__":
    main()
