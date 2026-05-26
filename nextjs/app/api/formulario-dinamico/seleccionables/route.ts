import { NextResponse } from "next/server";
const seleccionables = [
  { id: 1, pregunta_id: 1, elemento: "Nivel de satisfacción" },
  { id: 2, pregunta_id: 1, elemento: "Calidad del producto" },
  { id: 3, pregunta_id: 2, elemento: "Atención al cliente" },
  { id: 4, pregunta_id: 2, elemento: "Precio" },
  { id: 5, pregunta_id: 3, elemento: "Recomendaría" },
  { id: 6, pregunta_id: 4, elemento: "Frecuencia de uso" },
  { id: 7, pregunta_id: 5, elemento: "Preferencia de marca" },
];
export async function GET() {
  return NextResponse.json(seleccionables);
}
interface Seleccionable {
  pregunta_id: number;
  elemento: string;
}
export async function POST(req: Request) {
  const body: Seleccionable = await req.json();
  const newSeleccionable = { id: seleccionables[seleccionables.length - 1].id + 1, ...body };
  seleccionables.push(newSeleccionable);
  return NextResponse.json(newSeleccionable);
}
