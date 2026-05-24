import { REGEX_EMAIL, REGEX_NUMBERS } from "@/constants/regex";
import z from "zod";
export const signInSchema = z.object({
  email: z
    .string({ error: "Correo Es Requerido" })
    .regex(REGEX_EMAIL, "Solo se permiten correos")
    .min(6, "Minimo 6 digitos")
    .max(50, "Maximo 50 Digitos"),
  password: z
    .string({ error: "Contraseña Es Requerida" })
    .min(8, "Contraseña debe tener más de 8 caracteres")
    .max(32, "Contraseña debe tener menos de 32 caracteres"),
});
export type LoginSchema = z.infer<typeof signInSchema>;
