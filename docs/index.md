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
    color: #16333a;
  }

  .home-hero {
    position: relative;
    overflow: hidden;
    min-height: calc(100vh - 3.2rem);
    margin: 0 calc(50% - 50vw);
    padding: clamp(3.5rem, 8vw, 7rem) clamp(1.2rem, 8vw, 7rem) clamp(2rem, 5vw, 4rem);
    background:
      radial-gradient(circle at 18% 18%, rgba(255, 255, 255, 0.95), transparent 20%),
      radial-gradient(circle at 74% 28%, rgba(177, 227, 236, 0.55), transparent 24%),
      radial-gradient(circle at 78% 78%, rgba(214, 202, 235, 0.34), transparent 26%),
      linear-gradient(145deg, #f8fcff 0%, #eaf8fb 42%, #f6fbf7 100%);
  }

  [data-md-color-scheme="slate"] .home-hero {
    background:
      radial-gradient(circle at 18% 18%, rgba(201, 242, 244, 0.16), transparent 20%),
      radial-gradient(circle at 74% 28%, rgba(81, 166, 185, 0.24), transparent 24%),
      radial-gradient(circle at 78% 78%, rgba(156, 131, 199, 0.22), transparent 26%),
      linear-gradient(145deg, #10202b 0%, #172d37 50%, #102a2b 100%);
    color: #edf8fb;
  }

  .home-shell {
    display: grid;
    grid-template-columns: minmax(18rem, 42rem) minmax(20rem, 35rem);
    align-items: center;
    gap: clamp(2rem, 7vw, 7rem);
    max-width: 76rem;
    min-height: calc(100vh - 9rem);
    margin: 0 auto;
  }

  .home-hero h2 {
    margin: 0;
    max-width: 9em;
    font-size: clamp(3.1rem, 8vw, 7.2rem);
    line-height: 0.98;
    letter-spacing: 0;
  }

  .home-hero p {
    max-width: 34rem;
    margin: 1.25rem 0 0;
    color: var(--md-default-fg-color--light);
    font-size: clamp(1rem, 1.45vw, 1.24rem);
    line-height: 1.9;
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
    min-height: 12rem;
    padding: clamp(1.1rem, 2vw, 1.7rem);
    border: 1px solid rgba(87, 148, 164, 0.22);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.64);
    box-shadow: 0 24px 70px rgba(54, 104, 118, 0.14);
    color: inherit;
    text-decoration: none;
    backdrop-filter: blur(18px);
    transition: border-color 160ms ease, transform 160ms ease, box-shadow 160ms ease;
  }

  [data-md-color-scheme="slate"] .home-card {
    background: rgba(16, 33, 42, 0.62);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.2);
  }

  .home-card:hover {
    border-color: rgba(41, 137, 160, 0.5);
    transform: translateY(-3px);
    box-shadow: 0 30px 80px rgba(54, 104, 118, 0.18);
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
  }

  .home-card p {
    margin: 0.35rem 0 0;
    max-width: 15rem;
    font-size: 0.92rem;
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
    border: 1px solid rgba(56, 138, 158, 0.35);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.68);
    color: var(--md-primary-fg-color);
    font: inherit;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 14px 34px rgba(54, 104, 118, 0.12);
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
      padding-top: 3rem;
    }

    .home-shell {
      grid-template-columns: 1fr;
      min-height: auto;
    }

    .home-symbols {
      grid-template-columns: 1fr;
    }

    .home-card {
      min-height: 12rem;
      align-items: flex-start;
      flex-direction: column;
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
      <h2>云在高处成形，水母在海里发光。</h2>
      <p>一个收集天空与海水的私人资料库。这里不急着解释世界，只把云的形态、天气的暗示、水母的透明身体和缓慢漂游，一点点安放好。</p>
      <button class="home-search" type="button" onclick="document.querySelector('.md-search__input')?.focus()">搜索整个 Wiki</button>
    </div>

    <div class="home-symbols">
      <a class="home-card" href="clouds/">
        <div>
          <h3>云</h3>
          <p>云形、图版、观测和天气线索。</p>
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
          <p>伞盖、触手、生活史和观察笔记。</p>
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
