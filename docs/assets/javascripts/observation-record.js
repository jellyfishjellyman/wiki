(function () {
  const storageKey = "gwb-observation-draft";

  function initObservationTool() {
    const root = document.querySelector("[data-observation-tool]");
    if (!root || root.dataset.initialized === "true") return;
    root.dataset.initialized = "true";

    const form = root.querySelector("[data-observation-form]");
    const preview = root.querySelector("[data-observation-preview]");
    const status = root.querySelector("[data-observation-status]");
    const fields = Array.from(form.elements).filter((field) => field.name);
    const valueOf = (name) => form.elements[name]?.value.trim() || "未记录";

    const today = new Date();
    const dateField = form.elements.date;
    if (dateField && !dateField.value) dateField.value = today.toISOString().slice(0, 10);

    const readDraft = () => {
      try {
        return JSON.parse(localStorage.getItem(storageKey) || "{}");
      } catch {
        return {};
      }
    };

    const saveDraft = () => {
      const draft = Object.fromEntries(fields.map((field) => [field.name, field.value]));
      try {
        localStorage.setItem(storageKey, JSON.stringify(draft));
        if (status) status.textContent = "已保存本机草稿";
      } catch {
        if (status) status.textContent = "当前浏览器未允许保存草稿";
      }
    };

    const loadDraft = () => {
      const draft = readDraft();
      fields.forEach((field) => {
        if (draft[field.name]) field.value = draft[field.name];
      });
    };

    const markdown = () => {
      const date = valueOf("date");
      const time = valueOf("time");
      return `# 云观测记录：${date}\n\n- **时间**：${time}\n- **地点**：${valueOf("location")}\n- **方向**：${valueOf("direction")}\n- **云族 / 初步判断**：${valueOf("cloud")}\n- **云量**：${valueOf("cover")}\n- **天气现象**：${valueOf("weather")}\n- **云的变化**：${valueOf("change")}\n\n## 识别依据\n\n${valueOf("features")}\n\n## 补充笔记\n\n${valueOf("notes")}\n`;
    };

    const render = () => {
      if (preview) preview.textContent = markdown();
    };

    const copy = async () => {
      const text = markdown();
      try {
        await navigator.clipboard.writeText(text);
        if (status) status.textContent = "Markdown 已复制";
      } catch {
        if (status) status.textContent = "复制失败，请直接选取右侧预览";
      }
    };

    const download = () => {
      const date = valueOf("date").replace(/[^0-9-]/g, "") || "observation";
      const blob = new Blob([markdown()], { type: "text/markdown;charset=utf-8" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = `cloud-observation-${date}.md`;
      link.click();
      URL.revokeObjectURL(link.href);
      if (status) status.textContent = "记录已下载";
    };

    loadDraft();
    fields.forEach((field) => field.addEventListener("input", () => { render(); saveDraft(); }));
    root.querySelector("[data-observation-copy]")?.addEventListener("click", copy);
    root.querySelector("[data-observation-download]")?.addEventListener("click", download);
    root.querySelector("[data-observation-clear]")?.addEventListener("click", () => {
      form.reset();
      if (dateField) dateField.value = today.toISOString().slice(0, 10);
      localStorage.removeItem(storageKey);
      if (status) status.textContent = "已清空记录";
      render();
    });
    render();
  }

  if (typeof document$ !== "undefined") document$.subscribe(initObservationTool);
  else document.addEventListener("DOMContentLoaded", initObservationTool);
})();
