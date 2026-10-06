import './App.css'

function App() {
  return (
    <main className="app-shell">
      <header className="topbar">
        <span className="brand-mark">P</span>
        <span>Proyecto 331</span>
        <span className="status">Monorepo activo</span>
      </header>

      <section className="hero">
        <p className="eyebrow">PLATAFORMA UNIVERSITARIA · 2026</p>
        <h1>Construimos ideas<br /><em>con propósito.</em></h1>
        <p className="intro">
          Un espacio para desarrollar, documentar y presentar nuestro proyecto
          universitario desde un solo lugar.
        </p>
        <div className="actions">
          <a className="primary-button" href="#stack">Explorar el proyecto <span>↗</span></a>
          <a className="text-link" href="#documentacion">Ver documentación <span>→</span></a>
        </div>
      </section>

      <section className="details" id="stack">
        <div className="section-heading">
          <span className="section-number">01</span>
          <h2>Una base para crecer</h2>
        </div>
        <div className="cards">
          <article className="card backend-card">
            <div className="card-icon">⌘</div>
            <p className="card-label">BACKEND</p>
            <h3>Django + uv</h3>
            <p>Una API robusta y preparada para acompañar cada etapa del proyecto.</p>
            <span className="card-arrow">↗</span>
          </article>
          <article className="card frontend-card">
            <div className="card-icon">✦</div>
            <p className="card-label">FRONTEND</p>
            <h3>React + Vite</h3>
            <p>Una interfaz rápida, clara y lista para convertir ideas en experiencias.</p>
            <span className="card-arrow">↗</span>
          </article>
          <article className="card doc-card" id="documentacion">
            <div className="card-icon">▤</div>
            <p className="card-label">DOCUMENTACIÓN</p>
            <h3>Informe .odt</h3>
            <p>El conocimiento del proyecto vive en un documento compartido y editable.</p>
            <span className="card-arrow">↗</span>
          </article>
        </div>
      </section>

      <footer>
        <span>Proyecto universitario 331</span>
        <span>Hecho para aprender · 2026</span>
      </footer>
    </main>
  )
}

export default App
