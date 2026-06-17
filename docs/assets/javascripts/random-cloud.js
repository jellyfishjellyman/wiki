const randomCloudItems = [
  {
    number: "图 53",
    title: "积云性层积云",
    code: "CL4",
    category: "低云 / 层积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-075.webp",
    location: "辽宁 鞍山",
    time: "1999年6月24日06时30分",
    direction: "E",
    summary: "由积云平衍扩展而成的积云性层积云。云体多呈长条形，中间向上凸起，仍保持积云的特征。",
    origin: "积云发展减弱后向水平方向铺展，低层水汽继续凝结，形成带有积云痕迹的层积云。",
    features: "长条或块状云体较常见，云底较低，局部有凸起，云块之间可见缝隙或明暗变化。",
    classification: "本照片归入《中国云图》低云图版中的层积云条目，具体为积云性层积云。",
    source: "../china-cloud-atlas/plates/low-clouds-stratocumulus/"
  },
  {
    number: "图 56",
    title: "透光层积云",
    code: "CL5",
    category: "低云 / 层积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-078.webp",
    location: "内蒙古 呼和浩特",
    time: "1982年7月9日07时05分",
    direction: "E",
    summary: "云块呈灰色，形状不很规则，云块间的缝隙明显呈白色，阳光透过云隙照射到草原上。",
    origin: "低层潮湿空气在较弱抬升或湍流中凝结成片，云层不连续时留下透光云隙。",
    features: "云块较低、成片或成列排列，厚处灰暗，薄处或云隙处能透出天空亮光。",
    classification: "本照片归入层积云中的透光层积云，代码为 CL5。",
    source: "../china-cloud-atlas/plates/low-clouds-stratocumulus/"
  },
  {
    number: "图 60",
    title: "蔽光层积云",
    code: "CL5",
    category: "低云 / 层积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-082.webp",
    location: "广东 深圳",
    time: "1982年6月8日17时10分",
    direction: "SW",
    summary: "蔽光层积云布满全天，呈灰白色。由于云层厚度不均，有深灰浅白之分，远处云底已遮盖山顶。",
    origin: "低层水汽充足且云层横向扩展明显时，层积云可连成较厚云幕，遮蔽日光。",
    features: "覆盖范围大，云层较低且厚薄不均，整体灰白到暗灰，日光难以直接穿透。",
    classification: "本照片归入层积云中的蔽光层积云，代码为 CL5。",
    source: "../china-cloud-atlas/plates/low-clouds-stratocumulus/"
  },
  {
    number: "图 63",
    title: "层积云",
    code: "CL5",
    category: "低云 / 层积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-085.webp",
    location: "西藏 林芝",
    time: "1981年7月14日07时14分",
    direction: "N",
    summary: "雨后转晴，潮湿空气抬升形成了层积云，太阳升高后层积云逐渐消散。高空是分散的高积云。",
    origin: "降水后近地层空气湿度高，受地形或热力作用轻微抬升，水汽在低空凝结成层积云。",
    features: "云底低，云块连片但仍有起伏和块状结构，天气转晴后常随加热和混合而消散。",
    classification: "本照片归入低云中的层积云。",
    source: "../china-cloud-atlas/plates/low-clouds-stratocumulus/"
  },
  {
    number: "图 76",
    title: "积云和层积云",
    code: "CL8",
    category: "低云 / 积云与层积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-098.webp",
    location: "西藏 拉萨",
    time: "1981年6月22日10时10分",
    direction: "E",
    summary: "层积云呈深灰色，云体散乱，未布满全天。山峰附近的层积云正在抬高，发展为淡积云，远处有淡积云。",
    origin: "低层云受山地抬升和局地对流影响，层积云局部抬高并向积云形态发展。",
    features: "同一画面可见层积云的片状低云和积云的凸起结构，说明低云形态正在转化。",
    classification: "本照片归入低云图版中的积云和层积云，代码为 CL8。",
    source: "../china-cloud-atlas/plates/low-clouds-stratocumulus/"
  },
  {
    number: "图 84",
    title: "荚状高积云",
    code: "CM4",
    category: "中云 / 高积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-106.webp",
    location: "原页字段见图版页",
    time: "原页字段见图版页",
    direction: "原页字段见图版页",
    summary: "荚状高积云通常呈透镜或豆荚状，边缘较清楚，常与地形波或稳定层附近的波动有关。",
    origin: "稳定气层中气流越过山地或在波动中升降，水汽在波峰附近凝结、波谷附近蒸发，形成荚状云体。",
    features: "外形似透镜，常单独或成组出现，边缘平滑，厚处较暗，薄边较亮。",
    classification: "本照片归入中云中的荚状高积云。",
    source: "../china-cloud-atlas/plates/mid-clouds-altocumulus/"
  },
  {
    number: "图 117",
    title: "毛卷云",
    code: "CH1",
    category: "高云 / 卷云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-139.webp",
    location: "原页字段见图版页",
    time: "原页字段见图版页",
    direction: "原页字段见图版页",
    summary: "毛卷云具有纤维状、丝缕状外观，多由冰晶组成，常出现在较高空。",
    origin: "高空水汽在低温环境中凝华为冰晶，并被高空风拉伸成丝缕结构。",
    features: "云体纤细、边缘毛丝明显，通常不产生到达地面的降水。",
    classification: "本照片归入高云中的卷云类。",
    source: "../china-cloud-atlas/plates/high-clouds-cirrus/"
  },
  {
    number: "图 149",
    title: "卷积云",
    code: "CH9",
    category: "高云 / 卷积云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-171.webp",
    location: "原页字段见图版页",
    time: "原页字段见图版页",
    direction: "原页字段见图版页",
    summary: "卷积云常呈细小云块或波纹状排列，云块很小，民间常形容为鱼鳞状天空。",
    origin: "高空薄云层在波动或弱不稳定中分裂成细小云块，主要由冰晶组成。",
    features: "云块小而白，排列成群或波纹，单个云块视宽度通常较小。",
    classification: "本照片归入高云中的卷积云。",
    source: "../china-cloud-atlas/plates/high-clouds-cirrostratus-cirrocumulus/"
  },
  {
    number: "图 246",
    title: "珠穆朗玛峰旗云",
    code: "地形云",
    category: "特殊云 / 地形云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-275.webp",
    location: "西藏 珠峰北侧",
    time: "1979年10月",
    direction: "S",
    summary: "云层沿山坡向上伸展，云顶受西风带气流影响，起伏不平，中间波峰比较明显。",
    origin: "强风越过高山时，迎风坡空气被迫抬升冷却凝结，越过山脊后被风拉伸成旗帜状。",
    features: "常贴近山峰一侧出现，云体像旗帜一样从山顶向下风方向飘展。",
    classification: "本照片归入地形云图版中的珠峰旗云。",
    source: "../china-cloud-atlas/plates/terrain-clouds/"
  },
  {
    number: "图 253",
    title: "瀑布云",
    code: "地形云",
    category: "特殊云 / 地形云",
    image: "../../assets/images/clouds/china-cloud-atlas/page-282.webp",
    location: "江西 庐山",
    time: "1986年5月21日07时30分",
    direction: "E",
    summary: "山谷间充满云雾，受逆温层和风向影响，云雾沿水平方向移动，从山岭向下流动，好像山涧瀑布。",
    origin: "山谷云雾在地形和风场引导下越过山脊并下泄，视觉上形成流动的瀑布形态。",
    features: "云雾贴着山地流动，边界柔软，整体运动方向清晰，常见于山地湿润环境。",
    classification: "本照片归入地形云图版中的瀑布云。",
    source: "../china-cloud-atlas/plates/terrain-clouds/"
  }
];

function setRandomCloud(item) {
  const root = document.querySelector("[data-random-cloud-page]");
  if (!root) return;

  const setText = (selector, value) => {
    const element = root.querySelector(selector);
    if (element) element.textContent = value;
  };

  const image = root.querySelector("[data-random-cloud-image]");
  if (image) {
    image.src = item.image;
    image.alt = `${item.number}：${item.title}`;
  }

  setText("[data-random-cloud-number]", item.number);
  setText("[data-random-cloud-code]", item.code);
  setText("[data-random-cloud-title]", item.title);
  setText("[data-random-cloud-summary]", item.summary);
  setText("[data-random-cloud-category]", item.category);
  setText("[data-random-cloud-location]", item.location);
  setText("[data-random-cloud-time]", item.time);
  setText("[data-random-cloud-direction]", item.direction);
  setText("[data-random-cloud-origin]", item.origin);
  setText("[data-random-cloud-features]", item.features);
  setText("[data-random-cloud-classification]", item.classification);
  setText("[data-random-cloud-count]", `${randomCloudItems.length} 张精选图版`);

  const source = root.querySelector("[data-random-cloud-source]");
  if (source) source.href = item.source;
}

document$.subscribe(function () {
  const root = document.querySelector("[data-random-cloud-page]");
  if (!root) return;

  let previousIndex = -1;
  const pick = () => {
    let index = Math.floor(Math.random() * randomCloudItems.length);
    if (randomCloudItems.length > 1) {
      while (index === previousIndex) index = Math.floor(Math.random() * randomCloudItems.length);
    }
    previousIndex = index;
    setRandomCloud(randomCloudItems[index]);
  };

  root.querySelector("[data-random-cloud-next]")?.addEventListener("click", pick);
  pick();
});
