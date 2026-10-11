const CryptoJS = require('crypto-js')


function AESDecrypt(str) {
    var variate = {
        key: {"words": [863652730, 2036741733, 1164342596, 1782662963], "sigBytes": 16},
        aceIV: {"words": [1719227713, 1314533489, 1397643880, 1749959510], "sigBytes": 16}
    }
    var nContent = CryptoJS.AES.decrypt(str, variate.key, {
        iv: variate.aceIV,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    })

    return CryptoJS.enc.Utf8.stringify(nContent)

    //translate to object (meaningless)
    // var data = JSON.parse(constr);
    // return data;
}

s = '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'

console.log(AESDecrypt(s))