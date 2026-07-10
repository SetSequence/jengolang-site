// Self-destruct service worker.
//
// The old Jengo PWA (when the app lived at the root) registered `/sw.js` with a
// cache-first strategy that precached `/` — so returning visitors keep getting
// served the stale app shell from the SW cache, no matter what the server sends.
//
// This replaces that script at the same URL. On the browser's periodic SW update
// check (which fetches the script from the network, bypassing the SW cache), this
// installs, deletes every cache, unregisters itself, and reloads open tabs onto
// the live hub. Clean visitors never fetch this — the new site registers no SW —
// so it only heals browsers that still carry the ghost registration.
self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.map((k) => caches.delete(k)));
    await self.registration.unregister();
    const clients = await self.clients.matchAll({ type: 'window' });
    for (const client of clients) client.navigate(client.url);
  })());
});
