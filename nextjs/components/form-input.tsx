import {
  Controller,
  FieldValue,
  FieldValues,
  Path,
  UseFormReturn,
} from "react-hook-form";
import { Field, FieldDescription, FieldError, FieldLabel } from "./ui/field";
import { Input } from "./ui/input";

interface FormInput<T extends FieldValues> {
  form: UseFormReturn<T>;
  nameInput: Path<T>;
  placeholder?: string;
  type: string;
  className?: string;
  description?: string;
  label: string;
}
export default function FormInput<T extends FieldValues>(
  useForm: FormInput<T>,
) {
  return (
    <>
      <Controller
        name={useForm.nameInput}
        control={useForm.form.control}
        render={({ field, fieldState }) => (
          <Field data-invalid={fieldState.invalid}>
            <FieldLabel
              htmlFor={field.name}
              className="text-white placeholder:text-foreground "
            >
              {useForm.label}
            </FieldLabel>
            <Input
              {...field}
              id={field.name}
              aria-invalid={fieldState.invalid}
              placeholder={useForm.placeholder}
              autoComplete="off"
              type={useForm.type}
            />
            {useForm.description && (
              <FieldDescription>useForm.description</FieldDescription>
            )}
            {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
          </Field>
        )}
      />
    </>
  );
}
