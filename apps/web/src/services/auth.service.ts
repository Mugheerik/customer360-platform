import { api } from "@/lib/api/client";

import type {
  AuthToken,
  AuthUser,
  LoginCredentials,
} from "@/features/auth/types";

export interface RegisterCredentials {
  username: string;
  email: string;
  password: string;
}

export const AuthService = {
  async login(data: LoginCredentials): Promise<AuthToken> {
    const response = await api.post<AuthToken>(
      "/auth/login",
      data,
    );

    return response.data;
  },

  async register(
    data: RegisterCredentials,
  ): Promise<AuthUser> {
    const response = await api.post<AuthUser>(
      "/auth/register",
      data,
    );

    return response.data;
  },

  async me(): Promise<AuthUser> {
    const response = await api.get<AuthUser>(
      "/auth/me",
    );

    return response.data;
  },
};