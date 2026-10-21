const V = "urbansip-" + (self.registration.scope) + "-v1";
const ARCHIVOS = ["./", "./index.html", "./datos/datos.js", "./manifest.webmanifest", "./icono.svg"];
self.addEventListener("install", e => { e.waitUntil(caches.open(V).then(c => c.addAll(ARCHIVOS))); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(clients.claim()); });
// Primero la red (para ver precios nuevos); sin señal, lo guardado.
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(V).then(x => x.put(e.request, c)); return r; }).catch(() => caches.match(e.request)));
});
