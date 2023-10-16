


pythia_variants = ['70m', '160m', '410m', '1B', '1.4B', '2.8B', '6.9B' ,'12B']

def pythia_output_size(variant):
    if variant in ['70m', '160m', '410m', '1B', '1.4B', '2.8B']:
        return 50304
    if variant in ['6.9B']:
        return 50432
    if variant in ['12B']:
        return 50688
    assert False




# automatically generated using
#
# from transformers import AutoTokenizer
# tokenizer = dict()
# tokenizer['pythia-1B'] = AutoTokenizer.from_pretrained("EleutherAI/pythia-1B", revision="step143000")

# from memory import lives_in, has_a, is_a, persons

# print('pythia = dict()')
# print()
# for grp in [lives_in, has_a, is_a, persons]:
#     for key in grp:
#         nums = tokenizer['pythia-1B'].encode(' ' + key)   # THIS TOKENIZER SEPARATELY ENCODES WORDS INSIDE THE SENTENCE!!
#         toks = [tokenizer['pythia-1B'].decode(n) for n in nums]
#         print('pythia[{}] = {}    # {}'.format(token[key], nums[0], '-'.join(toks)))
#     print()

pythia = dict()

pythia[18220] = 24523    #  Dublin
pythia[31104] = 40892    #  Copenhagen
pythia[40959] = 50086    #  Budapest
pythia[32955] = 40431    #  Warsaw
pythia[14708] = 21924    #  Madrid
pythia[29679] = 38476    #  Stockholm
pythia[11790] = 17413    #  Tokyo
pythia[11852] = 17361    #  Sydney
pythia[12517] = 19950    #  Delhi
pythia[7312] = 16335    #  Seattle
pythia[40274] = 32977    #  Hav-ana
pythia[23732] = 37068    #  Cairo
pythia[14819] = 21818    #  Melbourne
pythia[4842] = 8068    #  Chicago
pythia[41898] = 48104    #  Lisbon
pythia[43296] = 10916    #  Hon-ol-ulu
pythia[22372] = 36546    #  Seoul
pythia[10598] = 12300    #  Rome
pythia[21891] = 27411    #  Athens
pythia[31721] = 43949    #  Manila

pythia[7161] = 13696    #  bike
pythia[3797] = 5798    #  cat
pythia[3290] = 4370    #  dog
pythia[10047] = 12609    #  guitar
pythia[19132] = 18542    #  piano
pythia[4676] = 6568    #  camera
pythia[13224] = 16556    #  laptop
pythia[18757] = 30649    #  motorcycle
pythia[2156] = 2419    #  house
pythia[6621] = 7586    #  sister
pythia[3956] = 4929    #  brother
pythia[40334] = 29154    #  trump-et
pythia[10586] = 15487    #  keyboard
pythia[38283] = 36608    #  violin
pythia[20182] = 32714    #  Toyota
pythia[28367] = 367    #  P-orsche
pythia[8092] = 12673    #  Ford
pythia[21279] = 35512    #  Mercedes
pythia[8223] = 8815    #  horse
pythia[8848] = 9735    #  boat

pythia[35261] = 1794    #  bi-ologist
pythia[4639] = 6254    #  driver
pythia[18739] = 24718    #  farmer
pythia[48251] = 39011    #  mathematic-ian
pythia[33013] = 49360    #  physicist
pythia[24292] = 34513    #  programmer
pythia[10099] = 17264    #  journalist
pythia[6853] = 11115    #  lawyer
pythia[6253] = 7345    #  doctor
pythia[23923] = 20997    #  surgeon
pythia[23540] = 35085    #  psychologist
pythia[14971] = 18468    #  politician
pythia[15849] = 15339    #  nurse
pythia[4701] = 9732    #  teacher
pythia[6260] = 8406    #  writer
pythia[10686] = 15796    #  soldier
pythia[8022] = 11572    #  pilot
pythia[46412] = 270    #  b-aker
pythia[34537] = 27343    #  painter
pythia[21623] = 26650    #  musician

pythia[3362] = 5171    #  Paul
pythia[22695] = 23442    #  Helen
pythia[5506] = 7359    #  Ann
pythia[5335] = 6393    #  Mary
pythia[3271] = 5119    #  David
pythia[2940] = 4744    #  Mark
pythia[3899] = 6277    #  Michael
pythia[14919] = 20222    #  Susan
pythia[5199] = 6911    #  Robert
pythia[5613] = 7993    #  Peter
pythia[26088] = 36449    #  Christine
pythia[10490] = 15458    #  Sarah
pythia[21798] = 27443    #  Ivan
pythia[14685] = 21438    #  Charlotte
pythia[21204] = 25298    #  Pierre
pythia[22578] = 23425    #  Catherine
pythia[48498] = 12469    #  Aud-rey
pythia[1757] = 2516    #  John
pythia[23040] = 33811    #  Amanda
pythia[7939] = 15273    #  Kevin
