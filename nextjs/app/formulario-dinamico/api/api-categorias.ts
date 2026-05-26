"use server";
import { fetcher } from "@/core/fetcher";
interface Categoria {
  id: number;
  categoria: string;
  es_sugerencia: boolean;
}
export const getCategorias = async (): Promise<Categoria[]> => {
  const result: Categoria[] = await fetcher({
    url: "/api/formulario-dinamico/categorias",
  });
  return result;
};

export const createCategoria = async (categoria: {
  categoria: string;
  es_sugerencia: boolean;
}): Promise<Categoria> => {
  const result: Categoria = await fetcher({
    url: "/api/formulario-dinamico/categorias",
    method: "POST",
    sendData: categoria,
  });
  return result;
};
