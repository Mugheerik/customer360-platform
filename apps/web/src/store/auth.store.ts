import { create } from "zustand";

import type { AuthToken, AuthUser } from "@/features/auth/types";

const ACCESS_TOKEN_KEY = "customer360_access_token";

type AuthState = {
  user: AuthUser | null;
  accessToken: string | null;
  isAuthenticated: boolean;
  setToken: (token: AuthToken) => void;
  setUser: (user: AuthUser | null) => void;
  setSession: (token: AuthToken, user: AuthUser) => void;
  clearSession: () => void;
};

function getStoredToken(): string | null {
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

export const useAuthStore = create<AuthState>((set) => {
  const accessToken = getStoredToken();

  return {
    user: null,
    accessToken,
    isAuthenticated: accessToken !== null,

    setToken: (token) => {
      localStorage.setItem(
        ACCESS_TOKEN_KEY,
        token.access_token,
      );

      set({
        accessToken: token.access_token,
        isAuthenticated: true,
      });
    },

    setSession: (token, user) => {
      localStorage.setItem(
        ACCESS_TOKEN_KEY,
        token.access_token,
      );

      set({
        user,
        accessToken: token.access_token,
        isAuthenticated: true,
      });
    },

    setUser: (user) =>
      set({
        user,
        isAuthenticated: user !== null,
      }),

    clearSession: () => {
      localStorage.removeItem(ACCESS_TOKEN_KEY);

      set({
        user: null,
        accessToken: null,
        isAuthenticated: false,
      });
    },
  };
});