"use client";
import FormInput from "@/components/form-input";
import {
  Button,
  Card,
  CardContent,
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui";
import { IconArrowLeft, IconArrowRight, IconSearch } from "@tabler/icons-react";
import { useForm } from "react-hook-form";
import { SchemaReceiptType } from "./schema/schema-receipt";
import { paramsConstructor } from "@/core/params-contructor";
import useSWR from "swr";
import { useState } from "react";
import { certifiedEquip } from "./api/homolagacion-valid";

export default function ComprobantePage() {
  const [params, setParams] = useState("");
  const form = useForm<SchemaReceiptType>({
    defaultValues: {
      marca: "",
      page: 1,
      search: "",
    },
  });
  const { data: equips, isLoading: isLoadingEquips } = useSWR(
    params ? params : null,
    async () => await certifiedEquip(params),
  );
  const onSubmit = (data: SchemaReceiptType) => {
    const url = paramsConstructor(data);
    setParams(params);
  };
  return (
    <Card className="h-dvh w-dvw rounded-none">
      <CardContent>
        <Card className="flex flex-col">
          <CardContent>
            <form onSubmit={form.handleSubmit(onSubmit)}>
              <div className="flex flex-row gap-2 items-baseline justify-center">
                <FormInput
                  form={form}
                  label="Marca"
                  nameInput="marca"
                  type="text"
                />
                <FormInput
                  form={form}
                  label="Busqueda"
                  nameInput="search"
                  type="text"
                />
                <Button className="self-baseline-last">
                  <IconSearch />
                  Buscar
                </Button>
              </div>
            </form>
          </CardContent>
          <CardContent className="flex flex-col gap-2 p-2">
            <Table>
              <TableCaption>Lista de equipos homologados</TableCaption>
              <TableHeader>
                <TableRow>
                  <TableHead className="w-25">Seleccionar</TableHead>
                  <TableHead className="w-25">Codigo</TableHead>
                  <TableHead>Marca</TableHead>
                  <TableHead>Modelo</TableHead>
                  <TableHead>Codigo de Homologación</TableHead>
                  <TableHead>F. Homologación</TableHead>
                  <TableHead>Estatus de Homologación</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell className="font-medium">
                    <Button>Agregar</Button>
                  </TableCell>

                  <TableCell className="font-medium">INV001</TableCell>
                  <TableCell>Paid</TableCell>
                  <TableCell>Credit Card</TableCell>
                  <TableCell>Credit Card</TableCell>
                  <TableCell>Credit Card</TableCell>
                  <TableCell className="text-center">$250.00</TableCell>
                </TableRow>
              </TableBody>
            </Table>
            <div className="self-end flex flex-row gap-2">
              <Button variant={"outline"}>
                <IconArrowLeft />
                Anterior
              </Button>
              <Button>
                Siguiente
                <IconArrowRight />
              </Button>
            </div>
          </CardContent>
        </Card>
      </CardContent>
    </Card>
  );
}
