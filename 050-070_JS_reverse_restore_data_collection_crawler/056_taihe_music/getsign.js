const Crypto = require('crypto-js')

function createSign(e) {
    var n = Object.keys(e);
    n.sort();
    for (var r = "", i = 0; i < n.length; i++) {
        var o = n[i];
        r += (0 == i ? "" : "&") + o + "=" + e[o]
    }
    r += '0b50b02fd0d73a9c4c8c3a781c30845f';
    return Crypto.MD5(r).toString();
}
var t = {
    "word": "zhou",
    "type": "",
    "appid": 16073360,
    "timestamp": 1790586978
}
var n = createSign(t)

console.log(n.toString())