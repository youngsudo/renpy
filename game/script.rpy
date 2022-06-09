init python:
    dienum = 0

define config.say_attribute_transition = dissolve
default preferences.text_cps = 20
define dubai = Character("独白:")
define mingshiying = Character("明世隐:",image="msyside")
define bailixuanceng = Character("明世隐:",image="blxc")
define kuangtie = Character("狂铁:",image="kt")
define huamulan = Character("花木兰:",image="hml")

image white = "#ffffff"
# 凯
image side kaiP =  "images/tx/kaiside.png"
image side kaiP y =  "images/tx/kaiside.png"
image side kaiP sg =  "images/tx/kaisgside.png"

# 露娜
define luna = Character("露娜",image="lunaP",color="#8A2BE2")
image side lunaP = "images/tx/lunaside.png"
image side lunaP y = "images/tx/lunaside.jpg"
image side lunaP zx = "images/tx/lunazxside.jpg"

# 强盗
define daozei = Character("盗贼:",image="dzside")
image side dzside = "images/tx/dzside.png"

# 狂铁
define kuangtie = Character("狂铁",image="kuangtieP",color="#E3CF57")
image side kuangtieP = "images/tx/ktside.png"

# 明世隐
define msy = Character("明世隐",image="mingshiyinP",color="#FFFAFA")
image side mingshiyinP = "images/tx/msyside.png"

# 百里玄策
define baiixc = Character("百里玄策",image="bailixuanceP",color="#CD0000")
image side bailixuanceP = "images/tx/blxcside.png"

# 花木兰
define hml = Character("花木兰",image="huangmulangP",color="#FF0000")
image side huangmulangP = "images/tx/hmlside.png"

label start:
    # 显示白色背景
    scene white
    show wzry
    with fade

    play sound "audio/王者大陆起源.mp3"
    nvl_narrator "王者大陆起源"
    nvl_narrator "相传超智慧体神明制造了\"奇迹之力\",打算控制王者大陆,"
    nvl_narrator "参与建造的22个家族担心她一旦成功,自己将会陷入被超智慧体永久统治的恐怖之中,"
    nvl_narrator "所以他们发起了叛乱!"
    nvl_narrator "打败了超智慧体后他们瓜分了未完成的\"奇迹之力\"。"
    nvl_narrator "其中一个收场碎片的家族就是你所在的艾文湖的阿尔卡纳。"

    stop sound
    play music "audio/王者荣耀背景音乐1.mp3"

    scene bj room
    #用户名称定义
    define pov = Character("[povname]", color='#0000FF', image="kaiP")
    python:
        # python 代码块
        povname = renpy.input("你的名字是什么？", length=32)
        povname = povname.strip()

        #设置默认名称
        if not povname:
            povname = "凯因"

    pov "我的名字是 {i}{size=35}{alpha=0.7}{color=#0000FF}[povname]{/color}{/alpha}{/size}{/i}。"
    hide kaiside

    stop music
    nvl clear
    jump label_luna
    return

label label_luna:
    # 魔与道之刃
    scene bj luna
    play music "audio/王者荣耀背景音乐2.mp3"
    dubai "在阿尔卡纳家族的继承仪式上，所有的候选子女必须在仪式当天互相比武，直至剩下一人。"
    dubai "这个人就可以得到奇迹碎片的力量，成为新一代阿尔卡纳家族的当家"
    dubai "于是在仪式举行前的一晚，有一个人开始动手了"

    scene bj zise
    show kai1 at topright
    with dissolve
    pov "是谁！？"
    show luna_fhzr at topleft
    with dissolve
    luna "哥哥，就剩下你了！奇迹之力是我的了！"
    pov "你干了什么！？"
    pov "不，是{size=35}{color=#ff0000}奇迹之力{/color}{/size}，你已经入魔了，必须让你清醒过来！"
    dubai "[povname]很清楚的意识到，由于妹妹的力量来源与月光，尚不清楚力量的本质与明天仪式的真正目的的她依旧在认真
    准备着明日的战斗，却不曾想在今天的月圆之夜最盛之际被疯狂所控制。为了获取力量，失控的她杀死了所有人。"

    dubai "在[povname]精湛的剑术与强大的实力下，[povname]成功得打败了陷入疯狂得妹妹，为了救下妹妹，[povname]
    以自己的身体为容器，将那些令人疯狂的魔力从露娜的身体中引出。"
    dubai "很快，[povname]也陷入了疯狂，但他凭借着自己强大的灵魂与坚定的意志，苦苦的支撑着，不让自己失去清醒。"
    dubai "露娜逐渐醒来，看见了大厅满地的尸体与大哥陷入疯狂的模样"
    dubai "魔道能赋予人力量，也能让人疯狂。露娜意识到，她的哥哥，正陷入这样的危险。"

    pov "拿起你的武器,和我战斗！"
    luna """
    不......

    我不会和你战斗的......

    我无法忘记你教导我的一切......

    还有你七年前救我的那件事.
    """

    pov "那些小事我已经忘了"
    luna """
    但我不会忘记的！

    我想成为[povname]哥哥这样的强者......

    因为......

    你是我最敬仰的亲哥哥啊！
    """
    hide kai1
    hide luna_fhzr

    show bj huse
    with zoomout
    nvl_narrator "七年前一伙马贼侵入了,抓住了看家的露娜,正巧遇到了返回家中的[povname]"
    show dzimage at topright
    daozei "你知道我是谁吗？ 我可是恶名昭彰的堂堂大盗恶斧啊!"
    daozei "看来我们需要做笔交易！小鬼！"
    daozei "把你们家的家传之宝拿出来交换你妹妹吧！"
    show kai xsh at topleft
    pov "家传之宝吗......"
    daozei "对,就是你们家族代代相传的那个东西！ 奇迹之力的碎片啊！"
    pov "你说的那个东西我在家族古籍中看过,确实有着么回事。"
    daozei "哦哦"
    pov "你会拿那个东西来做什么呢?"
    daozei "可以去争取下圣骑士团头领的位置或者搞个军队！再不济也能占领个城堡！能做的事太多了！"
    luna "哥哥快跑...... 不用管我......"
    daozei "别废话！快拿来啊！"
    pov "那么,我又能拿它来干什么呢......"
    daozei ".......?"


    dubai "[povname]拔出了自己的剑"
    dubai "[povname]凭借自己强劲的实力，很快就把所有盗贼消灭了。"

    luna "哥哥...... 呜......"
    luna "原来你是这么强大！你是为了救我才出手的吗？"
    luna "谢谢你！[povname]哥哥！"

    scene kai_luna_bieli
    pov "不要用这种眼神看我"
    pov """
    我当时并没有想过救你！我......

    我只是无法控制我之间而已......
    """
    luna "我们可是亲兄妹！难道奇迹之力比这更重要吗？"
    pov "你根本什么都不知道！"
    luna "什么？！"
    $ ans = 0
    menu:
        "告诉露娜真相":
            python:
                 ans = 1
                 dienum = dienum + 1
        "隐瞒并承担下罪恶":
            $ ans = 2

    pov "别说了！我们只是被当成奇迹碎片来养育的工具罢了！"
    pov "那时候我在家族古籍除了看到奇迹之力的来源,我还看到————真相"
    pov """
        奇迹之力根本不是一件东西,因为我们就是奇迹之力的组成碎片！

        等我们长大之后,就会参与这个自相残杀的仪式,

        然后所有人的身体和灵魂都会融合成一体！到时候......

        我们都不再是人了！

    """
    if ans == 1:
        pov "而且，杀死他们的人...\n是你!"
        luna "什么？怎么可能！？"
        pov "因为疯狂，这就是魔道的宿命，这就是我们所身负的诅咒"
        luna "……

            [povname]哥哥,这才是真相吗？这就是我们拥有奇迹之力的真正原因吗？

            我害死他们……

            原谅我的懦弱，我再也无法面对我自己了
        "
        dubai "露娜举起了自己的剑，狠狠得刺入了自己的身体"
        pov "不……！"
        luna "对不起，哥哥，永别了"
        dubai "[povname]看着死去得最后一位亲人，决心要终结掉这样得命运"
        dubai "之后后,他离开了空无一人的艾文湖。"
    else:
        pov """
            我要斩断这怪物般的家族和罪恶的命运！

            只有一个方法,就是把你们这些候选人统统杀掉！
        """
        luna "......"
        pov "不要怪我......"
        luna "[povname]哥哥,我相信你的决定,所以——"
        luna "我愿意把生命交给你！"
        pov "好！"
        show libie_image
        with fade
        pov "露娜......"
        luna "哥哥......"

        dubai "[povname]终究没有勇气迈出最后一步,去迎接他所等待的惨烈结局。"
        dubai "从那以后,他再也没有回过艾文湖了。"
        voice "audio/露娜 足够强大到挑战你.mp3"
        luna zx "足够强大到挑战你，哥哥，并带你回家。"

    voice "audio/一夜又一夜被惊醒.mp3"
    pov "一夜又一夜被惊醒，寒星下的别离"

    stop music
    jump label_kuangtie
    return

# 日落海
label label_kuangtie:
    scene bj kuangtie
    play music "audio/王者荣耀背景音乐2.mp3"
    nvl_narrator """
    好些年里，[povname]和他那令人颤栗的魔刃如同幽灵漂泊于勇士之地，引发同样身为魔道家族后人们的恐慌

    而在广阔无垠的日落海南面,崛起的强大城市阿尔卡纳由执政家族们建造。其中奠定城基的高塔家族,便被称为——筑城者。

    某个平静如水的夜晚，{color=#E3CF57}狂铁{/color}与商队在某座森林外宿营时，人们谈论起了八卦。

    听说过吗？广大的日落海上游荡着一个恶魔。

    他冷酷，无情又强大，刀锋挥舞之处，无生灵存在。

    他很强吗？

    谁知道呢？要知道人人都说他也拥有奇迹的力量。

    难道强过筑城者和执政家族吗？

    问问这位{color=#E3CF57}狂铁{/color}老兄吧！毕竟他可是跟筑城者对峙还活下来的家伙！
    """
    show ktp at topleft
    dubai "船上的人都在讨论这[povname]拥有奇迹的力量,这时候狂铁挤到一位神秘男子的身旁,与他交谈起来。"

    kuangtie """
    兄弟,你说,所谓奇迹究竟是什么呢?

    它能让人变得很强。让所有人都害怕它。对了,还自称是阿尔卡纳魔道家族还是奇迹家族。可我认为这是不对的。

    拥有了力量,就把自己当成神明,去为所欲为。让大地腐蚀,让动物变异。那他们不过也就是仿冒品。

    恶魔也没什么了不起,如果只不过仗着奇迹力量就干同样的事情。
    """
    dubai "鲁莽的佣兵挑衅的看着似乎举手间就能取走自己性命的人。他心想，自己可真是个蠢货，总是要去挑战一些比风车还要令人恐惧的庞然大物。"
    show kaip at topright
    pov "没错,这力量并非礼物,而是诅咒。"
    pov "如果无法解开诅咒,那么,阿尔卡纳家族的崩塌,会令整个日落海卷入灭顶之灾。"
    voice "audio/狂铁 是你吗.mp3"
    kuangtie "那么,你真的是......那个幽灵？"
    menu:
        "放过狂铁":
            pov "[povname]。记住我的名字,[povname]。因为,说不定什么时候,我就会失去它。"
            dubai "最后[povname]讥讽一笑,随后站起来消失在夜幕中。"
            dubai "狂铁更加肯定，他本来出现在这里，是为了干掉自己的。可因为自己说出了真实的想法，他放弃了打算。"

            kuangtie "他为什么会出现在这里"
            kuangtie "商人口中的污染,和他口中的诅咒,是否就是同一件事？"
            kuangtie "日落海的恶魔,不,不是恶魔,或者他也发现了自己同样恐惧的实力,并努力想要阻止吧,阻止诅咒。"

            scene kuangtie beili with dissolve
            dubai "太阳升起来的时侯,狂铁已经下定决心。"
            dubai "他会重返海之都。他会阻止污染的蔓延。"
            voice "audio/狂铁 越是恐惧,越要战胜它.mp3"
            dubai "越是恐惧,越要战胜它。"
            voice "audio/狂铁 凯因我永远的友人.mp3"
            kuangtie "凯因,被遗忘的名字，我永远记住的友人"

        "杀死狂铁":
            pov "是的，魔道的宿命，任何人都无法摆脱，你同样都是奇迹之力的后人，而我正是来杀死你的，或者让你来终结我。"
            kuangtie "那正好，我要挑战你！"
            voice "audio/迄今所有人生都大写着失败，但不妨碍我继续向前.mp3"
            kuangtie "迄今所有人生都大写着失败，但不妨碍我继续向前"
            voice "audio/勇气是唯一的信仰.mp3"
            kuangtie "而勇气是我唯一的信仰"
            voice "audio/被诅咒的可悲人生，终结于我的剑刃.mp3"
            pov "被诅咒的可悲人生，终结于我的剑刃"
            scene kuangtie beili with dissolve
            dubai "经过一场激烈的战斗，狂铁最终落败，被[povname]杀死"
            dubai "于是王者大陆再少了一位英雄"
            $ dienum += 1
    stop music
    nvl clear
    jump label_blxc
    return

# 云中漠地
label label_blxc:
    scene white
    play music "audio/王者荣耀背景音乐1.mp3"

    show bj blxc
    with dissolve
    nvl_narrator """好些年里,令人颤栗的魔刃如同幽灵漂泊于勇士之地,引发同样身为魔道家族后人们的恐慌。

    可所有毫无意义的战斗都不能填补灵魂的空虚,只会令绝望与日剧增。

    他终究消失了,在前方东方的路途上。他想去追溯魔道根源,也许可以令自己摆脱无尽宿命的折磨。

    他就这样步入滚滚黄沙深处——大片统称为 云中沙漠 的土地。而那里,正经立着改变所有人命运的剧变。
    """
    nvl clear

    nvl_narrator """
    大漠中的绿洲,稀有珍贵的泉水,深达地下的石井......

    围绕它们所建立起来的诸国,在漫长的时光为了水资源彼此攻伐,相互纷争不断,直到帝国铁骑的来临才有所改变。

    前所未有强盛的帝国建立起来都护府,打开关市,从丝绸之路运来茶和布匹.调解了冲突和争夺。

    大漠中因此平静数十年之久。
    """
    dubai '''
        可那前往东方的剑士路过时，看到的是毁灭的迹象。王庭沦陷了；都护府沦陷了；

        当地平民哭号着，帝国的士兵倒于路边奄奄一息，他们都认为对方才是背叛者。

        冷漠的剑士没兴趣了解谁对谁错，但魔道的泛滥令他厌恶，让他想起昼夜折磨他的噩梦。

        于是所有人逃离沦陷的城市时，他逆行步入灾厄深处。成群结队的魔物自剑下哀嚎着倒下，可危险的气息越来越浓烈：

        他想，有个家伙，非常擅长魔道的家伙，在窥视着。他要找出他，他有着这样的自信和骄傲。
        '''
    show bj mingshiyin with zoomout
    msy "我靠，这小子居然这么厉害"
    msy "不能让他发现我的目的"
    msy "使用幻术将他杀死"

    voice "audio/明世隐-我的就是我的.mp3"
    msy "让他知道,我的就是我的,终究属于我的"

    show kai ming
    with dissolve
    dubai """
        正当{color=#FFFAFA}明世隐{/color}想着怎么对付[povname]时,[povname]挥出了剑！

        剑光带着力量和意志斩破险恶的迷雾,明世隐发出惨叫和怒吼。

        幻术消失了。废墟中,剑士立刻明白为何你家伙死命阻止他:

        小小的少年,恐惧哭泣的魔种混血少年全身笼罩在刻印的法阵中,会被用来作为祭品唤醒某种强大的东西。
    """
    show bj blxc
    with dissolve
    baiixc "哥哥，哥哥,哥哥......"

    pov "哥哥……？"

    dubai """
    记忆中刻意想要忘掉的声音，同样呢喃\"哥哥。\" \"哥哥\"。剑士的记忆飘渺到很久以前:

    为强盗挟持的女孩伸手向他求援。“哥哥。”“哥哥。”

    冰封的心瞬间瓦解。饱吸生命的恐怖魔物没有抓住它渴求的最后祭品，少年被抛往远处。

    反倒是踏进法阵的剑士自己遭迷雾拖入黑暗。然后，某种有生命的物体挣扎着，牢牢包裹他，欲将他吞噬。

    [povname]听着啜泣的声音越来越远，却感觉越来越清晰入心。

    [povname]身体被撕裂，意志越发清醒。

    濒临死亡的剑士嘴角泛起冷笑，这邪恶的生物似乎不清楚，自己才是他们中间更可怕，更恐怖的那个。

    他再次挥剑。
    """
    voice "audio/无限接近死亡.mp3"
    pov sg "无限接近死亡，更能醒悟生存的真谛"
    voice "audio/多管闲事的命运.mp3"
    pov sg "多管闲事的命运,碎裂与剑士的意志"
    nvl clear
    stop music
    jump label_changcheng
    return

# 长城
label label_changcheng:
    scene white
    show bj ccbj with fade
    play music "audio/长城背景音乐.mp3"

    nvl_narrator """
    穿过大漠的风吹动着高扬的旗帜,凤鸟的图案鲜明如火。

    它傲然的矗立着,纵使经过七日七夜不断的战斗,宣示着长城一角始终难攻不破。

    第八天,围困这堡垒的魔种骚动起来,那么他们作对的绯红身影,从它们的来路发起了攻击。

    最终的战斗从夜晚持续到黎明,数量悬殊的双方始终无法取得决定性胜利:直到一个人,一个活生生的人,旁若无物,摇摇晃晃走进伤痕累累的战场。

    绯红的巡守着自战场中间捡到了异乡剑士。有生命的魔铠在她眼前快速退却,
    露出苍白的面庞和伤痕累累的身躯,手里紧紧抓住一把剑。周围是一堆砌如山的魔种尸体。
    """

    nvl clear
    show bj zise with fade
    show hmlp at topleft
    hml "你,从哪里来？"
    show kai kaijia at topright
    pov "忘记了"
    hml "名字呢"
    pov "忘......"
    hml "铠。就叫你铠吧。快起来,别装死。"
    hml "你很强,我们需要你这样的人。留下来吧。也许会后悔。反正你什么都忘记了,后悔也无所谓吧。"
    dubai "突然被取名为铠的剑士望着手里的剑。剑上的斑斑点点，让他想起绝境中的沙地，生长的花。"
    pov "铠吗？似乎不错。忘掉锐利的、只会伤人的剑，从此以守护的铠之名存在。"
    menu:
        '不,我要离开':
            hml "你都失忆了，离开这里你又能到哪里去呢？"
            pov "不知道"
            voice "audio/有个小小的影子.mp3"
            pov "有个小小的影子，留在我心底，挥之不去"
            hml "那么可惜了，希望你可以找到你想找到的东西"
            pov "嗯，谢谢你了，再见"

        '嗯，我留下来':
            hml "真的？那太好了。我代表长城守卫军欢迎你的加入"

    voice "audio/花木兰 想活命吗,紧跟着我.mp3"
    hml "异乡人,这里可是战场啊！想活命的话就紧跟着我！"

    dubai "他撑起身体,慢慢跟了上去。"
    dubai "前方,是延绵到天尽头的长城。"
    voice "audio/以绝望挥剑.mp3"
    dubai "以绝望挥剑,着逝者为铠！"

    if dienum > 0:
        pov "最终，王者峡谷少了[dienum]位英雄"
    return

label quit:
    return

label before_main_menu:
    return
