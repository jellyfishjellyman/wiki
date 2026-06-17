---
hide:
  - navigation
  - toc
---

<style>
  .md-content__button,
  .md-typeset h1 {
    display: none;
  }

  .md-main__inner {
    margin-top: 0;
  }

  .md-content {
    max-width: none;
  }

  .md-typeset {
    color: #eef7fb;
  }

  .home-hero {
    position: relative;
    overflow: hidden;
    min-height: calc(100vh - 3.2rem);
    margin: 0 calc(50% - 50vw);
    padding: clamp(3.5rem, 8vw, 7rem) clamp(1.2rem, 8vw, 7rem) clamp(2rem, 5vw, 4rem);
    background:
      radial-gradient(circle at 18% 58%, rgba(4, 18, 42, 0.58), rgba(4, 18, 42, 0.2) 34%, rgba(4, 18, 42, 0) 56%),
      linear-gradient(90deg, rgba(6, 20, 44, 0.68), rgba(11, 36, 63, 0.18) 43%, rgba(8, 28, 52, 0.14)),
      linear-gradient(180deg, rgba(3, 12, 30, 0.08), rgba(3, 14, 28, 0.28)),
      url("assets/images/home/cloud-jellyfish-bg.png");
    background-position: center;
    background-size: cover;
  }

  [data-md-color-scheme="slate"] .home-hero {
    background:
      radial-gradient(circle at 18% 58%, rgba(0, 8, 24, 0.64), rgba(0, 8, 24, 0.24) 34%, rgba(0, 8, 24, 0) 56%),
      linear-gradient(90deg, rgba(1, 9, 24, 0.74), rgba(8, 30, 56, 0.2) 44%, rgba(5, 18, 40, 0.18)),
      linear-gradient(180deg, rgba(0, 5, 18, 0.1), rgba(0, 7, 18, 0.34)),
      url("assets/images/home/cloud-jellyfish-bg.png");
    background-position: center;
    background-size: cover;
    color: #edf8fb;
  }

  .home-shell {
    display: grid;
    grid-template-columns: minmax(18rem, 36rem) minmax(17rem, 25rem);
    align-items: end;
    gap: clamp(2rem, 7vw, 7rem);
    max-width: 74rem;
    min-height: calc(100vh - 9rem);
    margin: 0 auto;
  }

  .home-hero h2 {
    margin: 0;
    max-width: 11em;
    font-size: clamp(2.5rem, 5.6vw, 5.7rem);
    line-height: 1.08;
    letter-spacing: 0;
    text-shadow: 0 18px 48px rgba(0, 12, 34, 0.54);
  }

  .home-hero p {
    max-width: 31rem;
    margin: 1.1rem 0 0;
    color: rgba(239, 248, 252, 0.9);
    font-size: clamp(1rem, 1.35vw, 1.16rem);
    line-height: 1.75;
    text-shadow: 0 10px 30px rgba(0, 12, 34, 0.52);
  }

  .home-symbols {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.1rem;
  }

  .home-card {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 10.5rem;
    padding: clamp(1.1rem, 2vw, 1.7rem);
    border: 1px solid rgba(233, 247, 252, 0.24);
    border-radius: 8px;
    background: rgba(7, 29, 54, 0.24);
    box-shadow: 0 24px 70px rgba(0, 15, 38, 0.18);
    color: inherit;
    text-decoration: none;
    backdrop-filter: blur(14px);
    transition: border-color 160ms ease, transform 160ms ease, box-shadow 160ms ease;
  }

  [data-md-color-scheme="slate"] .home-card {
    background: rgba(7, 24, 47, 0.36);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.22);
  }

  .home-card:hover {
    border-color: rgba(255, 255, 255, 0.66);
    transform: translateY(-3px);
    box-shadow: 0 30px 80px rgba(0, 15, 38, 0.24);
  }

  .home-card svg {
    width: 40%;
    min-width: 9rem;
    max-width: 15rem;
    height: auto;
  }

  .home-card h3 {
    margin: 0;
    font-size: 1.35rem;
    color: #ffffff;
  }

  .home-card p {
    margin: 0.35rem 0 0;
    max-width: 15rem;
    font-size: 0.92rem;
    color: rgba(239, 248, 252, 0.78);
  }

  .home-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin-top: 1rem;
  }

  .home-search {
    display: inline-flex;
    align-items: center;
    min-height: 2.7rem;
    margin-top: 1.35rem;
    padding: 0.45rem 1rem;
    border: 1px solid rgba(255, 255, 255, 0.38);
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.14);
    color: #ffffff;
    font: inherit;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 14px 34px rgba(0, 15, 38, 0.18);
    backdrop-filter: blur(18px);
  }

  .home-search:hover,
  .home-search:focus-visible {
    border-color: rgba(41, 137, 160, 0.62);
    outline: none;
  }

  [data-md-color-scheme="slate"] .home-search {
    background: rgba(255, 255, 255, 0.08);
    color: #9bd6df;
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
    .home-hero {
      min-height: auto;
      padding-top: 3.2rem;
      background-position: 58% center;
    }

    .home-shell {
      grid-template-columns: 1fr;
      min-height: auto;
    }

    .home-symbols {
      grid-template-columns: 1fr;
    }

    .home-card {
      min-height: 10rem;
      align-items: flex-start;
      flex-direction: column;
      background: rgba(7, 29, 54, 0.34);
    }

    .home-card svg {
      width: 70%;
      align-self: flex-end;
    }
  }
</style>

<section class="home-hero">
  <div class="home-shell">
    <div>
      <h2>云是天空的水母，水母是海中的云。</h2>
      <p>在天空里看见水母，在海水里看见云。</p>
      <button class="home-search" type="button" onclick="document.querySelector('.md-search__input')?.focus()">搜索整个 Wiki</button>
    </div>

    <div class="home-symbols">
      <a class="home-card" href="clouds/">
        <div>
          <h3>云</h3>
          <p>进入云的图谱</p>
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

      <a class="home-card" href="jellyfish/">
        <div>
          <h3>水母</h3>
          <p>进入水母花园</p>
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
  </div>
</section>
