import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
export function pagination(restart: boolean): number {
  let pagination = 0;
  
  if (pagination >= 0 && !restart) {
    pagination++;
  }

  if (restart) {
    pagination--;
  }
  return pagination;
}
