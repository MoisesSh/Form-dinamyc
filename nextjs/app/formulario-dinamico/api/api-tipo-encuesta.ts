"use server";
import { TipoPregunta } from "@/app/api/formulario-dinamico/tipo-pregunta/route";
import { fetcher } from "@/core/fetcher";

export const getTipoPreguntas = async (): Promise<TipoPregunta[]> => {
  const result: TipoPregunta[] = await fetcher({
    url: "/api/formulario-dinamico/tipo-pregunta",
  });
  return result;
};
