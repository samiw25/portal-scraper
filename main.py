import requests
import lxml.html

login_url = "https://sso.ncaa.org/login"
url = "https://web1.ncaa.org/saTransfer/otherInstitutions"

USERNAME = "*******"
PASSWORD = "*******"

def main():
    s = requests.session()

    login = s.get(login_url)
    tree = lxml.html.fromstring(login.text)
    auth_tokens = tree.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in auth_tokens}
    form['username'] = USERNAME
    form['password'] = PASSWORD
    # login
    response = s.post(
        login_url,
        data=form
    )
    html = s.get(url)
    tree = lxml.html.fromstring(html.text)
    info = tree.xpath('//table//tr[@role="row"]/text()')
    print(info)


if __name__ == '__main__':
    main()
