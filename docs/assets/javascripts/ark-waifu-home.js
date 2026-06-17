(function () {
  const path = window.location.pathname.replace(/\/+$/, "") || "/";
  const isHomePage = path === "/" || path.endsWith("/mywiki") || path.endsWith("/index.html");

  if (!isHomePage || document.querySelector("script[data-gwb-ark-waifu]")) {
    return;
  }

  const script = document.createElement("script");
  script.src = "https://cdn.jsdelivr.net/npm/ark-waifu@1.0.1/dist/ark-waifu.loader.js";
  script.dataset.gwbArkWaifu = "true";
  script.dataset.registryBase = "https://cdn.jsdelivr.net/npm/ark-waifu@1.0.1/dist/registry/";
  script.dataset.model = "models-4134-cetsyr-epoque-50-build-char-4134-cetsyr-epoque-50";
  script.dataset.cdn = "osyb";
  script.dataset.width = "280";
  script.dataset.height = "420";
  script.dataset.zIndex = "4";
  script.dataset.draggable = "true";
  script.dataset.hitTest = "true";
  script.dataset.clickAction = "touch";
  script.dataset.defaultAction = "auto";
  script.dataset.loadStrategy = "after-load";
  script.dataset.maxDpr = "1.25";
  script.dataset.fpsLimit = "24";
  script.dataset.bubbleDurationMs = "4200";
  script.dataset.tipsUrl = new URL("assets/registry/ark-waifu-home-tips.json", window.location.href).href;

  document.body.appendChild(script);
})();
