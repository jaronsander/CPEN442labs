# This is a sample Python script.
import collections

from contextlib import redirect_stdout

text = 'MQWIDQWNSGYLKQYGRNTMARIEMRATGRZAIHXUTYYMMRIAGKQTUZCEBHBEIGVYCDXNWCULIOYGMAYGKWDMNRDNTVMVWIKFYIAXIZLAWZEAGKTKCPOVQGEDUNFUTYYMSGDUGSRNKGRNZWRNSYKRWZRCTAVYTNWTTNFUTYYMCEIRRILMFNYMYGKTGINRRDYZRKAZTCFHWUEXODATEIYGRNLMFNYMIZOQCEBPVOKWYGMAATATDLOXRIMDZAFHQYRCLAZAYGTSODZRAQZACKCBLAAMVSAZYGKWDMNRDNTVLMFNYMBYWLEXZMRDTDKFLMFNYMGKQTUZRIWYDQTEGYYBRTCUTYYMMRUQYVWIGHGZCDEMTAGKPYIZQYRCWNCPDOMWLICPIZEXYGMZYGKGQDAREDUNQUTATWKRWZKBDKYGCTLMFNYMPYGIWZNDTYYMMRCBLAZAYGTSYLICGLUNGUYCBORCWKYGCTLHMZGUVSNGIWTBTDCMTYYMSGDIKGITTLKRUBRNCEDOIHGUEXTNNBEDUOMAGUVYFETCHKOBLAMGYGNWQDYFGINRZMMERTZDSHTVZIIUQDRIVMKBRNRTWYGKTSRNNWQDYGRNRQUNLAMGYGRNIGRNNWIGRNPYYHKWMRCQIGRNQNLDMGAENGKWLMFNYMMRIAGKQMEAGKEAGKTSRKMGYGNTAZRIUWYMDORCOVKRVYTNYGNIYLEMKAGRDMTNLAAMMEMPMZYGKTQYAITVRXOAGKZAQAWUIRLMFNYMKRQDODTWOIRGZAYZLMFNYMMRCBLAZAYGOTGZKRUBRNRQHUIWMRIBTAYLYWTYRGNRQALAYWGKMVWNNRAQGLNIIWTAGKFUQDNIZAFITYYMHDYGRNNWYHRILAWTMYKRWZKBCKBEMUTYYMGKQYDCLMFNYMMRCDWTQYILUNOAGUEXDTFCTALMFNYMVMNAOYYLYGUWMZUOBOCEWICUTYYMMRCDWCHKYLICULAMPYIZCETWVYDUYLICRTMITYYMYGKWAETQDTYFYIXNWNIQTWGSYLICLMTNYLMITYYMMRIABYWGYLICVHTLIOGKHKOBZTXFSKRTCBLAAIAZTAKSQYQTATCMIWBYMGYGUWQTWYKDNITYYMVYHKZTZCMKALIRAQRCGIEMMZRTWTEXGKDRNRQALAMGWICPCOKWTYIWGUEXQRYLAOYLKQZIQMRCYGNIYLEMKAOTLUMYNWZAFMTYYMQYDCYGKWDMNRDNTVLMFNYMSGRKHKKGQAWCECHKRIGKDACEKRDATAVYHKIWVOUBCTODDOPAIYRYKFYQLMFNYMMRUBTVBEMOZWRNOAGUEXQTWYGKNRLMFNYMMRUBTVYGNIMUOVKRBYCUQDEDRIGKEATAGUVFIKRNDORCMVVLLAMGYGKWDMNRDNTVIDWYRKRIDMNRSCCPUOLMFNYMMRUQTDCUTYYMDUMRZMYIRCRNWYMRIQKSOTYHPYLIIQUWGYVORTWZYGUWGRYDWTSCIUYLEMKAMRIBAPMDEYTAGKADMUTYYMBEMOZOMDKTYLDMCPUZMRQYQUTAYGMAUWGRDMYHKTYLBYWZZMRDTDKFMRVQRNRIYGIEDEICTAZMYMMGWIKBTVADRTKAMRIBDQOTDKPYTNQYNRLMFNYMGIGZVZIZMVVCKWBYRCPDMPALVTLIADMAGKZDLWIWGKNRYGMRCEMROTYGRNLMCKAEMUTYYMGRTWZWRNVYGRYDWTSCICTAYGRNITFKVZDOINIDZRPYTNLAMGYGKWDMNRDNTVWUBPRILAATXMYLKQITDMCNZMYIRCRNWYMRCDMITYYMGKQYDCLAWTSMYLKBRTUQGINRWYCSWNIQTWKHAETQLMFNYMIDZRTCKRLMFNYMOTISYLICBZAPQRUOODCPIDWZCEYGRGRTIYCWLIZOMDKWLMFNYMMRIAGKKZMRQYVQYLICBYWZZMGZVZIZMAODICTATWUWVMEACKMANWAZRYKFYQYGMAOTYKOQRGDQCEQUTAVTEMOTIYZICORTWYAZMUTYYMSGDIIGRTNRNRWYCEBTHURIYGNIGUICLAMGYGKWDMNRDNTVOVYZRIMAGKNBNRBZTMUXSCCPUOLMFNYMMRAQKFGINRCAOUCWKGYQGRRKVYHKAZMGYGMADERTCPUOZKTVZMYGCEEGBYWIWZDATATGYQMZUOYMIRAQAHNWAZKTKWWIDAMOLAWGBYYGOBGZKRCDEMGKVTZDARNWAZIWBYMGWTTNUWODILKZZMFEATTNLAOILUEUUOLMFNYMSGRKYGNWQDTNNAQANTSKRTCUTYYMMZZTWMGKWCKQMGYGCEHWGKCDIQYQATBOCEAYTKQDFUTYYMVYYGMAUGRTDASGMAQTWHTLEXMZLAMGYGRNIGYQMRTAGKNACKUXEUEFTWPHGUFMTYYMMRIAGKWCKQMGYGCEETGKQDIQYQYGNWQDTNKQMOCEXITYYMPYQITOYLIDZRYGYVNGRTKQYGKTQDRKYWAETDBPMITYYMMRVQRNRIYGZTYGRNLAMEZWRNTCRCLMFNYMQYDCYGNWQDTNDATAYGKTQDNGRTKQDLWYYGKWMYNITYYMSGDUGSYQAEIKRKYLBPLAMETVDICOYRIWGKKTKWLMFNYMQYDCYGNWQDTNNB'

separator = "\n"+"#"*15+"\n"
n = 8

common_mapping = ['']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    partials = [text[i:i+n] for i in range(0, len(text), n)]
    freq = {}
    sum = 0
    for i in partials:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
        sum+=1

    sortfreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    normalized = [(t[0], (t[1] / sum) * 100) for t in sortfreq]
    non_tuple = [t[0] for t in sortfreq]
    with open( "frequencies/ct_"+str(n) +"gram_out.txt", "w") as f:
        with redirect_stdout(f):
            print("Sorted, raw:\n")
            print(sortfreq)
            print(separator)
            print("Sorted, normalized:\n")
            print(normalized)
            print(separator)
            print("Sorted, non-tuple:\n")
            print(non_tuple)


