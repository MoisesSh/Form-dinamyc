"use server";

import { fetcher } from "@/core/fetcher";
import { CertifiedEquip } from "../models/types";
interface FetchWithPagination<T> {
  count: number;
  next: string;
  previous: null | string;
  result: T;
}
export const certifiedEquip = async (
  url: string,
): Promise<FetchWithPagination<CertifiedEquip[]>> => {
  const result: FetchWithPagination<CertifiedEquip[]> = await fetcher({
    url: `equipos-homologados/${url}`,
  });
  return result;
};
