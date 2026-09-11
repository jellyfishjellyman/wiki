---
title: 云观测记录
description: 用一张轻量表格记录云况，并生成可保存的 Markdown 观测条目。
---

# 云观测记录

把抬头看到的云留下来。填写几个关键字段后，可以复制一份结构化 Markdown，放进自己的日志、笔记或 Wiki 页面。

<section class="observation-tool" data-observation-tool>
  <form class="observation-form" data-observation-form>
    <div class="observation-form-heading">
      <div>
        <p class="observation-kicker">FIELD NOTE</p>
        <h2>今天的天空</h2>
      </div>
      <span class="observation-status" data-observation-status aria-live="polite">草稿会保存在本机</span>
    </div>

    <div class="observation-fields">
      <label>日期<input type="date" name="date"></label>
      <label>时间<input type="time" name="time"></label>
      <label>地点<input type="text" name="location" placeholder="例如：北京·海淀"></label>
      <label>观察方向
        <select name="direction">
          <option value="">未记录</option>
          <option>北</option><option>东北</option><option>东</option><option>东南</option>
          <option>南</option><option>西南</option><option>西</option><option>西北</option>
        </select>
      </label>
      <label>云族 / 初步判断<input type="text" name="cloud" placeholder="例如：低云 · 层积云"></label>
      <label>云量
        <select name="cover">
          <option value="">未记录</option><option>晴空或少云</option><option>疏云</option><option>裂云</option><option>多云</option><option>阴天</option>
        </select>
      </label>
      <label>天气现象<input type="text" name="weather" placeholder="例如：无降水，有薄雾"></label>
      <label>云的变化<input type="text" name="change" placeholder="例如：向东移动，逐渐增厚"></label>
      <label class="observation-wide">识别依据<textarea name="features" rows="4" placeholder="记录形态、云底、透光性、排列方式或与其他云的关系"></textarea></label>
      <label class="observation-wide">补充笔记<textarea name="notes" rows="4" placeholder="光线、地形、风、温度感受，或稍后想查证的疑问"></textarea></label>
    </div>

    <div class="observation-actions">
      <button class="observation-primary" type="button" data-observation-copy>复制 Markdown</button>
      <button class="observation-secondary" type="button" data-observation-download>下载记录</button>
      <button class="observation-quiet" type="button" data-observation-clear>清空</button>
    </div>
  </form>

  <aside class="observation-preview" aria-live="polite">
    <div class="observation-preview-top">
      <p class="observation-kicker">MARKDOWN PREVIEW</p>
      <span>实时生成</span>
    </div>
    <pre data-observation-preview></pre>
  </aside>
</section>

!!! note "记录建议"
    单张照片适合记录形态，连续观察更适合判断云的演变和天气意义。无法确定云类时，先记录可见特征，不必急着命名。

## 观测字段

需要更系统的观察时，可以参考 [云的观测方法](observation.md) 中的观测要素、校订原则和记录格式。
