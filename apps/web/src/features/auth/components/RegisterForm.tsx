import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { isAxiosError } from "axios";
import { Link } from "react-router-dom";

import Button from "@/components/ui/button";
import Card, {
  CardContent,
  CardHeader,
} from "@/components/ui/card";
import Input from "@/components/ui/input";
import { Body, H2 } from "@/components/ui/typography";
import { useRegister } from "@/hooks/useRegister";

import {
  registerSchema,
  type RegisterFormData,
} from "../schemas/register.schema";

function getErrorMessage(error: unknown): string {
  if (isAxiosError(error)) {
    if (error.response?.status === 409) {
      return "An account with this email or username already exists.";
    }

    if (error.response?.status === 422) {
      return "Please check the information you entered and try again.";
    }
  }

  return "Unable to create your account. Please try again.";
}

type FieldProps = {
  id: keyof RegisterFormData;
  label: string;
  type?: string;
  autoComplete?: string;
  placeholder?: string;
  error?: string;
  registration: ReturnType<
    ReturnType<typeof useForm<RegisterFormData>>["register"]
  >;
};

function Field({
  id,
  label,
  type = "text",
  autoComplete,
  placeholder,
  error,
  registration,
}: FieldProps) {
  return (
    <div>
      <label
        htmlFor={id}
        className="mb-2 block text-sm font-medium text-text"
      >
        {label}
      </label>

      <Input
        id={id}
        type={type}
        autoComplete={autoComplete}
        placeholder={placeholder}
        {...registration}
      />

      {error ? (
        <p className="mt-1.5 text-sm text-danger">{error}</p>
      ) : null}
    </div>
  );
}

export default function RegisterForm() {
  const registerUser = useRegister();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
  });

  const onSubmit = (data: RegisterFormData) => {
    registerUser.mutate(data);
  };

  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <H2 className="text-2xl">Create your account</H2>

        <Body className="mt-2">
          Register to start managing customers with Customer360.
        </Body>
      </CardHeader>

      <CardContent>
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="space-y-5"
        >
          <div className="grid gap-5 sm:grid-cols-2">
            <Field
              id="firstName"
              label="First name"
              autoComplete="given-name"
              error={errors.firstName?.message}
              registration={register("firstName")}
            />

            <Field
              id="lastName"
              label="Last name"
              autoComplete="family-name"
              error={errors.lastName?.message}
              registration={register("lastName")}
            />
          </div>

          <Field
            id="username"
            label="Username"
            autoComplete="username"
            error={errors.username?.message}
            registration={register("username")}
          />

          <Field
            id="email"
            label="Email"
            type="email"
            autoComplete="email"
            placeholder="you@example.com"
            error={errors.email?.message}
            registration={register("email")}
          />

          <Field
            id="password"
            label="Password"
            type="password"
            autoComplete="new-password"
            error={errors.password?.message}
            registration={register("password")}
          />

          <Field
            id="confirmPassword"
            label="Confirm password"
            type="password"
            autoComplete="new-password"
            error={errors.confirmPassword?.message}
            registration={register("confirmPassword")}
          />

          {registerUser.isError ? (
            <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
              {getErrorMessage(registerUser.error)}
            </p>
          ) : null}

          <Button
            type="submit"
            className="w-full"
            disabled={registerUser.isPending}
          >
            {registerUser.isPending
              ? "Creating account..."
              : "Create account"}
          </Button>

          <p className="text-center text-sm text-text-secondary">
            Already have an account?{" "}
            <Link
              to="/login"
              className="font-medium text-primary hover:underline"
            >
              Sign in
            </Link>
          </p>
        </form>
      </CardContent>
    </Card>
  );
}
