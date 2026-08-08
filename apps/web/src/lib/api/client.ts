import axios from "axios";

import { env } from "@/lib/env";
import { useAuthStore } from "@/store/auth.store";

export const api = axios.create({
  baseURL: env.apiBaseUrl,
  timeout: 10_000,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use((config) => {
  const accessToken = useAuthStore.getState().accessToken;

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});