const API_URL = import.meta.env.VITE_API_URL;

export async function getLessons() {
  const res = await fetch(`${API_URL}/lessons/`);  // ← FIGYELD A PER-T
  return res.json();
}
