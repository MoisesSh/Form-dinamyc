import { LoginSchema } from "@/app/(auth)/login/schema/login-schema";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Field, FieldDescription, FieldGroup } from "@/components/ui/field";
import { cn } from "@/lib/utils";
import { useForm } from "react-hook-form";
import FormInput from "./form-input";
import { useTransition } from "react";
import { loginAction } from "@/app/(auth)/login/actions/auth-actions";
import { useRouter } from "next/navigation";
export function LoginForm({
  className,
  ...props
}: React.ComponentProps<"div">) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const form = useForm<LoginSchema>({
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const onSubmit = (data: LoginSchema) => {
    startTransition(async () => {
      await loginAction(data);
      router.refresh();
    });
  };
  return (
    <div className={cn("flex flex-col gap-6 ", className)} {...props}>
      <Card className="overflow-hidden  p-0 bg-gray-800/20">
        <CardContent className="grid p-0 md:grid-cols-2 bg-blue-300/40 backdrop-blur-lg">
          <form
            className="p-6 md:p-8 sm:h-[50dvh] lg:h-[70dvh]"
            onSubmit={form.handleSubmit(onSubmit)}
          >
            <div className="flex flex-col justify-center h-full ">
              <div className="w-full">
                <FieldGroup>
                  <div className="flex flex-col items-center gap-2 text-center">
                    <h1 className="text-5xl font-bold text-white">
                      Bienvenido!
                    </h1>
                    <p className="text-balance text-2xl text-white">
                      Inicia Sesion En Homologación
                    </p>
                  </div>
                  <FormInput
                    form={form}
                    nameInput="email"
                    type="email"
                    label="Correo"
                  />
                  <FormInput
                    form={form}
                    nameInput="password"
                    type="password"
                    label="Contraseña"
                  />

                  <Field>
                    <Button type="submit">Iniciar</Button>
                  </Field>
                </FieldGroup>
              </div>
            </div>
          </form>
          <div className="relative hidden bg-muted md:block">
            <img
              src="/Banner_Homologacion.webp"
              alt="Image"
              className="absolute inset-0 h-full w-full object-cover dark:brightness-[0.2] dark:grayscale"
            />
          </div>
        </CardContent>
      </Card>
      <FieldDescription className="px-6 text-center">
        {/* By clicking continue, you agree to our <a href="#">Terms of Service</a>{" "}
        and <a href="#">Privacy Policy</a>. */}
      </FieldDescription>
    </div>
  );
}
