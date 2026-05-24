import { NextResponse } from "next/server";
const usuarios = [
  { id: 1, nombre: "Carlos", apellido: "Rodríguez" },
  { id: 2, nombre: "Ana", apellido: "Martínez" },
  { id: 3, nombre: "Luis", apellido: "Fernández" },
  { id: 4, nombre: "María", apellido: "González" },
  { id: 5, nombre: "José", apellido: "López" },
  { id: 6, nombre: "Laura", apellido: "Sánchez" },
  { id: 7, nombre: "Pedro", apellido: "Ramírez" },
  { id: 8, nombre: "Sofía", apellido: "Torres" },
  { id: 9, nombre: "Diego", apellido: "Flores" },
  { id: 10, nombre: "Elena", apellido: "Castro" },
];

export async function GET() {
  return NextResponse.json(usuarios);
}
