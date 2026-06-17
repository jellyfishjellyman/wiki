document$.subscribe(function () {
  document.querySelectorAll(".md-content img").forEach(function (image) {
    image.loading = "lazy";
    image.decoding = "async";
  });
});
