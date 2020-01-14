import requests


url = 'https://fanyi.baidu.com/sug'

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Cookie': "BAIDUID=97DA851F88C92BE45D7963ADA75C3434:FG=1; BIDUPSID=97DA851F88C92BE45D7963ADA75C3434; PSTM=1567649375; BD_UPN=12314753; BDUSS=3ZzTkJOTHRNVkpqVGR4cE9BaWlOVlJUcX5JbHVXMWEwWVQ3V1pmbUJEbVQxQmRlRUFBQUFBJCQAAAAAAAAAAAEAAABbuGacAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJNH8F2TR~Bdb; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=cvFOJeC62CrXf4cwU0e2tW9rYM4hm03TH6aIl2P5JFJeo_dcX41gEG0PDf8g0KubMVkPogKKBeOTHg_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JRA8oKPhtCvhDRTvhCcjh-FSMgTBKI62aKDs2ROYBhcqEIL4W6-aKPIp5nO8W4KL-6nH2IOK5DoEHxbSj4QzQU0zDPvl0RQuWI3bhqvztp5nhMJFXj7JDMP0qJ7j2RQy523ion6vQpn-KqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0j63-DaAJt6njJTRe0Rj-KbP_hDL9eKTjhPrMjHrJWMT-0bFH_JR2QJP5fUbJQpPVKJ3-MMc9BMvuJan7_JjYbRDVMfQhWhJChtLeyU6r3fQxtNRB-CnjtpvhKJjjWtcobUPUDMc9LUvqHmcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD05MDIwjTt3-4LtMxrXKK6QKCjj3toObnnqq6rkbJ83yhFzXP6-35KHf6rMKR_bbhrBj5CzKJOb5MrXeJb-5h37JD6yb-n5Lb8KDRPGehrAMJFYQ4oxJpO7BRbMopvaKquVoJQvbURvD-ug3-7qex5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoD-2tKD5MIDr5nJbq4I85M5H54cX--o2WbCQaM7O8pcNLTDKLnLNjb72-MC8BNrJ-KTua-PMjbCxjqO1j4_PMa8OKhFeLHIebbQJyIb-hl5jDh3Ub6ksD-Rt5frp2aRy0hvc0J5cShnkDMjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDG8JJ5_eJbCsL-35HJcqfbo4-tr_KICShUFs5b5lB2Q-5KL-0-oieCbn5p_2bjD33NrHXxuJ2IDjoMbdJJjzDKoMjf6Py4LeBUO2XT0D52TxoUJg5DnJhhvG-xc4Mp8ebPRi3tQ9QgbMMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjLBDTb33H; H_PS_PSSID=1460_21110_30210_30284_22160; yjs_js_security_passport=3b54287a45b25629d2f7cfdb10008d7e9d67b5bd_1576637318_js; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=2; BD_HOME=1; H_PS_645EC=b428Vxu0iZX7iP6ukpImwh5YVC5tlT7Iwn5ZIzZa5ijoKNVsMoi%2FCv%2FtNME"
}

data = {
    # 'from': 'zh',
    # 'to': 'en',
    'kw' : 'i love',
    # 'query': '666',
    # 'transtype': 'enter',
    # 'simple_means_flag': '3',
    # 'sign': '526899.846082',
    # 'token': '6ee8d59789dae108298b3540215f2ec8'
}

response = requests.post(url=url,data=data,headers=Headers)

response.encoding = 'utf8'

text = response.json()
print(text)
# with open('./fanyi.html','w',encoding='utf8') as f:
#     f.write(text)