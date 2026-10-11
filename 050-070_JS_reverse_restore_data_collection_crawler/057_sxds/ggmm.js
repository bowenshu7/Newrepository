const Crypto = require('crypto-js')

function ggmm(data, t) {
    var e = data + t
    //     , n = le;
    // return n.update(e),
    //     n.getHash("B64")
    return Crypto.SHA256(e).toString(Crypto.enc.Base64)
}

a = parseInt((new Date).getTime() / 1e3)
ggmm(a, "lzadIuYtSA6CpdE0llu8")

function result(t){
    return ggmm(t, "lzadIuYtSA6CpdE0llu8")
}

console.log(result(a))