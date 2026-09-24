
function f(n, r, t, e, u, c, f) {
        return o(t ^ (r | ~e), n, r, u, c, f)
    }
function c(n, r, t, e, u, c, f) {
        return o(r ^ t ^ e, n, r, u, c, f)
    }
function u(n, r, t, e, u, c, f) {
        return o(r & e | t & ~e, n, r, u, c, f)
    }
function r(n, r) {
        var t = (65535 & n) + (65535 & r);
        return (n >> 16) + (r >> 16) + (t >> 16) << 16 | 65535 & t
    }
function o(n, t, o, e, u, c) {
        return r(function(n, r) {
            return n << r | n >>> 32 - r
        }(r(r(t, n), r(e, c)), u), o)
    }
function e(n, r, t, e, u, c, f) {
        return o(r & t | ~r & e, n, r, u, c, f)
    }
function i(n, t) {
        n[t >> 5] |= 128 << t % 32,
        n[14 + (t + 64 >>> 9 << 4)] = t;
        var o, i, a, h, g, l = 1732584193, s = -271733879, v = -1732584194, d = 271733878;
        for (o = 0; o < n.length; o += 16)
            i = l,
            a = s,
            h = v,
            g = d,
            l = e(l, s, v, d, n[o], 7, -680876936),
            d = e(d, l, s, v, n[o + 1], 12, -389564586),
            v = e(v, d, l, s, n[o + 2], 17, 606105819),
            s = e(s, v, d, l, n[o + 3], 22, -1044525330),
            l = e(l, s, v, d, n[o + 4], 7, -176418897),
            d = e(d, l, s, v, n[o + 5], 12, 1200080426),
            v = e(v, d, l, s, n[o + 6], 17, -1473231341),
            s = e(s, v, d, l, n[o + 7], 22, -45705983),
            l = e(l, s, v, d, n[o + 8], 7, 1770035416),
            d = e(d, l, s, v, n[o + 9], 12, -1958414417),
            v = e(v, d, l, s, n[o + 10], 17, -42063),
            s = e(s, v, d, l, n[o + 11], 22, -1990404162),
            l = e(l, s, v, d, n[o + 12], 7, 1804603682),
            d = e(d, l, s, v, n[o + 13], 12, -40341101),
            v = e(v, d, l, s, n[o + 14], 17, -1502002290),
            l = u(l, s = e(s, v, d, l, n[o + 15], 22, 1236535329), v, d, n[o + 1], 5, -165796510),
            d = u(d, l, s, v, n[o + 6], 9, -1069501632),
            v = u(v, d, l, s, n[o + 11], 14, 643717713),
            s = u(s, v, d, l, n[o], 20, -373897302),
            l = u(l, s, v, d, n[o + 5], 5, -701558691),
            d = u(d, l, s, v, n[o + 10], 9, 38016083),
            v = u(v, d, l, s, n[o + 15], 14, -660478335),
            s = u(s, v, d, l, n[o + 4], 20, -405537848),
            l = u(l, s, v, d, n[o + 9], 5, 568446438),
            d = u(d, l, s, v, n[o + 14], 9, -1019803690),
            v = u(v, d, l, s, n[o + 3], 14, -187363961),
            s = u(s, v, d, l, n[o + 8], 20, 1163531501),
            l = u(l, s, v, d, n[o + 13], 5, -1444681467),
            d = u(d, l, s, v, n[o + 2], 9, -51403784),
            v = u(v, d, l, s, n[o + 7], 14, 1735328473),
            l = c(l, s = u(s, v, d, l, n[o + 12], 20, -1926607734), v, d, n[o + 5], 4, -378558),
            d = c(d, l, s, v, n[o + 8], 11, -2022574463),
            v = c(v, d, l, s, n[o + 11], 16, 1839030562),
            s = c(s, v, d, l, n[o + 14], 23, -35309556),
            l = c(l, s, v, d, n[o + 1], 4, -1530992060),
            d = c(d, l, s, v, n[o + 4], 11, 1272893353),
            v = c(v, d, l, s, n[o + 7], 16, -155497632),
            s = c(s, v, d, l, n[o + 10], 23, -1094730640),
            l = c(l, s, v, d, n[o + 13], 4, 681279174),
            d = c(d, l, s, v, n[o], 11, -358537222),
            v = c(v, d, l, s, n[o + 3], 16, -722521979),
            s = c(s, v, d, l, n[o + 6], 23, 76029189),
            l = c(l, s, v, d, n[o + 9], 4, -640364487),
            d = c(d, l, s, v, n[o + 12], 11, -421815835),
            v = c(v, d, l, s, n[o + 15], 16, 530742520),
            l = f(l, s = c(s, v, d, l, n[o + 2], 23, -995338651), v, d, n[o], 6, -198630844),
            d = f(d, l, s, v, n[o + 7], 10, 1126891415),
            v = f(v, d, l, s, n[o + 14], 15, -1416354905),
            s = f(s, v, d, l, n[o + 5], 21, -57434055),
            l = f(l, s, v, d, n[o + 12], 6, 1700485571),
            d = f(d, l, s, v, n[o + 3], 10, -1894986606),
            v = f(v, d, l, s, n[o + 10], 15, -1051523),
            s = f(s, v, d, l, n[o + 1], 21, -2054922799),
            l = f(l, s, v, d, n[o + 8], 6, 1873313359),
            d = f(d, l, s, v, n[o + 15], 10, -30611744),
            v = f(v, d, l, s, n[o + 6], 15, -1560198380),
            s = f(s, v, d, l, n[o + 13], 21, 1309151649),
            l = f(l, s, v, d, n[o + 4], 6, -145523070),
            d = f(d, l, s, v, n[o + 11], 10, -1120210379),
            v = f(v, d, l, s, n[o + 2], 15, 718787259),
            s = f(s, v, d, l, n[o + 9], 21, -343485551),
            l = r(l, i),
            s = r(s, a),
            v = r(v, h),
            d = r(d, g);
        return [l, s, v, d]
    }
function h(n) {
        var r, t = [];
        for (t[(n.length >> 2) - 1] = void 0,
        r = 0; r < t.length; r += 1)
            t[r] = 0;
        var o = 8 * n.length;
        for (r = 0; r < o; r += 8)
            t[r >> 5] |= (255 & n.charCodeAt(r / 8)) << r % 32;
        return t
    }
function a(n) {
        var r, t = "", o = 32 * n.length;
        for (r = 0; r < o; r += 8)
            t += String.fromCharCode(n[r >> 5] >>> r % 32 & 255);
        return t
    }
function l(n) {
        return unescape(encodeURIComponent(n))
    }
function s(n) {
        return function(n) {
            return a(i(h(n), 8 * n.length))
        }(l(n))
    }
function g(n) {
        var r, t, o = "0123456789abcdef", e = "";
        for (t = 0; t < n.length; t += 1)
            r = n.charCodeAt(t),
            e += o.charAt(r >>> 4 & 15) + o.charAt(15 & r);
        return e
    }
function d(n, r, t) {
        return r ? t ? v(r, n) : function(n, r) {
            return g(v(n, r))
        }(r, n) : t ? s(n) : function(n) {
            return g(s(n))
        }(n)
    }
function dd(n){
    return d(d(n))
}

console.log(dd('asdffghje'))
