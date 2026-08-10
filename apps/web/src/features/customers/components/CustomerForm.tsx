import { useForm } from "react-hook-form";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";

import type { CustomerCreate } from "../types/customer.types";

type CustomerFormProps = {
  onSubmit: (data: CustomerCreate) => void;
  initialValues?: CustomerCreate;
  isSubmitting?: boolean;
  submitLabel?: string;
  submittingLabel?: string;
  onCancel?: () => void;
};

export default function CustomerForm({
  onSubmit,
  initialValues,
  isSubmitting = false,
  submitLabel = "Create Customer",
  submittingLabel = "Creating...",
  onCancel,
}: CustomerFormProps) {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CustomerCreate>({
    defaultValues: initialValues ?? {
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
    },
  });

  return (
    <Card className="p-6">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="space-y-6"
      >
        <div className="grid gap-6 md:grid-cols-2">
          <div>
            <label
              htmlFor="first_name"
              className="mb-2 block text-sm font-medium text-text"
            >
              First name
            </label>

            <input
              id="first_name"
              {...register("first_name", {
                required: "First name is required.",
              })}
              className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-text outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
            />

            {errors.first_name && (
              <p className="mt-1 text-sm text-danger">
                {errors.first_name.message}
              </p>
            )}
          </div>

          <div>
            <label
              htmlFor="last_name"
              className="mb-2 block text-sm font-medium text-text"
            >
              Last name
            </label>

            <input
              id="last_name"
              {...register("last_name", {
                required: "Last name is required.",
              })}
              className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-text outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
            />

            {errors.last_name && (
              <p className="mt-1 text-sm text-danger">
                {errors.last_name.message}
              </p>
            )}
          </div>
        </div>

        <div>
          <label
            htmlFor="email"
            className="mb-2 block text-sm font-medium text-text"
          >
            Email
          </label>

          <input
            id="email"
            type="email"
            {...register("email", {
              required: "Email is required.",
            })}
            className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-text outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
          />

          {errors.email && (
            <p className="mt-1 text-sm text-danger">
              {errors.email.message}
            </p>
          )}
        </div>

        <div>
          <label
            htmlFor="phone"
            className="mb-2 block text-sm font-medium text-text"
          >
            Phone
          </label>

          <input
            id="phone"
            {...register("phone")}
            className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-text outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
          />
        </div>

        <div className="flex justify-end gap-3">
          {onCancel && (
            <Button
              type="button"
              variant="secondary"
              onClick={onCancel}
              disabled={isSubmitting}
            >
              Cancel
            </Button>
          )}

          <Button
            type="submit"
            disabled={isSubmitting}
          >
            {isSubmitting ? submittingLabel : submitLabel}
          </Button>
        </div>
      </form>
    </Card>
  );
}