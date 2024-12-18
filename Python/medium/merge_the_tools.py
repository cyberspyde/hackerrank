def merge_the_tools(string, k):
    text = ""
    for i in string:
        text += i
        if len(text) == k:
            s = ''.join(sorted(set(text), key=text.index))
            print(s)
            text = ""
# Example with a longer string
merge_the_tools("DHYSYZWKIYXKUNAGLFICSOMUEXODOCLRLJJLIFVQDUCZIDGVKQXDEMXLJNOXRCOELZPUEMMHHRIRUOMEGMJNYIYJYOGRQWWCVNYBAMIJDSCZJOGPCRCACCLATTTLPPPMDNNFCXQFQSHZINQLGVNIZZKSSEEKTTWYJMFNLVUBPBCYQVJXQYHPXSKSWOCRJASUMZHYVCBKFGKWBVVTUEKTWULUKNOUOGQCFYACCEPHKBFNXCGRHSKDNYAZLOTBUMEBMGGOKVXWWDLVHROOMBUZZUYMKUOGIUHUCNIPKFLJKXESQVICWCDVYEHIAXOIRYCUNKJARWLEVRWOMESIJWDJCLUCIIMCIOYWAJYTFJXDAVRNCJVLHBWLMQNWBBAJRYHTHHNPQKSTIJGKUDXCETNSKDRNGRYYSIRBPESGRKBBVHLQMIURBJJNMCATWBTOJKRYRKGKWHLSQWKDGGUHPFXEIZXEASUJCLIVXQFUYQOOOARUGNEVTDBDCAHFSDOVQYSORYKPQAFHAXDIKHFFMHIRHRWAUMXLNPBEPNTINYPPXUXKCERQLAHTRDVOQUBFLCJDPELEECTCWSOAWFRIHADBEAPWUQBHUMKLQXPUZKYYCOAYUTIDUNEANTYJLBRHNBUFZLZAVAAZOBAKUIOQWSQJOOVBRMLEPFJQRLTOLTOBUOMRYAJUUAGIQBMIPXOGCAXVLQKYJAZGQLZONILIKTSDWELLDBRGBQDMGNKSPMAFXBWNJJXWCPZYWKLZNEHPXLDFAOXQCZXBATOMCLIGDHGBTRCGYKXVVBAVRANTZLUCGJQLWYRBHYCCRFKPRIMMLPJCPZXQKRUSCKDBKVCTVHVMOIEFQSRDHCHYBERNXLGAYJDIGHCDOXSCHYJZQACAFJAINRWLFCNDNQLWZNBONTSURCUKEYMJIMSXGQILUXOHPZFPPHFEAXAUBWGGVSRFGLCMBNXVKLFCNMRCTWIWVISXHYFCSWJYKLLNAKJNWQPLCINYGXUBHMAOMFSEEBEOPPBRAMEYCVJHDYFLVBNEPNTBVNFZPJNGBOXDDEDFZMOFMVSJWFNLVIMQWTPLFETIUSLXWOFYCTFOPXXLFKZATLSRHJCONXWHPHFMXKMZFRPUOOITYHVTUNKDWORJNNTDWYRVKDWPULKKZUEADZVXPIDLYUXMKQRGOICYLAPHMZRNVVNYXLYMTBXTVWFHMWOCGSCRSSYGTQUPNJPKUNYPQWJOUQVHPJLVDQNYINEDFYUTIKFEZEUQCFEWVZFKLTGQJVOTITWORTJBDOGEUCUWHATCCAPNTVDCQSXANUOENZISOQWKSTHBTCFVCUKYPQCHKAIXUYDJYLDODZYXSFYOJELMYWMQMOXYOFVKEYTEMWSPYSPSANIJTUXUSJKEYHEOPZZTXUZLTRDRLSLLFUVBOSVGCFMCOQQDPPYOKXCDQFWCXHNCBKFRDAZHFLJWDZZURAJBXNGQSEUPLHTPUZIXZIGHVPDZQETHEEKERQUJWOYKXUBRTJQURWDNNIOENHLTMWZFOTPNJPXJJYCEHTZBREQFNEJCNWXBUXHJSWWELVNXTPBCKCDCHVJUBSYPQVQLSXWNVURJPEGIVJKGOQKVLTRNNPEDMUOHUKUPGLYVPGFKSQSGICBTXUIKLMQXJEEFRAUXLVVADANVSHDAKEWHAEULTKLEQRJHSFHDAEGGEVDXCHXONVYOASBVEOBUGKEARNFURNAVKDUNKUDAPBORVROBGPWOBCOTPVNGJPDTUYIFSMHJPVBNOPOUFMKIQYBFUQNFFRYARHHLVOUMLXZZNQWUEICVHGCDWQKEJIGCRNNODJBOJCPWUNSBWUWFCAKBQUFBELDYASMDEPTNUKLOYDPWZNDCOPDGJKKPVNNVICYMRTBNDMCDPTZOJESZTXFCHRUCFJZPLXDFQESUQWZHQZXZDQYZNFBXXXZEHZTUYWZRCUNSQMBGNYHTOHSEPVBMTCSCDNWELWVNQKHGWIPKGYFXGXDVSGJNIDPOQMSDKNQAXZIVHZHPYMOGJRDEXORIRJWJXOMHDEHADRXMTFBRRQZDHEHHSAPJLNUIBGPGKYGPSFBLKCEEUDHEHQLBSCMEPGMSMEYYCGNWLOHWSLCNQJRZZEARGMXXSMPGQNGUVVRGLAEEMGTCRMCQQEKYRJVJVKSNZYKUUBCFDJLPPEUHQYZICLGTVBFQNXGOXQIRTNZWWKONPIUHIWSKHYGECLXRKDGHTQBODAKZMYNBIJLQHFDRFJVHWSBIXHRSXSGDUTEHRTKCDXUMCXDIGBPEVSMTZELZYSETNIAGCMIHKDVMAZUJCMNXECQGICHGWLZJVBPZOAGYDEKFDHOFTECXIVFQZMWVXYGVBXUPZDPCHCKKJARCGVBOQHERVDOVBUQCUKUTNJYUNKGWKZARVCFNLMHGPVBSQRWMEQHRCHOPRWMCWOVTSAIDMPMDLPVDJSRNKYGMIWEZTSDPGYKZZSENIQTTIOYRIPGVPOJXLNXGFAVMZFLAZRPHKICSZCLJRTEHHOEUBBAJEXVFEIHEZWNJHSDGUQPMJWTTMZPNDSWHRTOWDVCFTPQAHUGEKYQWWLRIKGXPAWWSPMOVJSADJQDTKMXXMNVIAMSMUPCVLAPDNFYWXYZGQFZDRWAFLXPLLHYFYACKARPPWPMTPNCFSBILAKSLHHZSOZANZCZBUQRSFFOWSQBNTMATWTHGAGYRFAGGDHJZXCTEHHACXDRTPRMMMVUPBUGIVOQYXAZWCSAMACOZFHUVYHJNEDCGXKQSAHSXHTTLMTXOVNPAUKXVTGIXJKFJWWBWFWTOPMZBHXREKHGHTECMKKLWWRFSPIQUEJKUXJXEIPKVYQCRUEFHQQFOJMGYUYUBHEVEQUKAJUVJKXCHDHOVATJJFRKBPECWLZCDUODFKBRVATEEDSBFNLOUCAXSHAQUBVXXJCDUDUREPVKSPLXEWOYBQXTXXLRBGQYSTBMWXDCNAMHPAFTWVTXLQSLQGCRMTREOVSKSVNHXBPMBWHATAZETSPJYUCMPTRDQJNJHCSGEHVHFCHYFHDYBUJBONNFIGIZSWIBACHGKCORFXQKEVKFRVGGIWNQCWPUSZVUCDBOFRFMOVYTQKAIFJQNFDEHZVETVZQZERNMISYYQZRGJUQRFIEKOKTPIXLDZBEFURRCJSAZTUICQAVVLAHZMAQUABZBCDGYUAAGSDHNZPPPSLMDNTEBTUWVWXWABFZXFBDZGNMHEDYWQKBFDFHZADWYAVADAZBHDGGLTUTAXTWOEYTJDAKFFJDIEENGFQNKXVWSPRSMKRCQRYAWAMCGVHQZLDFRUSDTPZNESIRDBVTSTVOUISCDAUFLZKEVFKOUJEZCOSHPNAJJWXDESHJSBOFAZMWGWMCHSBLGVSVLVGURGZXYIISJXXLYLJEJYIRQMEXHXUUSBQLHRKHZSZKPYYPKHVTFEMYQTXZQRUKUKXDCHMDBLOTKOIWVERDIGBAZYZRRTBOGATKJGPKTFDFTMBPSTUABVCAVBROXUCFUYRDEGNZMTFFFIWXDQZENBEIEXXBRBGLZXQFGGFSZMZGUWFYMEEAHJKLGHNALVLKVEQBKXVLJURFQWDFCIHJTTUBBJBMHPYCTOFFNAQWUHCNFHUHRBQKUMMXYNLFCMJXCOCQQSMMBQZGAVNRYFCVUQSSFGZIUIHWYKMOCBAGTCMTXCLWHPRBFLVKTUUNECKCOYQSZTYVVLOSPBQWQHAXVXKOSECWIOBWMRPOMPLHAZCRDSQTCQTXNDLHJPGSFHQUAFKNVVUXUYPXRHTTXMQMRDWAVCSALJULQEYNZVNWTCVMLQFIEXWVDUWYWQYJZVVSZVFBQSXMWUYHLERPDOLIKJGJZHSBCNTBJYCBTBNPWMZHSQYXGLGRUMAUVSVXIQBROFUHHIZFWYOQOMNXYVOUKOOFILDQBGJSLEBUOAZKANCRCPOCNCWXSNCAYHTANCUBGVVWYVGYKKPMCFQPJNMBAQEYYXANBWOKSKGQHPQTZIGBNYQXLEALVGMVFOIHNZRFLXXUMPNOXVPNUIMFMOTHVHEAXPHKOYRBYOVKEIYDEQSYYEFKTAUOHYOHNYRDYJEWZZJFKJJOZDOZIVKBWGRDEHKSHEVGNCCODNUNXFDYIRYSPIVLOMOUWBODFKJUOOKRBEFALKZWEXOTHKEXYURUVGACSLYGBJZFPEFDREZVDNOKZSHYMZUKHWOZINHJYGQPLWSECTZGHNQIHAIVBDHIBWHJLQVJWLYJJTNMMMSVBKEIMOGNRNXTLGEWWBHTNGCWBQKNEEJGPPODDWRXKQSVXYSTAZMPHRLIJYYNCJTTAIXDEQCQGWODVGZVHNKREXBNVZBYKUTKEQQLIUDPRRUMZVHJJRAPQDFMFGMPCFCJYSWGMBXDTSPSPYDYRDOIHTWOBKDFPFQPZMWOOTRJNJDDJHDBMTLVOJJPTNXKUNAUCWISRBBHMGMYNRZCLMXZVHRQWOAQDAMFYWZSACZMJNKYELARZYRWHKMDYNTDPIJOEKGENHTWWFWCTXUSXNREXDHXSAAKKLYPWGVJPQHLWDNPAJJXWADTGKSANTKXEKOCSKNHAUUYYKPATBASDDNJQGMDZYAFLPKDBXNDSJCSTTSPUUJYAWJQCXTDWVJHKTMNQZRKJVCEOXVLTELTDUJFSCJQYUZKPLAHLRSWOWAEVYRPCCIFZUNRYYJWSIJHTJQGCKCSHFYEDQVHSEPRACKYATXUDGDZRTFVGIPPNNTQDPXWVOPVQAVSVSOBARATNFQTNFICTDSYSSUNGMKZOGRJAGKBZMUOSLHHSRKLVCKNWGDFUPEIXXSYFEZHRVVLIDSBWCORHAHFHMKBBOMZOGZTKAADVWQGBJHXLXRUYYAFKKINBUMPALKNLLSJJJPMSYJFVCCTACAMOLARHOIKCTZNGRYRCPDWNOCLRGGTKJGYUISDWANYVOOBGMUKEXHTMLEFRNABWIBSQTVPWLNRZDVHSPSWPZPDMWIDJKGHTHZLDWABJQULTPSNHMJWNBBZZJEIVKPOUQAZMAAWSWJMODBVQNTFOUHPFLXAWORSERRSTTQMPZADDBAVOVAEPHTWTSXRIOJMHCHCXXOOXQSAUUVKQXRHFMEAFDTNTECCGJEFGVTFNNHHICSACJJJVNJCSCSNGUPODWTLRMREAYMKDGKFRTOOJZRDBJRJFIXKEQVVEOCEPQOSYAZPWPDHQUKTFBCKMBUQTQOXGQEVIUNGVOVTFYAVVKOAOSNATHSMZGKGYOBGIRMFHHYNIYKFLZFBTSDNCVZBCLJAZNHKGVPNDQCNOPSBQZCJUHWWDWZFHJHJYQTEMKTRAWERLYUBXZMRGJPJHPQQYAZWQUCCHVVHRZAEZVHXUUQAFGMMXECXEEVVYXZFSVPMWPSWMAVIWLJDTXPQBTNGXIDYHCFAXUMUMGQAINJEYUHURYMUSCARKDPSGXUFRIZFORGXEPDFLNBCNNWHPZZCEQWMNQSHAROQLUNRLTWWIXAXNZFCAEGEWCRKUJTWCHNPECHPVDOFDQDSPKUPQDWMHNYEYRACZNSDQZUNEIVJBYBSKYKABGMKTLOTCPVBCPGUOBIVLDGMDIFNIRNJXBVSMKLRZISDYBYMCIJNNQCQAJFIAUTXXORKYCBXKVDKWBZALIQYASQADXIDRBCQQVAOXDOJBRUZUVAFDQDEKVENSPSLQWBGRCXQHNBIEXIASKHWCMCMHIBZXTKOPLWIPVYXIZHOXRORBVPDJRRQCSPBLBRCNOKCJKBSMJGLAXCCUSHELZUPRMRFNIJAWWFIGGCUPKFSHKWEEDIPEEFYQWFGEOIDMNNVWPPNZXFJHBNLHVCNBJNSFSAMJIRVYEQUVIHUFPFMQSXZPBNRLCJSVLGETXBRDSLYAVVHKATCVSCKTRBGTMZQXFUTFYKKSYJSTGZDIUHDMJQHCTOYGPOFULYBJLMBJXVEDWJNQQTEAJNECDCKSRSPCSSNDEOODLSIHBWZSPDUASYEWDPQWJFYBYNHEBXIOQQVTOUNDZJFRKKNNZEJKLJLLWUQZSANKSKDHETMDCSWMCKZDQKNDTARRVJSPJFZBPEKVXXYAPVMTHOWZYLEULVLIEEXPLYRDDBYAAZCPWRKFFGGFTKBHGPPMVPCGNVLSYKTZLXQJOBOVJUBDGCKOTBBOSFVIAGAASVZFTSOJVEFEAGJHKVVEZYSRDPBFYEGSZHAUZQEUVJBVRKEDGCHFACYGTCLRGRMFBMCACGXZRYXKKBNQFXXGBYOUAZOGTANUOPWQXVQQTPAEQOWYLWEMUUIWTWCOWRKKHJDGEVXYKXECNCAAYGOSAXOWTSKSKXETGJZKEYKQYOVLRXORECMGZACVVPNFORAUDBGHARAYHVLAUBSYEEHFGLADCPKQJKMMMTTOMVOTSBWNDONHUUOCGPGIESBNDNZRIVFUSTOLUKYXANGWIVAQMIAQBBGERFXZCCUVVKIRWIRYVXUDUWVGFWXGZDMQKJQPNMKKWSBSASQXSMBMIYTPUSXWXJOHUGYHSITOCVIEPACHOFWZDPOAHMWEXKNURMBLWXCBUKFJNHTBOPASGRUPDSTCCIWVWAHVXLWRVBCKLVMZMOTSFPHKHCPMNLHJNQEKBCDZEGJRDXSSMMKTDUGLYVXLIGXWZDGCGMDKUNDXMVPAJCWNYCYWXXIFDHBEKKHQYKCSZFRMBHOMLKZJMZHLWRTCYWGJINBGAEYZLQNOZEBMOAXDCEQYWJAWGJFOYJXYPVAALPRMTSYKUVPWCFXYRZWZIENHNKHCIHEVZVIUPGEKEVIGBFGUFCTPGIWTVEXDNEYOZGJPPPBVLLBOTHIYLBNSJMNESNJFRIUQQFHHUKCFWDVPMDPYGESSQFWISIQLQMCIRLQLYUTWYOLMUCMCGEUZMTJGBBSTNWBGJTUHOPDODQAZUPCDTYCHRNOUPINEERLPKHXAWCOBTRDNGFQBFUJXKZRZHHFNYSCKZBLXEBZZSCOAJHCODLNNKHOTOUGOOKYQMLNSNMRHOHIZOKOSXBHHKWAYSIMGSLWGYMYLYRTPZDOPNEJKIRTSNVRHDFNXSMERYEEYWXPXAGMPKWBSPUNEPGLULASGOYXOCBNABEXDKMTVKUPZREDGKODWOVCFVBTXEGAFLXJXJESTAKUROXYZNDXEYBJTECSILSOYSZVDDQZDCTVQTVRGYQMYTVTXANGLGWLAVIDAACFCWAVRXOXXFKXAHSYHGGUOCHOZQTZQWEVUHQLGEKGLWDMGYMPESKUWTKVLDWEBCZVJPISVVYHTDVZBHPHBBBZULWIPSMQULOGCYYZVYIPBDODMFMPGOODBKNQCZJZMZFQZFPVDYKGDALSGYHOMWTNIGGNFROTSTJRABOFZALEBXWJVGZJETYMZEBHXPCPKMJKNZPOADUDARMVZLGDGEPIJTPIIRATFLFUKVIKYDNAWBXVPDAVHRDSKUDTODMVORQYOALOFYQBANYPSYMAQQUCMXVAAJWQDORTOCIUAAXCOWTGWIIOYDRMCONFYLVBZMWNQGJRHHVXDRDBZOQZTJLVXACVNAYOMVEDDNWKUTHZKNBLBTKUCWRZYUXMUVAISENWSLGOFQORDRDGKNAMLTNKNKYJGYSAFHWXTFNAXBRCSUIEKISVBGHRQFAYGUBLCXIVEVVDZMFTJNYTXQQBWAUPFUPLPQWRQGOUEJADXFYGVWBUNUXLURCZOSNDIJWYSKVWVVBSCZBZYEULYRYSJBUXVJCDSAEMMZIHWLZANCALHUYHNWCYZYXWHZAZBGMNFWUDKWDXADIHZGRNETNERLCYMCZOKNDPKYUWWYTWDBEDHXSLQFRHSUFFYGVJUYAGYVCUVVRYWXBFUVSMBMTTIAAIGXRAYUGWRKTMFKKDJOKFJDRMRMIZMKHUIBXGVFEOQXAVHMBSALXMQQYHCIGQTQLBRKJOPNCFLCDUQGPTRMFIFFRJOAAJQNKHXVVOIXUVBZQRFFMYTTIAZAKPAKYQXKZWFUKPTGLUFBNMIALBTVCUVOLXYLNXVMTCIFSBMDXTENIOPVRKQVHMJSJHEZEBNZEWHWZVZZODMYTDTKNKGUYPPJXTIDUYFYUMWVHVUXAIWTLREZBKVBZKLYFVECTLCPZZLGUHFVQDOBVUAYEYAGINGOIKSEVUVUTGCOQKJGPZHKUKJYILGSYNIIZAOXVKTOSYCIINOXNWKHIVHSGQKGDTQETFBOPVDHTHSDVGCIEMROJAGRQRXTKQAFVBWMYBVRINWFUZPANGPXHVOZMOVYEVEBWANVBIOLWNRSOGUDPLAWHRXVHSWLNAMMCBJFJZQHMJBCQYGFJIDQZAOGVKTIMHUQIDVUFNDRZFUPFAWOIBHKDVSYHOHTVDJGJGCOVFHUMDLRFJGOKNAOKUORIVMGBXOMFQAAVJXINIBSUHIEWIUIFJBNGNVJMJVRBVUXFRHUBKMXSVCQFYBKHCAQSVZGHVAISUHZNQTQBGOVBSNGQOTATTSNQRTXOTIJPRICIEVLKJGNDVVTKOVFJNUAHNZVJHEYZPDJTYUFJCSMXPHJGFORSIRBYRXJADJZSMKLMESXIMLGCVPKAGBUQTWQMVZMYJOTXYEKFXJNJVTNSLZSRBOJWMAKHZWGIKZILFUQEDDQAZFSMFMFIBOGNOQXQMDAZEIKLCCSGHIIIPBUUPZESQKIGAFWPKXOQHABMETSLDCUTFQPVSUNIGVOHCNYMMOCTOGFUBZFFCBAHUPEMLUUSPKBUXZGJNLFDTKXUMEBQIBZCREOEYKWPUXJSWSDLFIOYVNUHSWXCXWEQAUVAETQATBURVYDAGTABHVKBRHFQGJHGFEJLXBLSCGKYGNYOIBQRWCSPKZFQKMYPSHASKOKNWULCJLQSOIJKLEZXFFPQTNFOXIGHWQWSNJWYXMSLXCWKIXHPEWFYLLMIVUSRMOLZYHYVVQISUEEEELUIHBIVMWDHQXADONEMUEJSXRMTYRAECWMMXXHMTMVMMWRAJVMGCXYZQKSQDSUGOHUMEDAZRVLDRCDDARLCOJDHVVXZQSHGBDUHGUGXQUBJYEOYYZCMKFVGDTHTLQZMTWVBQBYIXBSWIIWGIZUUEQCHJJCWBEIUAFVSGWBGXVCFDYLNZGIGWKPHWSDXYNUYSRSANTGLQKSWLELKMTQKGIREAUDYHZYBRQBEMIPESIADOMQCHIMPQDVSZZQGYQJPJKWXULBPVESLQKNZTZPLEMEDNWLMNUDYFBVZPYOKCJYSVLUQNLCRXGVLCIZRDEPKGKLVLCHNNFIKTCBGNDZKJWXLFWDKBUWJHHESLNFAVNLORMWEPVRASONXLSJONFXUODMASTCNJNBAZZHQVYSPOGMBYXRNCQHSTVUMRXBAKFCMEJEZJXOAFCBFBTTFJCYFYSTRRUTEBVSGHWHSVYSCCWIERDJCFJHFECWVZPZANTIUSQOPQHSSFCYWFKYKTIQXMMVLEWORQWLIOBXEKPZPTXNYHMJDWBAIPVWTUMKKKXSZZRFJJEBCEOBLCMOYNRJEOHYITKSDIMEJEKUNQVRUMSIOGYPVPAAGHYOCKJHSVMDBYAQQXINJAVYHTPELPETWEHYPSHJQTNRTPIKMQXWSUWBPLGCAKVWPFWGXFPPBEHUTPGGHFEZBABRLJVLTRJKYHSXMINNMUKILQQUYUTZUWSHFOUBHDNFMGCYQROENYMYQEUOYOQUMIBUWVXDAMKMSPNKGBPUZDUPIRGIHWDTEEPDCMGCZTRTIEGQFVMEYJVIABRHXUAEASHEGNHHIADQEJJJEVPEEMPEOGLNCOREIYJOOSWWSZPWKYHOVWUAKJGYRU", 7)