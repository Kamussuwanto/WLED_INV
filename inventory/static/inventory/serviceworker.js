const CACHE_NAME = 'inventory-pwa-v1';
const assetsToCache = [
    '/parts/',
    '/static/inventory/manifest.json'
];

// Installs background service workers
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(assetsToCache);
        })
    );
});

// Intercepts traffic to maintain operational speeds
self.addEventListener('fetch', event => {
    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.match(event.request);
        })
    );
});
