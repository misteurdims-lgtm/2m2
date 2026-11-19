# Panier du site : les visiteurs remplissent leur panier ici, puis un seul bouton
# l'envoie tout fait sur Amazon (formulaire « ajout au panier » des Partenaires).

CART_HTML = """<button type="button" class="cart-btn" id="cartBtn" aria-controls="cart" aria-expanded="false">Panier <span id="cartCount">0</span></button>"""

CART_PANEL = """<div class="cart-veil" id="cartVeil" hidden></div>
<aside class="cart" id="cart" aria-label="Ton panier" hidden>
<div class="cart-head"><h2>Ton panier</h2><button type="button" class="cart-x" id="cartClose" aria-label="Fermer le panier">✕</button></div>
<ul id="cartList"></ul>
<p class="cart-empty" id="cartEmpty">Ton panier est vide. Ajoute du matériel depuis les fiches, un kit ou le quiz.</p>
<div class="cart-foot" id="cartFoot" hidden>
<p class="cart-note">Tu verras les prix exacts et tu confirmeras ta commande sur Amazon. Rien n'est payé ici.</p>
<a class="btn cart-go" id="cartGo" href="#" rel="sponsored nofollow noopener" target="_blank">Commander sur Amazon<small id="cartN"></small></a>
<button type="button" class="cart-clear" id="cartClear">Vider le panier</button>
</div>
</aside>
<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>
<script>
(() => {
  const TAG = "__TAG__", NAMES = __NAMES__, KEY = "2m2-panier";
  let cart = [];
  try { cart = JSON.parse(localStorage.getItem(KEY) || "[]").filter(i => NAMES[i.a]); } catch (e) { cart = []; }
  const $ = id => document.getElementById(id);
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch (e) {} };
  const count = () => cart.reduce((n, i) => n + i.q, 0);
  function render() {
    $("cartCount").textContent = count();
    $("cartBtn").classList.toggle("full", count() > 0);
    $("cartList").innerHTML = cart.map(i => `<li><span class="nm">${NAMES[i.a]}</span>
      <span class="qty"><button type="button" data-q="-1" data-a="${i.a}" aria-label="Retirer un">−</button><b>${i.q}</b><button type="button" data-q="1" data-a="${i.a}" aria-label="Ajouter un">+</button></span>
      <button type="button" class="rm" data-rm="${i.a}" aria-label="Supprimer">Supprimer</button></li>`).join("");
    $("cartEmpty").hidden = cart.length > 0; $("cartFoot").hidden = cart.length === 0;
    $("cartN").textContent = `${count()} article${count() > 1 ? "s" : ""}`;
    $("cartGo").href = `https://www.amazon.fr/gp/aws/cart/add.html?${cart.map((i, n) => `ASIN.${n + 1}=${i.a}&Quantity.${n + 1}=${i.q}`).join("&")}&AssociateTag=${TAG}`;
  }
  function add(asins) {
    asins.forEach(a => { if (!NAMES[a]) return; const it = cart.find(i => i.a === a); it ? it.q++ : cart.push({a, q: 1}); });
    save(); render();
    const t = $("toast");
    t.innerHTML = (asins.length > 1 ? `${asins.length} articles ajoutés au panier` : `Ajouté au panier : ${NAMES[asins[0]]}`) + ' <button type="button" id="toastOpen">Voir le panier</button>';
    t.hidden = false; clearTimeout(t._h); t._h = setTimeout(() => t.hidden = true, 4000);
    $("toastOpen").onclick = open;
    if (window.goatcounter && goatcounter.count) goatcounter.count({path: "panier-ajout", event: true});
  }
  function open() { $("cart").hidden = false; $("cartVeil").hidden = false; $("cartBtn").setAttribute("aria-expanded", "true"); $("toast").hidden = true; $("cartClose").focus(); }
  function close() { $("cart").hidden = true; $("cartVeil").hidden = true; $("cartBtn").setAttribute("aria-expanded", "false"); }
  $("cartBtn").onclick = open; $("cartClose").onclick = close; $("cartVeil").onclick = close;
  addEventListener("keydown", e => { if (e.key === "Escape") close(); });
  $("cartList").addEventListener("click", e => {
    const b = e.target.closest("button"); if (!b) return;
    if (b.dataset.rm) cart = cart.filter(i => i.a !== b.dataset.rm);
    if (b.dataset.q) { const it = cart.find(i => i.a === b.dataset.a); it.q += +b.dataset.q; if (it.q < 1) cart = cart.filter(i => i !== it); }
    save(); render();
  });
  $("cartClear").onclick = () => { cart = []; save(); render(); };
  $("cartGo").addEventListener("click", () => { if (window.goatcounter && goatcounter.count) goatcounter.count({path: "panier-commande", event: true}); });
  document.addEventListener("click", e => {
    const b = e.target.closest("[data-add]"); if (!b) return;
    e.preventDefault(); add(b.dataset.add.split(","));
  });
  // Dans les guides : un bouton « Ajouter au panier » à côté de chaque lien vers un modèle précis
  const enhance = () => document.querySelectorAll(".buy a[href*='amazon.fr/dp/']").forEach(a => {
    const m = a.href.match(/dp\\/([A-Z0-9]{10})/); if (!m || !NAMES[m[1]]) return;
    const b = document.createElement("button"); b.type = "button"; b.className = "btn add"; b.dataset.add = m[1]; b.textContent = "Ajouter au panier";
    a.className = "see"; a.textContent = "Voir sur Amazon"; const w = document.createElement("span"); w.className = "buy-acts"; a.before(w); w.append(b, a);
  });
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", enhance) : enhance();
  render();
})();
</script>"""
