const Crypto= require('crypto-js')


function encrypt(s,key,iv) {
    var e = JSON.stringify(s)
        , n = Crypto.enc.Utf8.parse(key)
        , i = Crypto.enc.Utf8.parse(iv)
    e = Crypto.enc.Utf8.parse(e);
    return Crypto.AES.encrypt(e, n, {
            mode: Crypto.mode.CBC,
            padding: Crypto.pad.Iso10126,
            iv: i
        }).toString()
}




function get_userbehaviordata(cx,cy,iv,key){
    var s = {
        "cx": cx,
        "cy": cy,
        "scale": 0.5,
        "slidingEvents": [
        {
            "mx": 40,
            "my": 202,
            "ts": 1792937199844
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 44
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 9
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 9
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 9
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 9
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 8
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 11
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 15
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 19
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 15
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 13
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 9
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 12
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 8
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 13
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 13
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": -1,
            "ts": 7
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": -1,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 7
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": -1,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": -1,
            "ts": 8
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 0
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 6
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 3
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 1
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 4
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 2
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 5
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 20
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 13
        },
        {
            "mx": 1,
            "my": -1,
            "ts": 27
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 55
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 219
        },
        {
            "mx": 0,
            "my": -1,
            "ts": 28
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 13
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 14
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 30
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 82
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 54
        },
        {
            "mx": 0,
            "my": 0,
            "ts": 55
        },
        {
            "mx": 1,
            "my": 0,
            "ts": 28
        },
        {
            "mx": 1,
            "my": -1,
            "ts": 55
        }
    ]
    }
    return encrypt(s,key,iv)
}

cx = 112
cy = 30
iv = 'MaomqZFEk9TOf9SB'
key = 'djoO7oCAu3vHHEcm'

console.log(get_userbehaviordata(cx,cy,iv,key))