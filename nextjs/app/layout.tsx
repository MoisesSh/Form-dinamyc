import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
const myFont = localFont({
  src: "./fonts/RobotoCondensed-VariableFont_wght.ttf",
  variable: "--font-roboto-condensed",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Homologacion",
  icons: {
    icon: "/Logo_Sigitel-1.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  //  bg-[url(/fondo.jpg)]
  return (
    <html lang="en" className={`${myFont.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col bg-cover  backdrop-blur-lg ">
        {children}
      </body>
    </html>
  );
}
