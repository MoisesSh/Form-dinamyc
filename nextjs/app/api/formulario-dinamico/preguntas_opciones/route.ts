import { NextResponse } from "next/server";
const pregunta_opciones = [
  { id: 1, opcion: "Rojo", id_pregunta: 1, id_categoria: 2 },
  { id: 2, opcion: "Azul", id_pregunta: 1, id_categoria: 2 },
  { id: 3, opcion: "Verde", id_pregunta: 1, id_categoria: 2 },
  { id: 4, opcion: "Amarillo", id_pregunta: 1, id_categoria: 2 },
  { id: 5, opcion: "Fútbol", id_pregunta: 2, id_categoria: 3 },
  { id: 6, opcion: "Baloncesto", id_pregunta: 2, id_categoria: 3 },
  { id: 7, opcion: "Tenis", id_pregunta: 2, id_categoria: 3 },
  { id: 8, opcion: "Natación", id_pregunta: 2, id_categoria: 3 },
  { id: 9, opcion: "Sí", id_pregunta: 3, id_categoria: 1 },
  { id: 10, opcion: "No", id_pregunta: 3, id_categoria: 1 },
  { id: 11, opcion: "Tal vez", id_pregunta: 3, id_categoria: 1 },
  { id: 12, opcion: "Redes sociales", id_pregunta: 4, id_categoria: 1 },
  { id: 13, opcion: "TV", id_pregunta: 4, id_categoria: 1 },
  { id: 14, opcion: "Recomendación", id_pregunta: 4, id_categoria: 1 },
  { id: 15, opcion: "Evento", id_pregunta: 4, id_categoria: 1 },
  { id: 16, opcion: "Rock", id_pregunta: 5, id_categoria: 4 },
  { id: 17, opcion: "Pop", id_pregunta: 5, id_categoria: 4 },
  { id: 18, opcion: "Jazz", id_pregunta: 5, id_categoria: 4 },
  { id: 19, opcion: "Clásica", id_pregunta: 5, id_categoria: 4 },
  { id: 20, opcion: "Primaria", id_pregunta: 6, id_categoria: 8 },
  { id: 21, opcion: "Secundaria", id_pregunta: 6, id_categoria: 8 },
  { id: 22, opcion: "Universitario", id_pregunta: 6, id_categoria: 8 },
  { id: 23, opcion: "Postgrado", id_pregunta: 6, id_categoria: 8 },
  { id: 24, opcion: "Europa", id_pregunta: 9, id_categoria: 7 },
  { id: 25, opcion: "Asia", id_pregunta: 9, id_categoria: 7 },
  { id: 26, opcion: "América", id_pregunta: 9, id_categoria: 7 },
  { id: 27, opcion: "Oceanía", id_pregunta: 9, id_categoria: 7 },
  { id: 28, opcion: "Smartphone", id_pregunta: 10, id_categoria: 5 },
  { id: 29, opcion: "Laptop", id_pregunta: 10, id_categoria: 5 },
  { id: 30, opcion: "Tablet", id_pregunta: 10, id_categoria: 5 },
  { id: 31, opcion: "Smartwatch", id_pregunta: 10, id_categoria: 5 },
];

export async function GET() {
  return NextResponse.json(pregunta_opciones);
}
