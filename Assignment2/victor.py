from itertools import permutations
text = 'MQWIDQWNSGYLKQYGRNTMARIEMRATGRZAIHXUTYYMMRIAGKQTUZCEBHBEIGVYCDXNWCULIOYGMAYGKWDMNRDNTVMVWIKFYIAXIZLAWZEAGKTKCPOVQGEDUNFUTYYMSGDUGSRNKGRNZWRNSYKRWZRCTAVYTNWTTNFUTYYMCEIRRILMFNYMYGKTGINRRDYZRKAZTCFHWUEXODATEIYGRNLMFNYMIZOQCEBPVOKWYGMAATATDLOXRIMDZAFHQYRCLAZAYGTSODZRAQZACKCBLAAMVSAZYGKWDMNRDNTVLMFNYMBYWLEXZMRDTDKFLMFNYMGKQTUZRIWYDQTEGYYBRTCUTYYMMRUQYVWIGHGZCDEMTAGKPYIZQYRCWNCPDOMWLICPIZEXYGMZYGKGQDAREDUNQUTATWKRWZKBDKYGCTLMFNYMPYGIWZNDTYYMMRCBLAZAYGTSYLICGLUNGUYCBORCWKYGCTLHMZGUVSNGIWTBTDCMTYYMSGDIKGITTLKRUBRNCEDOIHGUEXTNNBEDUOMAGUVYFETCHKOBLAMGYGNWQDYFGINRZMMERTZDSHTVZIIUQDRIVMKBRNRTWYGKTSRNNWQDYGRNRQUNLAMGYGRNIGRNNWIGRNPYYHKWMRCQIGRNQNLDMGAENGKWLMFNYMMRIAGKQMEAGKEAGKTSRKMGYGNTAZRIUWYMDORCOVKRVYTNYGNIYLEMKAGRDMTNLAAMMEMPMZYGKTQYAITVRXOAGKZAQAWUIRLMFNYMKRQDODTWOIRGZAYZLMFNYMMRCBLAZAYGOTGZKRUBRNRQHUIWMRIBTAYLYWTYRGNRQALAYWGKMVWNNRAQGLNIIWTAGKFUQDNIZAFITYYMHDYGRNNWYHRILAWTMYKRWZKBCKBEMUTYYMGKQYDCLMFNYMMRCDWTQYILUNOAGUEXDTFCTALMFNYMVMNAOYYLYGUWMZUOBOCEWICUTYYMMRCDWCHKYLICULAMPYIZCETWVYDUYLICRTMITYYMYGKWAETQDTYFYIXNWNIQTWGSYLICLMTNYLMITYYMMRIABYWGYLICVHTLIOGKHKOBZTXFSKRTCBLAAIAZTAKSQYQTATCMIWBYMGYGUWQTWYKDNITYYMVYHKZTZCMKALIRAQRCGIEMMZRTWTEXGKDRNRQALAMGWICPCOKWTYIWGUEXQRYLAOYLKQZIQMRCYGNIYLEMKAOTLUMYNWZAFMTYYMQYDCYGKWDMNRDNTVLMFNYMSGRKHKKGQAWCECHKRIGKDACEKRDATAVYHKIWVOUBCTODDOPAIYRYKFYQLMFNYMMRUBTVBEMOZWRNOAGUEXQTWYGKNRLMFNYMMRUBTVYGNIMUOVKRBYCUQDEDRIGKEATAGUVFIKRNDORCMVVLLAMGYGKWDMNRDNTVIDWYRKRIDMNRSCCPUOLMFNYMMRUQTDCUTYYMDUMRZMYIRCRNWYMRIQKSOTYHPYLIIQUWGYVORTWZYGUWGRYDWTSCIUYLEMKAMRIBAPMDEYTAGKADMUTYYMBEMOZOMDKTYLDMCPUZMRQYQUTAYGMAUWGRDMYHKTYLBYWZZMRDTDKFMRVQRNRIYGIEDEICTAZMYMMGWIKBTVADRTKAMRIBDQOTDKPYTNQYNRLMFNYMGIGZVZIZMVVCKWBYRCPDMPALVTLIADMAGKZDLWIWGKNRYGMRCEMROTYGRNLMCKAEMUTYYMGRTWZWRNVYGRYDWTSCICTAYGRNITFKVZDOINIDZRPYTNLAMGYGKWDMNRDNTVWUBPRILAATXMYLKQITDMCNZMYIRCRNWYMRCDMITYYMGKQYDCLAWTSMYLKBRTUQGINRWYCSWNIQTWKHAETQLMFNYMIDZRTCKRLMFNYMOTISYLICBZAPQRUOODCPIDWZCEYGRGRTIYCWLIZOMDKWLMFNYMMRIAGKKZMRQYVQYLICBYWZZMGZVZIZMAODICTATWUWVMEACKMANWAZRYKFYQYGMAOTYKOQRGDQCEQUTAVTEMOTIYZICORTWYAZMUTYYMSGDIIGRTNRNRWYCEBTHURIYGNIGUICLAMGYGKWDMNRDNTVOVYZRIMAGKNBNRBZTMUXSCCPUOLMFNYMMRAQKFGINRCAOUCWKGYQGRRKVYHKAZMGYGMADERTCPUOZKTVZMYGCEEGBYWIWZDATATGYQMZUOYMIRAQAHNWAZKTKWWIDAMOLAWGBYYGOBGZKRCDEMGKVTZDARNWAZIWBYMGWTTNUWODILKZZMFEATTNLAOILUEUUOLMFNYMSGRKYGNWQDTNNAQANTSKRTCUTYYMMZZTWMGKWCKQMGYGCEHWGKCDIQYQATBOCEAYTKQDFUTYYMVYYGMAUGRTDASGMAQTWHTLEXMZLAMGYGRNIGYQMRTAGKNACKUXEUEFTWPHGUFMTYYMMRIAGKWCKQMGYGCEETGKQDIQYQYGNWQDTNKQMOCEXITYYMPYQITOYLIDZRYGYVNGRTKQYGKTQDRKYWAETDBPMITYYMMRVQRNRIYGZTYGRNLAMEZWRNTCRCLMFNYMQYDCYGNWQDTNDATAYGKTQDNGRTKQDLWYYGKWMYNITYYMSGDUGSYQAEIKRKYLBPLAMETVDICOYRIWGKKTKWLMFNYMQYDCYGNWQDTNNB'

separator = "#"*len(text)

pairs_frequencies = [('YG', 56), ('YM', 49), ('GK', 30), ('MR', 29), ('RN', 27), ('TY', 26), ('LM', 24), ('YL', 22), ('LA', 22), ('FN', 22), ('NR', 20), ('TA', 18), ('RT', 17), ('CE', 16), ('KW', 16), ('QD', 15), ('MG', 15), ('TN', 14), ('RI', 14), ('TV', 13), ('QY', 13), ('MA', 12), ('RC', 12), ('NW', 12), ('DM', 11), ('KR', 11), ('WY', 11), ('IC', 11), ('ZA', 10), ('VY', 10), ('WZ', 10), ('BY', 10), ('GU', 10), ('CP', 9), ('AZ', 9), ('EX', 9), ('ZM', 9), ('IW', 9), ('WI', 8), ('SG', 8), ('KQ', 8), ('AT', 8), ('WT', 8), ('KT', 8), ('RK', 8), ('PY', 8), ('MZ', 8), ('TW', 8), ('UO', 8), ('HK', 8), ('UW', 8), ('NI', 8), ('OT', 8), ('YQ', 8), ('GR', 7), ('CD', 7), ('IZ', 7), ('GI', 7), ('OD', 7), ('EM', 7), ('QT', 6), ('IG', 6), ('DN', 6), ('KF', 6), ('DO', 6), ('AE', 6), ('IQ', 6), ('DA', 6), ('WN', 5), ('IA', 5), ('WC', 5), ('EA', 5), ('UN', 5), ('KG', 5), ('AQ', 5), ('CK', 5), ('TD', 5), ('CU', 5), ('GZ', 5), ('KB', 5), ('UB', 5), ('QA', 5), ('MU', 5), ('DC', 5), ('ID', 5), ('DQ', 4), ('BE', 4), ('MV', 4), ('YI', 4), ('OV', 4), ('ED', 4), ('FU', 4), ('DU', 4), ('ZW', 4), ('IR', 4), ('TC', 4), ('BP', 4), ('MD', 4), ('TS', 4), ('ZR', 4), ('CB', 4), ('LI', 4), ('NG', 4), ('ME', 4), ('YH', 4), ('KA', 4), ('RG', 4), ('MI', 4), ('ZT', 4), ('MO', 4), ('SC', 4), ('AR', 3), ('UZ', 3), ('GS', 3), ('RD', 3), ('YZ', 3), ('WU', 3), ('VO', 3), ('AM', 3), ('UQ', 3), ('QU', 3), ('CT', 3), ('BO', 3), ('DI', 3), ('IT', 3), ('TL', 3), ('NB', 3), ('OB', 3), ('ZD', 3), ('ZI', 3), ('VM', 3), ('OA', 3), ('IB', 3), ('YW', 3), ('MY', 3), ('NA', 3), ('CO', 3), ('IY', 3), ('AD', 3), ('VQ', 3), ('VZ', 3), ('VT', 3), ('TM', 2), ('IE', 2), ('IH', 2), ('XN', 2), ('UL', 2), ('IO', 2), ('TK', 2), ('FH', 2), ('OQ', 2), ('DL', 2), ('VS', 2), ('GY', 2), ('YV', 2), ('DK', 2), ('GL', 2), ('CM', 2), ('FE', 2), ('YF', 2), ('IU', 2), ('RQ', 2), ('QM', 2), ('NT', 2), ('MP', 2), ('AI', 2), ('OI', 2), ('HU', 2), ('IL', 2), ('DT', 2), ('TQ', 2), ('WG', 2), ('SK', 2), ('KS', 2), ('AL', 2), ('QR', 2), ('LU', 2), ('FM', 2), ('RY', 2), ('IK', 2), ('YD', 2), ('AP', 2), ('ZO', 2), ('DE', 2), ('BZ', 2), ('CW', 2), ('KZ', 2), ('UX', 2), ('EU', 2), ('MQ', 1), ('XU', 1), ('BH', 1), ('AX', 1), ('QG', 1), ('SY', 1), ('EI', 1), ('OX', 1), ('WL', 1), ('TE', 1), ('YB', 1), ('GH', 1), ('MW', 1), ('ND', 1), ('YC', 1), ('WK', 1), ('LH', 1), ('TB', 1), ('SH', 1), ('CQ', 1), ('QN', 1), ('LD', 1), ('RX', 1), ('FI', 1), ('HD', 1), ('FC', 1), ('OY', 1), ('VH', 1), ('XF', 1), ('KD', 1), ('ZC', 1), ('MK', 1), ('DR', 1), ('AO', 1), ('EC', 1), ('PA', 1), ('VF', 1), ('VL', 1), ('EY', 1), ('VC', 1), ('PD', 1), ('LW', 1), ('FK', 1), ('IN', 1), ('XM', 1), ('CN', 1), ('SM', 1), ('CS', 1), ('KH', 1), ('IS', 1), ('YK', 1), ('BT', 1), ('CA', 1), ('OU', 1), ('ZK', 1), ('EG', 1), ('TG', 1), ('AH', 1), ('WM', 1), ('HW', 1), ('AY', 1), ('UG', 1), ('WH', 1), ('EF', 1), ('PH', 1), ('ET', 1), ('XI', 1), ('QI', 1), ('TO', 1), ('YR', 1)]
#Found using our OANC n-gram frequency analyser
en_most_frequent = ['th', 'ma', 'in', 'he', 'an', 'co', 're', 'er', 'om', 'es', 'on', 'at', 'ot', 'ti', 'do', 'en', 'st', 'nt', 'ed', 'mx', 'te', 'to', 'nd', 'or', 'ea', 'al', 'it', 'ha', 'se', 'ng', 'ar', 'is', 'et', 'ou', 'si', 'as', 'ec', 'ta', 'of', 'le', 've', 'ri', 'ro', 'ra', 'me', 'li', 'tx', 'ne', 'sa', 'de', 'di', 'ex', 'so', 'io', 'no', 'el', 'lx', 'ic', 'ts', 'la', 'hi', 'ce', 'ca', 'na', 'ly', 'ns', 'nc', 'sc', 'em', 'rt', 'sx', 'ei', 'ac', 'tr', 'ni', 'pr', 'fo', 'us', 'be', 'ho', 'we', 'ge', 'ep', 'ct', 'ch', 'rs', 'pe', 'ur', 'lo', 'da', 'dt', 'ut', 'su', 'il', 'eo', 'ol', 'mo', 'wi', 'wh', 'fi', 'id', 'yo', 'mi', 'ow', 'os', 'wa', 'ew', 'ad', 'sh', 'po', 'ie', 'ef', 'un', 'ft', 'pa', 'sd', 'am', 'im', 'ul', 'fe', 'ai', 'sp', 'ev', 'tc', 'ld', 'ig', 'od', 'ls', 'ia', 'tw', 'ty', 'ci', 'pl', 'tu', 'ab', 'ey', 'iv', 'vi', 'op', 'rc', 'rd', 'ds', 'ke', 'ox', 'ir', 'ry', 'td', 'ga', 'ht', 'gh', 'ap', 'bu', 'mp', 'lt', 'ay', 'fa', 'go', 'ag', 'um', 'bl', 'eb', 'wo', 'if', 'av', 'ye', 'eg', 'bo', 'sw', 'ys', 'fr', 'oc', 'rm', 'cl', 'gr', 'yt', 'du', 'gt', 'cr', 'dx', 'gi', 'ba', 'dc', 'tl', 'ov', 'hu', 'uc', 'yc', 'rn', 'eh', 'ob', 'bi', 'fx', 'cu', 'uh', 'sm', 'rx', 'lu', 'db', 'oi', 'dr', 'tm', 'sf', 'ue', 'mu', 'tb', 'ya', 'by', 'oa', 'lc', 'qu', 'ru', 'ki', 'eu', 'ud', 'va', 'pi', 'ck', 'sl', 'nf', 'ok', 'px', 'ny', 'og', 'au', 'ah', 'yi', 'ua', 'yd', 'up', 'tf', 'iu', 'sb', 'af', 'tp', 'kn', 'pt', 'ug', 'rg', 'dw', 'gu', 'nu', 'sn', 'fu', 'pu', 'ph', 'br', 'mb', 'rp', 'nx', 'rk', 'rl', 'gs', 'cx', 'dm', 'sr', 'hy', 'ak', 'df', 'oh', 'dn', 'hr', 'ik', 'ib', 'dh', 'ms', 'ub', 'ui', 'dp', 'nm', 'nl', 'rv', 'sy', 'ip', 'gn', 'dy', 'fl', 'yp', 'nk', 'nw', 'aw', 'lp', 'ix', 'rf', 'dl', 'lf', 'np', 'tn', 'ek', 'eq', 'my', 'wn', 'nb', 'uk', 'yb', 'gl', 'rb', 'hc', 'iz', 'oe', 'nh', 'yw', 'mt', 'rw', 'ym', 'fc', 'hs', 'gc', 'ax', 'fs', 'lb', 'rh', 'lm', 'hx', 'gd', 'dg', 'ws', 'tg', 'ps', 'nv', 'xp', 'vo', 'yr', 'hw', 'oy', 'ze', 'bs', 'cy', 'sk', 'nr', 'ka', 'yl', 'lr', 'sg', 'lw', 'wt', 'mc', 'yf', 'ks', 'gx', 'yh', 'fp', 'cd', 'hm', 'hd', 'mh', 'md', 'cs', 'fd', 'fm', 'yn', 'hn', 'gf', 'iw', 'kt', 'gm', 'lh', 'lg', 'fy', 'xa', 'fh', 'lv', 'xi', 'hb', 'gw', 'za', 'xt', 'lk', 'gp', 'wr', 'ko', 'pd', 'hp', 'tk', 'gy', 'dv', 'hl', 'pc', 'ih', 'fb', 'ln', 'fw', 'wx', 'yg', 'wy', 'wc', 'uf', 'wd', 'gb', 'yu', 'xc', 'mw', 'kc', 'ae', 'ao', 'fg', 'hf', 'tv', 'mn', 'sv', 'pm', 'xe', 'az', 'fn', 'mr', 'zi', 'mf', 'ml', 'kd', 'cp', 'py', 'uo', 'bt', 'yx', 'ky', 'bd', 'bx', 'sq', 'uy', 'bc', 'wl', 'hg', 'wm', 'uw', 'mg', 'kl', 'kh', 'cm', 'kw', 'cf', 'pb', 'yv', 'iq', 'wp', 'wb', 'dk', 'wu', 'pf', 'km', 'xo', 'ku', 'kf', 'pw', 'wf', 'yk', 'fv', 'aq', 'cb', 'zy', 'bm', 'cg', 'ez', 'kp', 'kb', 'zo', 'bp', 'kr', 'oz', 'cn', 'nz', 'tq', 'ux', 'uv', 'nq', 'vd', 'xd', 'kg', 'yz', 'xu', 'pn', 'cw', 'tz', 'fk', 'xy', 'xh', 'hv', 'vs', 'dq', 'zx', 'pg', 'gv', 'cq', 'rq', 'wg', 'cv', 'hk', 'pk', 'lq', 'oq', 'bv', 'gk', 'vy', 'vc', 'mv', 'xs', 'zl', 'xm', 'bw', 'mk', 'iy', 'xw', 'pv', 'wk', 'qa', 'uz', 'zc', 'bf', 'xf', 'bh', 'yq', 'hq', 'qi', 'vr', 'xr', 'bn', 'kx', 'zs', 'vu', 'xb', 'bg', 'sz', 'xx', 'vt', 'zd', 'qd', 'gq', 'rz', 'wv', 'fq', 'xl', 'dz', 'zu', 'vp', 'zh', 'zm', 'cz', 'lz', 'zt', 'xn', 'kv', 'qc', 'vh', 'vx', 'fz', 'xg', 'xv', 'vb', 'kq', 'qp', 'vw', 'vm', 'zb', 'vl', 'mz', 'zw', 'qt', 'zn', 'qs', 'vn', 'vf', 'hz', 'gz', 'zp', 'vg', 'mq', 'zf', 'pq', 'bk', 'zr', 'xk', 'qw', 'uq', 'wq', 'wz', 'qo', 'qr', 'zg', 'zk', 'zv', 'xq', 'bz', 'qm', 'qf', 'qe', 'qx', 'ql', 'qh', 'qb', 'zq', 'qn', 'qg', 'vk', 'bq', 'kz', 'pz', 'qk', 'qv', 'vq', 'vz', 'xz', 'qy', 'qz']
#["th","he","in","er","an","re","on","at","en","nd","ti","es","or","te","of","ed","is","it","al","ar","st","to","nt","ng","se","ha","as","ou","io","le","ve","co","me","de","hi","ri","ro","ic","ne","ea","ra","ce","li","ch","ll","be","ma","si","om","ur","ca","el","ta","la","ns","di","fo","ho","pe","ec","pr","no","ct","us","ac","ot","il","tr","ly","nc","et","ut","ss","so","rs","un","lo","wa","ge","ie","wh","ee","wi","em","ad","ol","rt","po","we","na","ul","ni","ts","mo","ow","pa","im","mi","ai","sh","ir","su","id","os","iv","ia","am","fi","ci","vi","pl","ig","tu","ev","ld","ry","mp","fe","bl","ab","gh","ty","op","wo","sa","ay","ex","ke","fr","oo","av","ag","if","ap","gr","od","bo","sp","rd","do","uc","bu","ei","ov","by","rm","ep","tt","oc","fa","ef","cu","rn","sc","gi","da","yo","cr","cl","du","ga","qu","ue","ff","ba","ey","ls","va","um","pp","ua","up","lu","go","ht","ru","ug","ds","lt","pi","rc","rr","eg","au","ck","ew","mu","br","bi","pt","ak","pu","ui","rg","ib","tl","ny","ki","rk","ys","ob","mm","fu","ph","og","ms","ye","ud","mb","ip","ub","oi","rl","gu","dr","hr","cc","tw","ft","wn","nu","af","hu","nn","eo","vo","rv","nf","xp","gn","sm","fl","iz","ok","nl","my","gl","aw","ju","oa","eq","sy","sl","ps","jo","lf","nv","je","nk","kn","gs","dy","hy","ze","ks","xt","bs","ik","dd","cy","rp","sk","xi","oe","oy","ws","lv","dl","rf","eu","dg","wr","xa","yi","nm","eb","rb","tm","xc","eh","tc","gy","ja","hn","yp","za","gg","ym","sw","bj","lm","cs","ii","ix","xe","oh","lk","dv","lp","ax","ox","uf","dm","iu","sf","bt","ka","yt","ek","pm","ya","gt","wl","rh","yl","hs","ah","yc","yn","rw","hm","lw","hl","ae","zi","az","lc","py","aj","iq","nj","bb","nh","uo","kl","lr","tn","gm","sn","nr","fy","mn","dw","sb","yr","dn","sq","zo","oj","yd","lb","wt","lg","ko","np","sr","nq","ky","ln","nw","tf","fs","cq","dh","sd","vy","dj","hw","xu","ao","ml","uk","uy","ej","ez","hb","nz","nb","mc","yb","tp","xh","ux","tz","bv","mf","wd","oz","yw","kh","gd","bm","mr","ku","uv","dt","hd","aa","xx","df","db","ji","kr","xo","cm","zz","nx","yg","xy","kg","tb","dc","bd","sg","wy","zy","aq","hf","cd","vu","kw","zu","bn","ih","tg","xv","uz","bc","xf","yz","km","dp","lh","wf","kf","pf","cf","mt","yu","cp","pb","td","zl","sv","hc","mg","pw","gf","pd","pn","pc","rx","tv","ij","wm","uh","wk","wb","bh","oq","kt","rq","kb","cg","vr","cn","pk","uu","yf","wp","cz","kp","dq","wu","fm","wc","md","kd","zh","gw","rz","cb","iw","xl","hp","mw","vs","fc","rj","bp","mh","hh","yh","uj","fg","fd","gb","pg","tk","kk","hq","fn","lz","vl","gp","hz","dk","yk","qi","lx","vd","zs","bw","xq","mv","uw","hg","fb","sj","ww","gk","uq","bg","sz","jr","ql","zt","hk","vc","xm","gc","fw","pz","kc","hv","xw","zw","fp","iy","pv","vt","jp","cv","zb","vp","zr","fh","yv","zg","zm","zv","qs","kv","vn","zn","qa","yx","jn","bf","mk","cw","jm","lq","jh","kj","jc","gz","js","tx","fk","jl","vm","lj","tj","jj","cj","vg","mj","jt","pj","wg","vh","bk","vv","jd","tq","vb","jf","dz","xb","jb","zc","fj","yy","qn","xs","qr","jk","jv","qq","xn","vf","px","zd","qt","zp","qo","dx","hj","gv","jw","qc","jy","gj","qb","pq","jg","bz","mx","qm","mz","qf","wj","zq","xr","zk","cx","fx","fv","bx","vw","vj","mq","qv","zf","qe","yj","gx","kx","xg","qd","xj","sx","vz","vx","wv","yq","bq","gq","vk","zj","xk","qp","hx","fz","qh","qj","jz","vq","kq","xd","qw","jx","qx","kz","wx","fq","xz","zx","jq","qg","qk","qy","qz","wq","wz"] #["th","er","on","an","re","he","in", "ed","nd","ha","at","en","es","of","or","nt","ea","ti","to","it","st","io","le","is","ou","ar","as","de","rt","ve"]
max_combs = 6
all_pot_encrypt_maps = []

additional_mappings = {"YG":"th", "RN":"er",'LM': 'co', 'FN': 'mx', 'YM': 'ma', "MR": 'an'}
# Logic behind populating the `additional_mappings` map:
#   1. YG = th, by comparing ciphertext (CT) and OANC bigram frequencies
#   2. RN = er, by noticing that, in OANC frequencies, 're' and 'er' are pretty common bigrams. Since this would result,
# upon encryption, in ".,"-",." where '.' is some letter ; ',' a different letter, by looking at the most common
# bigrams in the CT, "RN"-"NR" is the most frequent matching that property
#   3. LM = co, by comparing CT and OANC bigrams, as well as comparing 6grams
#   4. FN = mx, YM = ma, knowing 3., and comparing 6 grams evidently results in these mappings
#   5. MR = an, looking at 6 grams, we notice that "FNYMMR" is common in our CT. Knowing 3,4, this results in "mxma.."
#Looking at most OANC 6 grams, we notice the most frequent following that pattern are "mxmaan", and "mxmath".
# Knowing 1., we get MR=an .




if __name__ == '__main__':
    #generate top X potential mappings
    ct_freqs = [a_tuple[0] for a_tuple in pairs_frequencies]
    #update the frequencies to remove any from the "additional" (known) mappings:
    for k,v in additional_mappings.items():
        if k in ct_freqs: ct_freqs.remove(k)
        if k[::-1] in ct_freqs: ct_freqs.remove(k[::-1])
        if v in en_most_frequent: en_most_frequent.remove(v)
        if v[::-1] in en_most_frequent: en_most_frequent.remove(v[::-1])
    truncated_CT_freqs = ct_freqs[0:max_combs]
    truncated_EN_freqs = en_most_frequent[0:max_combs]
    all_permutations = [ i for i in permutations(truncated_CT_freqs)]
    print(all_permutations)
    print(len(all_permutations))
    for perm_tuple in all_permutations:
        map={}
        for i,two_letters in enumerate(perm_tuple):
            map[two_letters] = truncated_EN_freqs[i]
        all_pot_encrypt_maps.append(map)

    print(all_pot_encrypt_maps)
    print(len(all_pot_encrypt_maps))
    with open("out.txt",'w') as f:
         for dict in all_pot_encrypt_maps:
            plaintext = ""
            replaced = 0
            flag = False
            two_in_a_row = 0
            newDict = dict.copy()
            dict.update(additional_mappings)
            for i in range(0,len(text),2):
                alreadyReplaced = False
                for k,v in dict.items():
                    ct = text[i]+text[i+1]
                    if ct == k:
                        plaintext+=v
                        replaced += 1
                        two_in_a_row += 1
                        alreadyReplaced = True
                        break
                    elif ct == k[::-1]:
                        plaintext += v[::-1]
                        replaced += 1
                        two_in_a_row += 1
                        alreadyReplaced = True
                        break
                if(two_in_a_row >= 2) :
                    flag = True
                if not alreadyReplaced:
                    plaintext+=".."
                    two_in_a_row = 0
            tern = " HAVETWO!!!" if flag else " NOPAIR:("
            o = plaintext+'\n'+ "Replaced: " + str(replaced)  + ", using new mapping of "+str(newDict)+", assumed mapping: "+ str(additional_mappings) + " and therefore full mapping: " + str(dict) +tern + separator+'\n'
            #print(o)
            f.write(o)
