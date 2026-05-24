"use client";
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
  Input,
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui";
import useSWR from "swr";
import { getCategorias } from "./api/api-categorias";
import { getTipoPreguntas } from "./api/api-tipo-encuesta";
import { CartEncuesta } from "./components/cart-encuesta";

export default function FormDinamyc() {
  return (
    <Card className="w-9/12 m-auto mt-10 border p-2 ">
      <CardHeader>
        <CardTitle>Creador de encuestas</CardTitle>
      </CardHeader>
      <CardContent>
        <form>
          <div className="flex flex-row gap-2 justify-evenly">
            <CartEncuesta />
          </div>
        </form>
      </CardContent>
      <CardFooter></CardFooter>
    </Card>
  );
}
