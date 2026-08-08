import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import Button from "@/components/ui/button";
import Card, {
  CardContent,
  CardHeader,
} from "@/components/ui/card";
import Input from "@/components/ui/input";
import { Body, H2 } from "@/components/ui/typography";

import {
  loginSchema,
  type LoginFormData,
} from "../schemas/login.schema";
import { useLogin } from "@/hooks/useLogin";

export default function LoginForm() {
  const login = useLogin();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const onSubmit = (data: LoginFormData) => {
    login.mutate(data);
  };

  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <H2 className="text-2xl">
          Sign in
        </H2>

        <Body className="mt-2">
          Sign in to continue to Customer360.
        </Body>
      </CardHeader>

      <CardContent>
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="space-y-5"
        >
          <div>
            <label
              htmlFor="email"
              className="mb-2 block text-sm font-medium text-text"
            >
              Email
            </label>

            <Input
              id="email"
              type="email"
              autoComplete="email"
              placeholder="you@example.com"
              {...register("email")}
            />

            {errors.email ? (
              <p className="mt-1.5 text-sm text-danger">
                {errors.email.message}
              </p>
            ) : null}
          </div>

          <div>
            <label
              htmlFor="password"
              className="mb-2 block text-sm font-medium text-text"
            >
              Password
            </label>

            <Input
              id="password"
              type="password"
              autoComplete="current-password"
              placeholder="••••••••"
              {...register("password")}
            />

            {errors.password ? (
              <p className="mt-1.5 text-sm text-danger">
                {errors.password.message}
              </p>
            ) : null}
          </div>

          {login.isError ? (
            <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
              Unable to sign in. Please check your credentials and try again.
            </p>
          ) : null}

          <Button
            type="submit"
            className="w-full"
            disabled={login.isPending}
          >
            {login.isPending ? "Signing in..." : "Sign in"}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}