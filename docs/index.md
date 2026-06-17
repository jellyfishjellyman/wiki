# GWB Wiki

<style>
  .home-hero {
    position: relative;
    overflow: hidden;
    margin: 1.5rem 0 2rem;
    padding: clamp(2.4rem, 6vw, 5rem) clamp(1.2rem, 4vw, 3rem);
    border: 1px solid rgba(87, 148, 164, 0.22);
    border-radius: 18px;
    background:
      radial-gradient(circle at 18% 14%, rgba(255, 255, 255, 0.92), transparent 24%),
      radial-gradient(circle at 82% 28%, rgba(188, 229, 235, 0.62), transparent 28%),
      linear-gradient(145deg, #eef9fb 0%, #f7fbff 45%, #f2f7f4 100%);
  }

  [data-md-color-scheme="slate"] .home-hero {
    border-color: rgba(129, 204, 216, 0.28);
    background:
      radial-gradient(circle at 18% 14%, rgba(201, 242, 244, 0.18), transparent 24%),
      radial-gradient(circle at 82% 28%, rgba(81, 166, 185, 0.22), transparent 28%),
      linear-gradient(145deg, #142431 0%, #1a2e38 48%, #102a2b 100%);
  }

  .home-hero h2 {
    margin: 0;
    max-width: 10em;
    font-size: clamp(2rem, 7vw, 4.8rem);
    line-height: 1.05;
    letter-spacing: 0;
  }

  .home-hero p {
    max-width: 38rem;
    margin: 1rem 0 0;
    color: var(--md-default-fg-color--light);
    font-size: 1.02rem;
  }

  .home-symbols {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    margin-top: 2rem;
  }

  .home-card {
    position: relative;
    display: grid;
    min-height: 13.5rem;
    padding: 1.15rem;
    border: 1px solid rgba(87, 148, 164, 0.22);
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.54);
    box-shadow: 0 18px 50px rgba(54, 104, 118, 0.12);
    color: inherit;
  }

  [data-md-color-scheme="slate"] .home-card {
    background: rgba(16, 33, 42, 0.62);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.2);
  }

  .home-card:hover {
    border-color: rgba(41, 137, 160, 0.5);
  }

  .home-card svg {
    width: 100%;
    max-width: 16rem;
    height: auto;
    justify-self: end;
    align-self: end;
  }

  .home-card h3 {
    margin: 0;
    font-size: 1.35rem;
  }

  .home-card p {
    margin: 0.35rem 0 0;
    max-width: 22rem;
    font-size: 0.92rem;
  }

  .home-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin-top: 1rem;
  }

  .home-links a {
    display: inline-flex;
    align-items: center;
    min-height: 2.4rem;
    padding: 0.35rem 0.8rem;
    border: 1px solid rgba(87, 148, 164, 0.28);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.48);
  }

  [data-md-color-scheme="slate"] .home-links a {
    background: rgba(255, 255, 255, 0.06);
  }

  @media (max-width: 720px) {
    .home-symbols {
      grid-template-columns: 1fr;
    }

    .home-card {
      min-height: 12rem;
    }
  }
</style>

<section class="home-hero">
  <h2>云在高处成形，水母在海里发光。</h2>
  <p>这里现在只收集两类温柔又复杂的对象：天空中的云，海水里的水母。一个记录气象、形态与观测；一个整理物种、结构与水族馆笔记。</p>

  <div class="home-symbols">
    <a class="home-card" href="clouds/index.md">
      <div>
        <h3>云</h3>
        <p>从积云、卷云到天气现象，按分类、图版和观察方法慢慢整理。</p>
      </div>
      <svg viewBox="0 0 320 180" role="img" aria-label="标志性的云">
        <defs>
          <linearGradient id="cloud-fill" x1="0" x2="1" y1="0" y2="1">
            <stop offset="0" stop-color="#ffffff"/>
            <stop offset="1" stop-color="#bfe5ef"/>
          </linearGradient>
        </defs>
        <path d="M70 130c-22 0-39-15-39-34 0-18 16-32 36-33 9-26 34-45 64-45 35 0 64 25 69 57 25 1 45 18 45 40 0 23-21 42-48 42H70z" fill="url(#cloud-fill)" opacity="0.95"/>
        <path d="M55 131c44 10 96 8 151-5 29-7 55-7 78 1" fill="none" stroke="#6fb2c5" stroke-width="7" stroke-linecap="round" opacity="0.45"/>
        <path d="M86 79c16-24 47-32 73-18" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round" opacity="0.8"/>
      </svg>
    </a>

    <a class="home-card" href="jellyfish/index.md">
      <div>
        <h3>水母</h3>
        <p>记录伞盖、触手、生活史和观赏资料，先从海月水母开始。</p>
      </div>
      <svg viewBox="0 0 320 180" role="img" aria-label="标志性的水母">
        <defs>
          <linearGradient id="jelly-fill" x1="0" x2="1" y1="0" y2="1">
            <stop offset="0" stop-color="#f8d9ee"/>
            <stop offset="1" stop-color="#91d6df"/>
          </linearGradient>
        </defs>
        <path d="M160 28c45 0 81 31 81 72 0 18-36 31-81 31s-81-13-81-31c0-41 36-72 81-72z" fill="url(#jelly-fill)" opacity="0.9"/>
        <path d="M106 100c18 12 89 13 108 0" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round" opacity="0.82"/>
        <path d="M120 126c-6 19 8 27 0 43M145 128c8 17-10 25-2 42M170 128c-9 16 9 27 0 43M196 126c7 18-8 27 1 43" fill="none" stroke="#5baec1" stroke-width="5" stroke-linecap="round" opacity="0.66"/>
        <circle cx="137" cy="78" r="13" fill="#ffffff" opacity="0.4"/>
        <circle cx="182" cy="73" r="16" fill="#ffffff" opacity="0.34"/>
      </svg>
    </a>
  </div>
</section>

## 目前的分类

<div class="home-links">
  <a href="clouds/index.md">云知识 Wiki</a>
  <a href="jellyfish/index.md">水母</a>
</div>

## 写作约定

- 每个主题先有一个 `index.md` 作为入口页。
- 图片先放在 `docs/assets/images/`。
- 后续图片变多时，再考虑迁移到 Cloudflare R2。
