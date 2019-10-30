'''
Author: Walker Kroubalkian
Implementation of Affine Cipher Decryption with Frequency Analysis in Python 2.7
'''

import time

cipherText = "LREKMEPQOCPCBOYGYWPPEHFIWPFZYQGDZERGYPWFYWECYOJEQCMYEGFGYPWFCYMJYFGFMFGWPQGDZERGPGFFZEYCIEDBCGPFEHFBEFFERQCPJEEPQRODFEXFWCPOWPEWLYETERCBXGLLEREPFQGDZERFEHFBEFFERYXEDEPXGPSWPGFYDWYGFGWPGPFZEIEYYCSE"
ml = "e"
cl = "e"
# Correct multiplier is 7 and correct shift is 2.

def modInverse(r,m):
    for i in range(1,m):
        if(r*i%m==1):
            return i
    return -1

def affineDecrypt(c,mu,sh):
    c = c.lower()
    s = ""
    v = ord("a")
    w = modInverse(mu, 26)
    for x in c:
        s+=chr(v+((ord(x)-v-sh)*w)%26)
    return s

def gcd(a,b):
    if(a<0 or b<0):
        return gcd(abs(a),abs(b))
    if(min(a,b)==0):
        return max(a,b)
    if(a>b):
        return gcd(b,a%b)
    return gcd(a,b%a)

def affineFreqBrute(c, ml, cl):
    v = ord("a")
    for mu in range(1,26):
        if(gcd(mu,26)==1):
            sh=((ord(cl)-v)-(ord(ml)-v)*mu)%26
            while(sh<0):
                sh+=26
            print "Mu: " + str(mu) + ", Sh: " + str(sh) + ", M: " + affineDecrypt(c, mu, sh)
    exit

start = time.time()
affineFreqBrute(cipherText, ml, cl)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

Mu: 1, Sh: 0, M: lrekmepqocpcboygywppehfiwpfzyqgdzergypwfywecyojeqcmyegfgypwfcymjyfgfmfgwpqgdzergpgffzeyciedbcgpfehfbefferqcpjeepqrodfexfwcpowpewlyetercbxgllerepfqgdzerfehfbefferyxedepxgpswpgfydwygfgwpgpfzeieyycse
Mu: 3, Sh: 18, M: pregyeziqmzmdqcwckzzefnokznlciwvlerwczknckemcqxeimycewnwczknmcyxcnwnynwkziwvlerwzwnnlecmoevdmwznefndennerimzxeezirqvnetnkmzqkzekpcejermdtwpperezniwvlernefndennercteveztwzakzwncvkcwnwkzwznleoeccmae
Mu: 5, Sh: 10, M: vreaqebwgobotgiuisbbepzksbzdiwujderuibsziseoigfewoqieuzuibszoiqfizuzqzusbwujderubuzzdeiokejtoubzepztezzerwobfeebwrgjzenzsobgsbesvieherotnuvverebzwujderzepztezzerinejebnubmsbuzijsiuzusbubzdekeiiome
Mu: 7, Sh: 2, M: frequencyanalysisonnextmonthscipherisnotsoeasybecauseitisnotasubstitutioncipherinitthesameplaintextlettercanbeencryptedtoanyoneofseveraldifferentciphertextlettersdependingonitspositioninthemessage
Mu: 9, Sh: 20, M: zrewceloiylyvimkmgllenhqglhpmokbperkmlghmgeymiteoycmekhkmlghymctmhkhchkglokbperklkhhpemyqebvyklhenhvehheroylteeloribhejhgyliglegzmexeryvjkzzerelhokbperhenhvehhermjebeljkluglkhmbgmkhkglklhpeqemmyue
Mu: 11, Sh: 12, M: hreoaefymsfszmuquiffejxcifxnuyqlnerqufixuiesumveysaueqxqufixsuavuxqxaxqifyqlnerqfqxxneuscelzsqfxejxzexxerysfveefyrmlxebxisfmifeihuederszbqhherefxyqlnerxejxzexxerubelefbqfkifqxuliuqxqifqfxneceuuske
Mu: 15, Sh: 22, M: breuiedkwqdqjwosoaddezlgadlvoksxversodaloaeqownekqioeslsodalqoinolslilsadksxversdsllveoqgexjqsdlezljellerkqdneedkrwxlehlaqdwadeaboeferqjhsbberedlksxverlezljellerohexedhsdyadsloxaoslsadsdlvegeooqye
Mu: 17, Sh: 14, M: jremgexuakxknawywcxxevbscxbtwuyhterywxcbwcekwapeukgweybywxcbkwgpwbybgbycxuyhteryxybbtewksehnkyxbevbnebberukxpeexurahbezbckxacxecjwelerknzyjjerexbuyhterbevbnebberwzehexzyxocxybwhcwybycxyxbtesewwkoe
Mu: 19, Sh: 6, M: dresoevgkivixkqaquvvelpwuvpbqgatberaqvupqueiqkhegioqeapaqvupiqohqpapopauvgatberavappbeqiwetxiavpelpxeppergivheevgrktpefpuivkuveudqenerixfadderevpgatberpelpxepperqfetevfavcuvapqtuqapauvavpbeweqqice
Mu: 21, Sh: 24, M: nreisehmcuhupcaoaqhhetjyqhjfamozferoahqjaqeuacdemusaeojoahqjuasdajojsjoqhmozferohojjfeauyezpuohjetjpejjermuhdeehmrczjevjquhcqheqnaeberupvonnerehjmozferjetjpejjeravezehvohwqhojazqaojoqhohjfeyeaauwe
Mu: 23, Sh: 16, M: treckejaswjwfsgmgyjjedvuyjvxgamnxermgjyvgyewgsleawkgemvmgjyvwgklgvmvkvmyjamnxermjmvvxegwuenfwmjvedvfevverawjleejarsnvepvywjsyjeytgezerwfpmtterejvamnxervedvfevvergpenejpmjiyjmvgnygmvmyjmjvxeueggwie
Mu: 25, Sh: 8, M: xreywetsugtghukckmttebdamtdjkscfjercktmdkmegkuzesgwkecdcktmdgkwzkdcdwdcmtscfjerctcddjekgaefhgctdebdheddersgtzeetsrufdeldmgtumtemxkeperghlcxxeretdscfjerdebdhedderklefetlctqmtcdkfmkcdcmtctdjeaekkgqe
--- 0.000720024108887 seconds ---

for input of cipherText = "OYHYJLEVYQBLSRIJLYEC", mu = 5, sh = 4.
'''