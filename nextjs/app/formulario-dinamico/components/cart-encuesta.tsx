import {
  Button,
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
import { Badge } from "@/components/ui/badge";
import { Plus, Trash, Trash2, X } from "lucide-react";
import { useMemo, useState } from "react";
import useSWR from "swr";
import { createCategoria, getCategorias } from "../api/api-categorias";
import { getTipoPreguntas } from "../api/api-tipo-encuesta";

const VALIDATIONS = [
  { value: "solo_letras", label: "Letras" },
  { value: "solo_numeros", label: "Núm" },
  { value: "alfanumerico", label: "Alfa" },
] as const;

interface CategoryOption {
  id_category: number;
  category: string;
  options: {
    id: number;
    title: string;
  }[];
}

type OptionItem = {
  id: number;
  title: string;
  id_categoria: number;
};

export function CartEncuesta() {
  const [event, setEvent] = useState<
    "texto_libre" | "opcion_unica" | "opcion_multiple" | "fecha" | string
  >("texto_libre");
  const [title, setTitle] = useState<string>("");
  const [textField, setTextField] = useState<
    {
      title: string;
      validation: { type: string; min: number; max: number };
    }[]
  >([]);
  const [dateField, setDateField] = useState<{ title: string }[]>([]);
  const [uniqueOption, setUniqueOption] = useState<OptionItem[]>([]);
  const [multipleOption, setMultipleOption] = useState<OptionItem[]>([]);
  const [isExistCategory, setIsExistCategory] = useState<boolean>(true);
  const [category, setCategory] = useState<string>("");
  const [newCategoryName, setNewCategoryName] = useState<string>("");
  const [recommendCategory, setRecommendCategory] = useState<boolean>(false);
  const { data: categorias, mutate: mutateCategorias } = useSWR(
    "api/categorias",
    async () => await getCategorias(),
  );

  const { data: tipoPregunta } = useSWR(
    "api/tipo-pregunta",
    async () => await getTipoPreguntas(),
  );

  const options: OptionItem[] =
    event === "opcion_multiple" ? multipleOption : uniqueOption;
  const setOptions =
    event === "opcion_multiple" ? setMultipleOption : setUniqueOption;

  const categoryOptions = useMemo<CategoryOption[]>(() => {
    return options.reduce((acc, opt) => {
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
  }, [options, categorias]);

  const textFieldFn = () => {
    setTextField((prev) => [
      ...prev,
      {
        title: title,
        validation: { type: "solo_letras", min: 0, max: 0 },
      },
    ]);
  };
  const deleteTextField = (index: number) => {
    setTextField((prev) => prev.filter((_, i) => i !== index));
  };

  const dateFieldFn = () => {
    setDateField((prev) => [...prev, { title: title }]);
  };
  const deleteDateField = (index: number) => {
    setDateField((prev) => prev.filter((_, i) => i !== index));
  };

  const addOptionFn = async () => {
    if (!isExistCategory && !newCategoryName.trim()) return;

    let categoriaId: number;

    if (!isExistCategory) {
      try {
        const nuevaCategoria = await createCategoria({
          categoria: newCategoryName.trim(),
          es_sugerencia: recommendCategory,
        });
        categoriaId = nuevaCategoria.id;
        mutateCategorias();
        setNewCategoryName("");
        setRecommendCategory(false);
        setIsExistCategory(true);
      } catch {
        return;
      }
    } else {
      categoriaId = Number.parseInt(category);
      if (!categoriaId) return;
    }

    setOptions((prev) => {
      const newOption = [
        ...prev,
        {
          id: (prev[prev.length - 1]?.id ?? 0) + 1,
          title: "",
          id_categoria: categoriaId,
        },
      ];
      return newOption;
    });
  };
  const deleteAllCategoryOptions = (idCategoria: number) => {
    setOptions((prev) =>
      prev.filter((opt) => opt.id_categoria !== idCategoria),
    );
  };
  const deleteOption = (id: number) => {
    setOptions((prev) => prev.filter((opt) => opt.id !== id));
  };
  const isExistCategoryFn = () => {
    setIsExistCategory((prev) => !prev);
  };
  const selectEventConstructForm = () => {
    if (event === "texto_libre") {
      textFieldFn();
    }
    if (event === "opcion_unica") {
      addOptionFn();
    }
    if (event === "opcion_multiple") {
      addOptionFn();
    }
    if (event === "fecha") {
      dateFieldFn();
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
            {(event === "opcion_unica" || event === "opcion_multiple") && (
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
                            <Input
                              placeholder="Nueva Categoria"
                              value={newCategoryName}
                              onChange={(e) =>
                                setNewCategoryName(e.target.value)
                              }
                            />
                            <Label>
                              ¿Recomendar Categoria?
                              <Checkbox
                                checked={recommendCategory}
                                onCheckedChange={(checked) =>
                                  setRecommendCategory(checked === true)
                                }
                              />
                            </Label>
                          </>
                        )}
                      </div>

                      <Button
                        className=" top-0 right-0  text-sm "
                        type="button"
                        onClick={() => addOptionFn()}
                      >
                        Agregar Opcion
                        <Plus />
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}
            {categoryOptions.length > 0 && (
              <Card>
                <CardContent>
                  <div className="relative w-full mt-4 flex flex-col">
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

                          <div
                            className={
                              event === "opcion_multiple"
                                ? "grid grid-cols-3 gap-2 mt-6"
                                : "flex flex-col gap-2 mt-6 grow"
                            }
                          >
                            {group.options.map((opt, optIdx) => {
                              return (
                                <div
                                  key={`${group.id_category}-${optIdx}`}
                                  className="flex gap-2"
                                >
                                  <div className="flex grow items-center gap-1">
                                    {event === "opcion_unica" ? (
                                      <div className="h-4 w-4 rounded-full border-2 border-primary self-center shrink-0" />
                                    ) : (
                                      <Checkbox
                                        className="self-center shrink-0"
                                        disabled
                                      />
                                    )}
                                    <Input
                                      placeholder="Titulo..."
                                      className="border-l-0 border-r-0 border-t-0 rounded-none transition-all hover:border-b-2 ring-offset-0 focus:outline-none focus-visible:ring-0 grow min-w-0"
                                      onChange={(e) =>
                                        setOptions((prev) =>
                                          prev.map((u) =>
                                            u.id === opt.id
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
                        <div className="flex gap-2 items-center">
                          <Input className="grow" />
                          <div className="flex gap-0.5 shrink-0">
                            {VALIDATIONS.map((val) => (
                              <Badge
                                key={val.value}
                                variant={
                                  v.validation.type === val.value
                                    ? "default"
                                    : "outline"
                                }
                                className="cursor-pointer text-[10px] px-1 py-0 h-5 select-none"
                                onClick={() =>
                                  setTextField((prev) =>
                                    prev.map((tf, idx) =>
                                      idx === i
                                        ? {
                                            ...tf,
                                            validation: {
                                              ...tf.validation,
                                              type:
                                                tf.validation.type === val.value
                                                  ? ""
                                                  : val.value,
                                            },
                                          }
                                        : tf,
                                    ),
                                  )
                                }
                              >
                                {val.label}
                              </Badge>
                            ))}
                          </div>
                        </div>
                        <div className="flex gap-2 mt-1 items-center text-xs text-muted-foreground">
                          <span className="text-[11px] text-muted-foreground shrink-0">
                            {v.validation.type === "solo_numeros"
                              ? "Rango numérico"
                              : "Caracteres"}
                            :
                          </span>
                          <Label className="text-xs">Min</Label>
                          <Input
                            type="number"
                            className="w-16 h-7 text-xs"
                            placeholder="0"
                            min={0}
                            value={v.validation.min || ""}
                            onChange={(e) =>
                              setTextField((prev) =>
                                prev.map((tf, idx) =>
                                  idx === i
                                    ? {
                                        ...tf,
                                        validation: {
                                          ...tf.validation,
                                          min: Number(e.target.value),
                                        },
                                      }
                                    : tf,
                                ),
                              )
                            }
                          />
                          <Label className="text-xs">Max</Label>
                          <Input
                            type="number"
                            className="w-16 h-7 text-xs"
                            placeholder="0"
                            min={0}
                            value={v.validation.max || ""}
                            onChange={(e) =>
                              setTextField((prev) =>
                                prev.map((tf, idx) =>
                                  idx === i
                                    ? {
                                        ...tf,
                                        validation: {
                                          ...tf.validation,
                                          max: Number(e.target.value),
                                        },
                                      }
                                    : tf,
                                ),
                              )
                            }
                          />
                        </div>
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
            {dateField.length > 0 && (
              <Card>
                <CardContent>
                  {dateField.map((v, i) => (
                    <div
                      key={i}
                      className="flex flex-row gap-2 justify-around space-y-5"
                    >
                      <div className="grow">
                        <Label>{v.title}</Label>
                        <Input type="date" className="grow" />
                      </div>
                      <Button
                        type="button"
                        variant={"destructive"}
                        className="self-center"
                        onClick={() => deleteDateField(i)}
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
