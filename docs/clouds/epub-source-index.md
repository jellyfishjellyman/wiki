# EPUB 资料索引

!!! note "校订状态"
    本页记录 `cloud/` 目录下两本 EPUB 的结构、主题分布和待抽取字段。它是后续把 EPUB 内容并入主题 Wiki 的工作索引，不等同于已校订图版库。除章节标题、文件名、图片数量和关键词命中外，具体页码、地点、拍摄者、图注和案例解释均应视为“EPUB 待校订”。

## 整理范围

| 来源 | EPUB 文件 | 当前用途 | 校订状态 |
| --- | --- | --- | --- |
| 《云彩收集者手册》 | `cloud/云彩收集者手册 (【英】 加文·普雷特—平尼) (...).epub` | 云属、云种、变种、附属云、特殊云和光象的现代观察术语来源 | 已完成结构扫描；逐图图注、页码、地点和摄影者待校订 |
| 《一天一朵云》 | `cloud/一天一朵云（超豪华云彩科普巨制 《云彩收集者手册》作者新作） (...).epub` | 每日云图案例、现代摄影个例、特殊云形、光象和索引术语来源 | 已完成结构扫描；`part0005.html` 至 `part0009.html`、`part0011.html` 至 `part0015.html` 已开始分批建案例索引，`part0010.html` 仍需继续拆分，`part0016.html` 图片来源页已开始用于纸书页码线索校订 |

!!! tip "图文案例索引"
    章节级结构扫描之外，已开始把 EPUB 图文个例拆成可回查记录。见 [EPUB 图文案例索引](epub-case-index.md)：目前覆盖《云彩收集者手册》的积云、层云、层积云、雨层云、高层云、高积云、卷云、卷层云、卷积云、积雨云，以及荚状云、堡状云、幞状云、悬球状云、幡状云、弧状云、管状云、砧状云、航迹云、火积云、雨幡洞云、雾、钻石尘、贝母云、夜光云、宝光、彩虹、华、云虹、幻日、环天顶弧、日柱和 22 度晕等章节；并已分批拆分《一天一朵云》`text/part0005.html` 至 `text/part0009.html`、`text/part0011.html` 至 `text/part0015.html` 的图文案例，覆盖雾中迭浪云、荚状卷积云、米友仁《云山图》碎层云、卷层云虹彩、瀑布水雾彩虹、幞状云、鬃积雨云、钩卷云、土星六边形、ISS 云色、冯--卡门涡街、漏光成层状高积云、辐辏状高积云、悬球云、飞机宝光、弧状云、贝母云、平流雾、放射状云、环地平弧、马蹄涡、完整圆虹、混合天空、ISS 卷云带、鄂霍茨克海云街、洛杉矶环天顶弧、毛卷云 / 波状高积云对照、戈德尔明碎积云、高积云幡状云、钻石尘下映日、诺森伯兰郡卷积云、旧金山雾光束、鲍德温热气球俯瞰积云、金星云结构、网状云、荚状高积云、ISS 极光、马荣火山山帽云、黑海水华、火星日落、宝光 / 布罗肯幽灵、秃积雨云与鬃积雨云对照、《幻日之画》、糙面云、航迹云影、幻日环和 120 度幻日、堡状高积云、北斋漏光高积云、马拉维幞状云、滚轴云、海王星大暗斑、达尔文积雨云、中世纪钩卷云、对日点复杂晕象、古德岛山帽云、非洲海岸重力波层积云、ISS 夜光云、曙暮光条文化名、波状高积云投影、热带辐合带云线、墙云、日柱、多重彩虹、气辉、层积云洞、球状闪电、B-15T 冰山下方海洋层积云、乱卷云和瀑成性碎积云等。`part0016.html` 图片来源页已开始用于纸书页码线索校订，但当前仍是案例级索引，图片路径、图注边界和授权状态待校订。

## 源文件结构

| 来源 | EPUB 内文件数 | HTML / XHTML | 图片数 | 结构特点 |
| --- | ---: | ---: | ---: | --- |
| 《云彩收集者手册》 | 250 | 60 | 185 | 章节边界清楚，大多一章对应一个云属、云种、附属云或光象专题 |
| 《一天一朵云》 | 384 | 19 | 359 | 正文集中在少数长文件，图片数量多，需结合“图片来源”和“索引”回拆案例 |

## 《云彩收集者手册》章节索引

| EPUB 文件 | 章节 / 专题 | 图片数 | 主要主题 | 建议并入页面 | 状态 |
| --- | --- | ---: | --- | --- | --- |
| `OEBPS/Text/chapter1_0001.xhtml` | 如何收集云彩 | 2 | 观察方法、收集规则、云彩观察文化 | [云的观测方法](observation.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0002.xhtml` | 云的分类 | 2 | 云分类框架 | [云的分类体系](classification.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0003.xhtml` | 十种主要云彩类型 | 1 | 十属概览 | [云的分类体系](classification.md)、[术语表](glossary.md) | EPUB 待校订 |
| `OEBPS/Text/Section0002.xhtml` | 积云 CUMULUS | 5 | 积云、积雨云、对流发展 | [积云与积雨云](cumulus-cumulonimbus.md)、[低云](low-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0004.xhtml` | 层积云 STRATOCUMULUS | 5 | 层积云、高积云辨析 | [低云](low-clouds.md)、[层状云](layered-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0005.xhtml` | 层云 STRATUS | 4 | 层云、雾、低云幕 | [低云](low-clouds.md)、[层状云](layered-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0006.xhtml` | 高积云 ALTOCUMULUS | 5 | 高积云、荚状云、幡状云 | [中云](mid-clouds.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0007.xhtml` | 高层云 ALTOSTRATUS | 4 | 高层云、晕、降水前兆 | [中云](mid-clouds.md)、[层状云](layered-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0008.xhtml` | 卷云 CIRRUS | 5 | 卷云、积雨云砧部、晕 | [高云](high-clouds.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0009.xhtml` | 卷积云 CIRROCUMULUS | 4 | 卷积云、高积云辨析 | [高云](high-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0010.xhtml` | 卷层云 CIRROSTRATUS | 5 | 卷层云、晕 | [高云](high-clouds.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0011.xhtml` | 雨层云 NIMBOSTRATUS | 4 | 雨层云、连续性降水 | [低云](low-clouds.md)、[层状云](layered-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0012.xhtml` | 积雨云 CUMULONIMBUS | 5 | 积雨云、悬球状云、幞状云 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0014.xhtml` | 毛状云 FIBRATUS | 3 | 毛状卷云、毛状结构 | [高云](high-clouds.md)、[术语表](glossary.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0015.xhtml` | 堡状云 CASTELLANUS | 3 | 堡状高积云、堡状层积云、对流不稳定 | [中云](mid-clouds.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0016.xhtml` | 波状云 UNDULATUS | 4 | 波状结构、层积云、高积云 | [层状云](layered-clouds.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0017.xhtml` | 网状云 LACUNOSUS | 4 | 网状 / 孔状结构 | [特殊云形](special-forms.md)、[术语表](glossary.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0018.xhtml` | 辐辏状云 RADIATUS | 3 | 辐辏状卷云、积云列、航迹云 | [高云](high-clouds.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0019.xhtml` | 复云 DUPLICATUS | 3 | 多层云片、复云结构 | [层状云](layered-clouds.md)、[术语表](glossary.md) | EPUB 待校订 |
| `OEBPS/Text/Section0006.xhtml` | 幞状云 PILEUS | 3 | 幞状云、积云顶、积雨云发展 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0021.xhtml` | 缟状云 VELUM | 3 | 缟状云、积云 / 积雨云附属云 | [特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0022.xhtml` | 破片云 PANNUS | 3 | 破片云、碎雨云、低层破碎云 | [层状云](layered-clouds.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0023.xhtml` | 悬球状云 MAMMA | 4 | 悬球状云底、积雨云后部、下沉囊状结构 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0024.xhtml` | 幡状云 VIRGA | 4 | 雨幡、雪幡、未达地降水 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0025.xhtml` | 弧状云 ARCUS | 4 | 阵风锋、积雨云前缘、弧状低云 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0026.xhtml` | 管状云 TUBA | 3 | 漏斗云、龙卷胚胎、积雨云底 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0027.xhtml` | 砧状云 INCUS | 3 | 云砧、积雨云成熟阶段、伪卷云 | [积云与积雨云](cumulus-cumulonimbus.md)、[高云](high-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0029.xhtml` | 开尔文--亥姆霍兹波 | 4 | 剪切不稳定、波浪状云 | [特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0030.xhtml` | 航迹云 CONTRAILS | 3 | 飞机尾迹、人工卷云线 | [特殊云形](special-forms.md)、[云的观测方法](observation.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0031.xhtml` | 火积云 PYROCUMULUS | 4 | 火灾 / 火山触发对流云 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0032.xhtml` | 滚轴云 ROLL CLOUD | 4 | 孤立水平管状低云、阵风锋相关云 | [特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0033.xhtml` | 雨幡洞云 FALLSTREAK HOLE | 3 | 云洞、冰晶播撒、降水幡 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0034.xhtml` | 马蹄涡 HORSESHOE VORTEX | 4 | 小尺度涡旋云 | [特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0035.xhtml` | 雾和霭 FOG & MIST | 4 | 雾、霭、能见度 | [云与天气现象](weather-phenomena.md)、[层状云](layered-clouds.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0036.xhtml` | 钻石尘 DIAMOND DUST | 3 | 近地冰晶、寒冷地区光象 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0037.xhtml` | 贝母云 NACREOUS | 4 | 平流层云、虹彩、极地 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0038.xhtml` | 夜光云 NOCTILUCENT | 3 | 中间层云、暮光观测 | [特殊云形](special-forms.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0040.xhtml` | 华 CORONA | 4 | 云滴衍射、日华月华 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0041.xhtml` | 曙暮光条 CREPUSCULAR RAYS | 4 | 云隙光、低太阳高度光束 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0042.xhtml` | 宝光 GLORY | 4 | 反日点光环、飞机 / 山地观测 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0043.xhtml` | 彩虹 RAINBOW | 5 | 虹、霓、降水水滴 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0044.xhtml` | 云虹 CLOUD BOW | 3 | 小水滴、淡色虹 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0045.xhtml` | 22 度晕 22° HALO | 4 | 冰晶折射、卷层云 | [高云](high-clouds.md)、[云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0046.xhtml` | 幻日 SUNDOGS | 4 | 22 度幻日、冰晶取向 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0047.xhtml` | 环天顶弧 CIRCUMZENITHAL ARC | 4 | 高空冰晶光象 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/chapter1_0048.xhtml` | 日柱 SUN PILLARS | 4 | 柱状光象、冰晶反射 | [云与天气现象](weather-phenomena.md) | EPUB 待校订 |
| `OEBPS/Text/Section0008.xhtml` | 山帽云和旗云 CAP & BANNER | 4 | 地形云、山帽云、旗云 | [特殊云形](special-forms.md)、[云的观测方法](observation.md) | EPUB 待校订 |
| `OEBPS/Text/Section0010.xhtml` | 虹彩云 IRIDESCENCE | 4 | 虹彩、薄云、云滴尺度 | [云与天气现象](weather-phenomena.md)、[特殊云形](special-forms.md) | EPUB 待校订 |

## 《一天一朵云》文件索引

| EPUB 文件 | 识别内容 | 图片数 | 关键词线索 | 建议并入页面 | 状态 |
| --- | --- | ---: | --- | --- | --- |
| `text/part0002.html` | 云类型高亮列表 / 术语入口 | 0 | 十属、荚状、堡状、悬球状 | [云的分类体系](classification.md)、[术语表](glossary.md) | EPUB 待校订 |
| `text/part0003.html` | 中文版序 | 0 | 观察文化 | [参考资料与来源说明](references.md) | EPUB 待校订 |
| `text/part0004.html` | 书名页 / 引入 | 0 | 积云、卷云 | [云的基础概念](basics.md) | EPUB 待校订 |
| `text/part0005.html` | 早段案例组 | 7 | 开尔文--亥姆霍兹波、虹彩、雾、高积云、荚状云 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第六批案例索引，逐图待校订 |
| `text/part0006.html` | 案例组 | 39 | 幞状云、鬃积雨云、钩卷云、辐辏状高积云、悬球云、宝光、弧状云、贝母云、放射状云、马蹄涡、环地平弧 | [积云与积雨云](cumulus-cumulonimbus.md)、[中云](mid-clouds.md)、[高云](high-clouds.md)、[层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第七批案例索引，逐图待校订 |
| `text/part0007.html` | 案例组 | 17 | 卷云、云街、碎积云、幡状云、环天顶弧、曙暮光条、钻石尘下映日、卷积云 | [高云](high-clouds.md)、[积云与积雨云](cumulus-cumulonimbus.md)、[层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第八批案例索引，逐图待校订 |
| `text/part0008.html` | 案例组 | 49 | 雾、积云、积雨云、高积云、高层云、层云、层积云、网状云、荚状云、堡状云、幞状云、糙面云、滚轴云、宝光、幻日环、极光、行星和星际边界案例 | [基础概念](basics.md)、[低云](low-clouds.md)、[积云与积雨云](cumulus-cumulonimbus.md)、[中云](mid-clouds.md)、[高云](high-clouds.md)、[层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第九批案例索引，逐图待校订 |
| `text/part0009.html` | 案例组 | 10 | 钩卷云艺术史、对日点复杂晕象、山帽云、环天顶弧、重力波层积云、夜光云、曙暮光条、积雨云云底、波状高积云投影、热带辐合带 | [基础概念](basics.md)、[积云与积雨云](cumulus-cumulonimbus.md)、[中云](mid-clouds.md)、[高云](high-clouds.md)、[层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第十批案例索引，逐图待校订 |
| `text/part0010.html` | 大型案例组 | 137 | 十属、荚状、堡状、悬球状、幡状、光象、环地平弧、荚状高积云、穿洞云、夜光云、极光、贝母云、迭浪云、毛卷云、管状云、雨层云、反射虹、艺术 / 行星边界案例 | [积云与积雨云](cumulus-cumulonimbus.md)、[中云](mid-clouds.md)、[高云](high-clouds.md)、[层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已分批建立案例索引；第十二批补入后段 `../images/00230.jpeg` 至 `../images/00260.jpeg`，仍需继续核对遗漏和逐图校订 |
| `text/part0011.html` | 案例组 | 14 | 墙云、日柱、高积云对流单体、多重彩虹、气辉、层积云洞、球状闪电、海洋层积云、波状高积云、乱卷云、瀑成性碎积云、星云边界案例 | [积云与积雨云](cumulus-cumulonimbus.md)、[中云](mid-clouds.md)、[高云](high-clouds.md)、[层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第十一批案例索引，逐图待校订 |
| `text/part0012.html` | 案例组 | 30 | 糙面云、彩虹轮、土星极光、乱卷云、海面蒸汽雾、22 度月晕、雾虹宝光、网状高积云、弧状 / 滩云、云影、环天顶弧和上侧弧 | [层状云](layered-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md)、[高云](high-clouds.md)、[中云](mid-clouds.md)、[观测方法](observation.md) | 已建第四批案例索引；本轮已补入 `../images/00275.jpeg` 至 `../images/00304.jpeg` 中可对齐的图片路径和纸书页码线索，图片授权、个别页码、母云判定和术语规范仍待校订 |
| `text/part0013.html` | 案例组 | 41 | 悬球云、雨层云、荚状高积云、高积云幡状云、ISS 宝光、钻石尘幻日、层云宝光、糙面云、悬球状卷云与积雨云对照、耗散尾迹、少女峰旗云虹彩 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md)、[中云](mid-clouds.md)、[高云](high-clouds.md)、[层状云](layered-clouds.md)、[云与天气现象](weather-phenomena.md)、[观测方法](observation.md) | 已建第四批案例索引；本轮已补入 `../images/00308.jpeg` 至 `../images/00345.jpeg` 中可对齐的核心图片路径和纸书页码线索，图片授权、母云判定、耗散尾迹具体图序和个别艺术图像边界仍待校订 |
| `text/part0014.html` | 短案例组 | 4 | 双重彩虹、荚状高积云、积云、层云、高积云、卷层云 | [中云](mid-clouds.md)、[高云](high-clouds.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 已建第五批案例索引；已对齐 `../images/00346.jpeg` 至 `../images/00349.jpeg` 和纸书页码 336-339，页码 83 的同名摄影者线索、图像授权和少数云类细分仍待校订 |
| `text/part0015.html` | 后段案例组 | 9 | 碎层云、碎积云、外接晕、雾、高积云、钻石尘、迭浪云、艺术边界案例 | [层状云](layered-clouds.md)、[积云与积雨云](cumulus-cumulonimbus.md)、[高云](high-clouds.md)、[云与天气现象](weather-phenomena.md)、[特殊云形](special-forms.md)、[观测方法](observation.md) | 已建第五批案例索引；已对齐 `../images/00350.jpeg` 至 `../images/00358.jpeg` 和纸书页码 340-347，艺术图像边界、姓名译写、图像授权和光象中文名仍待校订 |
| `text/part0016.html` | 图片来源 | 0 | 页码、图片来源、摄影信息线索 | [EPUB 图文案例索引](epub-case-index.md) | 已开始用于纸书页码线索校订，图片路径和授权待校订 |
| `text/part0017.html` | 索引 | 0 | 中文名、英文名、专名索引、纸书页码线索 | [术语表](glossary.md)、[特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 已建立索引抽取表；本轮补入滚轴云 / 滚卷状云、云虹、宝光、幻日环、下映日、环地平弧、上侧弧 / 切弧、曙暮光条、极光和极地层结等页码线索；仍需逐条回查正文、图片路径、图片来源和授权 |

## 《一天一朵云》索引抽取表

`text/part0017.html` 明确说明“文内页码对应中文版纸书页码，电子版可搜索中文名称查找对应内容”。下表只记录索引条目、中文译名和纸书页码线索，用于后续在 EPUB 正文和图片来源中回查；它不能替代逐图校订。

| 索引项 | 中文索引名 | 纸书页码线索 | 主题归属 | 待校订项 |
| --- | --- | --- | --- | --- |
| `actinoform` | 放射状云 | 36 | [特殊云形](special-forms.md) | 是否按卫星云型、层积云组织或独立特殊云形处理 |
| `fluctus` / Kelvin-Helmholtz wave clouds | 迭浪云；开尔文--亥姆霍兹波 | `fluctus`：8、32、95、237、347；开尔文--亥姆霍兹波：8、32、95、347 | [特殊云形](special-forms.md) | `fluctus` 与开尔文--亥姆霍兹波的译名和分类关系 |
| `asperitas` | 糙面云 | 26、93、264、317 | [特殊云形](special-forms.md)、[层状云](layered-clouds.md) | 2017 年正式命名表述、图例归属 |
| `fallstreak holes` / `hole-punch clouds` | 落幡洞云；穿洞云 | 186、221、332 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 与《云彩收集者手册》“雨幡洞云”译名统一 |
| `wall clouds` | 墙云 | 73、143、244、252 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 与积雨云、管状云、龙卷潜势的边界 |
| `shelf clouds` | 滩云 | 24、281 | [特殊云形](special-forms.md) | 与弧状云、滚轴云、阵风锋云的译名关系 |
| `roll clouds` / `volutus` | 滚轴云、滚卷状云 | `roll clouds`：105、160、235；`volutus`：105、160、235 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 滚轴云、滚卷状云和弧状云 / 滩云的边界 |
| `mamma` | 悬球云、悬球状积雨云、悬球状卷云 | 22、159、302、320 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | `mamma` 中文名和母云差异 |
| `pileus` | 幞状云 | 9、100、231 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | 与《中国云图》“帽状云”图 24 对接 |
| `velum` | 缟状云 | 231、268 | [特殊云形](special-forms.md) | 与幞状云、层状残留云幕区分 |
| `pannus` | 破片云 | 194 | [层状云](layered-clouds.md)、[特殊云形](special-forms.md) | 与碎层云、碎雨云译名关系 |
| `virga` | 幡状云 | 57、306 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 雨幡、雪幡、降水线迹的区分 |
| `arcus` | 弧状云 | 24、281 | [特殊云形](special-forms.md) | 与滩云、滚轴云边界 |
| `tubas` | 管状云 | 243、252 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 漏斗云、龙卷、水龙卷边界 |
| `incus` | 砧状云 | 42、83、302 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | 与云砧、伪卷云对接 |
| `contrails` | 航迹云 | 94、136、229、318、333 | [特殊云形](special-forms.md)、[云的观测方法](observation.md) | 与飞机凝结尾迹、人工高云关系 |
| `aircraft dissipation trails` | 飞机耗散尾迹 | 134、332 | [特殊云形](special-forms.md) | `distrail` 中文译名和成因 |
| `homogenitus` | 人为云、 人为积云 | 150 | [特殊云形](special-forms.md) | 与 WMO `homogenitus`、`homomutatus` 边界 |
| `noctilucent clouds` | 夜光云 | 114、155、229 | [特殊云形](special-forms.md) | 高度、纬度、季节和观测时间 |
| `nacreous clouds` | 贝母云 | 27、236、323 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 珠母云 / 贝母云译名统一 |
| `diamond dust` | 钻石尘 | 60、97、149、310 | [云与天气现象](weather-phenomena.md) | 近地冰晶、寒冷地区光象关系 |
| `advection fog` | 平流雾 | 30、172 | [云与天气现象](weather-phenomena.md)、[层状云](layered-clouds.md) | 与《中国云图》海雾、锋面雾分类对接 |
| `radiation fog` | 辐射雾 | 184 | [云与天气现象](weather-phenomena.md) | 与《中国云图》辐射雾图 197-200 对接 |
| `river smoke fog` | 河雾 | 282 | [云与天气现象](weather-phenomena.md) | 与蒸发雾、锋面雾、海雾边界 |
| `fogbows` | 雾虹 | 277 | [云与天气现象](weather-phenomena.md) | 与云虹、虹、霓的光学差异 |
| `cloudbows` | 云虹 | 154 | [云与天气现象](weather-phenomena.md) | 与雾虹、虹、霓的光学差异 |
| `glories` | 宝光 | 23、81、277、309、315 | [云与天气现象](weather-phenomena.md)、[云的观测方法](observation.md) | 与布罗肯幽灵、飞机宝光和山地宝光关系 |
| `sun dogs` | 幻日 | 84、97、175、183、310、345 | [云与天气现象](weather-phenomena.md) | 与《中国云图》“假日”术语统一 |
| `sun pillars` | 日柱 | 215、253 | [云与天气现象](weather-phenomena.md) | 日出日落低太阳高度个例 |
| `parhelic circles` / `subparhelic circles` | 幻日环、下幻日环 | `parhelic circles`：84、97、110、175、183、310、345；`subparhelic circles`：110 | [云与天气现象](weather-phenomena.md) | 与幻日、22 度晕和飞机视角对日点晕象关系 |
| `sub-suns` | 下映日 | 60 | [云与天气现象](weather-phenomena.md)、[云的观测方法](observation.md) | 需从飞机 / 高处视角回查正文案例 |
| `circumhorizon arcs` | 环地平弧 | 39、219 | [云与天气现象](weather-phenomena.md) | 与环天顶弧、虹彩和“火彩虹”误称区分 |
| `circumzenithal arcs` | 环天顶弧 | 52、112、149、227、293 | [云与天气现象](weather-phenomena.md) | 与晕族光象分类 |
| `circumscribed halo` | 外接晕 | 343 | [云与天气现象](weather-phenomena.md) | 中文名和冰晶几何机制 |
| `supralateral arcs` / `tangent arcs` | 上侧弧、切弧 | `supralateral arcs`：149、293；`tangent arcs`：141、149、345；`upper tangent arcs`：141 | [云与天气现象](weather-phenomena.md) | 晕族光弧中文名、几何机制和同图关系 |
| `Brocken spectres` | 布罗肯幽灵 | 23、81、277、309、315 | [云与天气现象](weather-phenomena.md)、[云的观测方法](observation.md) | 与宝光、反日点光象关系 |
| `anti-crepuscular rays` | 反曙暮光条 | 131、297 | [云与天气现象](weather-phenomena.md) | 与曙暮光条几何关系 |
| `crepuscular rays` | 曙暮光条 | 58、62、115、147、173、197、217、233、297 | [云与天气现象](weather-phenomena.md) | 与《中国云图》曙暮光弧、反曙暮光条和文化名关系 |
| `anti-solar effects` | 对日效应 | 110 | [云与天气现象](weather-phenomena.md) | 包含宝光、布罗肯幽灵等现象的范围 |
| `aurora australis` / `aurora borealis` | 南极光、北极光 | 南极光：72、195；北极光：72、230 | [云与天气现象](weather-phenomena.md)、[特殊云形](special-forms.md) | 极光不是云；需与珠母云、夜光云和高层大气边界分开 |
| `polar mesospheric` / `polar stratospheric` | 极地中间层、极地平流层 | 极地中间层：114、155、229；极地平流层：27、236、323 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 对接夜光云 / 极地中间层云与贝母云 / 珠母云 |

## 术语和主题映射

| 术语 | 可能中文名 / 别名 | 主题归属 | 已并入页面 | 待校订项 |
| --- | --- | --- | --- | --- |
| `mamma` | 悬球状云、乳状云 | 附属云 / 积雨云云底形态 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | 中文译名差异、图片案例、页码 |
| `pileus` | 幞状云、帽状云 | 附属云 / 积云顶帽 | [积云与积雨云](cumulus-cumulonimbus.md)、[特殊云形](special-forms.md) | 与《中国云图》图 24 的对应关系 |
| `velum` | 缟状云、幕状云 | 附属云 / 扩展云幕 | [特殊云形](special-forms.md) | 中文译名、典型图例 |
| `incus` | 云砧、砧状云 | 积雨云成熟期顶部 | [积云与积雨云](cumulus-cumulonimbus.md)、[高云](high-clouds.md) | 伪卷云边界、案例图 |
| `virga` | 幡状云、雨幡、雪幡 | 未达地降水 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 雨幡 / 雪幡区分 |
| `arcus` | 弧状云 | 积雨云前缘、阵风锋 | [特殊云形](special-forms.md) | 与滚轴云、陆架云译名关系 |
| `tuba` | 管状云、漏斗云 | 积雨云底旋转伸展云 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 与龙卷、漏斗云边界 |
| `lenticularis` | 荚状云 | 地形波、波动云 | [中云](mid-clouds.md)、[特殊云形](special-forms.md) | 云属归属和具体案例 |
| `castellanus` | 堡状云 | 中层 / 高层不稳定 | [中云](mid-clouds.md)、[特殊云形](special-forms.md) | 与积云性高积云、堡状层积云区分 |
| `floccus` | 絮状云 | 小团絮状、降水幡可能 | [中云](mid-clouds.md)、[术语表](glossary.md) | 译名和图例 |
| `undulatus` | 波状云 | 波动变种 | [层状云](layered-clouds.md)、[特殊云形](special-forms.md) | 与地形波、重力波案例对应 |
| `radiatus` | 辐辏状云 | 透视汇聚云列 | [高云](high-clouds.md)、[特殊云形](special-forms.md) | 云属适用范围 |
| `duplicatus` | 复云 | 多层叠置 | [层状云](layered-clouds.md)、[术语表](glossary.md) | 中文名和图例 |
| `lacunosus` | 网状云、孔状云 | 云片孔洞结构 | [特殊云形](special-forms.md) | 中文译名 |
| `asperitas` | 糙面云 | 层积云 / 高积云下表面波皱 | [层状云](layered-clouds.md)、[特殊云形](special-forms.md) | 2017 年命名表述、案例来源 |
| `contrails` | 航迹云、飞机尾迹 | 人工云 / 高空凝结尾迹 | [特殊云形](special-forms.md) | 持续尾迹与普通尾迹区分 |
| `fallstreak hole` | 雨幡洞云、云洞 | 冰晶触发、局地降水幡 | [特殊云形](special-forms.md) | 译名和成因描述 |
| `pyrocumulus` | 火积云 | 火灾 / 火山热力对流 | [特殊云形](special-forms.md) | 与积云、积雨云等级关系 |
| `roll cloud` | 滚轴云 | 水平管状低云 | [特殊云形](special-forms.md) | 与弧状云、阵风锋关系 |
| `horseshoe vortex` | 马蹄涡 | 小尺度水平涡旋云 | [特殊云形](special-forms.md) | 是否作为正式云类、中文译名 |
| `distrail` | 耗散尾迹 | 飞机穿云造成的线状空隙 | [特殊云形](special-forms.md) | 与航迹云相反的机制、译名 |
| `cap cloud` / `banner cloud` | 山帽云、旗云 | 地形云 / 山地云 | [特殊云形](special-forms.md) | 与《中国云图》珠峰旗云图版对接 |
| `nacreous` | 贝母云、珠母云 | 极地平流层云 | [特殊云形](special-forms.md)、[云与天气现象](weather-phenomena.md) | 中文译名和高度范围 |
| `noctilucent` | 夜光云 | 中间层云 | [特殊云形](special-forms.md) | 高度、季节和观测纬度 |
| `corona` | 华 | 衍射光象 | [云与天气现象](weather-phenomena.md) | 与虹彩区分 |
| `glory` | 宝光 | 反日点光象 | [云与天气现象](weather-phenomena.md) | 飞机 / 山地案例 |
| `cloud bow` | 云虹 | 小水滴虹 | [云与天气现象](weather-phenomena.md) | 与雾虹、彩虹差异 |
| `22° halo` | 22 度晕 | 冰晶晕 | [高云](high-clouds.md)、[云与天气现象](weather-phenomena.md) | 与卷层云天气意义 |
| `sundogs` | 幻日、假日 | 冰晶光象 | [云与天气现象](weather-phenomena.md) | 译名统一 |
| `sun pillars` | 日柱 | 冰晶反射光象 | [云与天气现象](weather-phenomena.md) | 日出日落案例 |

## 图片和图注抽取规则

后续从 EPUB 抽取图文案例时，每条记录至少应包含：

| 字段 | 说明 | 当前处理 |
| --- | --- | --- |
| 来源书名 | 《云彩收集者手册》或《一天一朵云》 | 可确定 |
| EPUB 内文件 | 如 `OEBPS/Text/chapter1_0023.xhtml` | 可确定 |
| 图片路径 | EPUB 内部图片文件名 | 待抽取 |
| 原书页码 / 中文版页码 | 需要结合图片来源页或印刷页码 | 待校订 |
| 条目标题 | 云类、现象或每日案例标题 | 待抽取 |
| 中文名 / 英文名 / 拉丁名 | 术语对照 | 待校订 |
| 地点 | 原图注给出的地点 | 待校订 |
| 时间 / 日期 | 原图注或每日条目日期 | 待校订 |
| 拍摄者 / 供图者 | 原图注、图片来源或云彩欣赏协会信息 | 待校订 |
| 原图注摘要 | 只摘录必要信息，避免整段复制 | 待校订 |
| 识别要点 | 由主题页归纳，需标注依据 | 待校订 |
| 天气意义 | 区分书中明确说明和编辑归纳 | 待校订 |
| 并入位置 | 主题页、术语表、图例库或仅保留索引 | 待定 |

## 后续校订任务

| 优先级 | 任务 | 目标 |
| --- | --- | --- |
| 1 | 解析 `《云彩收集者手册》` 每章图片和相邻图注 | 建立可引用的附属云、特殊云和光象案例表 |
| 2 | 继续校订 `《一天一朵云》` 的大型案例文件，尤其 `part0010.html` 已拆条目的图片路径、图注边界和遗漏图片 | 将 137 张图片逐步补齐为可追溯案例；`part0005.html` 至 `part0009.html`、`part0011.html` 至 `part0015.html` 已进入 [EPUB 图文案例索引](epub-case-index.md)，`part0010.html` 已分多批索引但仍需查漏 |
| 3 | 对照 `part0016.html` 图片来源 | 已开始补纸书页码和摄影者 / 机构来源线索；下一步需批量对齐图片路径、正文图序和授权状态 |
| 4 | 用 `part0017.html` 索引扩展术语表 | 补中文名、英文名、别名和页码 |
| 5 | 将校订后的案例并入主题页 | 不重复整书结构，只把独特案例归入云类、现象或观测方法 |
| 6 | 建立 EPUB 图版 / 案例索引页 | 与《中国云图》图版库并行，但明确校订等级 |

## 来源

- `cloud/云彩收集者手册 (【英】 加文·普雷特—平尼) (z-library.sk, 1lib.sk, z-lib.sk).epub`
- `cloud/一天一朵云（超豪华云彩科普巨制 《云彩收集者手册》作者新作） (加文·普雷特-平尼) (z-library.sk, 1lib.sk, z-lib.sk).epub`
- 本页的文件名、HTML 数、图片数和关键词分布来自 EPUB 解包结构扫描；具体图注事实尚未逐图校订。
