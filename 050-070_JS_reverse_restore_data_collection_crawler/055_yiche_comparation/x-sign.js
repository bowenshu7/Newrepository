const Crypto = require('crypto-js')

function s(params, timestamp) {
    var cid = "508"
    var n = "";
    var i = JSON.stringify(params)
        , o = "19DDD1FBDFF065D3A4DA777D2D7A81EC";
    n = "cid=" + cid + "&param=" + i + o + timestamp
    var s = Crypto.MD5(n).toString()
    return s
}
var timestamp = 1785572057008
var params = {
    carIds:"189010,187033,187034",
    cityId: "1301"
}

console.log(s(params, timestamp));