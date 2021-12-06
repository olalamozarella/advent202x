import requests
import re

cookies = {'session': 'paste your session ID here'}
url = "https://adventofcode.com/2021/day/"


# Reads session cookie from cookie.txt and store it to cookies variable
# You can find your session cookie in Chrome-DevTools-Application-Cookies
def read_cookie():
    f = open("cookie.txt", "r")
    cookies['session'] = f.read()


# Reads input from the webpage using session cookie
# URL for the input is always https://adventofcode.com/2020/day/{day number}/input
def get_input(day):
    read_cookie()
    resp = requests.get(url=url + str(day) + "/input", cookies=cookies)
    return resp.text


# Posts answer for challenge and prints text result.
# URL for the answer is always https://adventofcode.com/2020/day/{day number}/answer
# Params:
# - day: day of the challenge
# - level: 1 for first part, 2 for second part
# - answer: answer that you wish to post (either number or string)
def post_answer(day, level, answer):
    # post response
    print("Posting response to day {:d} level {:d}:".format(day, level) + str(answer))
    form_data = {'level': str(level), 'answer': str(answer)}
    resp = requests.post(url + str(day) + "/answer", data=form_data, cookies=cookies)
    result = re.search('<main>.*<p>(.*)</p>.*</main>', resp.content.decode('utf-8'), flags=re.DOTALL)
    print("POST response: " + result.group(1))
