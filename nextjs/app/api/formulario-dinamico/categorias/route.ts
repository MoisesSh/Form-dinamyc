import { NextResponse } from "next/server";
interface Categoria {
  categoria: string;
  es_sugerencia: boolean;
}

const categorias = [
  { id: 1, categoria: "CATEGORIA_GENERICA", es_sugerencia: false },
  { id: 2, categoria: "Colores", es_sugerencia: true },
  { id: 3, categoria: "Deportes", es_sugerencia: false },
  { id: 4, categoria: "Música", es_sugerencia: true },
  { id: 5, categoria: "Tecnología", es_sugerencia: false },
  { id: 6, categoria: "Alimentos", es_sugerencia: true },
  { id: 7, categoria: "Viajes", es_sugerencia: false },
  { id: 8, categoria: "Educación", es_sugerencia: false },
  { id: 9, categoria: "Entretenimiento", es_sugerencia: true },
];
export async function GET() {
  return NextResponse.json(categorias);
}
export async function POST(req: Request) {
  const body: Categoria = await req.json();
  const newCategoria = {
    id: categorias[categorias.length - 1].id + 1,
    ...body,
  };
  categorias.push(newCategoria);
  return NextResponse.json(newCategoria);
}
