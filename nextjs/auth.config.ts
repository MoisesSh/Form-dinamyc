import type { NextAuthConfig } from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { signInSchema } from "./app/(auth)/login/schema/login-schema";
import { ApiResponse } from "./types/api-response";
import { API } from "./constants/constats";
export interface SessionType {
  access: string;
  refresh: string;
  user: {
    pk: number;
    email: string;
    first_name: string;
    last_name: string;
  };
}
export default {
  providers: [
    Credentials({
      authorize: async (credentials) => {
        const { data, success } = signInSchema.safeParse(credentials);
        if (!success) {
          return null;
        }
        try {
          const response = await fetch(
            `http://localhost:8000/api/auth/login/`,
            {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                email: data.email,
                password: data.password,
              }),
            },
          );
          if (!response.ok) {
            return null;
          }
          const userData: SessionType = await response.json();
          return {
            pk: userData.user.pk,
            email: userData.user.email,
            first_name: userData.user.first_name,
            last_name: userData.user.last_name,
          };
        } catch {
          return null;
        }
      },
    }),
  ],
} satisfies NextAuthConfig;
