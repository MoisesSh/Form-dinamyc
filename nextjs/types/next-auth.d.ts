import { DefaultSession } from "next-auth";
import "next-auth/jwt";

declare module "next-auth" {
  interface Session {
    user: {
      pk: number;
      email: string;
      first_name: string;
      last_name: string;
    } & DefaultSession["user"];
  }
  interface User {
    pk: number;
    email: string;
    first_name: string;
    last_name: string;
  }

  declare module "next-auth/jwt" {
    interface JWT {
      pk: number;
      email: string;
      first_name: string;
      last_name: string;
    }
  }
}
