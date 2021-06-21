# I want to make some simple readme files for each problem, but I hate
# writing readmes. Luckily, most problems on PE have a similar structure. I can probably
# get away with automatically making the readme if I do some clever stuff with
# beautiful soup.

import requests
from bs4 import BeautifulSoup

problem_out = \
"""
# Euler {problem_num}: {problem_title}

## Description

{description}
"""

def problem_num(num):
    # Make a BeautifulSoup from the contents of project euler's page
    url_template = "https://projecteuler.net/problem={num}"
    url = url_template.format(num=num)
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")

    # Title is the first h2
    problem_title = soup.find_all("h2")[0].get_text()

    # Problem description is in the div marked as "problem
    problem_desc = soup.find(role="problem")
    descriptions = []
    for paragraph in problem_desc.find_all("p"):
        descriptions.append(paragraph.get_text())
    description = "\n\n".join(descriptions)

    return problem_out.format(problem_num=num, problem_title=problem_title,
                              description=description)

if __name__ == '__main__':
    readme = problem_num(1)
    print(readme)