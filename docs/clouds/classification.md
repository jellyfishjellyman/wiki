# 云的分类体系

!!! note "第七批整理范围"
    本页吸收《中国云图》文字说明中的“云的分类”“云的编码”和“云的特征”三部分，重点整理 PDF 第 13 页表 1 和 PDF 第 18-19 页表 2。这里解决三个问题：云族、云属、云类如何命名；《中国云图》的 `CL`、`CM`、`CH` 云码如何使用；主题页中的细分条目应如何回接到原始图版和国际分类术语。两本 EPUB 中的现代云种、附属云和观察案例仍以概念线索并入，尚未完成逐图校订。

## 分类层级

《中国云图》采用地面观测和天气预报实用取向：先按云底高度分低云、中云、高云三族，再按宏观外形、物理结构和成因分为十属、二十九类云状。这个体系与国际通行的十云属体系兼容，但《中国云图》的“云类”和 `CL/CM/CH` 云码是观测编码层面的细分，不应和拉丁学名层级简单等同。

| 层级 | 含义 | 例子 | 在本 Wiki 中的用途 |
| --- | --- | --- | --- |
| 云族 | 按云底高度和观测习惯划分的大类 | 低云、中云、高云 | 导航页和主题总览 |
| 云属 | 云分类的主要形态层级 | 积云、层积云、高积云、卷云 | 云族页和云属专题页 |
| 云类 | 《中国云图》表 1 中的细分云状 | 淡积云、鬃积雨云、荚状高积云、薄幕卷层云 | 细粒度条目和图版索引 |
| 云码 | 地面观测云编码，分低云 `CL`、中云 `CM`、高云 `CH` | `CL1`、`CM8`、`CH7` | 图版字段、观测记录和云类组合判断 |
| 附属云 / 特征 | 横跨多个云属的特殊形态 | 云砧、雨幡、悬球状云底、幞状云 | [特殊云形](special-forms.md) 和具体云属页 |
| 天气现象 | 与云相伴但不一定属于云的现象 | 闪电、虹、雾、沙尘暴 | [云与天气现象](weather-phenomena.md) |

## 三族十属

| 云族 | 云属 | 一般云底高度 | 组成和天气意义 |
| --- | --- | --- | --- |
| 低云 | 积云、积雨云、层积云、层云、雨层云 | 多低于 2500 米，随季节、天气、地理位置变化 | 多由水滴组成；厚云或直展云中上部可含过冷水滴、冰晶、雪晶。积雨云多阵性降水、雷电、冰雹；雨层云多连续性降水。 |
| 中云 | 高层云、高积云 | 一般 2500-5000 米 | 可由微小水滴、过冷水滴、冰晶、雪晶混合组成。高层云常与锋面云系有关；高积云可显示波动、逆温、不稳定或天气系统移入。 |
| 高云 | 卷云、卷层云、卷积云 | 一般 5000 米以上，高原地区可较低 | 多由冰晶组成。卷云和卷层云系统性增厚、降低时常提示天气系统接近；卷层云可产生晕、假日、日柱等光象。 |

高度界限不是硬边界。高原、冬季、强天气系统、飞机观测和山地地形都会改变云底高度感知，因此本 Wiki 优先保留原书图版字段和观测条件，而不是只按固定高度判断。

## 表 1：云类总表

| 云族 | 云属 | 云属缩写 | 云类 | 云类缩写 | 拉丁文学名 | 主题页 |
| --- | --- | --- | --- | --- | --- | --- |
| 低云 | 积云 | Cu | 淡积云 | Cu hum | Cumulus humilis | [积云与积雨云](cumulus-cumulonimbus.md) |
| 低云 | 积云 | Cu | 碎积云 | Fc | Fractocumulus | [积云与积雨云](cumulus-cumulonimbus.md) |
| 低云 | 积云 | Cu | 浓积云 | Cu cong | Cumulus congestus | [积云与积雨云](cumulus-cumulonimbus.md) |
| 低云 | 积雨云 | Cb | 秃积雨云 | Cb calv | Cumulonimbus calvus | [积云与积雨云](cumulus-cumulonimbus.md) |
| 低云 | 积雨云 | Cb | 鬃积雨云 | Cb cap | Cumulonimbus capillatus | [积云与积雨云](cumulus-cumulonimbus.md) |
| 低云 | 层积云 | Sc | 透光层积云 | Sc tra | Stratocumulus translucidus | [层状低云](layered-clouds.md) |
| 低云 | 层积云 | Sc | 蔽光层积云 | Sc op | Stratocumulus opacus | [层状低云](layered-clouds.md) |
| 低云 | 层积云 | Sc | 积云性层积云 | Sc cug | Stratocumulus cumulogenitus | [层状低云](layered-clouds.md) |
| 低云 | 层积云 | Sc | 堡状层积云 | Sc cast | Stratocumulus castellanus | [层状低云](layered-clouds.md)、[特殊云形](special-forms.md) |
| 低云 | 层积云 | Sc | 荚状层积云 | Sc lent | Stratocumulus lenticularis | [层状低云](layered-clouds.md)、[特殊云形](special-forms.md) |
| 低云 | 层云 | St | 层云 | St | Stratus | [层状低云](layered-clouds.md) |
| 低云 | 层云 | St | 碎层云 | Fs | Fractostratus | [层状低云](layered-clouds.md) |
| 低云 | 雨层云 | Ns | 雨层云 | Ns | Nimbostratus | [层状低云](layered-clouds.md) |
| 低云 | 雨层云 | Ns | 碎雨云 | Fn | Fractonimbus | [层状低云](layered-clouds.md) |
| 中云 | 高层云 | As | 透光高层云 | As tra | Altostratus translucidus | [中云](mid-clouds.md) |
| 中云 | 高层云 | As | 蔽光高层云 | As op | Altostratus opacus | [中云](mid-clouds.md) |
| 中云 | 高积云 | Ac | 透光高积云 | Ac tra | Altocumulus translucidus | [中云](mid-clouds.md) |
| 中云 | 高积云 | Ac | 蔽光高积云 | Ac op | Altocumulus opacus | [中云](mid-clouds.md) |
| 中云 | 高积云 | Ac | 荚状高积云 | Ac lent | Altocumulus lenticularis | [中云](mid-clouds.md)、[特殊云形](special-forms.md) |
| 中云 | 高积云 | Ac | 积云性高积云 | Ac cug | Altocumulus cumulogenitus | [中云](mid-clouds.md) |
| 中云 | 高积云 | Ac | 絮状高积云 | Ac flo | Altocumulus floccus | [中云](mid-clouds.md) |
| 中云 | 高积云 | Ac | 堡状高积云 | Ac cast | Altocumulus castellanus | [中云](mid-clouds.md)、[特殊云形](special-forms.md) |
| 高云 | 卷云 | Ci | 毛卷云 | Ci fil | Cirrus filosus | [高云](high-clouds.md) |
| 高云 | 卷云 | Ci | 密卷云 | Ci dens | Cirrus densus | [高云](high-clouds.md) |
| 高云 | 卷云 | Ci | 伪卷云 | Ci not | Cirrus nothus | [高云](high-clouds.md) |
| 高云 | 卷云 | Ci | 钩卷云 | Ci unc | Cirrus uncinus | [高云](high-clouds.md) |
| 高云 | 卷层云 | Cs | 毛卷层云 | Cs fil | Cirrostratus filosus | [高云](high-clouds.md) |
| 高云 | 卷层云 | Cs | 薄幕卷层云 | Cs nebu | Cirrostratus nebulosus | [高云](high-clouds.md) |
| 高云 | 卷积云 | Cc | 卷积云 | Cc | Cirrocumulus | [高云](high-clouds.md) |

!!! note "拉丁名待校订"
    上表依据《中国云图》PDF 第 13 页表 1 转写。若与现行 WMO 国际云图或新版术语存在拼写、层级或中文译名差异，后续应在 [术语表](glossary.md) 中保留差异说明，不直接覆盖原书字段。结构化术语索引见 [术语表：核心云类结构化表](glossary.md)。

## 云码不是云类名

`CL`、`CM`、`CH` 是观测编码，不是单个云类的永久标签。它们常表达“当前天空中最需要报告的低云/中云/高云状态”，可能包含云类组合、演变趋势和云量优势。例如：

| 情况 | 分类名 | 可能云码 | 说明 |
| --- | --- | --- | --- |
| 淡积云和碎积云 | Cu hum / Fc | `CL1` | 同一云码容纳两种弱对流或破碎积云。 |
| 浓积云伴淡积云或层积云 | Cu cong 等 | `CL2` | 重点是垂直发展旺盛，且云底在同一高度附近。 |
| 积云性层积云 | Sc cug | `CL4` | 由积云扩展而成。 |
| 非积云性层积云 | Sc | `CL5` | 层积云不是由积云扩展而成。 |
| 雨层云和碎雨云 | Ns / Fn | `CL7`、`CM2` | 同一图版可同时标低云碎雨云和中云/雨层云状态。 |
| 荚状高积云 | Ac lent | `CM4` | 表示连续变化中的透光高积云或荚状云片。 |
| 堡状或絮状高积云 | Ac cast / Ac flo | `CM8` | 重点是中层积状不稳定信号。 |
| 卷层云布满全天 | Cs | `CH7` | 高云编码根据覆盖和系统侵入状态，而不只是云属。 |

因此主题页写作时应同时保留中文云类、云属缩写、拉丁名、云码和图版来源；不能只用一个代码代替完整分类判断。

## 低云编码 `CL`

| 电码 | 技术性说明 | 观测含义 | 主题页 |
| --- | --- | --- | --- |
| `CL0` | 没有 `CL` 云 | 没有层积云、层云、积云、积雨云 | [低云](low-clouds.md) |
| `CL1` | 淡积云或碎积云，或两者同现 | 垂直发展很小、形状扁平的积云或碎积云 | [积云与积雨云](cumulus-cumulonimbus.md) |
| `CL2` | 浓积云，可伴淡积云、碎积云或层积云，云底在同一高度上 | 垂直发展旺盛的塔状积云 | [积云与积雨云](cumulus-cumulonimbus.md) |
| `CL3` | 秃积雨云，可伴积云、层积云或层云 | 顶部轮廓模糊，但不是卷云状或砧状 | [积云与积雨云](cumulus-cumulonimbus.md) |
| `CL4` | 积云性层积云 | 层积云由积云扩展而成，常伴积云 | [层状低云](layered-clouds.md) |
| `CL5` | 非积云性层积云 | 层积云不是由积云扩展而成 | [层状低云](layered-clouds.md) |
| `CL6` | 层云和 / 或碎层云，但不是恶劣天气下碎雨云 | 层云或碎层云同现 | [层状低云](layered-clouds.md) |
| `CL7` | 恶劣天气下的碎雨云，通常在高层云或雨层云之下 | 降水时或降水前后一小段时间内的低碎云 | [层状低云](layered-clouds.md)、[天气现象](weather-phenomena.md) |
| `CL8` | 积云和非积云性层积云同时存在，底部高度不同 | 积云与层积云分属不同云底高度 | [低云](low-clouds.md) |
| `CL9` | 鬃积雨云，常呈砧状 | 具有清晰纤维状或卷云状顶部的积雨云 | [积云与积雨云](cumulus-cumulonimbus.md) |

## 中云编码 `CM`

| 电码 | 技术性说明 | 观测含义 | 主题页 |
| --- | --- | --- | --- |
| `CM0` | 没有 `CM` 云 | 没有高积云、高层云、雨层云 | [中云](mid-clouds.md) |
| `CM1` | 透光高层云 | 薄的半透明高层云，可朦胧看到日月 | [中云](mid-clouds.md) |
| `CM2` | 蔽光高层云或雨层云 | 厚高层云或雨层云；局部可能有较明亮小块 | [中云](mid-clouds.md)、[层状低云](layered-clouds.md) |
| `CM3` | 稳定透光高积云，同一高度 | 云块变化不显著并在同一高度 | [中云](mid-clouds.md) |
| `CM4` | 透光高积云或荚状层积云，连续变化，一个或几个高度 | 常呈荚状，云块不断变化 | [中云](mid-clouds.md)、[特殊云形](special-forms.md) |
| `CM5` | 成带或成层的透光高积云系统侵入天空 | 常全部增厚，部分转为蔽光或复高积云 | [中云](mid-clouds.md) |
| `CM6` | 积云性高积云 | 由积云或积雨云扩展而成 | [中云](mid-clouds.md) |
| `CM7` | 复高积云或蔽光高积云，或高层云与高积云同现 | 双层、不透明或中云复合状态 | [中云](mid-clouds.md) |
| `CM8` | 积云状高积云或堡状层积云 | 絮状、堡状或小塔状中云/层积云 | [中云](mid-clouds.md)、[特殊云形](special-forms.md) |
| `CM9` | 混乱天空高积云，常在几个高度上 | 多高度、多形态高积云混杂 | [中云](mid-clouds.md) |

## 高云编码 `CH`

| 电码 | 技术性说明 | 观测含义 | 主题页 |
| --- | --- | --- | --- |
| `CH0` | 没有 `CH` 云 | 没有卷云、卷层云、卷积云 | [高云](high-clouds.md) |
| `CH1` | 毛卷云分散在天空，不系统侵盖 | 丝状、条状卷云，俗称马尾云 | [高云](high-clouds.md) |
| `CH2` | 密卷云呈散片或曲束状，通常量不增加 | 有时像积雨云顶部残余；不能判断来自积雨云时可报此码 | [高云](high-clouds.md) |
| `CH3` | 伪卷云或积雨云顶部残余 | 卷云常呈砧状，源于可见或不可见母体积雨云 | [高云](high-clouds.md)、[特殊云形](special-forms.md) |
| `CH4` | 卷云通常为钩卷云，有系统地侵盖天空并增厚 | 钩状卷云逐渐伸展 | [高云](high-clouds.md) |
| `CH5` | 辐辏状卷云和卷层云，或只有卷层云，前缘高度角不到 45 度 | 系统侵入但前缘仍较低 | [高云](high-clouds.md) |
| `CH6` | 辐辏状卷云和卷层云，或只有卷层云，前缘高度角超过 45 度但未布满全天 | 系统侵入更明显 | [高云](high-clouds.md) |
| `CH7` | 卷层云布满全天 | 高云幕遮蔽整个天空 | [高云](high-clouds.md)、[天气现象](weather-phenomena.md) |
| `CH8` | 卷层云非系统侵盖，也未布满全天 | 非系统性卷层云 | [高云](high-clouds.md) |
| `CH9` | 卷积云 | 卷积云量多于其他高云，可伴卷云或卷层云 | [高云](high-clouds.md) |

## 识别顺序

1. 先判断是否有低云、中云、高云分别存在，不要只选一种云。
2. 对每一族分别判断主导云属和最有报告意义的状态。
3. 再用形态、透光性、云底高度、云顶结构和演变趋势选择云类或云码。
4. 遇到多个高度或多个云属同现时，保留组合，例如 `CL7 CM2`、`CM8 CH2`。
5. 记录不确定性：如果只能判断为“层积云”而不能确定积云性或非积云性，应写“层积云，代码待校订”。
6. 最后把判断链接到图版和主题页，避免孤立术语。

## 中国云图分类与国际分类的关系

《中国云图》前言说明其内容参考 WMO 修订过的云类内容，并以中国气象局 2003 年颁布的《地面气象观测规范》为依据。因而它兼具国际分类和中国地面观测业务规则两个层面。

| 关系 | 说明 |
| --- | --- |
| 十云属基本一致 | 积云、积雨云、层积云、层云、雨层云、高层云、高积云、卷云、卷层云、卷积云与国际十云属框架相通。 |
| 细分名带有观测业务色彩 | 透光、蔽光、积云性、堡状、荚状、絮状等在图版中服务于识别和编码。 |
| 云码是地面观测报告工具 | `CL/CM/CH` 不是拉丁学名，而是把云类、云量优势、演变和系统侵入状态综合成电码。 |
| EPUB 术语需要并列校订 | `mamma`、`pileus`、`velum`、`arcus`、`tuba`、`asperitas` 等现代或国际术语在两本 EPUB 中出现，但与《中国云图》中文名或图版对应仍需逐条确认。 |

## 来源

- 《中国云图》PDF 第 13 页表 1：云的分类。
- 《中国云图》PDF 第 18-19 页表 2：云的编码。
- [《中国云图》云的分类结构化表](china-cloud-atlas/text/cloud-classification.md)。
- [《中国云图》云的编码结构化表](china-cloud-atlas/text/cloud-coding.md)。
- [《中国云图》云的特征](china-cloud-atlas/text/cloud-features.md)。
- 《云彩收集者手册》EPUB：现代云种、附属云、特殊云形概念线索。
- 《一天一朵云》EPUB：云观察案例、光象和特殊云形概念线索。
