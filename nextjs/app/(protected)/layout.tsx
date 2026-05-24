"use server";

import { auth } from "@/auth";
import { SessionProvider } from "next-auth/react";

export default async function Layout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const session = await auth();
  return (
    <main>
      <SessionProvider session={session}>{children}</SessionProvider>
    </main>
  );
}
