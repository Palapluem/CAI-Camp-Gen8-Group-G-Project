// frontend/js/api.js
export const API_BASE =
  (location.hostname === "localhost" || location.hostname === "127.0.0.1")
    ? "http://127.0.0.1:8000"
    : "http://127.0.0.1:8000"; // เปลี่ยนถ้า deploy

export const state = {
  token: null,
  user: null
};

export async function api(path, { method="GET", body, json=true } = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...(state.token ? { "Authorization": `Bearer ${state.token}` } : {})
    },
    body: body ? JSON.stringify(body) : undefined
  });
  if (!res.ok) throw new Error(await res.text());
  return json ? res.json() : res.text();
}

// ใช้ในหน้า Login
export async function login(username, password) {
  const data = await api("/api/auth/login", { method:"POST", body:{ username, password }});
  state.token = data.token; state.user = data.user;
  return data;
}

// Barcode utility (คืน URL รูป)
export function barcodeURL(text) {
  return `${API_BASE}/api/barcode?text=${encodeURIComponent(text)}`;
}