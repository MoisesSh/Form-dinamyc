import { NextResponse } from "next/server";
import { configuraciones } from "./[id]/route";
interface Config {
  fecha_estimada: string;
  fecha_inicio: string;
  obligatorio: boolean;
  fecha_creacion: string;
  id_user_creator: number;
}
export async function POST(req: Request) {
  const body: Config = await req.json();
  const newConfig = {
    id: configuraciones[configuraciones.length - 1].id + 1,
    ...body,
  };
  configuraciones.push(newConfig);
  return NextResponse.json(newConfig);
}
