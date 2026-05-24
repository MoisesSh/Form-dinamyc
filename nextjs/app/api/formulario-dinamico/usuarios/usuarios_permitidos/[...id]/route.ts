import { NextResponse } from "next/server";
const usuario_permisos = [
  { id: 1, user_id: 1, id_pregunta_personalizada: 1 },
  { id: 2, user_id: 1, id_pregunta_personalizada: 2 },
  { id: 3, user_id: 2, id_pregunta_personalizada: 3 },
  { id: 4, user_id: 2, id_pregunta_personalizada: 4 },
  { id: 5, user_id: 3, id_pregunta_personalizada: 5 },
  { id: 6, user_id: 3, id_pregunta_personalizada: 6 },
  { id: 7, user_id: 4, id_pregunta_personalizada: 7 },
  { id: 8, user_id: 4, id_pregunta_personalizada: 8 },
  { id: 9, user_id: 5, id_pregunta_personalizada: 9 },
  { id: 10, user_id: 5, id_pregunta_personalizada: 10 },
  { id: 11, user_id: 6, id_pregunta_personalizada: 1 },
  { id: 12, user_id: 6, id_pregunta_personalizada: 2 },
  { id: 13, user_id: 7, id_pregunta_personalizada: 3 },
  { id: 14, user_id: 8, id_pregunta_personalizada: 5 },
  { id: 15, user_id: 9, id_pregunta_personalizada: 7 },
  { id: 16, user_id: 10, id_pregunta_personalizada: 9 },
];

export async function GET() {
  return NextResponse.json(usuario_permisos);
}
