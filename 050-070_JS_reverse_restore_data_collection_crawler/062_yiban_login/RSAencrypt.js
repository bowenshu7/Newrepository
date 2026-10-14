const JSEncrypt = require('node-jsencrypt')


function get_ras_password(pwd) {
    publickey = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCt3eAVJJUIXeoc2wrJCea3j/bt\nLBYHmkry7a7g+jZp8WwQm8mJw0QpJgW2ia5R6sxHvX2RU80BA/sWBdivE9eELjk9\nSsWe+X2zZFmwPgKW+kk1QMDYSjcnyq47tBvbyMy9msAYOGitLVWDrMnfVJQwZ10l\nsGx/KN6Ot8T1sBVMFQIDAQAB\n-----END PUBLIC KEY-----"
    var encrypt = new JSEncrypt()
    encrypt.setPublicKey(publickey)

    return encrypt.encrypt(pwd)
}

pwd = 123456

console.log(get_ras_password(pwd))