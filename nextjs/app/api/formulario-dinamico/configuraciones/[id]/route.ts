import { NextResponse } from "next/server";
export const configuraciones = [
  {
    id: 1,
    fecha_estimada: "2025-12-31",
    fecha_inicio: "2025-01-01",
    obligatorio: true,
    fecha_creacion: "2025-01-01T10:00:00",
    id_user_creator: 1,
  },
  {
    id: 2,
    fecha_estimada: "2025-06-30",
    fecha_inicio: "2025-03-01",
    obligatorio: false,
    fecha_creacion: "2025-03-01T09:30:00",
    id_user_creator: 2,
  },
  {
    id: 3,
    fecha_estimada: "2025-09-15",
    fecha_inicio: "2025-04-15",
    obligatorio: true,
    fecha_creacion: "2025-04-15T14:20:00",
    id_user_creator: 3,
  },
  {
    id: 4,
    fecha_estimada: "2026-01-20",
    fecha_inicio: "2025-05-01",
    obligatorio: false,
    fecha_creacion: "2025-05-01T11:00:00",
    id_user_creator: 4,
  },
  {
    id: 5,
    fecha_estimada: "2025-11-30",
    fecha_inicio: "2025-06-01",
    obligatorio: true,
    fecha_creacion: "2025-06-01T08:45:00",
    id_user_creator: 5,
  },
];

export async function GET(
  req: Request,
  { params }: { params: { id: string } },
) {
  const id = Number.parseInt(params.id);
  const getConfig = configuraciones.find((v) => v.id == id);
  return NextResponse.json(getConfig);
}
