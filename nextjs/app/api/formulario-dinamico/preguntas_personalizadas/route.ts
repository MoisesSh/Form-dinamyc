import { NextResponse } from "next/server";
const preguntas_personalizadas = [
  {
    id: 1,
    titulo: "¿Cuál es tu color favorito?",
    id_tipo_pregunta: 2,
    id_configuracion: 1,
    es_obligatorio: true,
  },
  {
    id: 2,
    titulo: "¿Qué deportes practicas?",
    id_tipo_pregunta: 3,
    id_configuracion: 1,
    es_obligatorio: false,
  },
  {
    id: 3,
    titulo: "¿Recomendarías nuestro servicio?",
    id_tipo_pregunta: 2,
    id_configuracion: 2,
    es_obligatorio: true,
  },
  {
    id: 4,
    titulo: "¿Cómo te enteraste de nosotros?",
    id_tipo_pregunta: 3,
    id_configuracion: 2,
    es_obligatorio: true,
  },
  {
    id: 5,
    titulo: "¿Qué género musical prefieres?",
    id_tipo_pregunta: 2,
    id_configuracion: 3,
    es_obligatorio: false,
  },
  {
    id: 6,
    titulo: "¿Cuál es tu nivel de estudios?",
    id_tipo_pregunta: 2,
    id_configuracion: 3,
    es_obligatorio: true,
  },
  {
    id: 7,
    titulo: "¿Qué opinas sobre la nueva función?",
    id_tipo_pregunta: 1,
    id_configuracion: 4,
    es_obligatorio: true,
  },
  {
    id: 8,
    titulo: "¿Qué sugerencias tienes para mejorar?",
    id_tipo_pregunta: 1,
    id_configuracion: 4,
    es_obligatorio: false,
  },
  {
    id: 9,
    titulo: "¿Cuál es tu destino de viaje soñado?",
    id_tipo_pregunta: 2,
    id_configuracion: 5,
    es_obligatorio: true,
  },
  {
    id: 10,
    titulo: "¿Qué tecnología usas a diario?",
    id_tipo_pregunta: 3,
    id_configuracion: 5,
    es_obligatorio: false,
  },
];
export async function GET() {
  return NextResponse.json(preguntas_personalizadas);
}
