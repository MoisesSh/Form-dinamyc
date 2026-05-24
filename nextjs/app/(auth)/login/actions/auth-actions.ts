"use server";
import { signIn } from "@/auth";
import { AuthError } from "next-auth";
import { z } from "zod";
import { signInSchema } from "../schema/login-schema";

export const loginAction = async (values: z.infer<typeof signInSchema>) => {
  try {
    await signIn("credentials", {
      email: values.email,
      password: values.password,
      redirect: false,
    });
    return { success: "Login successful" };
  } catch (error) {
    if (error instanceof AuthError) {
      return { error: "Credenciales Invalidas o Usuario Bloqueado" };
    }
    if (error instanceof Error) {
      return { error: error.message };
    }
    return { error: "Something went wrong" };
  }
};
