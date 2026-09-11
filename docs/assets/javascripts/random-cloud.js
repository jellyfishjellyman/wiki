(function () {
  const catalogUrl = new URL("/assets/registry/random-clouds.json", window.location.origin);

  function initRandomCloud() {
    const root = document.querySelector("[data-random-cloud-page]");
    if (!root || root.dataset.initialized === "true") return;
    root.dataset.initialized = "true";

    const setText = (selector, value) => {
      const element = root.querySelector(selector);
      if (element) element.textContent = value || "原页未列出";
    };

    const setRandomCloud = (item) => {
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
      setText("[data-random-cloud-count]", `${window.randomCloudItems.length} 张精选图版`);
    };

    const button = root.querySelector("[data-random-cloud-next]");
    const previousLabel = button?.textContent;
    let previousIndex = -1;

    const pick = () => {
      let index = Math.floor(Math.random() * window.randomCloudItems.length);
      while (window.randomCloudItems.length > 1 && index === previousIndex) {
        index = Math.floor(Math.random() * window.randomCloudItems.length);
      }
      previousIndex = index;
      setRandomCloud(window.randomCloudItems[index]);
    };

    const showError = () => {
      setText("[data-random-cloud-summary]", "图版目录暂时没有加载成功，请稍后刷新页面，或直接打开《中国云图》图版清单。");
      if (button) button.disabled = true;
    };

    if (button) {
      button.disabled = true;
      button.textContent = "正在加载图版…";
    }

    fetch(catalogUrl)
      .then((response) => {
        if (!response.ok) throw new Error(`catalog request failed: ${response.status}`);
        return response.json();
      })
      .then((items) => {
        if (!Array.isArray(items) || !items.length) throw new Error("empty catalog");
        window.randomCloudItems = items;
        if (button) {
          button.disabled = false;
          button.textContent = previousLabel || "随机一张";
          button.addEventListener("click", pick);
        }
        pick();
      })
      .catch(showError);
  }

  if (typeof document$ !== "undefined") document$.subscribe(initRandomCloud);
  else document.addEventListener("DOMContentLoaded", initRandomCloud);
})();
