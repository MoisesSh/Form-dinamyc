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
