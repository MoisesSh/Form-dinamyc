// constants/constats.ts (noté que está escrito "constats" en lugar de "constants")
export const API = {
  NEXT_PUBLIC_API_URL:
    process.env.NEXT_PUBLIC_API_URL || "http://localhost:3000",
  NEXT_PUBLIC_APP_URL:
    process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000",

  // Para el backend Django (si existe)
  DJANGO_API_URL: process.env.DJANGO_API_URL || "http://localhost:3000",
};
