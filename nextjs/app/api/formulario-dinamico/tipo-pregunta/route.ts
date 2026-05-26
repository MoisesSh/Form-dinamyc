import { NextResponse } from "next/server";
const tipo_pregunta = [
  { id: 1, tipo_pregunta: "texto_libre" },
  { id: 2, tipo_pregunta: "opcion_unica" },
  { id: 3, tipo_pregunta: "opcion_multiple" },
  { id: 4, tipo_pregunta: "fecha" },
];
export interface TipoPregunta {
  id: number;
  tipo_pregunta: string;
}
export async function GET() {
  return NextResponse.json(tipo_pregunta);
}
