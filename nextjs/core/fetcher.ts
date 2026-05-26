import { API } from "@/constants/constats";
import { ApiResponse } from "@/types/api-response";

interface Fetcher<U> {
  url: string;
  sendData?: object | Array<U>;
  method?: "POST" | "PATCH" | "PUT";
}
export const fetcher = async <T, U>({ url, sendData, method }: Fetcher<U>) => {
  const options: RequestInit = {
    method: sendData ? method : "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  if (sendData) {
    options.body = JSON.stringify(sendData);
  }
  const response = await fetch(`${API.DJANGO_API_URL}${url}`, options);
  const getResponse: T = await response.json();
  return getResponse;
};
