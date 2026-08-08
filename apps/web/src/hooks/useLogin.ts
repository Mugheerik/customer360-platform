import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";

import { loginSchema } from "@/features/auth/schemas/login.schema";
import type { LoginCredentials } from "@/features/auth/types";
import { AuthService } from "@/services/auth.service";
import { useAuthStore } from "@/store/auth.store";

export function useLogin() {
  const navigate = useNavigate();

  const setToken = useAuthStore(
    (state) => state.setToken,
  );

  const setUser = useAuthStore(
    (state) => state.setUser,
  );

  return useMutation({
    mutationFn: async (credentials: LoginCredentials) => {
      const validatedCredentials =
        loginSchema.parse(credentials);

      return AuthService.login(validatedCredentials);
    },

    onSuccess: async (token) => {
      setToken(token);

      const user = await AuthService.me();

      setUser(user);

      navigate("/dashboard", {
        replace: true,
      });
    },
  });
}