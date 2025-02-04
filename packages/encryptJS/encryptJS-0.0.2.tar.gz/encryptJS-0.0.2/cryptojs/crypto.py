import os
import subprocess
import  execjs
import hmac
import hashlib
from gmssl import sm3, func


class CryptoJS:
    def __init__(self,is_install=True):
        if not is_install:
            try:
                # 尝试执行 node --version 命令
                result = subprocess.run(['node', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)
                # 如果返回码为 0，表示命令执行成功
                if result.returncode == 0:
                    os.system("npm install crypto-js --registry=https://registry.npmmirror.com")
                    os.system('npm install sm-crypto --registry=https://registry.npmmirror.com')
                else:
                    print(f"执行命令时出错: {result.stderr.strip()}")
            except FileNotFoundError:
                print("未找到 node 命令，Node.js 可能未安装。")
    #工具类描述
    def desc(self):
        print("一个简易工具提供常见加密解密功能如MD5,AES,SHA1等,使用该工具前请确保已安装node-js")
    #检测nodejs版本
    def nodejs_version(self):
        os.system('node --version')
    #MD5加密
    def md5(self, data):
        js_code='''
        const CryptoJS = require("crypto-js");
        function MD5(value){
          return {
                             base64: CryptoJS.MD5(value).toString(CryptoJS.enc.Base64),
                             hex: CryptoJS.MD5(value).toString(CryptoJS.enc.Hex)
                             };
        }
        '''
        ctx = execjs.compile(js_code)
        return ctx.call('MD5', data)
    #SHA1加密
    def sha1(self, data):
        js_code='''
        const CryptoJS = require("crypto-js");
        function SHA1(value){
          return {
                             base64: CryptoJS.SHA1(value).toString(CryptoJS.enc.Base64),
                             hex: CryptoJS.SHA1(value).toString(CryptoJS.enc.Hex)
                             };
        }
        '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA1', data)
    #SHA256加密
    def sha256(self, data):
        js_code = '''
                const CryptoJS = require("crypto-js");
                function SHA256(value){
                  return {
                             base64: CryptoJS.SHA256(value).toString(CryptoJS.enc.Base64),
                             hex: CryptoJS.SHA256(value).toString(CryptoJS.enc.Hex)
                             };
                }
                '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA256', data)
    #SHA512加密
    def sha512(self, data):
        js_code = '''
                const CryptoJS = require("crypto-js");
                function SHA512(value){
                  return {
                             base64: CryptoJS.SHA512(value).toString(CryptoJS.enc.Base64),
                             hex: CryptoJS.SHA512(value).toString(CryptoJS.enc.Hex)
                             };
                }
                '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA512', data)
    #SHA384加密
    def sha384(self, data):
        js_code = '''
                  const CryptoJS = require("crypto-js");
                  function SHA384(value){
                          return  {
                             base64: CryptoJS.SHA384(value).toString(CryptoJS.enc.Base64),
                             hex: CryptoJS.SHA384(value).toString(CryptoJS.enc.Hex)
                             };
                  }
                  '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA384', data)
    #SHA224加密
    def sha224(self, data):
        js_code = '''
                     const CryptoJS = require("crypto-js");
                     function SHA224(value){
                             return {
                             base64: CryptoJS.SHA224(value).toString(CryptoJS.enc.Base64),
                             hex: CryptoJS.SHA224(value).toString(CryptoJS.enc.Hex)
                             };
                     }
                     '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA224', data)
    #SHA3-224加密
    def sha3_224(self, data):
        js_code = '''
                             const CryptoJS = require("crypto-js");
                             function SHA3_224(value){
                                     return {
                                     base64: CryptoJS.SHA3(value, { outputLength: 224 }).toString(CryptoJS.enc.Base64),
                                     hex:CryptoJS.SHA3(value, { outputLength: 224 }).toString(CryptoJS.enc.Hex)
                                     };
                             }
                             '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA3_224', data)
    #SHA3-256加密
    def sha3_256(self, data):
        js_code = '''
                             const CryptoJS = require("crypto-js");
                             function SHA3_256(value){
                                     return {
                                     base64: CryptoJS.SHA3(value, { outputLength: 256 }).toString(CryptoJS.enc.Base64),
                                     hex:CryptoJS.SHA3(value, { outputLength: 256 }).toString(CryptoJS.enc.Hex)
                                     };
                             }
                             '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA3_256', data)
    #SHA3-384加密
    def sha3_384(self, data):
        js_code = '''
                             const CryptoJS = require("crypto-js");
                             function SHA3_384(value){
                                     return {
                                     base64: CryptoJS.SHA3(value, { outputLength: 384 }).toString(CryptoJS.enc.Base64),
                                     hex:CryptoJS.SHA3(value, { outputLength: 384 }).toString(CryptoJS.enc.Hex)
                                     };
                             }
                             '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA3_384', data)
    #SHA3-512加密
    def sha3_512(self, data):
        js_code = '''
                             const CryptoJS = require("crypto-js");
                             function SHA3_512(value){
                                     return {
                                     base64: CryptoJS.SHA3(value, { outputLength: 512 }).toString(CryptoJS.enc.Base64),
                                     hex:CryptoJS.SHA3(value, { outputLength: 512 }).toString(CryptoJS.enc.Hex)
                                     };
                             }
                             '''
        ctx = execjs.compile(js_code)
        return ctx.call('SHA3_512', data)
    #BASE64加密
    def encryptBase64(self, data):
        js_code = '''
                  const CryptoJS = require('crypto-js');
                  function encrypt(value){
                       const wordArray = CryptoJS.enc.Utf8.parse(value);
                       const base64Encoded = wordArray.toString(CryptoJS.enc.Base64);
                       return base64Encoded;
                  }
                  '''
        ctx = execjs.compile(js_code)
        return ctx.call('encrypt', data)

    #BASE64解密
    def decryptBase64(self, data):
        js_code = '''
                  const CryptoJS = require('crypto-js');
                  function decrypt(value){
                    const wordArray = CryptoJS.enc.Base64.parse(value);
                    const originalString = wordArray.toString(CryptoJS.enc.Utf8);
                    return originalString;

                  }
                  '''
        ctx = execjs.compile(js_code)
        return ctx.call('decrypt', data)

    #ripemd160加密
    def ripemd160(self, data):
        ripemd160 = hashlib.new('ripemd160')
        # 更新哈希对象的内容
        ripemd160.update(data.encode('utf8'))
        # 获取哈希值（以十六进制字符串形式）
        hash_hex = ripemd160.hexdigest()
        return hash_hex

    #hmac加密
    def hMAC(self, data, key,hmac_type='md5'):
        if hmac_type.lower() == 'sha1':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha1)
        elif hmac_type.lower() == 'sha224':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha224)
        elif hmac_type.lower() == 'sha256':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha256)
        elif hmac_type.lower() == 'sha512':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha512)
        elif hmac_type.lower() == 'md5':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.md5)
        elif hmac_type.lower() == 'sha384':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha384)
        elif hmac_type.lower() == 'sha3_224':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha3_224)
        elif hmac_type.lower() == 'sha3_256':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha3_256)
        elif hmac_type.lower() == 'sha3_384':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha3_384)
        elif hmac_type.lower() == 'sha3_512':
            hmac_obj = hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha3_512)
        else:
            raise ValueError("Unsupported HMAC type: {}".format(hmac_type))
        hmac_digest = hmac_obj.hexdigest()
        return hmac_digest

    #AES加密
    def AES_encrypt(self, data, keystr, ivstr='',mod='ecb',pad='pkcs7'):
        js_code='''
         const CryptoJS = require('crypto-js');
         function encrypt(value,keystr,ivstr,mod,pad){
            const key = CryptoJS.enc.Utf8.parse(keystr);
            const ivs = CryptoJS.enc.Utf8.parse(ivstr);
            switch (mod){
                case 'cbc':
                    mod=CryptoJS.mode.CBC;break;
                case 'cfb':
                    mod=CryptoJS.mode.CFB;break;
                case 'ctr':
                    mod=CryptoJS.mode.CTR;break;
                case 'ofb':
                    mod=CryptoJS.mode.OFB;break;
                case 'ecb':
                    mod=CryptoJS.mode.ECB;break;
                default:
                    mod=CryptoJS.mode.ECB;break;
            }
            switch (pad){
                case 'pkcs7':
                    pad=CryptoJS.pad.Pkcs7;break;
                case 'ansix923':
                    pad=CryptoJS.pad.AnsiX923;break;
                case 'iso10126':
                    pad=CryptoJS.pad.Iso10126;break;
                case 'iso97971':
                    pad=CryptoJS.pad.Iso97971;break;
                case 'zeropadding':
                    pad=CryptoJS.pad.ZeroPadding;break;
                default:
                    pad=CryptoJS.pad.Pkcs7;break;
            }
            const encrypted = CryptoJS.AES.encrypt(value, key, {
               'iv': ivs,
               'mode': mod,
               'padding': pad
            });
            return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
         }
        '''
        ctx= execjs.compile(js_code)
        return ctx.call('encrypt',data,keystr,ivstr,mod,pad)
    #AES解密
    def AES_decrypt(self,  data, keystr, ivstr='',mod='ecb',pad='pkcs7'):
        js_code = '''
                 const CryptoJS = require('crypto-js');
function decrypt(value,keystr,ivstr,mod,pad){
                    const key = CryptoJS.enc.Utf8.parse(keystr);
                    const ivs = CryptoJS.enc.Utf8.parse(ivstr);
                    switch (mod){
                        case 'cbc':
                            mod=CryptoJS.mode.CBC;break;
                        case 'cfb':
                            mod=CryptoJS.mode.CFB;break;
                        case 'ctr':
                            mod=CryptoJS.mode.CTR;break;
                        case 'ofb':
                            mod=CryptoJS.mode.OFB;break;
                        case 'ecb':
                            mod=CryptoJS.mode.ECB;break;
                        default:
                            mod=CryptoJS.mode.ECB;break;
                    }
                    switch (pad){
                        case 'pkcs7':
                            pad=CryptoJS.pad.Pkcs7;break;
                        case 'ansix923':
                            pad=CryptoJS.pad.AnsiX923;break;
                        case 'iso10126':
                            pad=CryptoJS.pad.Iso10126;break;
                        case 'iso97971':
                            pad=CryptoJS.pad.Iso97971;break;
                        case 'zeropadding':
                            pad=CryptoJS.pad.ZeroPadding;break;
                        default:
                            pad=CryptoJS.pad.Pkcs7;break;
                    }
                    const decrypted = CryptoJS.AES.decrypt({ciphertext: CryptoJS.enc.Base64.parse(value)}, key, {
                                              'iv': ivs,
                                              'mode': mod,
                                              'padding': pad
                                              })
                    return decrypted.toString(CryptoJS.enc.Utf8);
}
                '''
        ctx = execjs.compile(js_code)
        return ctx.call('decrypt', data, keystr, ivstr, mod, pad)




