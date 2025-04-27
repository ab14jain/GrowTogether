from typing import Counter


class Solution:
    # def countOfSubstrings(self, word: str, k: int) -> int:

        #Brute Force:
        # TLE - 715 / 768
        # def is_possible(st,k):
        #     n = len(st)
        #     v = [0]*5
        #     c = 0
        #     for i in range(n):
        #         if st[i] == 'a':
        #             v[0] += 1
        #         elif st[i] == 'e':
        #             v[1] += 1
        #         elif st[i] == 'i':
        #             v[2] += 1
        #         elif st[i] == 'o':
        #             v[3] += 1
        #         elif st[i] == 'u':
        #             v[4] += 1
        #         else:
        #             c += 1
            
        #     if c == k and v.count(0) == 0:
        #         return True
        
        #     return False
            


        # n = len(word)
        # sub_str = []
        # total_substr = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if (j-i+1) >= (5 + k):                      
        #             sbstr = word[i:j+1]
        #             sub_str.append(sbstr)                    
        #             if is_possible(sbstr, k):
        #                 total_substr += 1   
        
        # # print(sub_str)
        # return total_substr

    # def isVowel(self, c: str) -> bool:
    #     return c in {'a', 'e', 'i', 'o', 'u'}

    

    def countOfSubstrings(self, word: str, k: int) -> int:

        def findNextConsonant(word: str, next_consonant: list) -> None:
            n = len(word)
            next = n
            for i in range(n - 1, -1, -1):
                next_consonant[i] = next
                if not word[i] in "aeiou":
                    next = i

        n = len(word)
        next_consonant = [0] * n
        findNextConsonant(word, next_consonant)

        count = 0
        consonants = 0
        vowel_freq = {}
        left = 0
        right = 0
        prev = -1

        while right < n:
            if prev != right:
                if word[right] in "aeiou":
                    vowel_freq[word[right]] = vowel_freq.get(word[right], 0) + 1
                else:
                    consonants += 1
                prev = right

            if right >= (5 + k - 1):
                if len(vowel_freq) == 5 and consonants == k:
                    count += next_consonant[right] - right
                
                if (len(vowel_freq) == 5 and consonants == k) or (consonants > k):
                    if word[left] in "aeiou":
                        vowel_freq[word[left]] -= 1
                        if vowel_freq[word[left]] == 0:
                            del vowel_freq[word[left]]
                    else:
                        consonants -= 1
                    left += 1
                else:
                    right += 1
            else:
                right += 1

        return count
            
            
            


s=Solution()
print(s.countOfSubstrings("baiidoadceubddcbuuuoeuedebidododaoobauaociecbbaaedueouoaiiddaeiooobcabbiuudceccaubbobacbuuioabiaubuedicccbuudeuoooeaocobdobdbooccdeoaciucddcoieoiuacudoaaboiaiciabaocaaaccidbuaiciocbecubuaiiaeboiecioidiiiiducacbduouaooduaudibcieoibdcdebdicaeocbouooiuiduucbieaaacaodboucbiduadaceiacecccbaiaoadcoeubeiiaibeecuboacobcubduacbuiaobouceuibouaoibeduuaaueidabcoidbiiueeeiaecbbeuecocacubecdiodeoaoeccuibdboboaeuoduuuebcdedaeaubiuddeeiiaoauuiieociadbcidieuuebbdbcciiccdeubudcbecoieeuiauooibabdoooduibeiacdccidiaebaudaiioeeicdbeeaiaidebbdcbuaidcbadaicoocoaaobbobdeieeiiieicoudieaauebaoedbecdbuocoudaeiibiioedaacidadaiiabddcauueibbduueaocdaoeiaeceoiibucieideaauobbudobecbocueaeiieeiacoadiuudcaoeidoeiddaiiiioeeiebdbdubobcbeouideabbeiuabeuobabedddceooocbudceaeoecbeciuuoocaiiuieodeiuuouidboeuioadoboaiaeaeebbcdbcoaadoadciiioiebicaoodouiuibecuuboeaecedeiubududuoiebdoidbiacadudiiieboeduuuiuuaueuoeeabcaeceucacaaeoaubeuoodiucidoidaaddbuaeeaucaiabeebucedddccuaiaubidoduocoeeiiuoieodudoaddbobeidcauaiobbuiccubcibdiaeoaiocedccooauueducbdbabdeodaaaeoieaicbaeibiuoueiieaebiucdaooiabuobiebaoiecoebouueueuieeiciiioeaiideceueobdcbuocaicoaoibooccoudbceaeucocbidouiddubaodeccoocubicbbaciodeeooiabdeuoiuuaoooiboidoodecdbcdbidbaciueibouuuiaidbdueaudeaeeeeiebceduabceedddedabcaobdaidudceaoabebobcdeiceaccecubiducoiadbdaacebiaididbboedouuuiiiiaoaiduaeaboaiaibbeecoccodbeddueacbioeebdeddaocacbdaaoaciaeaeuboidiebauucoebeaiidibaocieaboeadbdueiuueaduceaduadauaceaiucibadeeuaiedaiodbiuddcbcodaoodcoeiuebdiceucaddouoocodbbacdiceoibdaoeooboboobuibbaeiddbeubecacidcdubciaiibbccaecuubboucibaacceicebaccbaocucucbedcedcadcdeoaeeaiubaoacbobuciibcddeaaeeeouaoccacduiidaeuaebbdioieuabeoiuouieedoeciuoicicuudcuuuecbiibadbicoeeciuedcdibciuoeodbecaaadbcoodaububaoueubeadeddoaocceoaeccuduceoudeioicuauoecuaeccuibeiebooaucoiaabeebuecceeocaeccoaadeabueadccuaubdodbbcibuaiooecuceabecacbdecdcbcbddodcecueudecodieibdcoeaidaodbaaububebacciibdbcbeeaeoedbeudoabedoddooebeucoebaaaeiiuceduuueabduibbeddibocbiiiauocadeddciiceuaoaeiudaacidaaudubdobieuaiuoabacdeiadedubuduuauuaoucaaiobeoedbcbcobeebuuouebeboudiaoaoaccoouacaiibecciuabuuaabiocdcioibuioodbbbbdbboauebiodcaaiduuoubbeouaiddbiieuuueoiiudbciiiedaaeuoouiceboaieucaidaeoboabaacadooabedideddccbicuuaiceedddbcbdeuaadbcuacodibudeaeiebuouidbduucabuacuabbceooceouedeibccacbuedieaiieibubeeuodcdbbddoiudaiaducdidecouoicceeeuuuabbabeodcdiiiouddcddaaucdeoacidcbeibioadadicocbeioeoaibuddoccbidaaebacdebuuucadccdoibuduuuodoueabeuioduucbceccbeouicbbabibaddiaidcaododbadoeeobidicubuoaciaudcebioaciboioboideiucodaiducaceuoiodaiacbadaaddooucoieocococaccucdcoiaoacoeiidbeduueaibouaebcbeabaoeudbdoccecoueaiciiebbidcdudiiobaeuidoeaudoabdubooacbbcoeuouibceiaciiduodiecdcicobicuabuoaaaeidauueoiaooueiecbicoiuuudiiuudiedcdibodeeaiuuuccubcocdieaibicoueeucciaaebdbecuuiibuueooebudubuiiuaaobeoeibuuuodcoeoeoiooacabobuciueeaiodoabuauaddcaicobeouebiadeecoocceauocudeceeddadcauicadbdiuiciaaceecuiuacaeaeiecacdbdbicuuoubucddobeoeaeeubdbobibecedbubduaoeboeoodiiuduaccbdiccouocbdbauccbeobocicuuudcdouabuoucecbuiodaadcabocodaedabdoecdebeaudoiibebbbobodouioeeibicbdoibaudobiuaucacuccodeddideaciuaoaeeouadeaiaiaebdaedaoueidiaboieuebuboeieicociiioaciodbibbueedoacoeiioibiecocddoaeuiuaueaouaibcdciaioiucaaeabeudouduioaoccadbcadeeuueiaaiiuoecdbdcoccooebdecceouedcidcoeducicbabuoucdoibicbueicoduaicaoiicubbudaaaiieiecbdaeddocbaiocddoediubiabaudicciaidbbuebuocaabiodeduubedbciaadduebbbaiuodeduuadaidciobacdibeeauueouaaodbcoideooebcbddducaeeobudducubcdcocibebaacbebceuouiucoceoduobicucuaceuoedidbiedaiiibbcocbaeouadoeduaidaedodudiebdubiaubiddbebidddieedcueeoiuabuacaccoauiddaddiddiadduceaauouioedeabbuadiiiooioebaaedauididciobbdiacicueeoabecbdececaecaaidcioddouaobuuucdaidbaueacduiobadidueiioibdacaeadceucdeacucoocudbcaddoioiciddedebeuuuoddibiabdbicudauddouoccdbcodcibiduibaociiueubaduubdcuebdeubueedciocdccecouuuiooicocdauabdedebadabcdedueccbiuidocouoboeaaibbuiioccebeadobaueudeeaaaodiieieoceoibccboubaubbdubcbduebdabboodeicbebicueiecdaiubeoaoaeeecaaeceaaeddceudadeoadiiboacaecuabbbiiioabuiudociceoaubiieueiodadcbouudeiadeuouabbeeodbeeuaodiacadecbcedbbducdcuiiadueudoadeeeaiodoobobidcuubbouadcebcdidebiudbiuucoodbauacbueodcdceebeddceiuaccddoobabeobaiebdobbcbdiabaaidocudbuucbabcodieacuciecciebcucuddbaoabbobubeabiedbbcbouudciccuobaaebcucaiiibdduaooeboauoibbeudduceidodddaeuuiodbeoubecbiudoebiecdebauuebaacdaaoubiaueoacueuccuoaduboubodiudddadbaeeuauudcbeobuaobacdaeaeeeuuiiubaidociucedboouabcbciiocaoaoacaciboiieaoucieiieiciiocduioeeeeaducaiudcaaicebddccbecaodbbdbidbdebbiidbaddecdudadeudubbboaabdaiabbdeaodacbiuccabcidocedicuicucdeoibedocdoieuaabcauaaeaadcdbcoiedbubdbbecbbcicoiaedbuiaadobucoabocaoauubuuccbeeoeoibcdeddeueieabdcicbccuuocbdudcubbueacuaeiucicoccoeaabubbiiieaeooaboabuuicucudoedbbuuoduibueudiocicicbodcabbdecdabcbduobudbdaedeuucouaeiibcbceioeedocoiuieeobaoiiaoaouebdodoacdodabuabbeiioceauoaoeccouiueideaoubbeuieuucaicaaabeucoacdduiibbbcaoeodcauoabibeabdiabbcieuccdoauediuieedoubueucccboeobioaiiuuaoadaeoioaucbccaudubduuooduoedubbieiecaiiioabboobdoouiabucieeedoedaedebieeioudaeoaidudoibdoicbaboeeebuabuieeobcuddabaoeuadaeobaace", 2504))
print(s.countOfSubstrings("iqeaouqi", 2))
print(s.countOfSubstrings("aeioqq", 1))
print(s.countOfSubstrings("aeiou", 0))
print(s.countOfSubstrings("ieaouqqieaouqq", 1))
