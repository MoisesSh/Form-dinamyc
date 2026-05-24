import { API } from "@/constants/constats";
import { ApiResponse } from "@/types/api-response";

interface Fetcher<U> {
  url: string;
  sendData?: Object | Array<U>;
  method?: "POST" | "PATCH" | "PUT";
}
export const fetcher = async <T, U>({ url, sendData, method }: Fetcher<U>) => {
  const response = await fetch(`${API.DJANGO_API_URL}${url}`, {
    method: sendData ? method : "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const getResponse: T = await response.json();
  return getResponse;
};
