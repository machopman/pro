import  re
import  requests
from cut import mmcut
from json import load

from searchMovieNameInDic import searchMovieNameInDic
from namemoviebefore import findmovie

def movie_type(event,question,userid):
    movie_name = re.sub('[กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮฝฦใฬมฒท?ื์ิ.่๋้็เโ,ฯี๊ัํะำไๆ๙๘๗๖๕ึ฿ุู๔๓๒๑+ๅาแ]','',event.message.text).replace(' ', '')
    if movie_name != '':
        movie_name = movie_name.lower()
        URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
        r = requests.get(url=URL)
        data = r.json()
        found = False
        for movie in data:
            if movie_name == movie['nameEN'].lower().replace(' ', ''):
                found = True
                Movie_URL = 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=Movie_URL)
                movie_detail = r.json()
                detail = movie_detail['response'][0]['detailMovie'][0]['Genre']
                detail = detail.replace('\n','')

                if detail != '':
                    return detail
                else:
                    return 'ยังไม่รู้วันประเภทหนังเรื่องนี้เลยครับ'
        if found == False:
            return 'ยังไม่รู้วันประเภทหนังเรื่องนี้เลยครับ'
    elif (movie_name == '') and (searchMovieNameInDic(question)[0] == ''):
        mov = findmovie(userid)
        movie_name = mov.lower().replace(' ','')
        URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
        r = requests.get(url=URL)
        data = r.json()
        found = False
        for movie in data:
            if movie_name == movie['nameEN'].lower().replace(' ', ''):
                found = True
                Movie_URL = 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=Movie_URL)
                movie_detail = r.json()
                detail = movie_detail['response'][0]['detailMovie'][0]['Genre']
                detail = detail.replace('\n', '')

                if detail != '':
                    return detail
                else:
                    return 'ยังไม่รู้วันประเภทหนังเรื่องนี้เลยครับ'
        if found == False:
            return 'ยังไม่รู้วันประเภทหนังเรื่องนี้เลยครับ'
    else:
        cut = mmcut(event.message.text)
        with open('new.txt', mode='r', encoding='utf-8-sig') as f:
            a = load(f)
            for key, value in a.items():
                for i in cut:
                    try:
                        if i in value:
                            w = key.lower()
                            movie_name = w.lower()
                            URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
                            r = requests.get(url=URL)
                            data = r.json()
                            found = False
                            for movie in data:
                                if movie_name == movie['nameEN'].lower().replace(' ', ''):
                                    found = True
                                    Movie_URL = 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie=' + movie['idIMDb']
                                    r = requests.get(url=Movie_URL)
                                    movie_detail = r.json()
                                    detail = movie_detail['response'][0]['detailMovie'][0]['Genre']
                                    detail = detail.replace('\n', '')

                                    if detail != '':
                                        return detail
                                    else:
                                        return 'ยังไม่รู้วันประเภทหนังเรื่องนี้เลย'
                            if found == False:
                                return 'ยังไม่รู้วันประเภทหนังเรื่องนี้เลย'
                    except :
                        return 'ยังไม่ข้อมูลประเภทหนังเลย'
#print(movie_type('ประเภทของหนังวันเดอวูแมน'))
#print(movie_type('ประเภทของหนังwonderwoman'))
