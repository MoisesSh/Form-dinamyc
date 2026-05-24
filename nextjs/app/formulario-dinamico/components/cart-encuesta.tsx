import {
  Button,
  buttonVariants,
  Card,
  CardContent,
  Checkbox,
  Input,
  Label,
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
  Separator,
} from "@/components/ui";
import { Plus, Trash, Trash2, X } from "lucide-react";
import { useMemo, useState } from "react";
import useSWR from "swr";
import { getCategorias } from "../api/api-categorias";
import { getTipoPreguntas } from "../api/api-tipo-encuesta";
import { Badge } from "@/components/ui/badge";
interface CategoryOption {
  id_category: number;
  category: string;
  options: {
    id: number;
    title: string;
  }[];
}
export function CartEncuesta() {
  const [event, setEvent] = useState<
    | "texto_libre"
    | "opcion_unica"
    | "opcion_multiple"
    | "escala_numerica"
    | "fecha"
    | string
  >("texto_libre");
  const [title, setTitle] = useState<string>("");
  const [textField, setTextField] = useState<{ title: string }[]>([]);
  const [uniqueOption, setUniqueOption] = useState<
    { id: number; title: string; id_categoria: number }[]
  >([]);
  const [isExistCategory, setIsExistCategory] = useState<boolean>(true);
  const [category, setCategory] = useState<string>("");
  const { data: categorias } = useSWR(
    "api/categorias",
    async () => await getCategorias(),
  );

  const { data: tipoPregunta } = useSWR(
    "api/tipo-pregunta",
    async () => await getTipoPreguntas(),
  );

  const categoryOptions = useMemo<CategoryOption[]>(() => {
    return uniqueOption.reduce((acc, opt) => {
      const categoria =
        categorias?.find((c) => c.id === opt.id_categoria)?.categoria ??
        "Sin categoría";
      const grupo = acc.find((g) => g.id_category === opt.id_categoria);
      if (grupo) {
        grupo.options.push({ id: opt.id, title: opt.title });
      } else {
        acc.push({
          id_category: opt.id_categoria,
          category: categoria,
          options: [{ id: opt.id, title: opt.title }],
        });
      }
      return acc;
    }, [] as CategoryOption[]);
  }, [uniqueOption, categorias]);

  const textFieldFn = () => {
    setTextField((prev) => [...prev, { title: title }]);
  };
  const deleteTextField = (index: number) => {
    setTextField((prev) => prev.filter((_, i) => i !== index));
  };

  const uniqueOptionFn = () => {
    setUniqueOption((prev) => {
      const newUniqueOption = [
        ...prev,
        {
          id: (prev[prev.length - 1]?.id ?? 0) + 1,
          title: "",
          id_categoria: Number.parseInt(category),
        },
      ];
      return newUniqueOption;
    });
  };
  const deleteAllCategoryOptions = (idCategoria: number) => {
    setUniqueOption((prev) =>
      prev.filter((opt) => opt.id_categoria !== idCategoria),
    );
  };
  const deleteOption = (id: number) => {
    setUniqueOption((prev) => prev.filter((opt) => opt.id !== id));
  };
  const isExistCategoryFn = () => {
    setIsExistCategory((prev) => !prev);
  };
  const selectEventConstructForm = () => {
    if (event === "texto_libre") {
      textFieldFn();
    }
    if (event === "opcion_unica") {
      uniqueOptionFn();
    }
    if (event === "opcion_multiple") {
    }
    if (event === "escala_numerica") {
    }
    if (event === "fecha") {
    }
  };
  return (
    <div className="relative w-full">
      <Card className="grow ">
        <div className="absolute right-0 top-0 self-end -translate-y-2.5 translate-x-2.5 flex flex-row gap">
          <Button type="button" onClick={() => selectEventConstructForm()}>
            Agregar <Plus />
          </Button>
        </div>
        <CardContent className="mt-2">
          <div className="flex flex-row gap-2 ">
            <Input
              className="grow"
              placeholder="Pregunta Sin Titulo"
              onChange={(e) => setTitle(e.target.value)}
            />
            <Select onValueChange={(e) => setEvent(e)}>
              <SelectTrigger className="w-full max-w-48 grow">
                <SelectValue placeholder="Selecciona un tipo de encuesta" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Tipo de Preguntas</SelectLabel>
                  {tipoPregunta?.map((v, i) => (
                    <SelectItem key={i} value={v.tipo_pregunta}>
                      {v.tipo_pregunta}
                    </SelectItem>
                  ))}
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
          {event !== "texto_libre" && <Separator className="mt-2 mb-2" />}
          <div className="flex flex-col gap-2">
            {categoryOptions.length > 0 && (
              <Card>
                <CardContent>
                  <div className="relative w-full mt-4 flex flex-col">
                    <div className="flex w-full gap-2">
                      <div className="grow flex flex-col gap-0.5">
                        {isExistCategory ? (
                          <>
                            <Select onValueChange={(e) => setCategory(e)}>
                              <SelectTrigger className="w-full  ">
                                <SelectValue placeholder="Selecciona una categoria" />
                              </SelectTrigger>
                              <SelectContent>
                                <SelectGroup>
                                  <SelectLabel>Categorias</SelectLabel>
                                  {categorias?.map((v, i) => (
                                    <SelectItem key={i} value={v.id.toString()}>
                                      {v.categoria}
                                    </SelectItem>
                                  ))}
                                </SelectGroup>
                              </SelectContent>
                            </Select>
                            <Badge
                              variant={"link"}
                              className="text-sm text-slate-500 cursor-pointer hover:text-slate-700"
                              onClick={() => isExistCategoryFn()}
                            >
                              ¿No Existe La Categoria?
                            </Badge>
                          </>
                        ) : (
                          <>
                            <Input placeholder="Nueva Categoria" />
                            <Label>
                              ¿Recomendar Categoria?
                              <Checkbox />
                            </Label>
                          </>
                        )}
                      </div>

                      <Button
                        className=" top-0 right-0  text-sm "
                        type="button"
                        onClick={() => uniqueOptionFn()}
                      >
                        Agregar Opcion
                        <Plus />
                      </Button>
                    </div>

                    {categoryOptions.map((group) => {
                      return (
                        <div
                          key={group.id_category}
                          className="flex flex-col mt-2"
                        >
                          <div className="flex justify-between">
                            <span className="text-lg ">{group.category}</span>

                            <Button
                              variant={"destructive"}
                              className="self-end"
                              type="button"
                              onClick={() =>
                                deleteAllCategoryOptions(group.id_category)
                              }
                            >
                              {" "}
                              <Trash /> Eliminar opciones
                            </Button>
                          </div>
                          <Separator className="mt-2" />

                          <div className="flex flex-col gap-2 mt-6 grow">
                            {group.options.map((opt, optIdx) => {
                              return (
                                <div
                                  key={`${group.id_category}-${optIdx}`}
                                  className="flex gap-2"
                                >
                                  <div className="flex grow">
                                    <Checkbox
                                      className="self-center"
                                      disabled
                                    />{" "}
                                    <Input
                                      placeholder="Titulo..."
                                      className="border-l-0 border-r-0 border-t-0 rounded-none transition-all hover:border-b-2 ring-offset-0 focus:outline-none  focus-visible:ring-0 "
                                      onChange={(e) =>
                                        setUniqueOption((prev) =>
                                          prev.map((u) =>
                                            u.id_categoria ===
                                              group.id_category &&
                                            u.title === opt.title
                                              ? { ...u, title: e.target.value }
                                              : u,
                                          ),
                                        )
                                      }
                                      value={opt.title}
                                    />
                                    <Button
                                      type="button"
                                      variant="destructive"
                                      onClick={() => deleteOption(opt.id)}
                                    >
                                      <Trash2 />
                                      Eliminar Opción
                                    </Button>
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </CardContent>
              </Card>
            )}
            {textField.length > 0 && (
              <Card>
                <CardContent>
                  {textField.map((v, i) => (
                    <div
                      key={i}
                      className="flex flex-row gap-2 justify-around space-y-5"
                    >
                      <div className="grow">
                        <Label>{v.title}</Label>
                        <Input />
                      </div>
                      <Button
                        type="button"
                        variant={"destructive"}
                        className="self-center"
                        onClick={() => deleteTextField(i)}
                      >
                        <X />
                      </Button>
                    </div>
                  ))}
                </CardContent>
              </Card>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
