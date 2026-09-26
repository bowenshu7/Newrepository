
var e = "/youzy.dms.basiclib.api.college.query"
var t = {
    "keyword": "",
    "provinceNames": [],
    "natureTypes": [],
    "eduLevel": "",
    "categories": [],
    "features": [],
    "pageIndex": 1,
    "pageSize": 20,
    "sort": 11
}

function stringToBytes(e) {
    return binstringToBytes(unescape(encodeURIComponent(e)))
}

function binstringToBytes(e) {
    for (var t = [], r = 0; r < e.length; r++)
        t.push(255 & e.charCodeAt(r));
    return t
}

function wordsToBytes(e) {
    for (var t = [], r = 0; r < 32 * e.length; r += 8)
        t.push(e[r >>> 5] >>> 24 - r % 32 & 255);
    return t
}
function bytesToWords(e) {
    for (var t = [], r = 0, n = 0; r < e.length; r++,
        n += 8)
        t[n >>> 5] |= e[r] << 24 - n % 32;
    return t
}

function p(e, t, r, n, o, i, a) {
    var s = e + (t & r | ~t & n) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}
function y(e, t, r, n, o, i, a) {
    var s = e + (t ^ r ^ n) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}
function b(e, t, r, n, o, i, a) {
    var s = e + (t & n | r & ~n) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}

function m(e, t, r, n, o, i, a) {
    var s = e + (r ^ (t | ~n)) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}

function rotl(e, t) {
    return e << t | e >>> 32 - t
}
function endian(e) {
    if (e.constructor == Number)
        return 16711935 & rotl(e, 8) | 4278255360 & rotl(e, 24);
    for (var t = 0; t < e.length; t++)
        e[t] = endian(e[t]);
    return e
}
function ab(e, r) {
    e.constructor == String ? e = r && "binary" === r.encoding ? i.stringToBytes(e) : stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
    for (var s = bytesToWords(e), u = 8 * e.length, c = 1732584193, f = -271733879, d = -1732584194, l = 271733878, h = 0; h < s.length; h++)
        s[h] = 16711935 & (s[h] << 8 | s[h] >>> 24) | 4278255360 & (s[h] << 24 | s[h] >>> 8);
    s[u >>> 5] |= 128 << u % 32,
        s[14 + (u + 64 >>> 9 << 4)] = u;
    for (h = 0; h < s.length; h += 16) {
        var v = c
            , g = f
            , _ = d
            , w = l;
        c = p(c, f, d, l, s[h + 0], 7, -680876936),
            l = p(l, c, f, d, s[h + 1], 12, -389564586),
            d = p(d, l, c, f, s[h + 2], 17, 606105819),
            f = p(f, d, l, c, s[h + 3], 22, -1044525330),
            c = p(c, f, d, l, s[h + 4], 7, -176418897),
            l = p(l, c, f, d, s[h + 5], 12, 1200080426),
            d = p(d, l, c, f, s[h + 6], 17, -1473231341),
            f = p(f, d, l, c, s[h + 7], 22, -45705983),
            c = p(c, f, d, l, s[h + 8], 7, 1770035416),
            l = p(l, c, f, d, s[h + 9], 12, -1958414417),
            d = p(d, l, c, f, s[h + 10], 17, -42063),
            f = p(f, d, l, c, s[h + 11], 22, -1990404162),
            c = p(c, f, d, l, s[h + 12], 7, 1804603682),
            l = p(l, c, f, d, s[h + 13], 12, -40341101),
            d = p(d, l, c, f, s[h + 14], 17, -1502002290),
            c = b(c, f = p(f, d, l, c, s[h + 15], 22, 1236535329), d, l, s[h + 1], 5, -165796510),
            l = b(l, c, f, d, s[h + 6], 9, -1069501632),
            d = b(d, l, c, f, s[h + 11], 14, 643717713),
            f = b(f, d, l, c, s[h + 0], 20, -373897302),
            c = b(c, f, d, l, s[h + 5], 5, -701558691),
            l = b(l, c, f, d, s[h + 10], 9, 38016083),
            d = b(d, l, c, f, s[h + 15], 14, -660478335),
            f = b(f, d, l, c, s[h + 4], 20, -405537848),
            c = b(c, f, d, l, s[h + 9], 5, 568446438),
            l = b(l, c, f, d, s[h + 14], 9, -1019803690),
            d = b(d, l, c, f, s[h + 3], 14, -187363961),
            f = b(f, d, l, c, s[h + 8], 20, 1163531501),
            c = b(c, f, d, l, s[h + 13], 5, -1444681467),
            l = b(l, c, f, d, s[h + 2], 9, -51403784),
            d = b(d, l, c, f, s[h + 7], 14, 1735328473),
            c = y(c, f = b(f, d, l, c, s[h + 12], 20, -1926607734), d, l, s[h + 5], 4, -378558),
            l = y(l, c, f, d, s[h + 8], 11, -2022574463),
            d = y(d, l, c, f, s[h + 11], 16, 1839030562),
            f = y(f, d, l, c, s[h + 14], 23, -35309556),
            c = y(c, f, d, l, s[h + 1], 4, -1530992060),
            l = y(l, c, f, d, s[h + 4], 11, 1272893353),
            d = y(d, l, c, f, s[h + 7], 16, -155497632),
            f = y(f, d, l, c, s[h + 10], 23, -1094730640),
            c = y(c, f, d, l, s[h + 13], 4, 681279174),
            l = y(l, c, f, d, s[h + 0], 11, -358537222),
            d = y(d, l, c, f, s[h + 3], 16, -722521979),
            f = y(f, d, l, c, s[h + 6], 23, 76029189),
            c = y(c, f, d, l, s[h + 9], 4, -640364487),
            l = y(l, c, f, d, s[h + 12], 11, -421815835),
            d = y(d, l, c, f, s[h + 15], 16, 530742520),
            c = m(c, f = y(f, d, l, c, s[h + 2], 23, -995338651), d, l, s[h + 0], 6, -198630844),
            l = m(l, c, f, d, s[h + 7], 10, 1126891415),
            d = m(d, l, c, f, s[h + 14], 15, -1416354905),
            f = m(f, d, l, c, s[h + 5], 21, -57434055),
            c = m(c, f, d, l, s[h + 12], 6, 1700485571),
            l = m(l, c, f, d, s[h + 3], 10, -1894986606),
            d = m(d, l, c, f, s[h + 10], 15, -1051523),
            f = m(f, d, l, c, s[h + 1], 21, -2054922799),
            c = m(c, f, d, l, s[h + 8], 6, 1873313359),
            l = m(l, c, f, d, s[h + 15], 10, -30611744),
            d = m(d, l, c, f, s[h + 6], 15, -1560198380),
            f = m(f, d, l, c, s[h + 13], 21, 1309151649),
            c = m(c, f, d, l, s[h + 4], 6, -145523070),
            l = m(l, c, f, d, s[h + 11], 10, -1120210379),
            d = m(d, l, c, f, s[h + 2], 15, 718787259),
            f = m(f, d, l, c, s[h + 9], 21, -343485551),
            c = c + v >>> 0,
            f = f + g >>> 0,
            d = d + _ >>> 0,
            l = l + w >>> 0
    }
    return endian([c, f, d, l])
}

function bytesToHex(e) {
    for (var t = [], r = 0; r < e.length; r++)
        t.push((e[r] >>> 4).toString(16)),
            t.push((15 & e[r]).toString(16));
    return t.join("")
}
function n(e, r) {
    if (null == e)
        throw new Error("Illegal argument " + e);
    var n = wordsToBytes(ab(e, r));
    return r && r.asBytes ? n : r && r.asString ? i.bytesToString(n) : bytesToHex(n)
}
var r, o = "9SASji5OWnG41iRKiSvTJHlXHmRySRp1", i = "", a = t || {}, s = (e = e || "").split("?");

function u(e, t) {
    var r, o = "9SASji5OWnG41iRKiSvTJHlXHmRySRp1", i = "", a = t || {}, s = (e = e || "").split("?");
    if (s.length > 0 && (r = s[1]),
        r) {
        var u = r.split("&"), c = "";
        u.forEach(function (e) {
            var t = e.split("=");
            c += "".concat(t[0], "=").concat(encodeURI(t[1]), "&")
        }),
            i = "".concat(_.trimEnd(c, "&"), "&").concat(o)
    } else
        i = Object.keys(a).length > 0 ? "".concat(JSON.stringify(a), "&").concat(o) : "&".concat(o);
    return i = i.toLowerCase(), n(i)
}


console.log(u(e,t))