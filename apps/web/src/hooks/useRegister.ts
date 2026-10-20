import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";

import type { RegisterFormData } from "@/features/auth/schemas/register.schema";
import { AuthService } from "@/services/auth.service";
import { useAuthStore } from "@/store/auth.store";

export function useRegister() {
  const navigate = useNavigate();

  const setToken = useAuthStore((state) => state.setToken);
  const setUser = useAuthStore((state) => state.setUser);

  return useMutation({
    mutationFn: async (data: RegisterFormData) => {
      await AuthService.register({
        email: data.email,
        username: data.username,
        password: data.password,
        first_name: data.firstName,
        last_name: data.lastName,
      });

      // Sign the new user in immediately.
      return AuthService.login({
        email: data.email,
        password: data.password,
      });
    },

    onSuccess: async (token) => {
      setToken(token);

      const user = await AuthService.me();

      setUser(user);

      navigate("/dashboard", { replace: true });
    },
  });
}
