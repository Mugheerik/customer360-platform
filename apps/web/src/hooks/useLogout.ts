import { useAuthStore } from "@/store/auth.store";

export function useLogout() {
  const clearSession = useAuthStore(
    (state) => state.clearSession,
  );

  return {
    logout: clearSession,
  };
}