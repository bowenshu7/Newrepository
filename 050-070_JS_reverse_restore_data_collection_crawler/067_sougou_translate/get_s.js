window = global

!function(t) {
    function e(e) {
        for (var r, o, c = e[0], u = e[1], s = e[2], d = 0, l = []; d < c.length; d++)
            o = c[d],
            Object.prototype.hasOwnProperty.call(a, o) && a[o] && l.push(a[o][0]),
            a[o] = 0;
        for (r in u)
            Object.prototype.hasOwnProperty.call(u, r) && (t[r] = u[r]);
        for (f && f(e); l.length; )
            l.shift()();
        return i.push.apply(i, s || []),
        n()
    }
    function n() {
        for (var t, e = 0; e < i.length; e++) {
            for (var n = i[e], r = !0, o = 1; o < n.length; o++) {
                var u = n[o];
                0 !== a[u] && (r = !1)
            }
            r && (i.splice(e--, 1),
            t = c(c.s = n[0]))
        }
        return t
    }
    var r = {}
      , o = {
        "2": 0
    }
      , a = {
        "2": 0
    }
      , i = [];
    function c(e) {
        if (r[e])
            return r[e].exports;
        var n = r[e] = {
            "i": e,
            "l": !1,
            "exports": {}
        };
        console.log(e)
        return t[e].call(n.exports, n, n.exports, c),
        n.l = !0,
        n.exports
    }
    c.e = function(t) {
        var e = [];
        o[t] ? e.push(o[t]) : 0 !== o[t] && {
            "0": 1,
            "3": 1,
            "5": 1,
            "6": 1,
            "8": 1,
            "9": 1,
            "10": 1,
            "12": 1,
            "13": 1,
            "15": 1,
            "16": 1
        }[t] && e.push(o[t] = new Promise((function(e, n) {
            for (var r = "pc/static/css/" + t + "." + {
                "0": "3382dd17",
                "1": "31d6cfe0",
                "3": "e674dfb6",
                "4": "31d6cfe0",
                "5": "8106975a",
                "6": "3cb7488a",
                "7": "31d6cfe0",
                "8": "c1092e98",
                "9": "29fc9c62",
                "10": "c2c025bb",
                "12": "7a0342b5",
                "13": "0e433876",
                "14": "31d6cfe0",
                "15": "9d6461c8",
                "16": "a9dcb4cf",
                "17": "31d6cfe0"
            }[t] + ".css", a = c.p + r, i = document.getElementsByTagName("link"), u = 0; u < i.length; u++) {
                var s = (f = i[u]).getAttribute("data-href") || f.getAttribute("href");
                if ("stylesheet" === f.rel && (s === r || s === a))
                    return e()
            }
            var d = document.getElementsByTagName("style");
            for (u = 0; u < d.length; u++) {
                var f;
                if ((s = (f = d[u]).getAttribute("data-href")) === r || s === a)
                    return e()
            }
            var l = document.createElement("link");
            l.rel = "stylesheet",
            l.type = "text/css",
            l.onload = e,
            l.onerror = function(e) {
                var r = e && e.target && e.target.src || a
                  , i = new Error("Loading CSS chunk " + t + " failed.\n(" + r + ")");
                i.request = r,
                delete o[t],
                l.parentNode.removeChild(l),
                n(i)
            }
            ,
            l.href = a,
            0 !== l.href.indexOf(window.location.origin + "/") && (l.crossOrigin = "anonymous"),
            document.getElementsByTagName("head")[0].appendChild(l)
        }
        )).then((function() {
            o[t] = 0
        }
        )));
        var n = a[t];
        if (0 !== n)
            if (n)
                e.push(n[2]);
            else {
                var r = new Promise((function(e, r) {
                    n = a[t] = [e, r]
                }
                ));
                e.push(n[2] = r);
                var i, u = document.createElement("script");
                u.charset = "utf-8",
                u.timeout = 120,
                c.nc && u.setAttribute("nonce", c.nc),
                u.src = function(t) {
                    return c.p + "pc/static/js/" + ({
                        "0": "common",
                        "3": "docpreview",
                        "4": "document",
                        "5": "favorite",
                        "6": "home",
                        "7": "picture",
                        "8": "privacyPC",
                        "9": "tencentDocPreview",
                        "10": "text",
                        "12": "wapDocPreview",
                        "13": "writing"
                    }[t] || t) + "." + {
                        "0": "d2ad12a8",
                        "1": "b5e605d2",
                        "3": "f173893f",
                        "4": "1321cd26",
                        "5": "223b2c2d",
                        "6": "066437f3",
                        "7": "da74d952",
                        "8": "77b05e50",
                        "9": "954d00ef",
                        "10": "ecd30039",
                        "12": "b3278251",
                        "13": "7f566bd1",
                        "14": "9cf12997",
                        "15": "8873004d",
                        "16": "62954158",
                        "17": "1c53acfb"
                    }[t] + ".js"
                }(t),
                0 !== u.src.indexOf(window.location.origin + "/") && (u.crossOrigin = "anonymous");
                var s = new Error;
                i = function(e) {
                    u.onerror = u.onload = null,
                    clearTimeout(d);
                    var n = a[t];
                    if (0 !== n) {
                        if (n) {
                            var r = e && ("load" === e.type ? "missing" : e.type)
                              , o = e && e.target && e.target.src;
                            s.message = "Loading chunk " + t + " failed.\n(" + r + ": " + o + ")",
                            s.name = "ChunkLoadError",
                            s.type = r,
                            s.request = o,
                            n[1](s)
                        }
                        a[t] = void 0
                    }
                }
                ;
                var d = setTimeout((function() {
                    i({
                        "type": "timeout",
                        "target": u
                    })
                }
                ), 12e4);
                u.onerror = u.onload = i,
                document.head.appendChild(u)
            }
        return Promise.all(e)
    }
    ,
    c.m = t,
    c.c = r,
    c.d = function(t, e, n) {
        c.o(t, e) || Object.defineProperty(t, e, {
            "enumerable": !0,
            "get": n
        })
    }
    ,
    c.r = function(t) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            "value": "Module"
        }),
        Object.defineProperty(t, "__esModule", {
            "value": !0
        })
    }
    ,
    c.t = function(t, e) {
        if (1 & e && (t = c(t)),
        8 & e)
            return t;
        if (4 & e && "object" == typeof t && t && t.__esModule)
            return t;
        var n = Object.create(null);
        if (c.r(n),
        Object.defineProperty(n, "default", {
            "enumerable": !0,
            "value": t
        }),
        2 & e && "string" != typeof t)
            for (var r in t)
                c.d(n, r, function(e) {
                    return t[e]
                }
                .bind(null, r));
        return n
    }
    ,
    c.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t.default
        }
        : function() {
            return t
        }
        ;
        return c.d(e, "a", e),
        e
    }
    ,
    c.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }
    ,
    c.p = "//search.sogoucdn.com/translate/",
    c.oe = function(t) {
        throw t
    }
    ;
    var u = window.webpackJsonp = window.webpackJsonp || []
      , s = u.push.bind(u);
    u.push = e,
    u = u.slice();
    for (var d = 0; d < u.length; d++)
        e(u[d]);
    var f = s;
    i.push([359, 11]),
    // n()

    window.wreppack_n = c;
}({
    "58": function (t, n, r) {
        var e;
        e = () => ({
            "cond"() {
                const t = r(342)
                    , {"utf8": n} = r(148)
                    , e = r(343)
                    , {"bin": o} = r(148);
                return {
                    "crypt": t,
                    "utf8": n,
                    "isBuffer": e,
                    "bin": o
                }
            },
            "md5"(t, n) {
                t.constructor == String ? t = n && "binary" === n.encoding ? this.cond().bin.stringToBytes(t) : this.cond().utf8.stringToBytes(t) : this.cond().isBuffer(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
                const r = this.cond().crypt.bytesToWords(t)
                    , e = 8 * t.length;
                let o = 1732584193
                    , i = -271733879
                    , u = -1732584194
                    , a = 271733878;
                for (var c = 0; c < r.length; c++)
                    r[c] = 16711935 & (r[c] << 8 | r[c] >>> 24) | 4278255360 & (r[c] << 24 | r[c] >>> 8);
                r[e >>> 5] |= 128 << e % 32,
                    r[14 + (e + 64 >>> 9 << 4)] = e;
                const f = this._ff
                    , s = this._gg
                    , l = this._hh
                    , h = this._ii;
                for (c = 0; c < r.length; c += 16) {
                    const t = o
                        , n = i
                        , e = u
                        , p = a;
                    o = f(o, i, u, a, r[c + 0], 7, -680876936),
                        a = f(a, o, i, u, r[c + 1], 12, -389564586),
                        u = f(u, a, o, i, r[c + 2], 17, 606105819),
                        i = f(i, u, a, o, r[c + 3], 22, -1044525330),
                        o = f(o, i, u, a, r[c + 4], 7, -176418897),
                        a = f(a, o, i, u, r[c + 5], 12, 1200080426),
                        u = f(u, a, o, i, r[c + 6], 17, -1473231341),
                        i = f(i, u, a, o, r[c + 7], 22, -45705983),
                        o = f(o, i, u, a, r[c + 8], 7, 1770035416),
                        a = f(a, o, i, u, r[c + 9], 12, -1958414417),
                        u = f(u, a, o, i, r[c + 10], 17, -42063),
                        i = f(i, u, a, o, r[c + 11], 22, -1990404162),
                        o = f(o, i, u, a, r[c + 12], 7, 1804603682),
                        a = f(a, o, i, u, r[c + 13], 12, -40341101),
                        u = f(u, a, o, i, r[c + 14], 17, -1502002290),
                        i = f(i, u, a, o, r[c + 15], 22, 1236535329),
                        o = s(o, i, u, a, r[c + 1], 5, -165796510),
                        a = s(a, o, i, u, r[c + 6], 9, -1069501632),
                        u = s(u, a, o, i, r[c + 11], 14, 643717713),
                        i = s(i, u, a, o, r[c + 0], 20, -373897302),
                        o = s(o, i, u, a, r[c + 5], 5, -701558691),
                        a = s(a, o, i, u, r[c + 10], 9, 38016083),
                        u = s(u, a, o, i, r[c + 15], 14, -660478335),
                        i = s(i, u, a, o, r[c + 4], 20, -405537848),
                        o = s(o, i, u, a, r[c + 9], 5, 568446438),
                        a = s(a, o, i, u, r[c + 14], 9, -1019803690),
                        u = s(u, a, o, i, r[c + 3], 14, -187363961),
                        i = s(i, u, a, o, r[c + 8], 20, 1163531501),
                        o = s(o, i, u, a, r[c + 13], 5, -1444681467),
                        a = s(a, o, i, u, r[c + 2], 9, -51403784),
                        u = s(u, a, o, i, r[c + 7], 14, 1735328473),
                        i = s(i, u, a, o, r[c + 12], 20, -1926607734),
                        o = l(o, i, u, a, r[c + 5], 4, -378558),
                        a = l(a, o, i, u, r[c + 8], 11, -2022574463),
                        u = l(u, a, o, i, r[c + 11], 16, 1839030562),
                        i = l(i, u, a, o, r[c + 14], 23, -35309556),
                        o = l(o, i, u, a, r[c + 1], 4, -1530992060),
                        a = l(a, o, i, u, r[c + 4], 11, 1272893353),
                        u = l(u, a, o, i, r[c + 7], 16, -155497632),
                        i = l(i, u, a, o, r[c + 10], 23, -1094730640),
                        o = l(o, i, u, a, r[c + 13], 4, 681279174),
                        a = l(a, o, i, u, r[c + 0], 11, -358537222),
                        u = l(u, a, o, i, r[c + 3], 16, -722521979),
                        i = l(i, u, a, o, r[c + 6], 23, 76029189),
                        o = l(o, i, u, a, r[c + 9], 4, -640364487),
                        a = l(a, o, i, u, r[c + 12], 11, -421815835),
                        u = l(u, a, o, i, r[c + 15], 16, 530742520),
                        i = l(i, u, a, o, r[c + 2], 23, -995338651),
                        o = h(o, i, u, a, r[c + 0], 6, -198630844),
                        a = h(a, o, i, u, r[c + 7], 10, 1126891415),
                        u = h(u, a, o, i, r[c + 14], 15, -1416354905),
                        i = h(i, u, a, o, r[c + 5], 21, -57434055),
                        o = h(o, i, u, a, r[c + 12], 6, 1700485571),
                        a = h(a, o, i, u, r[c + 3], 10, -1894986606),
                        u = h(u, a, o, i, r[c + 10], 15, -1051523),
                        i = h(i, u, a, o, r[c + 1], 21, -2054922799),
                        o = h(o, i, u, a, r[c + 8], 6, 1873313359),
                        a = h(a, o, i, u, r[c + 15], 10, -30611744),
                        u = h(u, a, o, i, r[c + 6], 15, -1560198380),
                        i = h(i, u, a, o, r[c + 13], 21, 1309151649),
                        o = h(o, i, u, a, r[c + 4], 6, -145523070),
                        a = h(a, o, i, u, r[c + 11], 10, -1120210379),
                        u = h(u, a, o, i, r[c + 2], 15, 718787259),
                        i = h(i, u, a, o, r[c + 9], 21, -343485551),
                        o = o + t >>> 0,
                        i = i + n >>> 0,
                        u = u + e >>> 0,
                        a = a + p >>> 0
                }
                return this.cond().crypt.endian([o, i, u, a])
            },
            "_ff"(t, n, r, e, o, i, u) {
                const a = t + (n & r | ~n & e) + (o >>> 0) + u;
                return (a << i | a >>> 32 - i) + n
            },
            "_gg"(t, n, r, e, o, i, u) {
                const a = t + (n & e | r & ~e) + (o >>> 0) + u;
                return (a << i | a >>> 32 - i) + n
            },
            "_hh"(t, n, r, e, o, i, u) {
                const a = t + (n ^ r ^ e) + (o >>> 0) + u;
                return (a << i | a >>> 32 - i) + n
            },
            "_ii"(t, n, r, e, o, i, u) {
                const a = t + (r ^ (n | ~e)) + (o >>> 0) + u;
                return (a << i | a >>> 32 - i) + n
            },
            "_blocksize": 16,
            "_digestsize": 16,
            "cal"(t, n) {
                if (null == t)
                    throw new Error(`Illegal argument ${t}`);
                const r = this.cond().crypt.wordsToBytes(this.md5(t, n));
                return n && n.asBytes ? r : n && n.asString ? this.cond().bin.bytesToString(r) : this.cond().crypt.bytesToHex(r)
            }
        }),
            t.exports = e()
    },
    "343": function(t, n) {
        function r(t) {
            return !!t.constructor && "function" == typeof t.constructor.isBuffer && t.constructor.isBuffer(t)
        }
        /* !
     * Determine if an object is a Buffer
     *
     * @author   Feross Aboukhadijeh <https://feross.org>
     * @license  MIT
     */
        t.exports = function(t) {
            return null != t && (r(t) || function(t) {
                return "function" == typeof t.readFloatLE && "function" == typeof t.slice && r(t.slice(0, 0))
            }(t) || !!t._isBuffer)
        }
    },
    "148": function (t, n) {
        var r = {
            "utf8": {
                "stringToBytes": t => r.bin.stringToBytes(unescape(encodeURIComponent(t))),
                "bytesToString": t => decodeURIComponent(escape(r.bin.bytesToString(t)))
            },
            "bin": {
                "stringToBytes"(t) {
                    for (var n = [], r = 0; r < t.length; r++)
                        n.push(255 & t.charCodeAt(r));
                    return n
                },
                "bytesToString"(t) {
                    for (var n = [], r = 0; r < t.length; r++)
                        n.push(String.fromCharCode(t[r]));
                    return n.join("")
                }
            }
        };
        t.exports = r
    },
    "342": function (t, n) {
        !function () {
            const n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
            var r = {
                "rotl": (t, n) => t << n | t >>> 32 - n,
                "rotr": (t, n) => t << 32 - n | t >>> n,
                "endian"(t) {
                    if (t.constructor == Number)
                        return 16711935 & r.rotl(t, 8) | 4278255360 & r.rotl(t, 24);
                    for (let n = 0; n < t.length; n++)
                        t[n] = r.endian(t[n]);
                    return t
                },
                "randomBytes"(t) {
                    for (var n = []; t > 0; t--)
                        n.push(Math.floor(256 * Math.random()));
                    return n
                },
                "bytesToWords"(t) {
                    for (var n = [], r = 0, e = 0; r < t.length; r++,
                        e += 8)
                        n[e >>> 5] |= t[r] << 24 - e % 32;
                    return n
                },
                "wordsToBytes"(t) {
                    for (var n = [], r = 0; r < 32 * t.length; r += 8)
                        n.push(t[r >>> 5] >>> 24 - r % 32 & 255);
                    return n
                },
                "bytesToHex"(t) {
                    for (var n = [], r = 0; r < t.length; r++)
                        n.push((t[r] >>> 4).toString(16)),
                            n.push((15 & t[r]).toString(16));
                    return n.join("")
                },
                "hexToBytes"(t) {
                    for (var n = [], r = 0; r < t.length; r += 2)
                        n.push(parseInt(t.substr(r, 2), 16));
                    return n
                },
                "bytesToBase64"(t) {
                    for (var r = [], e = 0; e < t.length; e += 3) {
                        const o = t[e] << 16 | t[e + 1] << 8 | t[e + 2];
                        for (let i = 0; i < 4; i++)
                            8 * e + 6 * i <= 8 * t.length ? r.push(n.charAt(o >>> 6 * (3 - i) & 63)) : r.push("=")
                    }
                    return r.join("")
                },
                "base64ToBytes"(t) {
                    t = t.replace(/[^A-Z0-9+\/]/gi, "");
                    for (var r = [], e = 0, o = 0; e < t.length; o = ++e % 4)
                        0 != o && r.push((n.indexOf(t.charAt(e - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | n.indexOf(t.charAt(e)) >>> 6 - 2 * o);
                    return r
                }
            };
            t.exports = r
        }()
    }
});

function get_s(data) {
    var K = window.wreppack_n(58);
    return window.wreppack_n.n(K).a.cal(data)
}

console.log(get_s("autozh-CHS明天109984457"))
