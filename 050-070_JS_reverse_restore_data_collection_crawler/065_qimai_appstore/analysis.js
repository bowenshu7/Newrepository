var window = global

function p(t) {
    t = window["encodeURIComponent"](t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    try {
        return window["btoa"](t)
    } catch (n) {
        return window["Buffer"]["from"](t)["toString"]("base64")
    }
}

function o(n) {
    return window["String"]["fromCharCode"](n)
}

function h(n, t) {
    t = t || u();
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("")
}

function get_a(a,rank,r){
    a = a["sort"]()["join"]("")
    a = p(a)
    return (a + "@#"+rank+"@#" + r + "@#3")
}

function getanalysis(syncd,param,rank) {
    var r = +new window["Date"] - syncd - 1661224081041
    var a = get_a(param,rank,r)
    var d = "xyz517cda96efgh"
    return p(h(a, d))
}

var a = [
    "all",
    "36",
    "iphone",
    "cn",
    "2026-10-19",
    2
]
var rank = '/rank/indexPlus/brand_id/1'
console.log(getanalysis(506,a,rank))
