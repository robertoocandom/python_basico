# -*- coding: utf-8 -*-
import random
import time

def run():
    print('------------------------------------------------------------------------')
    print('------------------------¿Quieres jugar un juego?------------------------')
    print('---------------------tendras que adivinar el numero---------------------')
    print('-si no lo logras el dispositivo en el que estas ejecutando este archivo-')
    print('---va a explotar, solo para que no pienses que no tienes oportunidad,---')
    print('----te dejare elegir el numero limite, solo tieness 3 oportunidades-----')
    print('------------------------------------------------------------------------')
    print('-----------------------vivir o morir, tu decides------------------------')
    print('------------------------------------------------------------------------')
    i = 0
    number_found = False
    limit = int(input('Asigna un numero limite:\n'))
    random_number = int(random.random()*limit)
    while (not number_found and i <= 2):
        i += 1
        number = int(input('Intenta adivinar el numero:\n'))
        if (number == random_number):
            print('¡Lo lograste!')
            number_found = True
        elif (number > random_number):
            print('Pista: Es mas pequeño!')
        else:
            print('Pista: Es mas grande!')
    if (number_found == False):
        print('------------------------------------------------------------------------')
        print('----------------Iniciando protocolo de auto destruccion-----------------')
        print('------------------------------------------------------------------------')
        time.sleep(3)
        print('---------------- Self-destruction sequence activated -------------------')
        time.sleep(0.5)
        print('---------------- Remaining time for self destruction: ------------------')
        time.sleep(1)
        print('-------------------------------- T-10 ----------------------------------')
        time.sleep(1)
        print('-------------------------------- T-09 ----------------------------------')
        time.sleep(1)
        print('-------------------------------- T-08 ----------------------------------')
        time.sleep(1)
        print('-------------------------------- T-07 ----------------------------------')
        time.sleep(1)
        print('-------------------------------- T-06 ----------------------------------')
        time.sleep(1)
        print('-------------------------------- T-05 ----------------------------------')
        time.sleep(1)
        print('-------------------------------- T-04 ----------------------------------')
        time.sleep(1)
        print('------------------------------------------------------------------------')
        print('----------------------------- 333333333 --------------------------------')
        print('----------------------------- 333333333 --------------------------------')
        print('-----------------------------       333 --------------------------------')
        print('-----------------------------      333  --------------------------------')
        print('-----------------------------     333   --------------------------------')
        print('-----------------------------    333    --------------------------------')
        print('-----------------------------   333333  --------------------------------')
        print('-----------------------------   3333333 --------------------------------')
        print('-----------------------------        33 --------------------------------')
        print('-----------------------------        33 --------------------------------')
        print('-----------------------------        33 --------------------------------')
        print('----------------------------- 33     33 --------------------------------')
        print('----------------------------- 333333333 --------------------------------')
        print('-----------------------------  3333333  --------------------------------')
        print('------------------------------------------------------------------------')
        time.sleep(0.5)
        print('�??????????????????????????!"#$%&()*+,-./0123456789:;<=>?@ABCD')
        print('EFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹Œ')
        print('Ž‘’“”•–—˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×')
        time.sleep(0.5)
        print('------------------------------------------------------------------------')
        print('-----------------------------  2222222  --------------------------------')
        print('----İıĲĳĴĵĶķĸĹĺĻļĽľ---------- 22ñòóô222 --------------------------------')
        print('----------------------------- ɩɪ     22 --------------------------------')
        print('-----------------------------        22 --------------------------------')
        print('-----------------------------        22 --------------------------------')
        print('-----------------------------       222 ---------ǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯ-----')
        print('-----------------------------      ɑɒɓ  --------------------------------')
        print('-----------------------------     222   --------------------------------')
        print('-----------------------------    222    --------------------------------')
        print('-----------------------------   222     --------------------------------')
        print('-----------------------------  ɑɒɓ      --------------------------------')
        print('----------------------------- 222       --------------------------------')
        print('----------------------------- 222ñòóô22 --------ŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔ---')
        print('----------------------------- 222222222 --------------------------------')
        print('------------------------------------------------------------------------')
        time.sleep(0.5)
        print('ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ')
        print('ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũ')
        print('ŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲ')
        print('ƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻ')
        print('ǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄ')
        print('ɅɆɇɈɉɊɋɌɍɎɏɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍ')
        print('ʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯʰʱʲʳʴʵʶʷʸʹʺʻʼʽʾʿˀˁ˂˃˄˅ˆˇˈˉˊˋˌˍˎˏːˑ˒˓˔˕˖')
        print('˗˘˙˚HUNGRY˛˜˝˞˟ˠˡˢˣˤ˥˦˧˨˩˪˫ˬ˭ˮ˯˰˱˲˳˴˵˶˷˸˹˺˻˼˽˾˿	̀	́	̂	̃	̄	̅	̆	̇	̈	̉	̋')
        print('	̌	̍	̎	̏	̐	̑	̒	̓WAR	̔	̚	̛	̜	̝	̞	́	̂	̃	̟	̠	̡	̢	̣	̤')
        print('	̥	̦	̧	̨	̩	̪	̫	̬	̭	̮	̯	̰	̱	̲	̳	̴	̵	̶	̷	̸	̹	̺	̻	̼	̽')
        print('	̾	̿	̀	́DEATH	͂	̓	̈́	ͅ	͆	͇	͈	͉	͊	͋	͌	͍	͎	͏	͐	͑	͒	͓	͔	͖	͗')
        print('	͘	͙	͚	͛	͜	͝	͞	͟	͠	͡	͢	ͣ	ͤ	ͥ	ͦ	ͧ	ͨ	ͩ	ͪ	ͫ	ͬ	ͭ	ͮ	ͯ	Ͱ')
        print('	ͱ	Ͳ	ͳ	ʹ	͵	IT\'S THE END?Ͷ	ͷ	ͺ	ͻ	ͼ	ͽ	;	Ϳ	΄	΅	Ά	·	Έ	')
        time.sleep(0.5)
        print('ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ')
        print('ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľ   111    ĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŠšŢţŤťŦŧŨũ')
        print('ŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇ  1111    ƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƜƝƞƤƥƦƧƨƩƪƫƬƭƮƯưƱƲ')
        print('ƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐ    11    ǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǤǥǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻ')
        print('ǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘș    11    ȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȰȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄ')
        print('ɅɆɇɈɉɊɋɌɍɎɏɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢ    11    ɣɤɥɦɧɨɩɪɫɬɭɮɯɴɵɶɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍ')
        print('ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõ    11    ö÷øùüýþÿĀăĄćĈĊċČĐđĒēĔĕĖėĘęĚěĜĝĞğĠ')
        print('ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľ    11    ĿŀŁŃńņŇŊŋŌōŐŒœŔŕřŚśŜŝŞşŠšŢţŤťŦŧŨũ')
        print('ŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇ    11    ƈƉƊƋƌƍƎƑƒƓƔƕƖƘƜƝƞƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲ')
        print('ƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐ    11    ǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǥǦǧǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻ')
        print('ǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘș    11    ȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȰȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄ')
        print('ɅɆɇɈɉɊɋɌɍɎɏɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢ    11    ɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɹɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍ')
        print('ƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐ    11     ǑǒǓǔǕǖǗǘǙǚǛǜǝǞǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻ')
        print('ǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘș  111111  ȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȰȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄ')
        print('ɅɆɇɈɉɊɋɌɍɎɏɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢ  111111  ɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɶɷɸɹʀʁʂʃʄʅʆʇʈʉʊʋʌʍ')
        print('ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ')
        time.sleep(1)
        print('------------------------------------------------------------------------')
        print('-------------------------------- ... -----------------------------------')
        print('------------------------------------------------------------------------')
        time.sleep(1)
        print('--------------------- Self-destruction sequence... ---------------------')
        print('------------------------------------------------------------------------')
        time.sleep(1)
        print('----------------------------- COMPLETE ---------------------------------')
        print('------------------------------------------------------------------------')
        time.sleep(2)
        print('------------------------ Gracias por jugar :D --------------------------')
        print('------------------------------------------------------------------------')


if (__name__ == '__main__'):
    run()