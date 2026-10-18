const JSCrypt = require('crypto-js')

function getResCode() {
    var _0x228ea1 = JSCrypt["AES"]["encrypt"](JSCrypt["enc"]['Utf8']['parse'](Math['floor'](new Date()['getTime']() / 1000)), JSCrypt["enc"]['Utf8']['parse']('1234567887654321' || '1234567887654321'), {
            'iv': JSCrypt["enc"]['Utf8']['parse']('1234567887654321'),
            'mode': JSCrypt['mode']['CBC'],
            'padding': JSCrypt['pad']['Pkcs7']
        });
    return JSCrypt["enc"]['Base64']['stringify'](_0x228ea1['ciphertext']);
}

console.log(getResCode());