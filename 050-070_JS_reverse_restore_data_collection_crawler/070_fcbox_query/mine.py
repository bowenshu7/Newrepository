#name: fcbox item query
#author: Bowen
#goal: to get the information about query results from fcbox web
#date: 2026/10/26
#stage: finished

import requests
import execjs
from jsonpath import jsonpath
import ddddocr
from random import randint
import time

#define headers
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fcbox.com",
    "Pragma": "no-cache",
    "Referer": "https://fcbox.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"156\", \"Google Chrome\";v=\"156\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
def get_parts(uuid):
    #define url
    url = 'https://acs.fcbox.com/captcha/querySlideImage/'+uuid
    #get the response
    response = requests.post(url, headers=headers)

    checkid = jsonpath(response.json(),'$..checkId')[0]
    clientip = jsonpath(response.json(),'$..clientIp')[0]
    key = jsonpath(response.json(),'$..key')[0]

    shadeurl = jsonpath(response.json(),'$..shadeImageUrl')[0]
    shadecontent = requests.get(shadeurl,headers=headers).content
    slideurl = jsonpath(response.json(),'$..slideImageUrl')[0]
    slidecontent = requests.get(slideurl,headers=headers).content
    ocr = ddddocr.DdddOcr(show_ad=False)
    result = ocr.slide_match(slidecontent,shadecontent)
    cx = result.get('target_x')
    cy = jsonpath(response.json(),'$..pointY')[0]

    return checkid,clientip,cx,cy,key
def get_track(cx,cy):
    t = int(time.time()*1000)
    track = []
    x=0
    mid = cx/10
    while x < cx:
        if x<mid or x>cx-mid:
            v=randint(0,1)
        else:
            v=randint(1,2)
        dt = randint(1,2)
        x += v
        t += dt
        track.append({
            "x": x,
            "y": cy,
            "time": t,
        })
    return track

def send_verify(uuid,data):
    url = 'https://acs.fcbox.com/captcha/checkCode/'+uuid
    #data = '5vlByVoikIyG1hEaoVMj7TrEkjahZOsldXBFQI1SSDYlgn5DpNXManWykerka6LsB6ZI3in0F4ePlgmOHE8GgeJlDkGaYr0nhYhDHV+PBvMKBxLqEG6vHJSqYbIYp+C+TIMzqkurYlIHuzc/kp9njX9wO0Pz49QBBGuA/0G+QkOZxcI6sX1KOEoPuymmEJIU/vno0kvvEb53PnI/TNYgdhSkHiyRaZe9VC+hvN9G1Mm6IUAxiiXUg9zu2UyTjsPw+qhVEgS/Zx1eX6CW+LVknuJlDkGaYr0nhYhDHV+PBvNArnlbT7roXxMPMftisGchTIMzqkurYlIHuzc/kp9njegsh7f3yzIFKBs6FTjHmHCkI8BQpDxn/OOZya7gDhZh2uVpaa6WkZeF1yU26yuGovLB2WqXQx50RRWwmVvemLe6IUAxiiXUg9zu2UyTjsPwTUTrnEl0TFNzJXL6DV4my+JlDkGaYr0nhYhDHV+PBvPn0gxhZ21gqVXLHK0XM5k3TIMzqkurYlIHuzc/kp9njfps/IX6NkgeiBcJLNf378iiL1/hdWS5wWd0SvvXYRGpNYeEKLNKOQnvkITRbEcSQgh5+MQ541e2iauLMGmmnO645xMdjSuqo5jbvAN0d1wC7P+OxXSd3rXwWxre2r2MV07YyCVXTtOGZhxLm38n/g05dYhFtoMCno23fRIcDDPd0ib3V8M0HQHNJZbSt34yfkhY0YYcvQSzp5SXqHTiN91BK4OKH0U3feiR6PHp9qbluiFAMYol1IPc7tlMk47D8Ft3IZFJVEO+25BBIzk5CT7XV9YPEop+KnFdtGQTFyBuFun0Bpe1J47Fx9d7StwTke4hQjHnCJfcIUGYjgVN1mv2MwtFRAjhdTPl71jbNKT7xMJZQUhTxhKWwKIlzEaJyvyoerIcGg0tFZf/+3md/jvKrE+qcDNlV/VrQ6nKTX6R4mUOQZpivSeFiEMdX48G82GRHNrLnRYgSrog882TZy90jAgFTe7bdNRD/k8wfZYXMZ6w5+ljmO9Rvb5o6OpDhMGMx9SpXiDbnHNoe45ttW2w/rBE3J3ADWGkXOE/cvMbFIHl54NKp03X02r71dLgLOODYXtT8nrZqDlN9q6aS+caqVlgLc3MjKrHDppv9LRiTIMzqkurYlIHuzc/kp9njfUyNiQzLf+0/3oJdwdjI9NFZzAd0McAESt+NzZI02BCrIi03tDQ9ypl9Mj1QhxUfRnnk6JeVgQLRq0IDquFa29fFgv62tb93gz5Z1ZMq5ISH9le6V87HHQjNtieP+QO6m5NEZl1b8ipC0XrUi8aVRoiFBgMm/QSyhorjqVm/PuJJZXa+tkTz/ZHtWiMR2OmJy5WZ46dJ+4Zf52DIcwcdO5+aksucVRZUVYiP3ZY945DuOcTHY0rqqOY27wDdHdcAtDdlNL5DHMXlVC0qVj+Xy1O2MglV07ThmYcS5t/J/4NpBqj/57S+dvSovvivsvFzczBADq2w8vTPIDMddJgv2vTLAePUbFnSjhmZ/Ho6McxWSLWL+ufyaxlZGDflJlfj1L+cZygm697UzPY34p69ActZq4hv7uVixLFLxDHooaF11fWDxKKfipxXbRkExcgbrSm7E0jPzBeuI6aMq0+NQvuIUIx5wiX3CFBmI4FTdZrqAjeXu52cEmB59IQ6bJ0CiY3Vyc3jIPJ05UanTLbNXhqTtZQjU+ouvvczDG0PPmbps7cgVfiqRsK5kW/B004deJlDkGaYr0nhYhDHV+PBvPC1RtGCbMK5D4ruW4nkkqcdIwIBU3u23TUQ/5PMH2WF8ivEU0n41hiV044tAZZBffvzY/w0MBJ89AuLhCgi/nHT9oNaO4s8uMSq7F05pAQU6e2CwKRNj4VKTqbFkcgKLbjg2F7U/J62ag5TfaumkvnlMeZ7XXrbywPtGcYOQgS0UyDM6pLq2JSB7s3P5KfZ41sxO7L32PoYAM+0ywjFLlllhB56PCtFEQkKc0KQqleZB1DN7eSTgGXlXgIF8cI2rUwMQdtgzRzaXqMhWB/eqaMXxYL+trW/d4M+WdWTKuSEtf59EXdBLyNq6IQMg5EfMNuTRGZdW/IqQtF61IvGlUaAvjmwGmCc252pXrO2tl2UNgshL1HXLhl6+rEUfI2GimCaHEJYmWkmSRsHjYRWOTZbnisVVP09mUfiXQdICA4BrjnEx2NK6qjmNu8A3R3XAJDGLeDChHzlVJtcYa0NBeoTtjIJVdO04ZmHEubfyf+DafhKMXZG4DcB/sGhkwkH9xoC6vpTMa1V0RaV2at6TUZkQU7B7emntTTyQL8UbIVvzxmu3MVIAHNJ9MS/KQmgwxS/nGcoJuve1Mz2N+KevQHNqTPjIDFXCl5nHm9euFsk9dX1g8Sin4qcV20ZBMXIG568P5XDmZoEyJSODGig1sP7iFCMecIl9whQZiOBU3Wa43jFiNq91znYgTnA0RkrUR1Jw4MLhxV7o8CrSFMnUcePN61pf7+lqooi8TXtiKNWg33waQJvGkgWI6yfMlrWojiZQ5BmmK9J4WIQx1fjwbzfXU8Noat5d4LUDIOJYR32nSMCAVN7tt01EP+TzB9lhcFOct4W1u+yHQIHXCzyEG42p5EFrv8YzjQ2X+PDNpBWXwK0LMR+S89G4LqxVFj1EFx7sZyOip+bTL/bKYeaXLt44Nhe1PyetmoOU32rppL5/Gh0QBUXMiWorvT1iEaCsNMgzOqS6tiUge7Nz+Sn2eNDdSWpV1yRRYYKQYyl8WBj3AujH0iwY64TYXCmhnzeOb5lbTzj6D+HAMcaKA4ELMJFi65av2YE29Jh2+//xl3VF8WC/ra1v3eDPlnVkyrkhLPMI70rXh10vr6Hrs/FLS6bk0RmXVvyKkLRetSLxpVGitgMkjReJgmbE4NsvgD7FE5/OzodNxWXYuqs79rHTMfaxxVOL4vFbJfALuiUr9/ylhmS4/hTrLT5dKWZpqnydS45xMdjSuqo5jbvAN0d1wCt79N0Im5IWAxNUSj3938YE7YyCVXTtOGZhxLm38n/g0a0iZaS8z+Xrqw4gaXzOK2q77gOx1LUlSj9aevf/DYMxvAFcDbjrDqylHQRj+fn2aA/tIDUnw1sdY3NOiwltE2Uv5xnKCbr3tTM9jfinr0BzJMBs4QxPAwJthPFbNhyyHXV9YPEop+KnFdtGQTFyBubYZKeUetEGrdZIngxHKQ5O4hQjHnCJfcIUGYjgVN1mvFaxZfap8wrI4NLdEEYBhU+ATIHTutMYOI+0FoXSrPeKCG+TEBeadjTFPmkIOEn01akiJj71TUcXZneUvywgzK4mUOQZpivSeFiEMdX48G8zzAwVJ5fey2QNLKA5LxmT90jAgFTe7bdNRD/k8wfZYXJPpc8jzRyZ9exG2s+gGq+WZZ1n/peV+asGi0slMFi/8R2GRT3cGeU/j75Myb3zy7uvUoBUS+AdRieGUWHsSd7eODYXtT8nrZqDlN9q6aS+fQbpj1yCqWx4TZjIFDGt2xTIMzqkurYlIHuzc/kp9njenGg5ACaqNE5dG+kztbQrNauCexE3tSwI7W0Cnp5gnCPQ+XutL8wKRjAmFLYPAex1Fw5DsuaHbPh5I2+ddj6gxfFgv62tb93gz5Z1ZMq5ISsrBw8cImdvtxxCA8HMYJXG5NEZl1b8ipC0XrUi8aVRpNRugHwMfiBtMkPhLBSyOo2vENyEinDOhj5sx9VV7XyS2skIiOmV2BipYXZDGrnQccKK45oSCge/VJ2Id+39FjuOcTHY0rqqOY27wDdHdcAsd4opxuzhjD/ERGBaORsFRO2MglV07ThmYcS5t/J/4NXZ4GnM70B1I+J1obGkGq9antUqNO+nzhZw30Zhjc9JGjRM78vfLxTgjiqiqwLVog897CzqH2c6E1hafHfiJDJK7LpcV/Lxc4S+xykH0RFbEshgJJSx8HpXJ0xEhzR/J911fWDxKKfipxXbRkExcgbkibqLtNIE/gDwq1mpAXFunuIUIx5wiX3CFBmI4FTdZrc+tO0ZgKXc0LgvesS0PGLDrUkSw9EAfO6RAP8wT7msbvN4Au34J+8cf0gXbe2aweVaDvZrEVaCnQsIrPKHdxv+JlDkGaYr0nhYhDHV+PBvObF5vh5pMvBffePilRA1HzdIwIBU3u23TUQ/5PMH2WFwBicayLOoWEGXg22OUoRFRCxnUX9bdfKSEg1EGlVW7ACAJSnEeQ5LpQQ/xfH5shz4itdUDi+lS6Z2dwBsxDxlPjg2F7U/J62ag5TfaumkvnvbqN4WXP47BMGjfVO03FCEyDM6pLq2JSB7s3P5KfZ40RCbR1851c1a52Bf7ugDnIf4nWpeTbJlLclx3nDiw2SnRGSNC8W/kgV+dDtwHQM/ppGyZxUQXqfkfow2KZUqdtXxYL+trW/d4M+WdWTKuSEtMiV/191M17Sdc/MPmHEGluTRGZdW/IqQtF61IvGlUaPB3AZh8hTwjtPazkehG2cpQM/iq2oJzbxiw8NYLr0R1ZbdF4dBlm79XCoibGXhmsdwgY+Rhsj9GqqoEv3CZw6V8WC/ra1v3eDPlnVkyrkhIsLr0bEHJYJjxeoXOsuq6gTIMzqkurYlIHuzc/kp9njb+ux/ODxn1IYvoKKbl6T/pzh98sEWd1smHl/GlSdKdpIlQUo+IsFoyHtcX1pV7RXg3/nzv9eBCYHl59nfBdjGviZQ5BmmK9J4WIQx1fjwbzYp8MwduOtAoQmqEzLo+fk+4hQjHnCJfcIUGYjgVN1ms9tRRyzKWKVTNjJVdah80ONjwF+dIkIoiOxMpGnHVXUa7LpcV/Lxc4S+xykH0RFbGAjlfx9aG0HsZ53gVm1XiITtjIJVdO04ZmHEubfyf+DRmc3i+0+Nt6cHgIAEaHij6HvPsXjkf1X+mfBxBW2KLyamrPznn/iYsbE7+2V0I2bzVX4suwrRvNvXSKXL8zxV1fFgv62tb93gz5Z1ZMq5ISiC4cZBoxLATVoRKnxeZYxEyDM6pLq2JSB7s3P5KfZ43IGY/NZ00k79StALiuIaHYc4B9Tcs96GEdTGEAlaR1WLGUuhr+MTCc7jKeRhPXfo2yrTE8REcU6iXeGJJZRCdk4mUOQZpivSeFiEMdX48G8663FoME1Uuo7A2WMq49P0buIUIx5wiX3CFBmI4FTdZrR80JpK0caTRs1o4uonekJU22zNUkcliNvra1MrO5vq+uy6XFfy8XOEvscpB9ERWxfyr0727DiV55zbaaTKnmlU7YyCVXTtOGZhxLm38n/g183Axmi7LakoqcBLUNYNK/OXSomiJ2Q78KGVNDz2TNXgF83Z8uB7KPK4U7Jzzyx43IXxmZ1bxwjerroYQHMqTZXxYL+trW/d4M+WdWTKuSEmO/TThphnqGfvMWwUFYzSZMgzOqS6tiUge7Nz+Sn2eN7lp+tRfnFsk5JBLWvfbrysZwg6bApGEmFNqsjN3HDXn8t670V7orjCY8dklWHH67vWcEzXx/39BoiHAyw1AwGOJlDkGaYr0nhYhDHV+PBvPkR/F/lU3pEDulrV1hN/iX7iFCMecIl9whQZiOBU3Wa7rXP2/uS9PeVPzMWaIMlvtDUkUdL6TqzL3cvY171fevrsulxX8vFzhL7HKQfREVsTyJ8QOvjA0b3K/AdgXDhINO2MglV07ThmYcS5t/J/4NwycgY9ohInARMWAa0iY0x7f6bR+n5SsEKHFQ34EZ3GQ18XWeE8Zvuq1NrVEohRotxiHvf5bk7yxABaoZIaT21l8WC/ra1v3eDPlnVkyrkhJfjdnzP/A4MF4V0/ILO42rTIMzqkurYlIHuzc/kp9njU6ixvdZm44ZrIXARmVohu8DF7ihud7+ZxYOQoQPBoGFbP1sf//OfTU/9TwE4tG4l5tpZbSscYstDPk1HvjhGKfiZQ5BmmK9J4WIQx1fjwbzXUB0q10qAEbpCt1H7XVzQ+4hQjHnCJfcIUGYjgVN1mv8sLev7pu9grCxkBEhIT1ezEMTDyfERdkVno425+y57EJ4/m420lBunsbOvDSto4h/qXxFcswHEErctbGwlIsETtjIJVdO04ZmHEubfyf+DSmuMNjHnYHfQV2pztKwzpV5bNeHQkhqg/NKHEYEhjrVs2qZoksYFRMbTWQ/XJ5S/ifhHe2MxBfJo3s60zLEz5NfFgv62tb93gz5Z1ZMq5ISjEYvsSA86YoT8BgV5bdHmkyDM6pLq2JSB7s3P5KfZ43azVGb3zqqEHRPRGKnBuLQoIH4OYSWTcW85/4bFg6CvflPyxW7oS3LAv1qo2QSIrtXVI6yMBzrgH9iIudC+dmf4mUOQZpivSeFiEMdX48G88HP69WgN3dr2WUbYuGKraDuIUIx5wiX3CFBmI4FTdZrdbG2nyR4h+/1x4+UxfnsCKjlvqQvxAo7bBtP3xVJhSdCeP5uNtJQbp7Gzrw0raOIqAVWTdIGxTCH1tV1ndQPe07YyCVXTtOGZhxLm38n/g3iO/lRlFX17iCYrUA5vPe0Un1mrcezyLCU51MhbYjN86yuokMZpLIT8HsvACS3E+EOH0lv4mkR83/7zpaVx6Z3XxYL+trW/d4M+WdWTKuSEhF18pRs1iW0Fes84bh/TCtMgzOqS6tiUge7Nz+Sn2eN3njexNUuLsjmYXiAnY1qZvZ2nbePqRAfZpkWrUPiarKYKQ+Yy+X7pevQzjgmQUAoK25AJZOa4ietVPlzNLycueJlDkGaYr0nhYhDHV+PBvMZVqdHF6NwM+p12/4zJ19R7iFCMecIl9whQZiOBU3Wa9S+YYdeTGFlPGWXG2UbTouOVQQhxeKMXK+6yjXYhgzjQnj+bjbSUG6exs68NK2jiJ4NGKhFpf5LAoljf169/NtO2MglV07ThmYcS5t/J/4N+g4EoEhZZSwtf/t585Iz0W+yzowZnlxo1OuisVsYE25m4blyELR7EZZqPiMqHZ952pUt5o8AWSOlCxmv9lnIll8WC/ra1v3eDPlnVkyrkhKcqoxiaVU/3Oo4iWSayZPXTIMzqkurYlIHuzc/kp9njSceUG7Er3jS9qsx/UjOyMSZWXl32c58ymsTx8zL8wVTiBHtzKVwl+MwXuPwxsWm/Xf4KkonMGSpTGyhNwPv0CPiZQ5BmmK9J4WIQx1fjwbzjmgY3ADrse8F8bJO/speF+4hQjHnCJfcIUGYjgVN1mtks1ndN60l6n0gkWulzlWpT0rEpXbzgMXZrzUeDqMElUJ4/m420lBunsbOvDSto4gaISPUswfrXoZsQym6yUOmTtjIJVdO04ZmHEubfyf+DbDcT06O+G9jjuaJ0UhN7tGWYhdEO6B+fTBKmTtO1nvh/XSvg64HlvDiFvuz6+Bl/QevR9P18KoQJQkVdCivFR9fFgv62tb93gz5Z1ZMq5ISaqdRm6QaTE5ye+/rzS9iX0yDM6pLq2JSB7s3P5KfZ414PA3b5mt5Mmvk2tSANt44tO3qIf6qDCejD/+iyYGPPE1TRjz6ZUUFQ0fVire1DKE8HVg7CtLMFEz4qZuLrUr14mUOQZpivSeFiEMdX48G85tbk9zxyFUZyUOqds9x8ZHuIUIx5wiX3CFBmI4FTdZrQH8sXRFogonVKUrNMQwQWuGMagI97fmZs7eJudjS3wlCeP5uNtJQbp7Gzrw0raOI7h0mRs3ozjwvDYAiQN7dUE7YyCVXTtOGZhxLm38n/g2M+lMr2DlCknriucu7DK1JAIBtgtns6jCSshWbCYlXjxOQV1z5U6Q9MuqS2Yf+f2A2UQV/Up4PC7QxG8G6m+YqXxYL+trW/d4M+WdWTKuSEvV4p0Q0iUgZ41dotSf6LzVMgzOqS6tiUge7Nz+Sn2eNjyVmhdmzCW2v2ilM/k/2Ns9ZRVHFQkyBUC7MlhI3MZnOIg2n2/lC9NXm0C/f771esJyxMzbhlS1AFHYtDSTiS+JlDkGaYr0nhYhDHV+PBvP2cxCRe5svGi8/yUjU4G5W7iFCMecIl9whQZiOBU3Wa8Acld7djUr7s4vKoG6rJHvGDiicI6AK1ERtU9ryDL31XkfEd0JBhOLkI1sziH6gqwYCCOKen4k+pUOgqEal9zJO2MglV07ThmYcS5t/J/4NK6Od9cnE+3BEy40MeFhamXdKCq23CX8hIrXg574CFfhdG756Te8BnmibTZwHfsVibFwj8QeHbqlzR7zEVa9tP18WC/ra1v3eDPlnVkyrkhIyKqFOiBqxGoGfoCJ5Z9vWTIMzqkurYlIHuzc/kp9njaITH0O4M35sqPc5TysA3ehYREdXRhT/dpktdPdeTQN9kAiRxqoa8Cwv75QiauxhEfMTo9Xy4hQITH7DppoM+iHiZQ5BmmK9J4WIQx1fjwbzx+kzl/INl+RJ85V0WauIT+4hQjHnCJfcIUGYjgVN1mv79c7z8L3jpG9Eq/SSddA/9vBAaNylg+JKl3tiFO/D5F5HxHdCQYTi5CNbM4h+oKtqipNy2Mo0Ok/N/qxmnWAWTtjIJVdO04ZmHEubfyf+DVeLnjlVNZ/mZTJwzfPGQMOKXTpmvldaQUoIknURmFnPvin4FfAZAISN8MZNjNdFKCpbuAZOAtVhEfxDhKdPHV5fFgv62tb93gz5Z1ZMq5ISxzz7XgrLHQVW8XKPUr4KpkyDM6pLq2JSB7s3P5KfZ42ZAnEZXSFQIOmxFCMCJqyEfOqtSrAW/meynHKOAajwmYO1Q1I4WYi3t2Afc4j9jNOJnsa7273X3dfZ4eYiTMG84mUOQZpivSeFiEMdX48G8yRsYKVLuJu/YLXYlerIIRruIUIx5wiX3CFBmI4FTdZr45apynNInx/GTPwTIWYdIIblnug3h0E+JUJQOLV5BjxeR8R3QkGE4uQjWzOIfqCrxmQT7UfrhSMA/v1cGl2TCE7YyCVXTtOGZhxLm38n/g2sp5zoskGAIDW7RMHkI8exsdtVRbJB8y5/uUrmwb92h/uDF+GWLv35Z6yUJBb/pw3ye7kMFzI0ETjlvbmY3oN7XxYL+trW/d4M+WdWTKuSEiGMiaxJl0OsFeJD0LqzxjZMgzOqS6tiUge7Nz+Sn2eNRxtpnarTxbOh4Ll5F+tiQvteJUeSLIO544C2NIjTu+CjN0Gzuk2lNvk2W9LTlKd2q0IciUXOnK2CNK5n2uKM1uJlDkGaYr0nhYhDHV+PBvOEiKZfPNd0nah4rJVzKd0d7iFCMecIl9whQZiOBU3Wa7MhFfez+p1UhxwL4vkAp6zaevLU77Fdy3GUAQ3FDq4lXkfEd0JBhOLkI1sziH6gqzREgjmdrrVtB6xaP+2SrCpO2MglV07ThmYcS5t/J/4NJZPOmVvWJITXyJdlC+JDeinKLI5qzKruTzkb7qaACmjCyv9Le6Q5rZP2KrQRZtPh6bJ/zMNu7dCQ+Q1xs3OZ0F8WC/ra1v3eDPlnVkyrkhI5e9dQAjNkCG3zMqqMLwTqTIMzqkurYlIHuzc/kp9njbjxyCAEab97HYP0VSw4vZ0YRZpey++HxLQse7F0cggM8s27oaaxIR/iN8JK+Ldam2YzSbhdYe1CKKAHr48Kj8HiZQ5BmmK9J4WIQx1fjwbzlDrLuI44zzejhZE2PHRWeu4hQjHnCJfcIUGYjgVN1msmPw/OTIvruUZpkbG/ngpHqpNGlHlZ5zIs3NqwEUrf9i88oaRDuvFWELWJu/HGVVCbnQ+fmGrxjUYpjjuJ1hQnTtjIJVdO04ZmHEubfyf+DVUZ2bjuBvyq8H4Ku0voOEvoxjlhgAgquQ4Y3d0b9MjSlNLOZO6z3hQTf2z5UXCj5phqGH7X4HDbSDPSxIZC1vk='
    response = requests.post(url, headers=headers, data=data)

    print(response.text)

if __name__ == '__main__':
    with open('assistant.js','r',encoding='utf-8') as f:
        jscode = f.read()
    uuid = execjs.compile(jscode).call('uuid')
    checkid,clientip,cx,cy,key = get_parts(uuid)
    track = get_track(cx-33,cy)
    track[-1]['x'] = cx-33
    track[-1]['y'] = cy
    data = execjs.compile(jscode).call('data',uuid,checkid,clientip,track,key)
    send_verify(uuid,data)

