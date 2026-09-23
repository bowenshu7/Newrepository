//安装crypto-js库
const Crypto = require('crypto-js')


// 导入数据处理方法
function signMethods() {
    try {
        const signKey = "4a3688a5gcd88g443fga6b7fcb";
        const secretKey = "fcb8f0ddg5c92g45b7g9d33g04cc55d3be3b";
        if (signKey && secretKey) {
            const timeStamp = Math.floor(Date.now() / 1e3);
            const signingString = `${signKey}
${secretKey}
${timeStamp}`;
            const signature = Crypto.HmacSHA256(signingString, secretKey).toString();
            return {
                "X-HMAC-SIGNATURE": signature,
                "X-HMAC-TIMESTAMP": timeStamp,
                "X-HMAC-SIGNKEY": signKey
            };
        }
        return null;
    } catch (error) {
        console.log("error: ", error);
        throw error;
    }
}

console.log(signMethods());