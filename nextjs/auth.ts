import NextAuth from "next-auth";
import authConfig from "./auth.config";

export const { handlers, signIn, signOut, auth } = NextAuth({
  session: {
    strategy: "jwt",
    maxAge: 5 * 60,
  },

  trustHost: true,
  ...authConfig,
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id;
        token.email = user.email;
        token.first_name = user.first_name;
        token.last_name = user.last_name;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.pk = token.id as number;
        session.user.email = token.email as string;
        session.user.last_name = token.last_name as string;
        session.user.first_name = token.first_name as string;
      }
      return session;
    },
  },
});
