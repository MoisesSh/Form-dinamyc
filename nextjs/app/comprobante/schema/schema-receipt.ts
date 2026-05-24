import z from "zod";

export const schemaReceipt = z.object({
  marca: z.string().optional(),
  page: z.number(),
  search: z.string().optional(),
});
export type SchemaReceiptType = z.infer<typeof schemaReceipt>;
